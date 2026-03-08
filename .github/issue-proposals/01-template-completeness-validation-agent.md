---
title: "Add a GitHub Copilot agent to validate template and example completeness on pull requests"
labels: ["enhancement", "automation", "copilot-agent"]
---

## Summary

Use a GitHub Copilot coding agent, triggered on every pull request that adds or modifies a building example or template, to automatically review the submitted content against this repository's 8-point evaluation rubric and content rules. The agent posts a structured review comment identifying gaps and requesting improvements before merge.

## Background

This repository's [`AGENTS.md`](/AGENTS.md) defines a clear evaluation rubric with eight criteria that every building example must satisfy:

1. Discoverability
2. Arrival clarity
3. Entrance clarity
4. Internal navigation
5. Facilities clarity
6. Program accommodations
7. Transparency
8. Format quality

It also specifies content rules: no marketing language, no vague assertions such as "fully accessible", concrete operational details (distances, door types, surface types), separation of "features exist" from "how to use them", and US-ADA framing paired with international equivalents.

Currently these rules are enforced only through manual review. As the examples collection grows, inconsistent review quality is likely.

## Proposed agent behaviour

1. **Trigger:** Any PR that touches `examples/_examples/*.md` or `templates/*.md`.
2. **Inputs read by the agent:**
   - The changed file(s).
   - The rubric and content rules defined in `AGENTS.md`.
   - The front matter schema from `examples/_examples/sample-example.md` (rubric scores, `last_reviewed`, `url`, `building_type`, `country`).
3. **Agent outputs:**
   - A structured PR comment with a completeness table (one row per rubric criterion, flagging missing or insufficient content).
   - Inline suggestions for any content rule violations detected (marketing language, missing distances, vague assertions, US-only framing).
   - A pass/warn/fail summary badge in the comment.
4. **Merge gate (optional phase 2):** Require the agent's completeness check to pass before a PR can be merged.

## Implementation sketch

```yaml
# .github/workflows/template-review.yml
name: Template Completeness Review

on:
  pull_request:
    paths:
      - 'examples/_examples/**'
      - 'templates/**'

jobs:
  review:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - name: Run Copilot template review agent
        uses: github/copilot-agent-action@v1   # placeholder – use actual action when available
        with:
          instructions: |
            Review the changed files against the 8-point evaluation rubric and
            content rules in AGENTS.md. Post a structured comment.
          model: gpt-4o
```

> **Note:** The exact action reference should be updated once GitHub publishes the stable agent action. See the [GitHub Copilot agents guide](https://accessibility.github.com/documentation/guide/getting-started-with-agents/) for the current recommended approach.

## Why this is uniquely valuable for this project

- The rubric is specific to this repository and cannot be enforced by generic linters.
- Accessibility documentation quality is mission-critical: a disabled visitor relying on an incomplete guide may arrive to find a barrier they were not warned about.
- An automated completeness check sets a consistent bar, regardless of who reviews the PR.

## Acceptance criteria

- [ ] Agent is triggered automatically on the correct file paths.
- [ ] The rubric completeness table appears as a PR comment within 5 minutes of opening.
- [ ] Content-rule violations (marketing language, vague assertions) are flagged with inline suggestions.
- [ ] The agent does not fail builds for optional improvements — only for missing required sections.
- [ ] False-positive rate is reviewed and the instructions prompt is refined after the first 10 real PRs.
