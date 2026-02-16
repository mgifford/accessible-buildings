---
layout: page
title: Resources
permalink: /community/resources/
---

# Accessibility Resources

This toolkit is built on existing best practices and international frameworks. Here are the key resources that inform our guidance.

## Frameworks and Guidance

{% for resource in site.data.resources %}
### [{{ resource.title }}]({{ resource.url }})
**Organization:** {{ resource.org }}
**Type:** {{ resource.type }}
*{{ resource.notes }}*
{% endfor %}

## Government Guidance

- **[ADA.gov (USA)](https://www.ada.gov):** Official guidance on the Americans with Disabilities Act. Use their museum and small business guides for conceptual models.
- **[GOV.UK Accessibility (UK)](https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-bodies):** Standards for public sector accessibility.
- **[Australian Human Rights Commission (AU)](https://humanrights.gov.au/our-work/disability-rights/guides/access-buildings-and-services):** Guidelines on access to buildings and services.

## Technical Standards

- **[WCAG 2.2 (W3C)](https://www.w3.org/TR/WCAG22/):** The global standard for web accessibility. This toolkit follows WCAG 2.2 AA.
- **[ISO 21542:2021](https://www.iso.org/standard/71518.html):** Building construction — Accessibility and usability of the built environment.

## Featured: Tactile Mapping

Tactile maps are essential for visitors who are blind or have low vision. Modern technology has made these significantly more accessible to create.

- **[LightHouse Tactile Mapping Project](https://www.youtube.com/watch?v=n8p2dxnoV-M):** Learn how the LightHouse for the Blind and Visually Impaired uses tactile maps to empower independent navigation.
- **[3D Printed Tactile Maps](https://www.instructables.com/Tactile-Map-for-People-With-Blindness-or-Partial-B/):** A DIY guide to creating 3D printed maps. Many public libraries now offer 3D printing services that can be used for this purpose.

## Canonical Reference Extracts

We maintain structured extracts of key guidance documents to ensure their operational insights are preserved.

- [View Canonical Resources]({{ "/community/resources/canonical/" | relative_url }})
