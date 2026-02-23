---
layout: page
title: Machine-Readable Accessibility
permalink: /framework/machine-readable/
---

# Making Accessibility Machine-Readable

Publishing accessibility information in HTML is the first step. The next step is making that information discoverable by search engines and assistive technologies through structured data.

## Why Structure Data?

When you use structured data (like Schema.org and OpenStreetMap tags), search engines and accessibility apps can:
- Display accessibility features directly in search results.
- Help users find "accessible parking near me."
- Verify the information automatically for accessibility-focused apps.
- Enable cross-platform data sharing and integration.

## Using Schema.org

The primary vocabulary for building accessibility is [LocationFeatureSpecification](https://schema.org/LocationFeatureSpecification).

### Example: JSON-LD for an Entrance

Add this to the `<head>` of your access page or specifically near the entrance description.

```json
{
  "@context": "https://schema.org",
  "@type": "CivicStructure",
  "name": "Main Library",
  "amenityFeature": [
    {
      "@type": "LocationFeatureSpecification",
      "name": "Step-free entrance",
      "value": "true",
      "hoursAvailable": "Mo-Fr 09:00-17:00"
    },
    {
      "@type": "LocationFeatureSpecification",
      "name": "Power-assisted doors",
      "value": "true"
    }
  ]
}
```

## Recommended Tags

Use these names in your `amenityFeature` array for maximum compatibility:

- **Step-free entrance**
- **Accessible toilet**
- **Changing Places toilet**
- **Assistive listening system** (Specify type: Loop, IR, FM)
- **Accessible parking**
- **Quiet space**

## Implementation Without Custom Tools

You don't need complex build tools to do this. You can manually include the JSON-LD script block in your HTML or use Jekyll's `_data` files to generate it dynamically.

### Simple Jekyll Approach

In your page front matter:

```yaml
accessibility:
  step_free_entrance: true
  accessible_parking: true
```

In your layout:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CivicStructure",
  "amenityFeature": [
    {% if page.accessibility.step_free_entrance %}
    {
      "@type": "LocationFeatureSpecification",
      "name": "Step-free entrance",
      "value": "true"
    }
    {% endif %}
  ]
}
</script>
```

---

## OpenStreetMap Accessibility Tagging

[OpenStreetMap (OSM)](https://www.openstreetmap.org) uses community-maintained accessibility tags that provide structured, machine-readable metadata about building accessibility. These tags are used by accessibility-focused mapping apps worldwide.

### Why Use OSM Tags?

- **Global standard**: Used by accessibility mapping projects worldwide
- **Interoperability**: Works across multiple platforms and apps
- **Machine-readable**: Structured format for automated processing
- **Active community**: Continuously maintained and improved

### Core OSM Accessibility Tags

Use these tags as HTML data attributes or in your structured data:

| Feature | OSM Tag | Values |
|---------|---------|--------|
| Wheelchair access | `wheelchair` | `yes`, `no`, `limited` |
| Accessible toilet | `wheelchair:toilet` | `yes`, `no`, `limited` |
| Accessible parking | `wheelchair:parking` | `yes`, `no` |
| Automatic doors | `automatic_door` | `yes`, `no` |
| Hearing loop | `hearing_loop` | `yes`, `no` |
| Ramp available | `ramp` | `yes`, `no` |
| Lift/elevator | `lift` | `yes`, `no` |
| Braille signage | `braille` | `yes`, `no` |
| Tactile paving | `tactile_paving` | `yes`, `no` |

[View complete OSM accessibility tagging reference]({{ "/community/resources/canonical/OpenStreetMap-AccessibilityTagging/" | relative_url }})

### Adding OSM Tags to Your HTML

You can include OSM tags as data attributes for machine processing:

```html
<div itemscope itemtype="https://schema.org/Place" 
     data-osm-wheelchair="yes" 
     data-osm-wheelchair-toilet="yes"
     data-osm-automatic-door="yes"
     data-osm-hearing-loop="yes">
  
  <h2 itemprop="name">Main Library</h2>
  <p>The main entrance has a power-assisted door and ramp access...</p>
</div>
```

### Combining Schema.org with OSM Semantics

Use OSM tag names in your Schema.org markup for consistency:

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
    },
    {
      "@type": "LocationFeatureSpecification",
      "name": "hearing_loop",
      "value": "yes"
    }
  ]
}
```

### OSM Tags vs. Building Access Narratives

**OSM tags are for structured features.** Your building access guide provides the operational context:

- OSM: `wheelchair=yes`
- Guide: "The main entrance has a ramp with a 1:12 gradient and power-assisted doors. If the main entrance is closed after hours, use the north entrance, which has similar features."

**Use both**: OSM tags for machine processing, narrative text for human decision-making.

---

## Mapping Your Building in OpenStreetMap

Consider adding your building's accessibility information directly to OpenStreetMap:

1. **Create an OSM account** at [openstreetmap.org](https://www.openstreetmap.org)
2. **Find your building** on the map
3. **Add accessibility tags** using the editor
4. **Link to your full access guide** using the `website` or `contact:website` tag

This makes your building discoverable in accessibility-focused apps like [Wheelmap.org](https://wheelmap.org).

---

## Resources

- [OpenStreetMap Accessibility Tagging Reference]({{ "/community/resources/canonical/OpenStreetMap-AccessibilityTagging/" | relative_url }})
- [OSM Wiki: Wheelchair Accessibility](https://wiki.openstreetmap.org/wiki/Key:wheelchair)
- [Schema.org LocationFeatureSpecification](https://schema.org/LocationFeatureSpecification)
