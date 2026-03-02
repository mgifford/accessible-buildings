# Accessibility Commitment (ACCESSIBILITY.md)

> **Our commitment to digital accessibility for the Building Access Guide Toolkit**

## 1. Our Commitment

We believe accessibility is a subset of quality. This toolkit helps organizations communicate physical building accessibility, and **our own website must model digital accessibility best practice**.

This project commits to **[WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/)** standards for all digital content and interfaces.

See also: [Accessibility Statement](/about/accessibility-statement/) for our detailed conformance status.

## 2. Current Status

| Metric | Status / Value |
| :--- | :--- |
| **Target Standard** | WCAG 2.2 Level AA |
| **Testing Method** | Automated (pa11y-ci with axe-core) + Manual review |
| **CI/CD Enforcement** | Link checking, spelling, Jekyll build validation, pa11y-ci accessibility scan |
| **Last Full Audit** | February 2026 |

### What We Test

- **Automated Testing:** We run automated checks on the built site using industry-standard tools (axe-core engine)
- **Manual Testing:** Periodic keyboard-only navigation and screen reader testing
- **Link Integrity:** Automated link checking on every PR via lychee-action
- **Accessibility Testing:** pa11y-ci with axe + htmlcs engines runs against key pages on every PR and weekly
- **Build Validation:** Jekyll builds must succeed before merge

## 3. Accessibility Features Implemented

### 3.1 Color and Contrast
- All brand colors meet WCAG AA contrast ratios (4.5:1 minimum for normal text)
- CSS custom properties define accessible color palettes for both light and dark modes
- Footer text colors explicitly darkened for improved readability

**Code Reference:** [`assets/main.scss`](assets/main.scss) lines 10, 22, 33

### 3.2 Keyboard Accessibility
- All interactive elements are keyboard accessible
- Visible focus indicators on all focusable elements (2px outline with offset)
- Dropdown navigation works with both hover and keyboard focus (`:focus-within`)
- No keyboard traps
- Logical tab order follows visual layout

**Code References:**
- [`assets/main.scss`](assets/main.scss) lines 216-220 (focus styles)
- [`assets/main.scss`](assets/main.scss) lines 268-280 (keyboard-accessible dropdowns)
- [`_includes/header.html`](_includes/header.html) line 23 (tabindex on group titles)

### 3.3 Dark Mode Support
- Manual dark/light mode toggle with accessible button
- Theme toggle button includes proper ARIA labels that update with state
- System preference detection with `prefers-color-scheme`
- Theme preference persisted in localStorage
- All UI components maintain accessible contrast in both modes

**Code References:**
- [`assets/theme-toggle.js`](assets/theme-toggle.js) (complete implementation)
- [`assets/main.scss`](assets/main.scss) lines 31-72 (dark mode color variables)
- [`_includes/header.html`](_includes/header.html) line 34 (theme toggle button)

### 3.4 Semantic HTML and ARIA
- Proper use of semantic HTML5 elements (`<header>`, `<nav>`, `<main>`, `<footer>`)
- ARIA roles used appropriately (`role="banner"`)
- ARIA labels on interactive controls (theme toggle button)
- Form controls properly associated with labels

**Code Reference:** [`_includes/header.html`](_includes/header.html) line 1 (role="banner")

### 3.5 Link Accessibility
- Links have clear, descriptive text
- Footer links use underlines for visual distinction (not color alone)
- Text underline offset improves readability
- Hover and focus states provide visual feedback

**Code Reference:** [`assets/main.scss`](assets/main.scss) lines 305-313 (footer link styles)

### 3.6 Typography and Readability
- Modern web font (Inter) with system font fallbacks
- Text scaling support (text-spacing-trim, text-autospace)
- Font smoothing for improved rendering
- Readable line heights and spacing

**Code Reference:** [`assets/main.scss`](assets/main.scss) lines 6-16, 74-85

## 4. Contributor Requirements

To contribute to this repository, please follow these guidelines:

### Before Submitting a PR
1. **Test with keyboard only:** Ensure all interactive elements work without a mouse
2. **Check color contrast:** Verify any new colors meet WCAG AA standards (use browser DevTools or online checkers)
3. **Validate HTML:** Use the W3C Markup Validation Service
4. **Test in both themes:** Check light mode and dark mode appearance
5. **Follow existing patterns:** Match the accessibility patterns in existing code

### Jekyll and HTML
- Use semantic HTML elements
- Provide alt text for all images (use empty alt="" for decorative images)
- Maintain proper heading hierarchy (don't skip levels)
- Ensure sufficient color contrast for any custom styling

### CSS and Styling
- Use CSS custom properties (variables) for colors to support theming
- Include `:focus` styles alongside `:hover` styles
- Don't rely on color alone to convey information
- Test at 200% zoom to ensure content remains usable

### JavaScript
- Ensure any interactive components work with keyboard
- Update ARIA attributes dynamically when UI state changes
- Test with JavaScript disabled where appropriate
- Don't create keyboard traps

### Documentation
- Write in plain language
- Use proper Markdown heading hierarchy
- Include descriptive link text (avoid "click here")

## 5. Reporting Issues

We take accessibility seriously. If you discover an accessibility barrier, please report it:

### How to Report
- **[Report an Issue on GitHub](https://github.com/mgifford/accessible-buildings/issues/new)**
- Label your issue with `accessibility` if possible
- Include:
  - What you were trying to do
  - What happened instead
  - Your browser, OS, and assistive technology (if applicable)
  - Steps to reproduce

### Our Response Commitment
- We aim to respond to accessibility issues within **7 business days**
- Critical issues that prevent core functionality will be prioritized
- We will provide updates on progress and expected timelines

### Severity Guidelines
- **Critical:** Prevents a user from completing a core task (e.g., cannot navigate to templates, cannot read main content)
- **High:** Significant difficulty, but a workaround exists
- **Medium:** Annoyance or inconsistent experience
- **Low:** Minor issue with minimal user impact

## 6. Testing Infrastructure

### Continuous Integration (CI)
Our CI pipeline includes several accessibility-related checks:

- **Jekyll Build:** Ensures site builds without errors
- **Link Checking:** Validates all internal and external links (lychee-action)
- **Spelling:** Prevents typos that could cause confusion (codespell)
- **Accessibility:** pa11y-ci with axe and htmlcs engines scans key pages against WCAG2AA on every PR and weekly

**See:** [`.github/workflows/ci.yml`](.github/workflows/ci.yml) and [`.github/workflows/accessibility.yml`](.github/workflows/accessibility.yml)

### Local Testing Tools
We recommend these tools for contributors:

- **axe DevTools** (browser extension): Free accessibility testing
- **WAVE** (browser extension): Visual accessibility evaluation
- **Lighthouse** (Chrome DevTools): Automated audits including accessibility
- **NVDA/JAWS/VoiceOver:** Screen reader testing
- **Keyboard only:** Unplug your mouse and navigate the site

### Automated Coverage Limitations
Automated tools can only catch ~30-50% of accessibility issues. We rely on:
- Manual keyboard testing
- Screen reader testing
- User feedback
- Community review

## 7. Trusted Accessibility Resources

We align our practices with guidance from trusted sources in the accessibility community.

For a comprehensive, machine-readable list of vetted accessibility resources, see:
**[TRUSTED_SOURCES.yaml](https://github.com/mgifford/ACCESSIBILITY.md/blob/main/examples/TRUSTED_SOURCES.yaml)**

### Primary Standards and Guidelines
- **[WCAG 2.2](https://www.w3.org/TR/WCAG22/)** - W3C Web Content Accessibility Guidelines
- **[ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)** - W3C guidance on ARIA usage
- **[WebAIM](https://webaim.org/)** - Practical accessibility resources and training

### Tools and Testing
- **[axe-core](https://github.com/dequelabs/axe-core)** - Open source accessibility testing engine
- **[pa11y](https://pa11y.org/)** - Automated accessibility testing
- **[Deque University](https://dequeuniversity.com/)** - Accessibility training and reference

### Government and Standards Bodies
- **[Section 508](https://www.section508.gov/)** - US federal accessibility requirements
- **[Government of Canada Digital Standards](https://a11y.canada.ca/)** - Canadian accessibility guidance
- **[GOV.UK Accessibility](https://www.gov.uk/service-manual/helping-people-to-use-your-service/making-your-service-accessible-an-introduction)** - UK government service manual

### Community Resources
- **[The A11Y Project](https://www.a11yproject.com/)** - Community-driven accessibility knowledge
- **[Adrian Roselli's Blog](https://adrianroselli.com/)** - Practical WCAG and ARIA guidance
- **[Inclusive Components](https://inclusive-components.design/)** - Accessible component patterns

## 8. Related Documentation

This file focuses on **digital accessibility** (WCAG compliance for our website).

For information about **physical building accessibility** (the content this toolkit helps you publish), see:
- [About the Building Access Guide](/about/)
- [Access Chain Framework](/framework/access-chain/)
- [Templates](/templates/)
- [Governance and Maintenance](/publishing/governance/)

## 9. Scope and Maintenance

### What This Document Covers
- Website accessibility (WCAG 2.2 AA compliance)
- Code and template accessibility
- Testing and contribution requirements
- Issue reporting process

### What This Document Does NOT Cover
- Physical building accessibility standards (see [About](/about/))
- Legal compliance advice (consult accessibility lawyers)
- Individual building access guides (see [Examples](/examples/))

### Document Maintenance
- **Owner:** Repository maintainers
- **Review Frequency:** Every 6 months or when significant changes are made
- **Last Updated:** February 2026
- **Next Review:** August 2026

## 10. AI Agent Instructions

If you are an AI coding assistant (GitHub Copilot, Cursor, Claude, etc.), please:

1. **Always maintain WCAG 2.2 AA compliance** when suggesting code changes
2. **Include focus states** alongside hover states for interactive elements
3. **Use semantic HTML** elements rather than generic divs
4. **Provide alt text** for images (context-appropriate, empty for decorative)
5. **Maintain keyboard accessibility** for all interactive features
6. **Test color contrast** before suggesting color changes
7. **Update ARIA attributes** when changing interactive component states
8. **Preserve existing accessibility patterns** in this codebase
9. **Reference this document** and [AGENTS.md](AGENTS.md) for detailed guidelines

### Component-Specific Guidance
When working with specific components, consult these resources:
- **Forms:** [W3C Form Instructions](https://www.w3.org/WAI/tutorials/forms/)
- **Navigation:** [W3C Menu Tutorial](https://www.w3.org/WAI/tutorials/menus/)
- **Images:** [W3C Images Tutorial](https://www.w3.org/WAI/tutorials/images/)
- **Tables:** [W3C Tables Tutorial](https://www.w3.org/WAI/tutorials/tables/)

For additional AI-specific guidance, see: [AGENTS.md](AGENTS.md)

---

**This commitment reflects our dedication to making the Building Access Guide Toolkit accessible to all users, regardless of ability or assistive technology.**
