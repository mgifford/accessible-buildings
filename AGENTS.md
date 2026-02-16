# AGENTS.md

## Purpose

This repository publishes a practical toolkit for describing the physical accessibility of buildings on the web.

It is not a digital accessibility statement generator. It is a publishing framework for visitor-facing, decision-grade information about arrival, entry, navigation, facilities, programs, and known constraints.

The site is built for GitHub Pages with Jekyll.

## Non-negotiables

- HTML-first. PDFs may be offered as secondary downloads only.
- Task-based content. People need to answer “Can I get there and use the place safely and independently?”.
- Access chain model. Accessibility is sequential and can fail at any link.
- Maintenance accountability. Accessibility degrades when routes are blocked, lifts fail, signage is moved, or temporary setups create barriers.
- Neutral and building-type agnostic. Museums are examples, not the scope.

## What to build and maintain

### 1. Core pages
- `index.md`: clear entry point and navigation.
- `access-chain.md`: the conceptual model and failure modes.
- `website-placement.md`: where this content belongs on websites and how it should be linked.
- `governance.md`: ownership, review cadence, change triggers, and public change log model.
- `resources.md`: curated references and tooling.
- `examples.md`: how examples are structured and evaluated.

### 2. Templates
All templates must be immediately copy-paste usable.

Minimum template set:
- `templates/building-access-guide.md` (primary)
- `templates/summary-template.md` (short visitor summary)
- `templates/arrival-template.md` (arrival by mode)
- `templates/facilities-template.md` (toilets, seating, quiet spaces, etc.)
- `templates/sensory-profile.md` (sensory conditions and supports)
- `templates/maintenance-checklist.md` (internal operations checklist)

### 3. Examples collection
Examples are a Jekyll collection under:
- `examples/_examples/`

Each example must include:
- A public URL.
- Last reviewed date.
- Building type and country.
- Strengths and gaps using this repo’s evaluation rubric.
- Notes on website placement and discoverability.
- Whether content is HTML-first or PDF-only.

## Content rules

### Visitor-facing content must:
- Use concrete, operational details (distances, surfaces, routes, entrances, door types).
- State what is not accessible and provide alternatives.
- Separate “features exist” from “how to use them”.
- Avoid vague assertions like “fully accessible” unless scoped and defined.

### Internal/ops content must:
- Translate accessibility obligations into routine checks.
- Include temporary barrier risks (events, installations, queue barriers).
- Include failure plans (lift down, powered doors off, alternate entrance locked).
- Require staff knowledge, not just infrastructure.

### Language rules
- No marketing language.
- No legal advice. You may cite laws/standards as context but do not present compliance determinations.
- Avoid US-only framing. Where US ADA concepts appear, pair them with general equivalents (step-free, accessible toilet, etc.).
- Prefer plain language over jargon.
- Use consistent terms: “step-free”, “accessible toilet”, “Changing Places”, “hearing loop”, “quiet space”.

## Structured data guidance

When adding machine-readable guidance:
- Keep it implementable without custom build tooling.
- Provide copy-paste JSON-LD examples.
- Prefer conservative claims. If a feature’s status is unknown, say “unknown”.

Do not invent a “standard URL.” Recommend patterns (e.g., `/visit/access/`, `/access-guide/`) and emphasize cross-linking from Contact and Visit pages.

## Evidence handling

When incorporating reference material:
- Summarize and translate it into templates and checklists.
- Do not paste long excerpts.
- Attribute sources in `resources.md`.
- If any repository content is derived from an uploaded reference document, keep it high-level and operational, not a reproduction.

## What agents should not do

- Do not turn the project into a list of links.
- Do not ship a single monolithic page.
- Do not depend on Ruby plugins not supported by GitHub Pages.
- Do not add heavy JS frameworks.
- Do not create content that implies a building is compliant.

## Repository conventions

### Jekyll
- Use the `minima` theme unless explicitly changed.
- Use front matter on all pages.
- Use `_data/*.yml` for reusable structured content.
- Use `_includes/*.html` sparingly for repeated UI patterns.

### File changes
- Prefer small, reviewable PR-sized changes.
- When editing templates, preserve backwards compatibility where possible.
- If you rename URLs, add a redirect note in `README.md` (GitHub Pages does not support server-side redirects by default).

## Example evaluation rubric (minimum)

Every example must be assessed against:

1. Discoverability
   - Linked from footer and contact/visit pages.
2. Arrival clarity
   - Transit, taxi, cycling, driving guidance.
3. Entrance clarity
   - Step-free routes, door types, alternate entrance instructions.
4. Internal navigation
   - Lifts, signage, route widths, temporary barrier handling.
5. Facilities clarity
   - Toilets, Changing Places, seating, quiet space.
6. Program accommodations
   - Assistive listening, captions, tactile, staff help.
7. Transparency
   - Explicit constraints and workarounds.
8. Format quality
   - HTML-first, accessible downloads, printable page.

## Contribution workflow

Agents should:
1. Propose changes in a brief plan (files to add/edit).
2. Implement changes.
3. Validate:
   - Jekyll front matter correctness
   - Internal links work
   - Navigation is coherent
4. Add or update a short entry in `README.md` if behavior changes.

## Success criteria

The repository is successful when an organization can:
- Copy a template page into their site.
- Fill it out without guessing what to include.
- Publish it in a predictable location.
- Keep it accurate via a maintenance checklist.
- Provide enough detail that a disabled visitor can plan with confidence.

## Accessibility Requirements (Non-Negotiable)

This site publishes guidance about accessibility. It must model best practice.

All content and code in this repository must meet WCAG 2.2 AA at minimum.

This requirement applies to:
- All templates
- All example pages
- All navigation and components
- All includes and layout files
- All future changes

### 1. WCAG 2.2 Conformance

The site must conform to WCAG 2.2 Level AA.

At minimum this includes, but is not limited to:

- Fully keyboard operable (no keyboard traps).
- Visible focus indicators.
- Logical focus order.
- Proper heading hierarchy.
- Landmarks and semantic HTML.
- Sufficient color contrast.
- No reliance on color alone.
- Meaningful link text.
- Proper form labeling.
- Accessible tables.
- No autoplay media.
- Captions for video.
- Transcripts for audio.
- No pointer-only interactions.
- No hover-only content.
- Target size compliance (2.5.8).
- Dragging alternatives (2.5.7).
- Focus not obscured (2.4.11 / 2.4.12).
- Accessible authentication patterns if ever introduced (3.3.8).

Do not rely on theme defaults. Verify.

### 2. Automated Testing Requirements

Every change must pass:

- axe-core automated testing
- Keyboard-only navigation testing

#### axe Testing

Use one of:
- axe DevTools browser extension
- axe CLI in CI
- pa11y with axe engine
- GitHub Action with axe

No known serious or critical violations may be merged.

If an issue cannot be resolved, it must be:
- Documented in an issue
- Assigned
- Not ignored silently

#### Keyboard Testing

Every interactive element must be tested for:

- Tab navigation
- Shift+Tab reverse navigation
- Visible focus indicator
- Logical reading order
- No focus traps
- All functionality operable without a mouse

Testing must include:
- Navigation menu
- In-page links
- Example cards
- Expandable sections (if used)
- Any embedded media

### 3. CI Enforcement (Recommended)

If GitHub Actions are introduced:

- Add automated axe checks on PR.
- Fail the build on serious violations.
- Optionally integrate pa11y-ci.

Accessibility regressions must block merges.

### 4. Design and Theme Constraints

When modifying layout or styling:

- Do not remove visible focus styles.
- Do not introduce low-contrast color combinations.
- Do not hide content on focus.
- Do not rely on CSS-only hover interactions.
- Do not introduce inaccessible accordions or tabs without ARIA correctness.

Prefer:
- Native HTML elements
- Semantic markup
- Minimal JavaScript

### 5. Templates Must Model Accessibility

All templates in `/templates/` must:

- Use correct heading levels.
- Demonstrate accessible table markup.
- Provide skip links where appropriate.
- Include example alt text for images.
- Include caption and transcript placeholders for video.
- Include instructions for accessible PDF export (if offered).

This toolkit must not publish inaccessible examples.

### 6. Accessibility Review Before Release

Before tagging a release:

- Run full axe scan.
- Test keyboard-only navigation.
- Test at 200% zoom.
- Test in high contrast mode.
- Verify focus indicators are visible.
- Validate HTML.

Accessibility must be treated as a release criterion.

### 7. Accessibility Debt Policy

If accessibility defects are discovered:

- Fix immediately if minor.
- Create an issue and label it `accessibility`.
- Do not defer without documentation.
- Do not suppress warnings.

This project’s credibility depends on its own conformance.

## Canonical Resource Preservation Policy

This repository depends on external guidance, frameworks, and public materials
that define how physical accessibility information should be structured.

External sites may:
- Move
- Disappear
- Change content
- Remove documents
- Break links

To prevent loss of institutional knowledge, critical reference materials must
be preserved inside this repository as structured Markdown summaries.

This is not a scraping exercise. It is a structured preservation effort.

### 1. What Should Be Preserved

Only preserve materials that:

- Define structured accessibility guidance.
- Provide operational or publishing models.
- Introduce frameworks such as the Access Chain.
- Define maintenance responsibilities.
- Provide templates or structured content patterns.

Do not preserve:
- Marketing copy.
- General advocacy pages.
- Entire government statutes.
- Full-length copyrighted works unless explicitly allowed.

### 2. How to Preserve a Resource

When incorporating a resource:

1. Create a new file under:
   `/resources/canonical/`

2. Use this filename format:
   `YYYY-OrgName-ShortTitle.md`

3. The file must contain:

   - Title
   - Original organization
   - Original publication date (if known)
   - Original URL
   - Date archived
   - Summary of purpose
   - Structured extraction of key concepts
   - Operational implications for this toolkit
   - What has been intentionally omitted

4. Do NOT reproduce copyrighted material verbatim beyond short excerpts.
   Summarize and translate into structured guidance.

5. If a public domain or explicitly open-licensed document is included,
   note the license clearly at the top of the file.

### 3. Preservation Style

Canonical resource files must:

- Convert narrative guidance into structured headings.
- Extract actionable requirements.
- Translate general principles into checklists.
- Identify failure points.
- Identify maintenance implications.
- Avoid copying large blocks of prose.

This repository preserves structure and meaning, not formatting.

### 4. Provenance Block (Required)

Every canonical resource file must begin with:

---
Title:
Organization:
Original Publication Date:
Original URL:
Archived URL (if applicable):
License:
Date Added to Toolkit:
Added By:
---

If license is unclear, note:
"License not explicitly stated. Summary only."

### 5. Relationship to Templates

Every canonical resource added must:

- Map to at least one template section.
- Identify which part of the toolkit it informs.
- Not exist as an isolated archive.

### 6. Updating Canonical Resources

If an original source is updated:

- Add a new version file.
- Do not overwrite the prior summary.
- Note differences in a change log section.
- Preserve version history.

This toolkit must remain historically traceable.

### 7. Avoid Legal Risk

If there is uncertainty about copyright:

- Do not reproduce full text.
- Provide structured summary only.
- Link to the source.
- Prefer archived copies for stability.