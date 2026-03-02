---
layout: page
title: Museums and Cultural Venues
permalink: /framework/museums/
---

# Museums and Cultural Venues: Pioneering Accessibility

Museums and cultural institutions occupy a distinctive place in accessibility progress. Constrained by heritage buildings, irreplaceable collections, and the challenge of making art, science, and history legible across diverse audiences, they have been forced to develop creative, repeatable solutions to hard problems.

This page collects and evaluates those approaches—not to limit the scope of this toolkit to museums, but because the solutions museums have found frequently transfer to other building types and program contexts.

---

## Why Museums Are a Useful Reference Point

Museums face challenges common to many public buildings, but often in concentrated form:

- **Inaccessible historic fabric:** Listed and heritage buildings where structural change is limited.
- **Content that resists standard access methods:** How do you make a painting accessible to a blind visitor? How do you describe a fragile artefact without tactile access?
- **High visitor diversity:** Museums serve people with a wide range of mobility, sensory, cognitive, and communication needs, often in a single visit.
- **Temporary configurations:** Exhibitions change. Routes that were clear last month may be blocked today.
- **Multiple program layers:** A building, a collection, public events, education programs—each requiring distinct access planning.

The solutions developed for museums—tactile objects, audio description, mobile web tours, accessible interactive kiosks, visual description training for staff—apply directly to libraries, science centres, historic sites, civic buildings, and any space where people encounter complex content.

---

## Key Innovations Worth Knowing

### 1. Tactile Maps and Touch Trails

Tactile maps translate floor plans and spatial relationships into formats that can be understood by touch. They are essential for blind and low-vision visitors and benefit visitors with cognitive disabilities who struggle with abstract spatial representations.

What good tactile provision includes:

- A tactile floor plan at the entrance, oriented to match the direction visitors face when they pick it up.
- Tactile objects or replicas of key collection items in a dedicated discovery space or at collection points.
- Raised-line route guides through major gallery sequences.
- Clear labelling in both braille and large print.

Tactile maps are now much cheaper to produce than they were a decade ago:

- **3D printing** allows museums and public libraries to produce raised-surface maps and replica objects at low cost.
- **Thermoform printing** produces lightweight tactile sheets from digital files.
- **Laser cutting** enables detailed topographic reproductions.

See also: [Tactile Mapping resources in the Community Resources page](/community/resources/)

---

### 2. QR Codes Linking to Accessible Content

QR codes placed at exhibit labels, entrance signs, and route decision points allow visitors to access content on their own device without touching shared equipment.

When implemented well, QR codes:

- Link to an HTML page (not a PDF) with the exhibit description, label text, or route information.
- Provide content that works with screen readers and browser text-to-speech.
- Give visitors options: text, audio, simplified language, or large print.
- Eliminate the problem of borrowing shared equipment (handheld devices, headsets).

**Critical implementation requirements:**

- The QR code must be placed at a reachable height—between 900mm and 1200mm from floor level—and must not require bending or stretching to scan.
- The linked page must meet WCAG 2.2 AA as a minimum.
- The code must be large enough to scan reliably in typical gallery lighting conditions.
- A fallback must exist: the text of the label should also appear in accessible print.

QR codes that link to PDFs, app download prompts, or pages that require account creation create barriers, not access.

---

### 3. Audio Descriptions and Mobile Web Tours

Audio tours have existed for decades, but the model of borrowing a dedicated handheld device has significant drawbacks:

- Devices require sanitisation between uses.
- Device availability is limited.
- Shared equipment creates hygiene and infection-control concerns.
- Device interfaces are often not accessible to screen reader users.
- Visitors cannot use the tour before or after their visit.

**The preferred model is a mobile web tour—a tour delivered through a web browser on the visitor's own device, with no app download required.**

What a mobile web tour should include:

- A QR code at the entrance linking to the tour start page.
- Audio playable directly in the browser without plugin requirements.
- Transcript available beneath each audio segment.
- Clear progress indicators between stops.
- Works offline or on low connectivity (consider using a service worker to cache content).
- Large touch targets for navigation controls (minimum 44px × 44px).

Describing art and artefacts in audio requires trained writers. The Museum Studies field has developed detailed guidance on verbal description methodology. Key principles:

- Begin with overall composition, scale, and medium before moving to detail.
- Use spatial language: left, right, foreground, background, centre.
- Include colour and tone—these are meaningful even to some low-vision visitors.
- Describe what the work shows, not just what it is.
- Avoid aesthetic judgements ("beautiful", "striking") in favour of concrete description.
- State explicitly what is not visible or discernible.

---

### 4. Describing Art and Artefacts: The Core Challenge

The question posed in the original museum accessibility literature is pointed: *How do you describe the work of a master painter in just a few words?*

The honest answer is that you cannot do it in just a few words—but you can do it well by following structured approaches.

**The layered description model:**

| Layer | Purpose | Length |
| :--- | :--- | :--- |
| Label text | Identification and minimal description | 2–4 sentences |
| Short audio description | Core content for audio guide stops | 90–120 seconds |
| Extended verbal description | Full accessible interpretation | 3–5 minutes |
| Object handling / tactile replica | Touch-based understanding | Variable |

The label, short audio, and extended audio can all be published on the same web page—visitors choose the depth they need.

**Visual description training:**

Many museums have invested in training staff and volunteers to give verbal descriptions on request. This is a programmatic rather than a technological solution, but it is often the most effective one in practice. It requires:

- Training in structured verbal description methodology.
- Staff awareness of when and how to offer descriptions.
- A clear way for visitors to request the service.

---

### 5. Sensory Profiles for Exhibitions

Exhibitions vary significantly in sensory conditions: lighting levels, noise, crowds, video or audio content, scent, movement. A sensory profile helps visitors with sensory processing differences, chronic illness, anxiety, or autism plan their visit with confidence.

A sensory profile for an exhibition should state:

- Baseline lighting level and whether it varies.
- Ambient noise level and sources.
- Whether video content autoplay is used.
- Whether strobing or flashing content is present.
- Whether there are strong scents.
- Estimated crowd level by time of day.
- Whether there is a quiet space within or near the exhibition.

For permanent collection spaces, sensory profiles can be maintained over time. For temporary exhibitions, they should be published before the exhibition opens and updated if conditions change.

See [Sensory Profile Template](/templates/sensory-profile/) and [Quiet Spaces](/framework/quiet-spaces/) for implementation guidance.

---

### 6. Accessible Programming: Beyond Physical Access

Physical access is the floor, not the ceiling. Museums that lead on accessibility address programmatic access too:

- **Touch tours:** Guided handling of objects or replicas for blind and low-vision visitors, usually offered in small groups with advance booking.
- **BSL / signed tours:** Guided tours delivered in British Sign Language or other signed languages. Consider whether tours are offered by Deaf staff or interpreters—this matters to many Deaf visitors.
- **Relaxed openings:** Reduced lighting, lower noise levels, no sudden sounds, freedom to move and vocalise. Originally developed for autistic visitors, these sessions benefit a wider population.
- **Audio described events:** Performances, talks, and screenings with live or pre-recorded audio description.
- **Easy Read materials:** Exhibition guides and collection information in plain English with supporting images.
- **Large print guides:** Physical copies and on-demand printing.

Each of these programs requires a booking system, a communications plan, and maintenance. They cannot be treated as one-off events. They must be recurring, reliably available, and listed prominently in the plan-your-visit section of the website.

---

## Implementation Checklist for Museums and Cultural Venues

The following extends the [Building Access Guide Template](/templates/building-access-guide/) with museum-specific considerations.

### Arrival and Orientation

- [ ] Accessible entrance clearly identified and signed from public transport stops and accessible parking.
- [ ] Step-free route from accessible parking to entrance described with surface type and distance.
- [ ] Pre-visit information includes sensory conditions at entrance (noise, crowds, lighting).
- [ ] Large print site maps available at entrance.
- [ ] Tactile map available at entrance or from reception on request.

### Wayfinding and Navigation

- [ ] Gallery floor plan available in accessible digital format.
- [ ] QR codes at decision points link to HTML wayfinding pages.
- [ ] Route descriptions published for key paths (entrance to toilets, entrance to gallery, entrance to café).
- [ ] Temporary exhibition layouts reviewed before opening for route width and obstruction.
- [ ] Lift locations, dimensions, and working hours stated.
- [ ] Galleries that are not step-free are identified explicitly.

### Collection and Exhibition Access

- [ ] Exhibit labels available in large print and on accessible web pages.
- [ ] Audio descriptions available for key collection items via mobile web tour (no app download required).
- [ ] QR codes at exhibit labels link to accessible HTML pages.
- [ ] Tactile replicas or handling objects identified and listed.
- [ ] Sensory profile published for permanent galleries and temporary exhibitions.
- [ ] Object labels and panel text available in Easy Read format on request.

### Programmatic Access

- [ ] Touch tours offered on a regular schedule and listed on the website.
- [ ] Signed tours (BSL or other) offered regularly and listed on the website.
- [ ] Relaxed opening sessions offered and listed on the website.
- [ ] Audio described tours available via mobile web browser.
- [ ] Staff trained in verbal description methodology.
- [ ] Large print and Easy Read guides available at reception.

### Facilities

- [ ] Accessible toilet locations described with routes.
- [ ] Changing Places facility status stated (available, not available, or nearest alternative).
- [ ] Seating available throughout galleries—type, height, and locations noted.
- [ ] Quiet space available and identified on the accessible map.
- [ ] Hearing loop coverage areas identified (whole building, specific rooms, portable loop available).

### Maintenance

- [ ] Mobile web tour content reviewed each time an exhibition changes.
- [ ] QR codes tested regularly to confirm links are active and pages are accessible.
- [ ] Tactile map accuracy verified when floor plans or gallery layouts change.
- [ ] Programmatic access schedule reviewed at each season change.
- [ ] Staff training in verbal description and programmatic access completed annually.

---

## Resources and Examples

### Reference Documents

- [U.S. DOJ: Maintaining Accessibility in Museums (2009)](/community/resources/canonical/2009-USDOJ-MaintainingAccessibilityInMuseums/) — Structured summary of the core DOJ operational guidance, with maintenance implications.
- [Building Access Guide Template](/templates/building-access-guide/) — Primary template for documenting physical access.
- [Sensory Profile Template](/templates/sensory-profile/) — For documenting sensory conditions.
- [Maintenance Checklist Template](/templates/maintenance-checklist/) — For operational maintenance planning.

### External Starting Points

The following organisations have published accessible exhibits, mobile web tours, or accessibility guides worth reviewing:

- **[Smithsonian Institution Accessibility](https://www.si.edu/visit/accessibility)** — One of the most comprehensive museum accessibility programmes in the world, including audio tours, ASL resources, and tactile experiences.
- **[Victoria and Albert Museum (V&A) Access](https://www.vam.ac.uk/info/accessibility)** — Detailed access information including handling collections, touch tours, and BSL-interpreted events.
- **[Natural History Museum London Accessibility](https://www.nhm.ac.uk/visit/accessibility.html)** — Visitor-facing access information for a major heritage building.
- **[Museum of Modern Art (MoMA) Accessibility](https://www.moma.org/visit/accessibility/)** — Audio descriptions, verbal description tours, and multi-language access programmes.
- **[Te Papa Tongarewa (Museum of New Zealand) Accessibility](https://www.tepapa.govt.nz/visit/plan-your-visit/accessibility)** — A strong Pacific and indigenous cultural institution example.
- **[Science Museum Group Accessibility](https://www.sciencemuseumgroup.org.uk/about-us/access/)** — Guidance across multiple UK sites with sensory, mobility, and programmatic access information.

---

## Transferable Lessons for Non-Museum Buildings

The following museum innovations apply directly to other building types:

| Museum Innovation | Direct Transfer |
| :--- | :--- |
| Mobile web audio tour (no app required) | Any multi-room or multi-level building: hospital, university, civic centre |
| QR codes linking to accessible HTML | Any building with display panels, signage, or information points |
| Tactile map at entrance | Libraries, transit hubs, civic buildings |
| Sensory profile for spaces | Cinemas, concert halls, sports venues, workplaces |
| Relaxed openings | Shops, leisure venues, public services |
| Touch tours / handling sessions | Science centres, archives, historic houses |
| Easy Read guides | Any venue with written interpretive content |
| Verbal description training for staff | Any public-facing role in a content-rich environment |

---

*This page forms part of the [Building Access Guide Toolkit]({{ "/" | relative_url }}). It is intended as a starting point for organisations looking to learn from museum-sector innovation—not as a definitive or complete account of the field.*
