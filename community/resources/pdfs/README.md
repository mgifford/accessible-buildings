# PDF Archive

This directory stores PDF versions of canonical resources for reference and preservation.

## Purpose

External accessibility guides may:
- Be moved or removed from their original URLs
- Change content over time
- Become inaccessible

Storing PDF copies alongside canonical summaries preserves the original material for verification and reference.

## Storage Guidelines

### What to Store

- PDF versions of guides analyzed in `/community/resources/canonical/`
- Original accessibility guides that inform this toolkit
- Published building accessibility documentation used as examples

### File Naming Convention

Use the format: `{organization-slug}-{document-type}-{year}.pdf`

Examples:
- `sesame-place-sensory-guide-2025.pdf`
- `sesame-place-park-accessibility-guide-2025.pdf`
- `british-museum-access-guide-2024.pdf`

### What NOT to Store

- Copyrighted materials where permission has not been obtained
- Materials that are not referenced in canonical summaries or examples
- Large collections of unanalyzed documents

## Copyright and Licensing

All PDF files stored here should:
1. Be publicly available materials
2. Have a corresponding canonical summary that analyzes (not reproduces) the content
3. Include a note in the canonical summary about copyright status
4. Be used for reference and educational purposes only

## Adding PDFs

When you have obtained a PDF to store:

1. Download from the original URL
2. Verify the file is not corrupted
3. Rename according to the convention above
4. Place in this directory
5. Update the canonical summary to reference the local copy
6. Do not commit if file size exceeds reasonable limits (>5MB) - store externally and link instead

## Sesame Place PDFs

The following PDFs should be stored here when available:

### Sesame Place Sensory Guide
- **Filename:** `sesame-place-sensory-guide-2025.pdf`
- **Original URL:** https://sesameplace.com/philadelphia/-/media/migrated-media/sesame-place-langhorne/files/pdf/sesame-place-sensory-guide.pdf
- **Canonical Summary:** `/community/resources/canonical/2025-SesamePlace-SensoryGuide.md`
- **Status:** Pending download (network restrictions in build environment)

### Sesame Place Park Accessibility Guide
- **Filename:** `sesame-place-park-accessibility-guide-2025.pdf`
- **Original URL:** https://sesameplace.com/philadelphia/-/media/commercial/sesame-place-philadelphia/files/accessibility-files/spl_park_accessibility_guide_2025_final.pdf
- **Canonical Summary:** `/community/resources/canonical/2025-SesamePlace-ParkAccessibilityGuide.md`
- **Status:** Pending download (network restrictions in build environment)

## Manual Download Instructions

If you have access to download these files:

```bash
# Download Sesame Place Sensory Guide
curl -L -o community/resources/pdfs/sesame-place-sensory-guide-2025.pdf \
  "https://sesameplace.com/philadelphia/-/media/migrated-media/sesame-place-langhorne/files/pdf/sesame-place-sensory-guide.pdf"

# Download Sesame Place Park Accessibility Guide
curl -L -o community/resources/pdfs/sesame-place-park-accessibility-guide-2025.pdf \
  "https://sesameplace.com/philadelphia/-/media/commercial/sesame-place-philadelphia/files/accessibility-files/spl_park_accessibility_guide_2025_final.pdf"
```

Or download manually from the URLs above and save with the specified filenames.

## Verification

After adding PDFs, verify:
- File is not corrupted (can be opened)
- File size is reasonable
- Filename matches convention
- Canonical summary references the file
- Copyright status is documented

## Alternative: External Storage

For large files or when Git storage is impractical:
- Store on Internet Archive
- Use organization's own hosting
- Reference external URL in canonical summary
- Document archival location
