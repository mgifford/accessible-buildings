---
title: "Add a Copilot agent to generate schema.org JSON-LD structured data from completed access guide templates"
labels: ["enhancement", "automation", "structured-data", "copilot-agent"]
---

## Summary

Create a GitHub Copilot agent that, when a PR adds or significantly updates a completed building access guide, reads the narrative content and automatically generates the corresponding schema.org `LocationFeatureSpecification` JSON-LD block. The agent posts the generated markup as a PR comment, ready for the contributor to paste into their live web page's `<head>`.

## Background

This repository's [`framework/machine-readable.md`](/framework/machine-readable.md) explicitly recognises structured data as the next step beyond HTML-first publishing:

> *"Publishing accessibility information in HTML is the first step. The next step is making that information discoverable by search engines and assistive technologies through structured data."*

The framework already defines the canonical JSON-LD vocabulary (schema.org `LocationFeatureSpecification`, `CivicStructure`) and recommended tags (step-free entrance, accessible toilet, Changing Places, assistive listening system, accessible parking, quiet space). However, generating this markup is currently a manual, technical task that most contributors will skip.

The [GitHub Copilot agents guide](https://accessibility.github.com/documentation/guide/getting-started-with-agents/) describes agents that can read documents, extract structured information, and output machine-readable artefacts. This maps directly onto converting narrative accessibility descriptions into JSON-LD.

## Proposed agent behaviour

1. **Trigger:** Any PR that touches `templates/building-access-guide.md` or adds a file matching `examples/_examples/*.md`.
2. **Agent task:**
   - Parse the changed file for known accessibility features as defined in `framework/machine-readable.md`:
     - Step-free entrance (and hours of availability if mentioned).
     - Accessible toilet (location and Changing Places designation if present).
     - Accessible parking (number of spaces).
     - Hearing / assistive listening system (type: loop, IR, FM).
     - Quiet space (permanent or temporary).
     - Power-assisted or automatic doors.
     - Lift availability (and any known failure plan).
   - For each identified feature, set `value` to `"true"`, `"false"`, or `"unknown"` — following the repository's conservative claims guidance:
     > *"If a feature's status is unknown, say 'unknown'."*
   - Produce a complete `application/ld+json` script block.
   - Post the block as a collapsible PR comment section with a brief explanation of how to use it.
3. **Conservative defaults:**
   - If a feature is mentioned but its availability is ambiguous, output `"unknown"` rather than `"true"`.
   - Never assert compliance or certification status.

## Example agent output (PR comment)

````markdown
### 🤖 Suggested schema.org JSON-LD for [Building Name]

The following structured data was generated from the access guide content.
Add it to the `<head>` of your published access page.

<details>
<summary>View generated JSON-LD</summary>

```json
{
  "@context": "https://schema.org",
  "@type": "CivicStructure",
  "name": "Main Library",
  "amenityFeature": [
    {
      "@type": "LocationFeatureSpecification",
      "name": "Step-free entrance",
      "value": "true",
      "hoursAvailable": "Mo-Fr 09:00-17:00"
    },
    {
      "@type": "LocationFeatureSpecification",
      "name": "Accessible toilet",
      "value": "true"
    },
    {
      "@type": "LocationFeatureSpecification",
      "name": "Changing Places toilet",
      "value": "unknown"
    },
    {
      "@type": "LocationFeatureSpecification",
      "name": "Assistive listening system",
      "value": "true",
      "description": "Hearing loop in main hall"
    },
    {
      "@type": "LocationFeatureSpecification",
      "name": "Accessible parking",
      "value": "true",
      "description": "4 spaces in north car park"
    },
    {
      "@type": "LocationFeatureSpecification",
      "name": "Quiet space",
      "value": "true"
    }
  ]
}
```

**Review before publishing:** Verify each `value` field matches the current
state of the building. Set any uncertain features to `"unknown"`.

</details>
````

## Implementation sketch

```yaml
# .github/workflows/jsonld-generator.yml
name: JSON-LD Structured Data Generator

on:
  pull_request:
    paths:
      - 'examples/_examples/**'
      - 'templates/building-access-guide.md'

jobs:
  generate-jsonld:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - name: Generate JSON-LD from access guide
        uses: github/copilot-agent-action@v1   # placeholder
        with:
          instructions: |
            Read the changed access guide file. Extract accessibility features
            as defined in framework/machine-readable.md. Generate a
            schema.org LocationFeatureSpecification JSON-LD block. Post it
            as a collapsible PR comment with usage instructions. Use
            "unknown" for any features that are ambiguous. Do not assert
            compliance status.
```

## Why this is uniquely valuable for this project

- The vocabulary is already fully specified in `framework/machine-readable.md` — the agent has a precise source of truth to work from, not a generic prompt.
- JSON-LD generation is technically daunting for building managers and accessibility staff who are the primary template contributors; an agent removes this barrier entirely.
- Machine-readable accessibility data has compounding value: it enables third-party accessibility apps (such as AccessNow, AXS Map, and Wheelmap) and search engine rich results that surface the building's accessibility features to disabled users before they visit.
- No existing tool in this repository generates structured data automatically. This closes the gap between the narrative templates and the structured-data guidance in the framework.

## Acceptance criteria

- [ ] Agent is triggered on the correct file paths.
- [ ] Generated JSON-LD validates against schema.org `CivicStructure` + `LocationFeatureSpecification`.
- [ ] Features not mentioned in the guide default to `"unknown"`, never `"false"` unless the guide explicitly says a feature is unavailable.
- [ ] Compliance or certification language is never included in generated output.
- [ ] The PR comment is collapsible to avoid cluttering short reviews.
- [ ] The comment includes a clear instruction to review all `value` fields before publishing.
- [ ] Agent handles both new files and significant edits to existing files.
