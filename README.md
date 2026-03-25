# Building Access Guide

> ⚠️ **Experimental — Not Yet Validated**
>
> This toolkit is in early, experimental development. Most content was generated with AI assistance and **has not yet been validated against real buildings or real-world use**. Do not treat anything here as authoritative guidance until it has been reviewed and confirmed by disabled people, accessibility practitioners, and building operators.
>
> **Your feedback is essential.** If you try this toolkit — whether the results are positive or negative — please [open an issue](https://github.com/mgifford/accessible-buildings/issues) to share what you found. Include links and references so claims can be discussed and improved.

A practical framework for publishing structured, transparent physical accessibility information for buildings.

## Purpose

The Building Access Guide Toolkit helps organizations provide the specific, operational details that disabled visitors need to plan a visit with confidence. It focuses on the **Access Chain**—the sequential journey from travel to navigation and use of facilities.

## Core Principles

- **Task-based:** Answers "Can I get there and use the place?"
- **Sequential:** Follows the visitor journey (the Access Chain).
- **Maintenance-aware:** Documents how accessibility fails when routines break.
- **Machine-readable:** Structured for search and automated discovery.
- **HTML-first:** Prioritizes accessible web content over PDFs.

## How to Use This Toolkit

1. **Pick a Template:** Use the [templates]({{ "/templates/" | relative_url }}) to build your access guide.
2. **Review the Access Chain:** Ensure your content covers every link in the journey.
3. **Internal Governance:** Use the [maintenance checklist]({{ "/templates/maintenance-checklist/" | relative_url }}) to keep information accurate.
4. **Placement:** Follow the [website placement guidance]({{ "/publishing/website-placement/" | relative_url }}) to make sure visitors can find your information.

## Contributing

We welcome contributions of new templates, examples, and improvements to the framework. See [CONTRIBUTING.md]({{ "/community/contribute/" | relative_url }}) for details.

**Digital Accessibility:** This toolkit website follows WCAG 2.2 AA standards. See [ACCESSIBILITY.md](/ACCESSIBILITY.md) for our digital accessibility commitment and contributor requirements.

## AI Disclosure

This project values transparency about the use of AI in its development. The table below records which AI tools have contributed and in what capacity.

| AI Tool | Provider | Used for | Used at runtime | Browser-based AI |
|---|---|---|---|---|
| GitHub Copilot (Coding Agent) | GitHub / OpenAI | Generating and editing content, templates, framework pages, CSS, JavaScript, and CI configuration throughout the project | No | No |
| Claude (Sonnet / Opus) | Anthropic | Generating and editing content, templates, framework pages, and code as a coding agent | No | No |

**Notes:**

- **Runtime AI:** No LLM or AI model is invoked when the site is served or visited. The site is a static Jekyll build hosted on GitHub Pages.
- **Browser-based AI:** The read-aloud feature uses the browser's built-in [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) (a native browser capability, not an external AI model). No browser-based LLM is enabled by this toolkit.
- **Content provenance:** Most initial content was generated with AI assistance and has not yet been fully validated against real buildings. See the experimental warning at the top of this file.
- AI agents contributing to this repository are required by [AGENTS.md](AGENTS.md) to update this table when they add or change features.

## Automation

### JSON-LD Structured Data Generator

Any PR that adds or updates a file in `examples/_examples/` or modifies `templates/building-access-guide.md` will automatically receive a PR comment with a generated schema.org `CivicStructure` + `LocationFeatureSpecification` JSON-LD block. The generated markup is ready to paste into the `<head>` of a published access page.

The generator (`scripts/generate-jsonld.py`) detects eight accessibility features defined in `framework/machine-readable.md`: step-free entrance, accessible toilet, Changing Places toilet, assistive listening system, accessible parking, quiet space, power-assisted doors, and lift. Features default conservatively to `"unknown"` when not mentioned or ambiguous, and only resolve to `"true"` or `"false"` when the guide content is explicit.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
