---
layout: page
title: Audio Navigation Example
permalink: /framework/audio-navigation-example/
---

# Audio Navigation Example
{: .read-aloud-section}

This page demonstrates how to structure route descriptions for text-to-speech accessibility. Try using the **🔊 Read Aloud** button or enable your browser's reading mode (Edge, Safari, or use a Chrome/Firefox extension).

## Route to Accessible Toilets
{: .read-aloud-section}

From the main entrance, continue straight ahead for 15 meters. You will pass the information desk on your left. The corridor continues with smooth, level flooring.

At the corridor intersection, turn right. You will notice a slight echo from the ceiling height in this area. Continue for 10 meters.

The accessible toilet is the second door on your left, marked with the International Symbol of Access. The door is painted blue and opens automatically when you press the large button at waist height, approximately 90 centimeters from the floor.

Inside, the toilet has left-hand transfer space. An emergency alarm cord hangs by the toilet. A baby changing table is available on the right wall.

## Route to Cafe
{: .read-aloud-section}

From the main entrance, turn left immediately after entering. You will see a large glass wall ahead.

Walk straight for 20 meters along the corridor. The flooring is smooth tile. There are benches on your right at the halfway point if you need to rest.

The cafe entrance is on your right through an open archway. No doors to navigate. During busy times, you may hear considerable background noise from this point.

The accessible seating area is at the far end of the cafe, away from the kitchen noise. Tables have adequate knee clearance for wheelchair users.

## Route to Quiet Space
{: .read-aloud-section}

From the main entrance, turn right and follow the corridor for 25 meters. You will pass the lift on your left.

At the end of the corridor, turn left. The quiet space is the first door on your right, marked with a "Quiet Space" sign showing a person resting.

The door is manual and opens inward. Inside, the lighting is dim and adjustable. There are soft seating options and noise-canceling headphones available for use.

The room has carpet flooring and sound-dampening wall panels. The temperature is maintained at a comfortable 21 degrees Celsius.

## Route to Lifts
{: .read-aloud-section}

From the main entrance, turn right. The lift lobby is 30 meters ahead on your left.

There are two lifts available. Both are wheelchair accessible with dimensions of 1.4 meters wide by 1.6 meters deep.

The lift call buttons are at 110 centimeters height. Lifts have voice announcements for floor levels and door operation.

Inside each lift, buttons have Braille labels and raised numbers. A handrail runs along three walls at 90 centimeters height.

---

## Technical Implementation Notes

This page demonstrates several accessibility features:

1. **Semantic HTML Structure**: Clear headings (H1, H2) allow screen readers and browser reading modes to navigate efficiently
2. **Read-Aloud Sections**: Each route description has the `read-aloud-section` class, enabling section-specific reading
3. **Clear Language**: Simple sentences, active voice, specific measurements
4. **Sequential Instructions**: Step-by-step directions from a consistent starting point
5. **Sensory Landmarks**: Descriptions include what visitors will see, hear, and feel
6. **Distance Information**: Specific meters rather than vague terms like "nearby"
7. **Door Operation Details**: Explains how to interact with physical elements

### How Visitors Can Use This

- **Browser Reading Modes**: Microsoft Edge (Immersive Reader), Safari (Reader + Speech)
- **Screen Readers**: JAWS, NVDA, VoiceOver will read content naturally
- **Read-Aloud Button**: Web Speech API implementation (click 🔊 buttons)
- **Voice Assistants**: Content can be accessed via mobile voice assistants

### For Content Creators

When writing your own route descriptions:

```markdown
## Route to [Destination]
{: .read-aloud-section}

From [starting point], [first action with distance].

[Landmark description and any sensory information].

[Next step with direction and distance].

[Final destination description and how to use it].
```

---

<aside class="callout callout-tip" role="note">
  <p><strong>Tip – Test Your Content:</strong> Use browser reading modes to hear how your directions sound when spoken. Adjust phrasing if sentences are too long or confusing when read aloud.</p>
</aside>

## Browser Compatibility

| Browser | Built-in TTS | Quality | How to Activate |
|---------|--------------|---------|-----------------|
| **Microsoft Edge** | ✅ Excellent | High-quality natural voices | Click book icon or F9 → Immersive Reader |
| **Safari (macOS)** | ✅ Excellent | System voices | Reader View → Edit → Speech → Start Speaking |
| **Safari (iOS)** | ✅ Excellent | System voices | Reader View → Aa → Speak |
| **Chrome** | ⚠️ Extension needed | Varies | Install "Read Aloud" extension |
| **Firefox** | ⚠️ Extension needed | Varies | Install "Read Aloud" extension |

### Web Speech API Support
This demonstration page uses the Web Speech API, which is supported in:
- ✅ Chrome/Edge (Chromium): Excellent support
- ✅ Safari: Good support
- ⚠️ Firefox: Limited support (desktop only)
- ❌ Internet Explorer: Not supported

---

**Related Resources:**
- [Audio Descriptions Framework](/framework/audio-descriptions/)
- [Building Layout Guidance](/framework/building-layout/)
- [Building Access Guide Template](/templates/building-access-guide/)
