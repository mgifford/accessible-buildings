# Issue Proposals: GitHub Copilot Agent Opportunities

This directory contains structured proposals for GitHub issues. Each file is formatted as a ready-to-file GitHub issue and can be pasted directly into the "new issue" form or imported via the GitHub CLI:

```bash
# Example: create an issue from a proposal file (copy the title from the 'title:' front-matter field)
gh issue create \
  --title "Add a GitHub Copilot agent to validate template and example completeness on pull requests" \
  --body-file 01-template-completeness-validation-agent.md \
  --label enhancement,automation
```

## Why these proposals exist

These proposals were created in response to the techniques described in the [GitHub Copilot Agents guide](https://accessibility.github.com/documentation/guide/getting-started-with-agents/). Each proposal identifies a **unique, project-specific** opportunity to use a Copilot agent to improve the quality, maintenance, or usefulness of this toolkit.

## Proposals

| File | Issue title | Area |
| :--- | :--- | :--- |
| [`01-template-completeness-validation-agent.md`](01-template-completeness-validation-agent.md) | Agent-powered template and example completeness validation on PRs | Contribution quality |
| [`02-stale-example-detection-agent.md`](02-stale-example-detection-agent.md) | Scheduled agent to detect and flag stale building examples | Maintenance accountability |
| [`03-jsonld-structured-data-generator-agent.md`](03-jsonld-structured-data-generator-agent.md) | Agent to generate schema.org JSON-LD from completed access guide templates | Machine-readable data |

## How each proposal maps to repository goals

### 1 — Template completeness validation
Enforces the 8-point evaluation rubric and content rules defined in `AGENTS.md` automatically on every PR. Protects the quality of visitor-facing accessibility information.

### 2 — Stale example detection
Operationalises the maintenance-accountability non-negotiable from `AGENTS.md`. Stale building information can cause disabled visitors to encounter barriers they were not warned about.

### 3 — JSON-LD structured data generation
Bridges the gap between the narrative templates and the machine-readable guidance in `framework/machine-readable.md`. Enables search engine rich results and third-party accessibility apps without requiring contributors to write JSON-LD manually.
