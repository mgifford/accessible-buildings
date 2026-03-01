---
layout: page
title: Audio Descriptions and Text-to-Speech
permalink: /framework/audio-descriptions/
---

# Audio Descriptions and Text-to-Speech for Wayfinding

Text and audio descriptions of routes and facilities are essential accessibility features. Many disabled visitors benefit from having information available in audio format, whether through screen readers, text-to-speech tools, or pre-recorded audio.

> [!NOTE]
> **Try It Yourself:** See our [Audio Navigation Example](/framework/audio-navigation-example/) for a working demonstration of text-to-speech route descriptions. Click the 🔊 Read Aloud button or use your browser's reading mode.

## Why Audio Matters

Audio descriptions serve multiple accessibility needs:

- **Blind and low-vision visitors:** Primary information format when navigating unfamiliar spaces
- **Dyslexic visitors:** Audio reinforces written information and reduces cognitive load
- **Visitors with cognitive disabilities:** Spoken instructions can be easier to process than text
- **Visitors with literacy challenges:** Audio provides equal access to information
- **All visitors:** Hands-free information access while navigating

## Types of Audio Support

### 1. Browser-Native Text-to-Speech

Modern browsers include built-in text-to-speech capabilities that work without additional software.

#### Edge Reading Mode
Microsoft Edge offers Immersive Reader with natural-sounding voices:
- Activate via the book icon in the address bar or Settings menu
- Adjustable reading speed and voice selection
- Highlights current word being read
- Works on most web pages without special coding

#### Safari Reading Mode
Safari on macOS and iOS includes text-to-speech:
- Activate Reader View (Safari → View → Show Reader)
- Use Text to Speech (Edit → Speech → Start Speaking)
- Clean presentation without distractions

#### Chrome and Firefox Extensions
Both browsers support extensions like:
- Read Aloud: A Text to Speech Voice Reader
- Natural Reader
- SpeakIt!

**Recommendation:** Ensure your accessibility pages work well with these native tools by using semantic HTML and clear structure.

### 2. Web Speech API

The Web Speech API allows websites to add read-aloud functionality directly into pages.

#### Benefits
- Works across modern browsers
- No external dependencies or downloads required
- Respects user's system voice settings
- Lightweight implementation

#### Implementation Considerations
- Requires JavaScript to be enabled
- Voice quality varies by operating system
- Network connection may be needed for cloud-based voices
- Not a replacement for screen reader compatibility

### 3. Pre-Recorded Audio

Professional audio recordings provide the highest quality but require maintenance.

#### When to Use Pre-Recorded Audio
- Critical safety information
- Complex navigation instructions
- Information that changes infrequently
- Multilingual support

#### Maintenance Requirements
- Must be updated when information changes
- Requires accessible audio player controls
- Should include synchronized text transcript
- File size and bandwidth considerations

## Implementing Text-to-Speech on Your Website

### Minimal Implementation

At minimum, ensure your access guide:
1. **Uses semantic HTML** with proper headings, lists, and landmarks
2. **Avoids content in images** - use alt text and provide text equivalents
3. **Is readable by browser extensions** - avoid complex layouts that break reader modes
4. **Provides clear navigation** - use skip links and table of contents

### Enhanced Implementation

Add read-aloud functionality to your page:

```html
<button id="read-aloud" aria-label="Read this section aloud">🔊 Read Aloud</button>
```

```javascript
// Basic Web Speech API implementation
function readAloud(text) {
  if ('speechSynthesis' in window) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 0.9; // Slightly slower for clarity
    window.speechSynthesis.speak(utterance);
  } else {
    // Show accessible notification instead of alert
    const message = document.createElement('div');
    message.setAttribute('role', 'status');
    message.setAttribute('aria-live', 'polite');
    message.textContent = 'Text-to-speech is not supported in your browser. Try Microsoft Edge Reading Mode or Safari Reading Mode.';
    document.body.appendChild(message);
  }
}
```

### Best Practices

#### Content Structure
- **Short paragraphs:** Easier to listen to in segments
- **Clear headings:** Allow users to skip to relevant sections
- **Bulleted lists:** Break information into digestible chunks
- **Avoid abbreviations:** Write "accessible toilet" not "acc. toilet"

#### Voice-Friendly Writing
- **Use simple language:** Avoid jargon and complex sentences
- **Spell out acronyms on first use:** "Americans with Disabilities Act (ADA)"
- **Provide directional cues:** "Turn right" not "Go east"
- **Use distances and times:** "50 meters" or "about 2 minutes walk"

#### Controls and User Experience
- **Pause/Resume buttons:** Allow users to control playback
- **Reading speed control:** Let users adjust to their preference
- **Visual highlighting:** Show what's currently being read
- **Keyboard accessible:** All controls must work without a mouse

## Audio Descriptions for Routes

Describe routes to common destinations in clear, sequential steps:

### Example: Accessible Toilet Route

**Text/Audio Description:**
> "From the main entrance, continue straight for 15 meters. You will pass the information desk on your left. At the corridor intersection, turn right. The accessible toilet is the second door on your left, marked with the International Symbol of Access. The door opens automatically when you press the large button at waist height."

### Format Guidelines

For each route description:
1. **Starting point:** Name the clear reference point
2. **Distance:** Provide approximate distances in meters/feet
3. **Landmarks:** Reference distinctive features along the route
4. **Turns:** Specify left/right with reference to direction of travel
5. **Destination markers:** Describe what visitors will see/feel at destination
6. **Door operation:** Explain how to open/activate doors

### Multi-Modal Support

Combine audio with other formats:
- **Tactile maps:** Physical maps at entrance with raised routes
- **Large print signs:** Visual reinforcement of audio directions
- **Staff assistance:** Backup option when technology fails
- **QR codes:** Link to detailed audio navigation

## Open-Source Text-to-Speech Libraries

If implementing custom TTS functionality, consider these libraries:

### ResponsiveVoice.js
- Simple JavaScript API
- Multiple voices and languages
- Free for non-commercial use
- Commercial license required for business websites

### Speech-to-Text Libraries
Note: Most modern implementations should use the Web Speech API (built into browsers) rather than third-party libraries.

### Considerations
- **Licensing:** Verify license permits your use case
- **Maintenance:** Check if library is actively maintained
- **Accessibility:** Test with screen readers to avoid conflicts
- **Performance:** Consider impact on page load time
- **Privacy:** Understand if content is sent to external services

## Testing Your Audio Implementation

Before publishing:

1. **Test with screen readers:** Ensure TTS doesn't conflict with JAWS, NVDA, VoiceOver
2. **Test browser compatibility:** Chrome, Firefox, Safari, Edge
3. **Test on mobile devices:** iOS Safari, Android Chrome
4. **Test keyboard controls:** All features work without mouse
5. **Test with actual users:** Get feedback from blind and low-vision visitors
6. **Verify focus management:** Focus doesn't get lost during playback
7. **Check ARIA attributes:** Proper labels and live regions for dynamic content

## Operational Implications

### Maintenance
- Review audio content when information changes (routes, facilities, hours)
- Test TTS functionality after website updates
- Ensure backup methods remain available

### Staff Training
- Staff should know how to enable reading mode in different browsers
- Staff should be able to describe routes verbally as backup
- Staff should understand visitor needs may vary

### Governance
Document your audio support in your maintenance checklist:
- Which routes have audio descriptions
- How audio content is generated (TTS vs. pre-recorded)
- Update trigger events (renovations, signage changes, facility changes)
- Testing frequency for TTS functionality

## Resources

- [Audio Navigation Example](/framework/audio-navigation-example/) - Working demonstration of audio route descriptions
- [Web Speech API - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
- [Microsoft Edge Immersive Reader](https://support.microsoft.com/en-us/topic/use-immersive-reader-in-microsoft-edge-78a7a17d-52e1-47ee-b0ac-eff8539015e1)
- [WCAG 2.2 Success Criterion 1.2.1: Audio-only and Video-only (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded.html)
- [Web Accessibility Initiative - Making Audio and Video Media Accessible](https://www.w3.org/WAI/media/av/)

---

> [!TIP]
> **Start Simple:** Begin by ensuring your content works well with browser reading modes. Add enhanced TTS features only after confirming basic accessibility is solid. See our [Audio Navigation Example](/framework/audio-navigation-example/) for a working demonstration.
