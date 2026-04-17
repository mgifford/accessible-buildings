#!/usr/bin/env python3
"""
Detect stale building examples and open GitHub issues for review.

A building example is considered stale when its last_reviewed front-matter
date is more than STALE_DAYS days in the past (default: 365).

Usage:
    python3 scripts/check-stale-examples.py

Environment variables:
    GITHUB_TOKEN        GitHub API token with issues:write permission.
    GITHUB_REPOSITORY   owner/repo (e.g. mgifford/accessible-buildings).
    STALE_DAYS          Days before an example is stale (default: 365).
    DRY_RUN             If 'true', print actions without creating issues.

Exit codes:
    0   Completed successfully (issues may or may not have been opened).
    1   Fatal error (missing token, API failure, etc.).
"""

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path


# ---------------------------------------------------------------------------
# Front-matter parsing (no third-party dependencies)
# ---------------------------------------------------------------------------

def parse_front_matter(content):
    """Return a dict of front-matter fields from a Jekyll Markdown file."""
    if not content.startswith('---'):
        return {}

    close = content.find('\n---', 3)
    if close == -1:
        return {}

    yaml_str = content[3:close].strip()
    data = {}

    for line in yaml_str.splitlines():
        # Match top-level scalar key: value pairs only
        m = re.match(r'^([\w_]+):\s*(.+)?$', line)
        if m:
            key = m.group(1)
            val = (m.group(2) or '').strip().strip('"\'')
            data[key] = val

    return data


# ---------------------------------------------------------------------------
# GitHub API helpers
# ---------------------------------------------------------------------------

def _api_request(method, path, token, body=None):
    """
    Make a GitHub REST API call.  Returns the parsed JSON response dict/list.
    Raises RuntimeError on non-2xx status.
    """
    url = f'https://api.github.com{path}'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'accessible-buildings-stale-check/1.0',
    }
    data = json.dumps(body).encode('utf-8') if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as exc:
        raise RuntimeError(
            f'GitHub API {method} {url} failed: {exc.code} {exc.reason}'
        ) from exc


def get_open_issues(token, repo, label):
    """Return all open issues with the given label (handles pagination)."""
    issues = []
    page = 1
    while True:
        path = (
            f'/repos/{repo}/issues'
            f'?state=open&labels={urllib.parse.quote(label)}'
            f'&per_page=100&page={page}'
        )
        batch = _api_request('GET', path, token)
        if not isinstance(batch, list) or not batch:
            break
        issues.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return issues


def create_issue(token, repo, title, body, labels):
    """Open a new GitHub issue and return the issue URL."""
    payload = {'title': title, 'body': body, 'labels': labels}
    result = _api_request('POST', f'/repos/{repo}/issues', token, payload)
    return result.get('html_url', '')


# ---------------------------------------------------------------------------
# Issue body builder
# ---------------------------------------------------------------------------

def build_issue_body(title, building_type, country, url, last_reviewed_str,
                     days_stale, file_path):
    """Return a Markdown issue body for a stale example."""
    return (
        f'## Stale Example Review Request: {title}\n'
        '\n'
        f'The building example for **{title}** ({building_type}, {country})'
        f' was last reviewed on **{last_reviewed_str}** —'
        f' {days_stale} days ago.\n'
        '\n'
        f'**Live page to review:** {url}\n'
        f'**Repository file:** {file_path}\n'
        '\n'
        '### What to check\n'
        '\n'
        '- [ ] Step-free entrance route is still accurate\n'
        '- [ ] Lift dimensions, weight limit, and operating hours unchanged\n'
        '- [ ] Accessible toilet locations unchanged\n'
        '- [ ] Quiet space still available\n'
        '- [ ] Hearing loop coverage unchanged\n'
        '- [ ] Contact details / email for accessibility queries still valid\n'
        '- [ ] Temporary barriers from events or renovations noted\n'
        '- [ ] Any known constraints still current\n'
        '\n'
        'Once the review is complete, update `last_reviewed` in the front'
        ' matter and close this issue.\n'
        '\n'
        f'<!-- stale-example-file: {file_path} -->\n'
    )


# ---------------------------------------------------------------------------
# Staleness detection
# ---------------------------------------------------------------------------

def parse_date(value):
    """
    Parse a date string in YYYY-MM-DD format (or a datetime.date/datetime
    object when yaml is available).  Returns a date object or None.
    """
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        m = re.match(r'^(\d{4})-(\d{2})-(\d{2})', value.strip())
        if m:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None


def find_stale_examples(examples_dir, stale_days, repo_root=None):
    """
    Scan examples_dir for Markdown files whose last_reviewed date is more
    than stale_days in the past.

    Returns a list of dicts with keys:
        file_path, title, building_type, country, url,
        last_reviewed_str, days_stale
    """
    examples_path = Path(examples_dir)
    root = Path(repo_root) if repo_root else examples_path.parent.parent
    today = date.today()
    stale = []

    for md_file in sorted(examples_path.glob('*.md')):
        content = md_file.read_text(encoding='utf-8')
        fm = parse_front_matter(content)

        last_reviewed_raw = fm.get('last_reviewed', '')
        last_reviewed = parse_date(last_reviewed_raw)

        if last_reviewed is None:
            print(
                f'  [WARN] {md_file.name}: missing or unparseable'
                f' last_reviewed ({last_reviewed_raw!r}) — skipping',
                file=sys.stderr,
            )
            continue

        days_stale = (today - last_reviewed).days
        if days_stale <= stale_days:
            continue

        stale.append({
            'file_path': str(md_file.relative_to(root)),
            'title': fm.get('title', md_file.stem),
            'building_type': fm.get('building_type', 'Unknown'),
            'country': fm.get('country', 'Unknown'),
            'url': fm.get('url', ''),
            'last_reviewed_str': str(last_reviewed),
            'days_stale': days_stale,
        })

    return stale


# ---------------------------------------------------------------------------
# Duplicate detection
# ---------------------------------------------------------------------------

def already_has_open_issue(file_path, open_issues):
    """
    Return True if any open issue body contains the stale-example-file
    marker for this file_path, or if the issue title mentions the file name.
    """
    marker = f'<!-- stale-example-file: {file_path} -->'
    file_name = Path(file_path).name

    for issue in open_issues:
        body = issue.get('body') or ''
        if marker in body:
            return True
        # Fallback: check if issue title mentions the file name (for issues
        # opened before the marker convention was introduced)
        issue_title = issue.get('title') or ''
        if file_name in issue_title:
            return True

    return False


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    token = os.environ.get('GITHUB_TOKEN', '').strip()
    repo = os.environ.get('GITHUB_REPOSITORY', '').strip()
    dry_run = os.environ.get('DRY_RUN', '').strip().lower() == 'true'

    try:
        stale_days = int(os.environ.get('STALE_DAYS', '365'))
    except ValueError:
        print('[ERROR] STALE_DAYS must be an integer', file=sys.stderr)
        return 1

    if not token:
        print('[ERROR] GITHUB_TOKEN environment variable is required',
              file=sys.stderr)
        return 1
    if not repo:
        print('[ERROR] GITHUB_REPOSITORY environment variable is required',
              file=sys.stderr)
        return 1

    # Locate examples directory relative to this script
    repo_root = Path(__file__).parent.parent
    examples_dir = repo_root / 'examples' / '_examples'

    if not examples_dir.is_dir():
        print(f'[ERROR] Examples directory not found: {examples_dir}',
              file=sys.stderr)
        return 1

    print(f'Scanning {examples_dir} for examples stale > {stale_days} days…')
    stale = find_stale_examples(examples_dir, stale_days, repo_root=repo_root)

    if not stale:
        print('No stale examples found.')
        return 0

    print(f'Found {len(stale)} stale example(s). Checking for open issues…')

    # In dry-run mode skip the API call — no issues will be created anyway
    if dry_run:
        open_issues = []
    else:
        try:
            open_issues = get_open_issues(token, repo, 'maintenance')
        except RuntimeError as exc:
            print(f'[ERROR] Could not fetch open issues: {exc}', file=sys.stderr)
            return 1

    opened = 0
    skipped = 0

    for example in stale:
        fp = example['file_path']

        if already_has_open_issue(fp, open_issues):
            print(f'  [SKIP] {fp} — open review issue already exists')
            skipped += 1
            continue

        issue_title = f'Stale Example Review: {example["title"]}'
        issue_body = build_issue_body(
            title=example['title'],
            building_type=example['building_type'],
            country=example['country'],
            url=example['url'],
            last_reviewed_str=example['last_reviewed_str'],
            days_stale=example['days_stale'],
            file_path=fp,
        )
        labels = ['maintenance', 'examples']

        if dry_run:
            print(f'  [DRY RUN] Would open issue: {issue_title!r}')
            opened += 1
            continue

        try:
            issue_url = create_issue(token, repo, issue_title, issue_body,
                                     labels)
            print(f'  [OPENED] {fp} → {issue_url}')
            opened += 1
        except RuntimeError as exc:
            print(f'  [ERROR] Failed to open issue for {fp}: {exc}',
                  file=sys.stderr)

    print(
        f'\nDone. Opened: {opened}  Skipped (duplicate): {skipped}'
        f'  Total stale: {len(stale)}'
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
