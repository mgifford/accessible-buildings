#!/usr/bin/env python3
"""
Validate building example and template files against the 8-point evaluation
rubric and content rules defined in AGENTS.md.

Usage:
    python3 scripts/validate-content.py file1.md file2.md ...
    python3 scripts/validate-content.py --files-from /path/to/list.txt

Exit codes:
    0  All files pass (or only warnings).
    1  One or more files have required fixes (errors).

Output:
    Markdown-formatted report suitable for posting as a GitHub PR comment.
"""

import os
import re
import sys

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


# ---------------------------------------------------------------------------
# Front-matter parsing
# ---------------------------------------------------------------------------

def parse_front_matter(content):
    """Return (data_dict, body_str, yaml_str) for a Jekyll markdown file."""
    if not content.startswith('---'):
        return {}, content, ''

    close = content.find('\n---', 3)
    if close == -1:
        return {}, content, ''

    yaml_str = content[3:close].strip()
    body = content[close + 4:].strip()

    if YAML_AVAILABLE:
        try:
            data = yaml.safe_load(yaml_str)
            return data or {}, body, yaml_str
        except yaml.YAMLError:
            return {}, body, yaml_str

    # Minimal fallback: extract only top-level scalar keys
    data = {}
    for line in yaml_str.splitlines():
        m = re.match(r'^([\w_]+):\s*(.+)?$', line)
        if m:
            data[m.group(1)] = m.group(2)
    return data, body, yaml_str


# ---------------------------------------------------------------------------
# Rubric and rule definitions
# ---------------------------------------------------------------------------

RUBRIC_CRITERIA = [
    ('discoverability',        'Discoverability'),
    ('arrival_clarity',        'Arrival Clarity'),
    ('entrance_clarity',       'Entrance Clarity'),
    ('internal_navigation',    'Internal Navigation'),
    ('facilities_clarity',     'Facilities Clarity'),
    ('program_accommodations', 'Program Accommodations'),
    ('transparency',           'Transparency'),
    ('format_quality',         'Format Quality'),
]

REQUIRED_EXAMPLE_FM = [
    'url', 'last_reviewed', 'building_type', 'country',
    'rubric', 'strengths', 'gaps',
]

REQUIRED_EXAMPLE_SECTIONS = [
    'Rubric Scores',
    'Building Details',
    'Notable Strengths',
    'Identified Gaps',
    'Website Placement Notes',
    'Format Notes',
]

MARKETING_PATTERNS = [
    (r'\bworld[- ]class\b',             'world-class'),
    (r'\bstate[- ]of[- ]the[- ]art\b',  'state-of-the-art'),
    (r'\bbest[- ]in[- ]class\b',        'best-in-class'),
    (r'\baward[- ]winning\b',           'award-winning'),
    (r'\bground[- ]break\w*\b',         'ground-breaking'),
    (r'\bunparalleled\b',               'unparalleled'),
    (r'\bsecond[- ]to[- ]none\b',       'second-to-none'),
    (r'\bcutting[- ]edge\b',            'cutting-edge'),
]

VAGUE_PATTERNS = [
    (r'\bfully accessible\b',       'fully accessible'),
    (r'\bcompletely accessible\b',  'completely accessible'),
    (r'\b100\s*%\s*accessible\b',   '100% accessible'),
    (r'\bentirely accessible\b',    'entirely accessible'),
    (r'\bwheelchair[- ]friendly\b', 'wheelchair-friendly'),
    (r'\bdisability[- ]friendly\b', 'disability-friendly'),
]

ADA_ONLY_PATTERNS = [
    (r'\bADA[- ]compliant\b',   'ADA-compliant'),
    (r'\bADA compliance\b',     'ADA compliance'),
    (r'\bmeets\s+ADA\b',        'meets ADA'),
    (r'\bADA requirements\b',   'ADA requirements'),
]

# Icons used in the rubric completeness table
STATUS_ICONS = {'pass': '✅', 'warn': '⚠️', 'fail': '❌'}


# ---------------------------------------------------------------------------
# Content-rule checking
# ---------------------------------------------------------------------------

def _scan_patterns(text, pattern_list, message_template):
    """Return a list of warning strings for each matched pattern."""
    results = []
    for pattern, label in pattern_list:
        if re.search(pattern, text, re.IGNORECASE):
            results.append(message_template.format(label=label))
    return results


def find_content_violations(body, yaml_str):
    """
    Scan body and yaml_str for content-rule violations.
    Returns (marketing_list, vague_list, ada_only_list) of warning strings.
    """
    full_text = yaml_str + '\n' + body
    marketing = _scan_patterns(
        full_text,
        MARKETING_PATTERNS,
        'Marketing language detected: `{label}` — remove or replace with'
        ' neutral, factual language',
    )
    vague = _scan_patterns(
        full_text,
        VAGUE_PATTERNS,
        'Vague assertion: `{label}` — scope and define this claim'
        ' (e.g. "step-free access to all public floors")',
    )
    ada_only = _scan_patterns(
        full_text,
        ADA_ONLY_PATTERNS,
        'US-only framing: `{label}` — pair with an international'
        ' equivalent (e.g. step-free, accessible toilet)',
    )
    return marketing, vague, ada_only


# ---------------------------------------------------------------------------
# Per-file validation
# ---------------------------------------------------------------------------

def validate_example(content):
    """
    Validate an example file.
    Returns (errors, warnings, rubric_rows).
    rubric_rows: list of (label, display_str, status) where status in
                 {'pass', 'warn', 'fail'}.
    """
    front_matter, body, yaml_str = parse_front_matter(content)
    errors = []
    warnings = []
    rubric_rows = []

    # Required front-matter fields
    for field in REQUIRED_EXAMPLE_FM:
        if field not in front_matter:
            errors.append(f'Missing required front matter field: `{field}`')

    # Rubric scores
    rubric = front_matter.get('rubric') or {}
    if not isinstance(rubric, dict):
        rubric = {}

    for key, label in RUBRIC_CRITERIA:
        score = rubric.get(key)
        if score is None:
            errors.append(f'Missing rubric score: `rubric.{key}`')
            rubric_rows.append((label, '❌ Missing', 'fail'))
        elif not isinstance(score, (int, float)) or not (1 <= float(score) <= 5):
            errors.append(
                f'Invalid rubric score for `{key}`: must be 1–5, got `{score}`'
            )
            rubric_rows.append((label, f'⚠️ {score}', 'warn'))
        elif float(score) <= 2:
            warnings.append(
                f'Low score for `{key}`: {score}/5 — consider improving or'
                f' explicitly documenting why this is rated so low'
            )
            rubric_rows.append((label, f'⚠️ {score}/5', 'warn'))
        else:
            rubric_rows.append((label, f'✅ {score}/5', 'pass'))

    # Non-empty strengths and gaps
    if not front_matter.get('strengths'):
        errors.append('`strengths` list is empty or missing in front matter')
    if not front_matter.get('gaps'):
        warnings.append(
            '`gaps` list is empty — every example should document known'
            ' limitations, even minor ones'
        )

    # Required body sections
    for section in REQUIRED_EXAMPLE_SECTIONS:
        pattern = rf'^#+\s+{re.escape(section)}\b'
        if not re.search(pattern, body, re.MULTILINE | re.IGNORECASE):
            errors.append(f'Missing required section: `## {section}`')

    # Content rules
    marketing, vague, ada_only = find_content_violations(body, yaml_str)
    warnings.extend(marketing)
    warnings.extend(vague)
    warnings.extend(ada_only)

    return errors, warnings, rubric_rows


def validate_template(content):
    """
    Validate a template file.
    Returns (errors, warnings, []).
    """
    front_matter, body, yaml_str = parse_front_matter(content)
    errors = []
    warnings = []

    # Required front-matter fields
    for field in ('layout', 'title'):
        if field not in front_matter:
            errors.append(f'Missing required front matter field: `{field}`')

    # Content rules
    marketing, vague, ada_only = find_content_violations(body, yaml_str)
    warnings.extend(marketing)
    warnings.extend(vague)
    warnings.extend(ada_only)

    return errors, warnings, []


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------

def build_file_report(filepath, errors, warnings, rubric_rows, file_type):
    """Return a markdown string for one file."""
    filename = os.path.basename(filepath)

    if errors:
        badge = '🔴 FAIL'
    elif warnings:
        badge = '⚠️ WARN'
    else:
        badge = '✅ PASS'

    lines = [f'### `{filename}` — {badge}', '']

    if file_type == 'example' and rubric_rows:
        lines.append('<details><summary>Rubric completeness table</summary>')
        lines.append('')
        lines.append('| Criterion | Score | Status |')
        lines.append('| :--- | :---: | :---: |')
        for label, display, status in rubric_rows:
            lines.append(f'| {label} | {display} | {STATUS_ICONS.get(status, "")} |')
        lines.append('')
        lines.append('</details>')
        lines.append('')

    if errors:
        lines.append('**❌ Required fixes — must be resolved before merge:**')
        lines.append('')
        for e in errors:
            lines.append(f'- {e}')
        lines.append('')

    if warnings:
        lines.append('**⚠️ Improvements recommended (not blocking):**')
        lines.append('')
        for w in warnings:
            lines.append(f'- {w}')
        lines.append('')

    if not errors and not warnings:
        lines.append('✅ No issues found.')
        lines.append('')

    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    # Support --files-from <path> to read newline-delimited file list
    if len(argv) >= 2 and argv[0] == '--files-from':
        with open(argv[1], encoding='utf-8') as fh:
            argv = [line.rstrip('\n') for line in fh if line.strip()]

    header_marker = '<!-- template-completeness-review -->'
    header = '## 🔍 Template & Example Completeness Review'

    if not argv:
        print(header_marker)
        print(header)
        print('')
        print('No relevant files changed in this pull request.')
        return 0

    # Filter to existing .md files only
    files = [f for f in argv if f.endswith('.md') and os.path.isfile(f)]

    if not files:
        print(header_marker)
        print(header)
        print('')
        print('No relevant markdown files found to validate.')
        return 0

    total_errors = 0
    total_warnings = 0
    reports = []

    for filepath in files:
        with open(filepath, encoding='utf-8') as fh:
            content = fh.read()

        if filepath.startswith('examples/_examples/'):
            errors, warnings, rubric_rows = validate_example(content)
            ftype = 'example'
        elif filepath.startswith('templates/'):
            errors, warnings, rubric_rows = validate_template(content)
            ftype = 'template'
        else:
            continue

        total_errors += len(errors)
        total_warnings += len(warnings)
        reports.append(
            build_file_report(filepath, errors, warnings, rubric_rows, ftype)
        )

    if not reports:
        print(header_marker)
        print(header)
        print('')
        print('No example or template files to review.')
        return 0

    if total_errors:
        overall = '🔴 FAIL'
        fix_word = 'fix' if total_errors == 1 else 'fixes'
        summary = (
            f'{total_errors} required {fix_word} must be resolved before this'
            f' PR can be merged. See details below.'
        )
    elif total_warnings:
        overall = '⚠️ WARN'
        summary = (
            f'{total_warnings} improvement(s) recommended.'
            f' No blocking issues — these are optional but encouraged.'
        )
    else:
        overall = '✅ PASS'
        summary = 'All checked files meet the completeness and content rules.'

    out = [
        header_marker,
        header,
        '',
        f'**Overall: {overall}**',
        '',
        f'> {summary}',
        '',
        '---',
        '',
    ]
    for report in reports:
        out.append(report)
    out.extend([
        '---',
        '',
        (
            '*Reviewed automatically against the'
            ' [8-point rubric and content rules in AGENTS.md](AGENTS.md).'
            ' Required fixes (🔴) must be resolved before merge.'
            ' Recommended improvements (⚠️) are optional.*'
        ),
        '',
    ])

    print('\n'.join(out))
    return 1 if total_errors else 0


if __name__ == '__main__':
    sys.exit(main())
