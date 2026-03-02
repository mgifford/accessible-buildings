---
layout: page
title: "Smithsonian Institution"
building_type: "Museum / Cultural Institution"
country: "USA"
url: "https://www.si.edu/visit/accessibility"
last_reviewed: 2026-03-02
evaluation_summary: "The Smithsonian Institution's central accessibility page is one of the most comprehensive in the museum sector. It covers physical access, programmatic access (audio descriptions, ASL, sign language tours), and tactile experiences across multiple buildings. Strong HTML-first presentation with detailed per-venue information. A reference-point example for large multi-site cultural organisations."

rubric:
  discoverability: 5
  arrival_clarity: 4
  entrance_clarity: 4
  internal_navigation: 4
  facilities_clarity: 4
  program_accommodations: 5
  transparency: 4
  format_quality: 4

strengths:
  - "Central accessibility landing page with clear links to individual museum accessibility guides"
  - "Dedicated sections for mobility, sight, hearing, and cognitive accessibility needs"
  - "Audio descriptions available for select collection items and exhibitions"
  - "American Sign Language (ASL) tours and signed content across multiple venues"
  - "Tactile tours and handling objects documented and available by advance booking"
  - "Sensory-friendly programming listed with dates and booking information"
  - "Accessibility information available in multiple formats including large print"
  - "Information covers all major Smithsonian sites, not just flagship buildings"
  - "Free admission removes financial barrier often associated with accessible programming"

gaps:
  - "Per-venue arrival information varies in detail—some venues have more specific transit and parking guidance than others"
  - "Mobile web audio tour provision is uneven across venues; some still rely on borrowed devices"
  - "Sensory profiles for individual exhibitions are not consistently published before opening"
  - "QR code wayfinding within galleries is not systematically documented across the estate"
  - "Large print and Easy Read guide availability varies by venue and is not always listed clearly"
---

# Evaluation: {{ page.title }}

{{ page.evaluation_summary }}

## Rubric Scores

| Criterion | Score / 5 |
| :--- | :--- |
| Discoverability | {{ page.rubric.discoverability }} |
| Arrival Clarity | {{ page.rubric.arrival_clarity }} |
| Entrance Clarity | {{ page.rubric.entrance_clarity }} |
| Internal Navigation | {{ page.rubric.internal_navigation }} |
| Facilities Clarity | {{ page.rubric.facilities_clarity }} |
| Program Accommodations | {{ page.rubric.program_accommodations }} |
| Transparency | {{ page.rubric.transparency }} |
| Format Quality | {{ page.rubric.format_quality }} |

## Building Details
- **Building Type:** {{ page.building_type }}
- **Country:** {{ page.country }}
- **Original URL:** [{{ page.url }}]({{ page.url }})
- **Last Evaluated:** {{ page.last_reviewed }}

## Notable Strengths
{% for strength in page.strengths %}
- {{ strength }}
{% endfor %}

## Identified Gaps
{% for gap in page.gaps %}
- {{ gap }}
{% endfor %}

## Website Placement Notes

The Smithsonian's accessibility information is positioned at `/visit/accessibility/` — a clear, expected URL pattern consistent with the recommendations in this toolkit. The page is linked from the main navigation under "Visit."

Key placement observations:

1. **Central hub model:** A single accessibility landing page aggregates links to per-venue guides. This is the right model for a multi-building organisation.
2. **Consistent link placement:** The Accessibility link appears in the Visit section navigation bar across all venue pages.
3. **Individual venue guides:** Each Smithsonian museum and gallery has its own accessibility page, consistent in format.

The main gap in placement is that accessibility information is not linked from the footer, which is a recommended location in this toolkit for findability by visitors who land on pages other than the Visit hub.

## Format Notes

Content is primarily HTML with clear heading structure. Downloadable resources (large print guides, audio content) are offered as secondary formats.

### Format Strengths
- HTML-first presentation throughout.
- Content is structured using headings and lists, not wall text.
- Telephone and email contact for accessibility requests is clearly presented.
- Individual programme listings include booking instructions.

### Format Improvements
- Some venue-level guides use embedded PDFs for floor plans—accessible HTML alternatives would improve the experience for screen reader users.
- Audio descriptions for collection items link to external media players rather than embedding player controls with accessible controls on the page.

## Content Quality

### Physical Access

The Smithsonian covers mobility access well, with step-free entrances identified, lift locations noted, and service animal policies stated. The level of detail on exact lift dimensions and threshold measurements varies across venues.

### Programmatic Access — A Sector-Leading Example

The Smithsonian is notable for the breadth and consistency of its programmatic access:

- **Audio Description:** Available for select exhibitions via the Smithsonian's audio tour platform. The National Museum of American History and the National Air and Space Museum have the most developed programmes.
- **Tactile Experiences:** The National Museum of Natural History has a dedicated "Discovery Room" with hands-on objects. Touch tours of specific collection items are available at several venues.
- **ASL Tours:** Available at multiple venues, provided by Deaf museum educators where possible.
- **Sensory-Friendly Events:** Documented and scheduled, with advance notice on the website.

### Comparison to Toolkit Frameworks

The Smithsonian model demonstrates several principles from the [Museum Accessibility page in this toolkit](/framework/museums/):

| Toolkit Principle | Smithsonian Implementation |
| :--- | :--- |
| Mobile web audio tour (no app) | Partial — some tours require app download |
| QR codes linking to accessible HTML | Not systematically documented |
| Tactile map at entrance | Available at some venues on request |
| Sensory profile for exhibitions | Ad hoc — not a standard pre-opening publication |
| Relaxed / sensory-friendly openings | Yes — scheduled and listed |
| Touch tours / handling sessions | Yes — Discovery Room and booked tours |
| Easy Read guides | Limited public documentation |
| Verbal description training for staff | Strong — trained museum educators |

## Key Lessons for Other Organisations

1. **Central hub + per-venue detail:** A single accessible landing page with consistent links to venue-specific information is scalable across multi-site organisations.

2. **Programmatic access as a standard offering:** Signed tours, tactile access, and sensory-friendly sessions should be scheduled, recurring, and listed on the same page as the visit plan—not as special requests.

3. **Free admission removes one barrier:** Where admission is charged, accessibility programme costs should not be in addition to entry fees.

4. **Staff expertise matters:** The quality of the Smithsonian's verbal description and signed tour programmes reflects investment in trained, specialist staff—not just infrastructure.

5. **Central coordination with venue autonomy:** Each Smithsonian venue adapts the core accessibility framework to its building and collection. This model scales well.

## Implications for This Toolkit

This example confirms the value of the [Museums and Cultural Venues framework page](/framework/museums/), specifically:

- The need for a layered audio description model (short label, medium tour stop, extended description).
- The gap between physical access documentation (generally strong) and operational programme documentation (uneven).
- The case for treating sensory profiles as standard pre-opening publication practice rather than optional additions.
