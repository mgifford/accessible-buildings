---
title: "Add a scheduled Copilot agent to detect and flag stale building examples"
labels: ["enhancement", "automation", "maintenance", "copilot-agent"]
---

## Summary

Create a scheduled GitHub Copilot agent (or Actions workflow) that runs monthly, reads the `last_reviewed` date in every file under `examples/_examples/`, identifies examples that have not been reviewed in more than 12 months, and automatically opens a GitHub issue requesting a content review for each one.

## Background

The repository's [`AGENTS.md`](/AGENTS.md) makes maintenance accountability a non-negotiable:

> *"Maintenance accountability. Accessibility degrades when routes are blocked, lifts fail, signage is moved, or temporary setups create barriers."*

Each example file includes a `last_reviewed` front-matter field (e.g. `last_reviewed: 2024-05-12`). However, there is currently no automated mechanism to act on this date. Building accessibility information can change rapidly — a lift refurbishment, a new step-free entrance, a closed quiet room — and stale examples are actively harmful to disabled visitors who rely on them to plan their trips.

The [GitHub Copilot agents guide](https://accessibility.github.com/documentation/guide/getting-started-with-agents/) describes scheduled agents that can autonomously inspect repository content and open issues. This pattern maps directly onto the maintenance workflow this repository needs.

## Proposed agent behaviour

1. **Schedule:** First Monday of each month at 09:00 UTC.
2. **Agent task:**
   - Read all `examples/_examples/*.md` files.
   - Parse the `last_reviewed` front-matter field.
   - Identify files where `last_reviewed` is more than 365 days ago.
   - For each stale file, check whether an open review-request issue already exists (to avoid duplicates).
   - Open a new issue for each stale example that lacks an open review issue, using a standardised template.
3. **Issue template fields:**
   - Building name and type.
   - Country.
   - Original URL (so a reviewer can visit the live page).
   - Last reviewed date.
   - Days since last review.
   - Direct link to the file in the repository.
   - Checklist of what to verify (entrance, lift, toilets, temporary barriers, contact details).

## Example auto-generated issue body

```markdown
## Stale Example Review Request: City Museum of Art

The building example for **City Museum of Art** (Museum, UK) was last reviewed
on **2024-05-12** — 13 months ago.

**Live page to review:** https://example.com/museum/access
**Repository file:** examples/_examples/city-museum-of-art.md

### What to check

- [ ] Step-free entrance route is still accurate
- [ ] Lift dimensions, weight limit, and operating hours unchanged
- [ ] Accessible toilet locations unchanged
- [ ] Quiet space still available
- [ ] Hearing loop coverage unchanged
- [ ] Contact details / email for accessibility queries still valid
- [ ] Temporary barriers from events or renovations noted
- [ ] Any known constraints still current

Once the review is complete, update `last_reviewed` in the front matter and
close this issue.
```

## Implementation sketch

```yaml
# .github/workflows/stale-example-check.yml
name: Stale Example Review Check

on:
  schedule:
    - cron: '0 9 1-7 * 1'   # Mondays where the day is 1–7, i.e. approximately the first Monday each month
  workflow_dispatch:

jobs:
  stale-check:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - name: Run stale example detection agent
        uses: github/copilot-agent-action@v1   # placeholder
        with:
          instructions: |
            Read every file in examples/_examples/. Parse the last_reviewed
            front-matter field. For any file reviewed more than 365 days ago,
            open a GitHub issue using the template in
            .github/ISSUE_TEMPLATE/stale-example-review.md.
            Do not open a duplicate if an open issue already references the
            same file.
```

## Why this is uniquely valuable for this project

- Stale building accessibility information is not merely outdated — it can cause a disabled visitor to arrive at a building and encounter an unexpected barrier.
- The `last_reviewed` metadata is already present and structured, making this an ideal fit for an automated agent.
- No equivalent automation exists in the current CI pipeline (`ci.yml`, `accessibility.yml`, `link-check.yml`).
- A human maintainer reviewing dozens of examples manually each month is unrealistic; an agent makes maintenance scalable.

## Acceptance criteria

- [ ] Workflow runs on schedule and can be triggered manually via `workflow_dispatch`.
- [ ] Issues are only opened for examples with `last_reviewed` > 365 days ago.
- [ ] Duplicate issues are not opened if an open review issue already exists for a file.
- [ ] Each issue includes the building name, URL, last reviewed date, and the verification checklist.
- [ ] Issues are labelled `maintenance` and `examples`.
- [ ] The staleness threshold (365 days) is configurable without changing the workflow file.
