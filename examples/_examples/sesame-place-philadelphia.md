---
layout: page
title: "Sesame Place Philadelphia"
building_type: "Theme Park"
country: "USA"
url: "https://sesameplace.com/philadelphia/help/accessibility-guide/"
last_reviewed: 2025-01-01
evaluation_summary: "Strong example of comprehensive accessibility documentation for a theme park, with detailed sensory guide and park accessibility guide. Notable for providing multiple formats and detailed ride-by-ride accessibility information."

rubric:
  discoverability: 4
  arrival_clarity: 4
  entrance_clarity: 4
  internal_navigation: 5
  facilities_clarity: 5
  program_accommodations: 5
  transparency: 5
  format_quality: 4

strengths:
  - "Comprehensive sensory guide detailing stimuli for each attraction"
  - "Detailed park accessibility guide with ride-by-ride information"
  - "Clear information about Guest Assistance Pass program"
  - "Multiple formats provided (web and PDF)"
  - "Specific measurements and requirements for each ride"
  - "Clear wheelchair/mobility device policies"
  - "Detailed facilities information including accessible restrooms and quiet spaces"
  - "Strong transparency about limitations and restrictions"

gaps:
  - "Sensory guide is located separately from main accessibility guide (different URL path)"
  - "Would benefit from HTML-first presentation of sensory information rather than PDF-only"
  - "Some navigation required to find all accessibility resources"
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

Sesame Place provides multiple accessibility resources:

1. **Main Accessibility Guide:** Located at `/help/accessibility-guide/`
   - Accessible from Help section
   - Provides comprehensive park accessibility information
   - Links to downloadable PDF version

2. **Sensory Guide:** Separate location (migrated media path)
   - Not immediately discoverable from main accessibility page
   - Provides valuable ride-by-ride sensory information
   - Only available as PDF download

### Co-location Recommendation

The sensory guide contains critical decision-making information for visitors with sensory sensitivities. Best practice would be to:
- Integrate sensory information into the main accessibility guide
- Provide both HTML and PDF versions
- Use consistent URL structure (e.g., `/help/accessibility-guide/sensory/`)
- Cross-link between resources

## Format Notes

Content is primarily provided as downloadable PDFs with web-based navigation:

- **Park Accessibility Guide 2025:** Comprehensive PDF with ride details, facility information, and policies
- **Sensory Guide:** PDF with detailed sensory profiles for attractions
- Web presence provides navigation and high-level information

### Format Strengths
- PDFs are well-structured and accessible
- Information is detailed and operational
- Multiple entry points exist

### Format Improvements
- HTML-first presentation would improve searchability
- Integrating sensory data into web interface would reduce need for separate downloads
- Single comprehensive accessibility landing page would improve discoverability

## Content Quality

Sesame Place excels in several areas:

### Ride-by-Ride Information
Each attraction includes:
- Transfer requirements
- Restraint systems
- Mobility device policies
- Height requirements
- Sensory characteristics (noise, light, motion)

### Sensory Profiles
Detailed breakdown of:
- Visual stimuli (darkness, flashing lights, projections)
- Auditory stimuli (volume levels, types of sounds)
- Physical motion characteristics
- Tactile elements
- Duration and intensity

### Operational Details
- Guest Assistance Pass procedures
- Service animal policies
- Wheelchair and ECV rental information
- Accessible parking locations
- Companion restroom locations
- Quiet space availability

## Key Lessons for Other Organizations

1. **Comprehensive Coverage:** Theme parks require detailed attraction-level information. Sesame Place demonstrates thorough documentation.

2. **Sensory Information:** The separate sensory guide recognizes that sensory processing needs are distinct from mobility accessibility.

3. **Transparency:** Clear communication about what is and isn't accessible, with specific reasons.

4. **Multiple Audiences:** Content serves both advance planners and on-site decision makers.

5. **Integration Opportunity:** While comprehensive, consolidating all accessibility resources into a single discoverable location would improve the user experience.

## Implications for This Toolkit

Sesame Place demonstrates:

- Need for **sensory profile templates** distinct from but integrated with mobility/navigation guidance
- Value of **attraction/program-level** detail in addition to facility-level information  
- Importance of **Guest Assistance Pass/accommodation programs** as part of operational accessibility
- Benefits of **structured, repeatable formats** for describing similar spaces (rides, shows, attractions)

These principles apply beyond theme parks to museums, cultural venues, and any space with multiple distinct experiences within a facility.
