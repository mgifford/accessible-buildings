# Copilot Instructions

This repository publishes a practical toolkit for describing the physical accessibility of buildings on the web. It is built with Jekyll for GitHub Pages.

## Key Instruction Files

Before making any changes, read these files in full:

- **[AGENTS.md](../AGENTS.md)** — Primary instructions for coding agents: project purpose, non-negotiables, content rules, repository conventions, contribution workflow, and success criteria.
- **[ACCESSIBILITY.md](../ACCESSIBILITY.md)** — Non-negotiable accessibility requirements: WCAG 2.2 AA conformance, automated testing, keyboard testing, design constraints, and template accessibility standards. This project publishes accessibility guidance and must itself model best practice.

## Repository Layout

```
/                        # Root: AGENTS.md, ACCESSIBILITY.md, README.md, _config.yml
/templates/              # Copy-paste ready templates for building access guides
/framework/              # Conceptual guidance (access chain, photo guidance, event spaces, etc.)
/community/              # Examples, resources, and canonical preserved references
/publishing/             # Guidance on website placement and governance
/about/                  # About page and accessibility statement
/_data/                  # YAML data files (navigation, field definitions, resources)
/_includes/              # Jekyll HTML includes (header, footer, navigation)
/assets/                 # CSS (main.scss) and JavaScript (personalization, read-aloud)
/.github/workflows/      # CI workflows including link checker and accessibility tests
```

## Technology Stack

- **Jekyll** with the `minima` theme, hosted on GitHub Pages
- **No Ruby plugins** beyond those supported by GitHub Pages
- **Minimal JavaScript** — prefer native HTML and semantic markup
- Front matter required on all pages

## Coding Conventions

- HTML-first; no heavy JS frameworks
- WCAG 2.2 AA is a release criterion — run axe and keyboard tests on every change
- Use `_data/*.yml` for reusable structured content
- Use `#` (empty anchor) for placeholder links in templates to avoid CI link-checker failures
- Use `nonspeaking` (not `non-verbal`) when referring to people who use AAC
- No marketing language, no legal compliance determinations, no US-only framing
- Consistent terminology: "step-free", "accessible toilet", "Changing Places", "hearing loop", "quiet space"
- Canonical resource files go in `/community/resources/canonical/` following the provenance block format defined in AGENTS.md

## CI

The `.github/workflows/` directory contains automated checks. Ensure all workflows pass before merging. Accessibility regressions must block merges.
