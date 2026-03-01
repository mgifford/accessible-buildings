---
layout: page
title: Resources
permalink: /community/resources/
---

# Accessibility Resources

This toolkit is built on existing best practices and international frameworks. Here are the key resources that inform our guidance.

---

## Quick Navigation

- **[Facility Standards and Design Guidance]({{ "/community/facility-standards/" | relative_url }}):** Building codes, technical standards, and universal design principles for physical infrastructure
- **[Canonical Reference Extracts]({{ "/community/resources/canonical/" | relative_url }}):** Preserved summaries of key operational guidance
- **[Best Practices Case Studies]({{ "/community/resources/sesame-place-best-practices/" | relative_url }}):** Real-world examples of comprehensive accessibility documentation
- **[Emergency Readiness Resources]({{ "/framework/emergency-readiness/" | relative_url }}):** Comprehensive emergency preparedness framework
  - [Digital-to-Physical Resilience]({{ "/community/resources/emergency-digital-physical/" | relative_url }})
  - [Advanced Digital Accessibility]({{ "/community/resources/emergency-digital-accessibility/" | relative_url }})
  - [Disability-Inclusive Disaster Infrastructure]({{ "/community/resources/emergency-disability-inclusive/" | relative_url }})

---

## Frameworks and Guidance

{% for resource in site.data.resources %}
### [{{ resource.title }}]({{ resource.url }})
**Organization:** {{ resource.org }}
**Type:** {{ resource.type }}
*{{ resource.notes }}*
{% endfor %}

## Government Guidance

- **[ADA.gov (USA)](https://www.ada.gov):** Official guidance on the Americans with Disabilities Act. Use their museum and small business guides for conceptual models.
- **[GOV.UK Accessibility (UK)](https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps):** Standards for public sector accessibility.
- **[City of Melbourne Accessibility (AU)](https://www.melbourne.vic.gov.au/community/health-support-services/disability-services/Pages/disability-services.aspx):** Resources for accessibility in the city.

## Technical Standards

- **[WCAG 2.2 (W3C)](https://www.w3.org/TR/WCAG22/):** The global standard for web accessibility. This toolkit follows WCAG 2.2 AA.
- **For physical infrastructure standards** (ADA, ISO, EN standards), see our [Facility Standards page]({{ "/community/facility-standards/" | relative_url }}).
- **[OpenStreetMap Accessibility](https://wiki.openstreetmap.org/wiki/Key:wheelchair):** Community-maintained accessibility tagging standards for machine-readable metadata. See our [OSM tagging reference]({{ "/community/resources/canonical/OpenStreetMap-AccessibilityTagging/" | relative_url }}).

## Featured: Tactile Mapping

Tactile maps are essential for visitors who are blind or have low vision. Modern technology has made these significantly more accessible to create.

- **[LightHouse Tactile Mapping Project](https://www.youtube.com/watch?v=n8p2dxnoV-M):** Learn how the LightHouse for the Blind and Visually Impaired uses tactile maps to empower independent navigation.
- **[3D Printed Tactile Maps](https://www.instructables.com/Tactile-Map-for-People-With-Blindness-or-Partial-B/):** A DIY guide to creating 3D printed maps. Many public libraries now offer 3D printing services that can be used for this purpose.

## Canonical Reference Extracts

We maintain structured extracts of key guidance documents to ensure their operational insights are preserved.

- [View Canonical Resources]({{ "/community/resources/canonical/" | relative_url }})

---

## Physical Infrastructure Standards

For building codes, technical specifications, and universal design principles, see:

- **[Facility Standards and Design Guidance]({{ "/community/facility-standards/" | relative_url }}):** Comprehensive collection of ADA standards, ISO standards, European standards, Canadian standards, and universal design frameworks

---

## Emergency Preparedness Resources

For comprehensive guidance on inclusive emergency management, we maintain specialized resource directories:

### Emergency Readiness Framework
- **[Emergency Readiness]({{ "/framework/emergency-readiness/" | relative_url }}):** Strategic overview of digital-to-physical resilience, multi-platform redundancy, and accessible emergency communications

### Specialized Emergency Resource Directories

1. **[Digital-to-Physical Resilience & Distributed Manufacturing]({{ "/community/resources/emergency-digital-physical/" | relative_url }})**
   - Distributed manufacturing and medical supplies
   - Print-ready emergency guides and templates
   - Tactile and sensory physical media
   - Technology for offline portability

2. **[Advanced Digital Accessibility & Multi-Platform Communications]({{ "/community/resources/emergency-digital-accessibility/" | relative_url }})**
   - Strategic planning and policy frameworks
   - Multi-platform and tactical communication
   - Academic and technological research
   - Implementation best practices

3. **[Disability-Inclusive & Sustainable Infrastructure]({{ "/community/resources/emergency-disability-inclusive/" | relative_url }})**
   - Policy and global standards
   - Sustainable and resilient digital design
   - Implementation and advocacy tools
   - Government and local registry examples

---

## Best Practices Case Studies

Learn from real-world examples of comprehensive accessibility documentation:

- **[Sesame Place Philadelphia Best Practices]({{ "/community/resources/sesame-place-best-practices/" | relative_url }}):** Analysis of attraction-level accessibility documentation and sensory guide frameworks from a theme park environment, with lessons applicable to museums, theaters, and other multi-experience venues.
