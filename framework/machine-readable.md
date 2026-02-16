---
layout: page
title: Machine-Readable Accessibility
permalink: /framework/machine-readable/
---

# Making Accessibility Machine-Readable

Publishing accessibility information in HTML is the first step. The next step is making that information discoverable by search engines and assistive technologies through structured data.

## Why Structure Data?

When you use structured data (like Schema.org), search engines can:
- Display accessibility features directly in search results.
- Help users find "accessible parking near me."
- Verify the information automatically for accessibility-focused apps.

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
