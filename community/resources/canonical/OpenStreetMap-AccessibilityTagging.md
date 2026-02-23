---
Title: OpenStreetMap Accessibility Tagging Standards
Organization: OpenStreetMap Foundation
Original Publication Date: Ongoing (community-maintained)
Original URL: https://wiki.openstreetmap.org/wiki/Key:wheelchair
Archived URL: N/A
License: Open Database License (ODbL) and CC-BY-SA 2.0
Date Added to Toolkit: 2026-02-22
Added By: Building Access Guide Toolkit
---

## Purpose

OpenStreetMap (OSM) is a collaborative mapping project that includes comprehensive accessibility tagging standards developed and maintained by the global community. These standards provide structured, machine-readable ways to describe physical accessibility features of buildings and spaces.

## Why OSM Accessibility Standards Matter

1. **Global standardization**: Battle-tested tagging schemas used worldwide
2. **Interoperability**: Enables data sharing across accessibility mapping projects
3. **Active maintenance**: Community continuously refines and extends tags
4. **Machine-readable**: Structured format suitable for apps and services
5. **Open license**: Free to use and adapt

## Core Wheelchair Accessibility Tags

### Primary Tag: `wheelchair=*`

The most fundamental tag for describing wheelchair accessibility:

- **`wheelchair=yes`**: Fully accessible with no barriers
- **`wheelchair=no`**: Not accessible (steps, narrow doors, or other barriers)
- **`wheelchair=limited`**: Accessible with assistance or partial accessibility

**Important**: "Limited" should be clarified with additional tags describing specific constraints.

### Specific Facility Tags

- **`wheelchair:toilet=yes/no/limited`**: Accessible restroom availability
- **`wheelchair:parking=yes/no`**: Designated accessible parking spaces
- **`wheelchair:description=*`**: Free-text field for additional detail

## Entry and Access Feature Tags

### Entrances
- **`entrance=main/secondary/service`**: Entry point type
- **`entrance:wheelchair=yes/no`**: Wheelchair accessibility of specific entrance
- **`automatic_door=yes/no`**: Powered automatic doors
- **`door:width=*`**: Door width in centimeters
- **`door:type=swing/automatic/revolving`**: Door mechanism

### Vertical Access
- **`ramp=yes/no`**: Ramp availability
- **`ramp:wheelchair=yes/no/limited`**: Ramp usability for wheelchairs
- **`lift=yes/no`**: Elevator/lift availability
- **`stairs=yes/no`**: Stair presence

## Navigation and Wayfinding Tags

### Assistive Features
- **`braille=yes/no`**: Braille signage availability
- **`tactile_paving=yes/no`**: Tactile ground surface indicators
- **`hearing_loop=yes/no`**: Induction loop system for hearing aids
- **`audio_signals=yes/no`**: Audible navigation cues

### Service Support
- **`service:guide_dog=yes/no`**: Guide dog policy
- **`mobility_scooter=yes/no`**: Mobility scooter accessibility

## Measurement and Detail Tags

OSM encourages precise measurements where possible:

- **`step:height=*`**: Step height in centimeters
- **`step:count=*`**: Number of steps
- **`width=*`**: Passage width in meters
- **`capacity:wheelchair=*`**: Number of wheelchair users that can be accommodated

## Operational Implications for Building Access Guides

### Alignment Opportunities

When creating building access documentation using this toolkit, consider OSM tagging as:

1. **Validation reference**: Check if your descriptive language aligns with OSM's structured categories
2. **Metadata layer**: Add OSM-style tags to your HTML using data attributes or Schema.org properties
3. **Mapping integration**: Encourage tagging your building in OSM to improve discoverability
4. **Consistency check**: Use OSM categories to ensure you're covering all major accessibility dimensions

### Translation Table: Toolkit Terms → OSM Tags

| Building Access Guide Term | OSM Tag Equivalent |
|----------------------------|-------------------|
| Step-free entrance | `entrance:wheelchair=yes` + `ramp=yes` or `stairs=no` |
| Accessible toilet | `wheelchair:toilet=yes` |
| Changing Places toilet | `toilets:wheelchair=yes` + `changing_table=yes` |
| Assistive listening system (Loop) | `hearing_loop=yes` |
| Accessible parking | `wheelchair:parking=yes` + `capacity:disabled=*` |
| Power-assisted doors | `automatic_door=yes` |
| Quiet space | No direct tag; use `amenity=*` + description |

### What This Toolkit Adds Beyond OSM

OSM tagging is excellent for **structured features**, but building access guides need:

- **Operational context**: "The lift is located past the reception desk on the right"
- **Failure modes**: "If the main entrance is closed, use the north entrance"
- **Temporary conditions**: "During events, accessible parking may be limited"
- **Maintenance state**: "The ramp is inspected monthly"
- **Sequential guidance**: Full journey from arrival to exit

Use OSM tags for **what exists**. Use this toolkit's narrative templates for **how to use it**.

## Implementation: Combining OSM Tags with Building Access Guides

### In HTML Markup

```html
<div itemscope itemtype="https://schema.org/Place" 
     data-osm-wheelchair="yes" 
     data-osm-wheelchair-toilet="yes"
     data-osm-hearing-loop="yes">
  
  <h2 itemprop="name">Main Library</h2>
  <p>The main entrance has a power-assisted door and ramp access...</p>
</div>
```

### In Structured Data

Combine Schema.org's `LocationFeatureSpecification` with OSM semantics:

```json
{
  "@context": "https://schema.org",
  "@type": "CivicStructure",
  "name": "Main Library",
  "amenityFeature": [
    {
      "@type": "LocationFeatureSpecification",
      "name": "wheelchair",
      "value": "yes"
    },
    {
      "@type": "LocationFeatureSpecification",
      "name": "wheelchair:toilet",
      "value": "yes"
    }
  ]
}
```

## Intentional Omissions

This summary excludes:

- Full OSM tagging documentation (see wiki for complete reference)
- Historical tag changes and deprecations
- Regional tagging variations
- Advanced mapping editor workflows

## Resources

- [OSM Wiki: Key:wheelchair](https://wiki.openstreetmap.org/wiki/Key:wheelchair)
- [OSM Wiki: Accessibility](https://wiki.openstreetmap.org/wiki/Accessibility)
- [Wheelmap.org](https://wheelmap.org): Public OSM-based accessibility map

## Maintenance Notes

OSM tagging is community-evolved. New tags are proposed through the OSM proposal process. Check the wiki regularly for updates, especially around emerging assistive technologies and new facility types.
