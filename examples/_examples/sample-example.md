---
layout: page
title: "City Museum of Art"
building_type: "Museum"
country: "UK"
url: "https://example.com/museum/access"
last_reviewed: 2024-05-12
evaluation_summary: "An excellent example of HTML-first guidance with a strong focus on the sensory profile and arrival logistics."

rubric:
  discoverability: 5
  arrival_clarity: 4
  entrance_clarity: 5
  internal_navigation: 4
  facilities_clarity: 5
  program_accommodations: 3
  transparency: 5
  format_quality: 5

strengths:
  - "Integrated into 'Visit' page dropdown."
  - "Detailed lift dimensions and weight limits."
  - "Clear distinction between step-free and alternate entrances."
  - "Honest assessment of the inaccessible basement galleries."

gaps:
  - "Missing hearing loop locations for individual galleries."
  - "No clear signage for the quiet space."
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
The guide is linked directly from the 'Plan Your Visit' landing page and the footer. It correctly uses the `/visit/access/` URL pattern.

## Format Notes
Content is hosted directly in HTML. A 'Printable Version' is offered as an accessible PDF, but it is secondary to the web content.
