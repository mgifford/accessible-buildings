---
layout: page
title: Building Layout and Maps
permalink: /framework/building-layout/
---

# Building Layout and Maps

For many visitors, especially those with mobility, sensory, or cognitive disabilities, understanding the layout of a building before they arrive is essential for a successful visit.

## Why Maps and Layouts Matter
A map isn't just a picture; it's a tool for planning. Visitors need to know:
- Which levels are accessible and how to move between them.
- Where key facilities (accessible toilets, quiet rooms, lifts) are located in relation to where they enter.
- The "flow" of the building to avoid dead-ends or overwhelming spaces.

## Best Practices for Digital Maps

### 1. Simplify and Focus
Don't just upload a complex architectural floor plan. Create a simplified version that highlights:
- **Accessible Routes:** CLEAR paths that avoid stairs or heavy manual doors.
- **Key Points of Interest:** Toilets, elevators, seating areas, and reception.
- **Step-Free Access:** Clearly mark which entrances and areas are level or ramped.

### 2. Multi-Level Support
If your building has multiple floors, provide a way to switch between levels.
- **Level Descriptions:** Use clear, consistent names (e.g., "Level 0 / Ground Floor").
- **Vertical Circulation:** Explicitly show where the lifts and accessible stairs are.

### 3. Machine-Readability and Alt-Text
Maps are highly visual. You MUST provide a text-based alternative.
- **Tactile Maps:** State if you have physical tactile maps available at reception for blind or low-vision visitors.
- **Detailed Alt-Text:** Describe the layout in words: "The ground floor contains the cafe to the left of the entrance and the accessible toilets at the far end of the main corridor."
- **Photos:** Consider supplementing maps with photos showing actual routes, corridors, and spaces. Photos help sighted visitors with disabilities understand spatial relationships and plan their positioning. See [Photo Guidance](/framework/photo-guidance/) for accessible implementation.

## Interactive vs. Static
- **Static Images:** High-contrast, scalable SVG or high-resolution PNG files.
- **Interactive Maps:** If using interactive maps (like Mapbox or Google Maps indoors), ensure they are keyboard-navigable and compatible with screen readers.

## Wayfinding Systems

A wayfinding system helps visitors navigate your building independently. Effective wayfinding is especially important for people with cognitive disabilities, but benefits all visitors.

### Elements of Good Wayfinding
- **Consistent Landmarks:** Use recognizable features (artworks, colors, distinctive shapes) that visitors can reference.
- **Color Coding:** Assign colors to different areas or routes (e.g., "Follow the blue line to the accessible toilets").
- **Clear Signage:** Signs should have high contrast, large print, simple icons, and consistent placement.
- **Directional Cues:** Use arrows and directional indicators at decision points (intersections, elevator exits).
- **Entry and Exit Markers:** Clearly identify all entrances and exits, especially emergency exits.
- **Room Numbering:** Use logical, sequential numbering systems with high-contrast numbers on doors.

### Multi-Modal Wayfinding
Different visitors use different navigation methods. Provide multiple ways to find destinations:
- **Visual:** Signs, maps, color-coded routes
- **Tactile:** Tactile paving, braille on signs, textured wall surfaces
- **Auditory:** Voice announcements in lifts, audio beacons
- **Digital:** Mobile apps with indoor navigation, QR codes linking to location information, digital navigation codes (e.g., NaviLens, Microsoft Soundscape) that provide audio-based wayfinding for blind and low-vision visitors

### Documenting Your Wayfinding System
When describing your wayfinding system on your website:
1. Explain the overall system (e.g., "We use color-coded routes to major facilities")
2. Describe specific aids (e.g., "Blue tactile path from entrance to accessible toilets")
3. List any digital wayfinding technologies available (e.g., "NaviLens codes installed at decision points throughout the building")
4. Note where to get help if the system is unclear
5. State if staff can provide guided navigation

#### Digital Wayfinding Technologies
Consider implementing digital navigation aids that enhance independence for blind and low-vision visitors:
- **NaviLens:** High-contrast, colorful codes that can be detected from up to 12 meters away and provide audio navigation information via smartphone app
- **Bluetooth beacons:** Trigger location-specific information on visitors' smartphones
- **NFC tags:** Provide information when visitors tap their phone to a sign or location marker
- **Indoor positioning systems:** GPS-like navigation within buildings using Wi-Fi or Bluetooth
- **Text-to-speech on website:** Implement read-aloud functionality for route descriptions and facility information
- **Pre-recorded audio routes:** Professional recordings for common destinations (toilets, exits, facilities)

When implementing digital wayfinding:
- Ensure codes/beacons are placed at consistent heights and locations
- Provide instructions for downloading and using required apps (at entrance, on website)
- Maintain a fallback system (staff assistance, printed guides) for visitors without smartphones
- Test with members of the blind and low-vision community before deployment
- Consider text-to-speech for website content - see [Audio Descriptions Framework](/framework/audio-descriptions/)

For detailed guidance on wayfinding for people with cognitive disabilities, see the [W3C Wayfinding guidance](https://www.w3.org/TR/coga-wayfinding/).

---

> [!TIP]
> **Sensory Mapping:** Consider adding a "Quiet/Busy" overlay to your map to help neurodivergent visitors identify areas with high sensory input.
