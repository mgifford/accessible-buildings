#!/usr/bin/env python3
"""
Generate schema.org LocationFeatureSpecification JSON-LD structured data
from a building access guide markdown file.

Reads narrative content and produces a CivicStructure + LocationFeatureSpecification
JSON-LD block based on the vocabulary defined in framework/machine-readable.md.

Usage:
    python3 scripts/generate-jsonld.py file1.md file2.md ...
    python3 scripts/generate-jsonld.py --files-from /path/to/list.txt

Output:
    Markdown-formatted PR comment with generated JSON-LD, ready to post.

Exit codes:
    0  Success (comment written, or no relevant files found).
    1  Unexpected error.

Conservative defaults:
    - If a feature is mentioned but ambiguous, output "unknown".
    - If a feature is not mentioned, output "unknown" (never "false" by default).
    - Only output "false" when the guide explicitly states a feature is unavailable.
    - Never assert compliance or certification status.
"""

import json
import os
import re
import sys

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

COMMENT_MARKER = "<!-- jsonld-generator -->"


# ---------------------------------------------------------------------------
# Front-matter parsing
# ---------------------------------------------------------------------------

def parse_front_matter(content):
    """Return (data_dict, body_str) for a Jekyll markdown file."""
    if not content.startswith("---"):
        return {}, content

    close = content.find("\n---", 3)
    if close == -1:
        return {}, content

    yaml_str = content[3:close].strip()
    body = content[close + 4:].strip()

    if YAML_AVAILABLE:
        try:
            data = yaml.safe_load(yaml_str)
            return data or {}, body
        except yaml.YAMLError:
            return {}, body

    # Minimal fallback: top-level scalar keys only
    data = {}
    for line in yaml_str.splitlines():
        m = re.match(r"^([\w_]+):\s*(.+)?$", line)
        if m:
            data[m.group(1)] = m.group(2)
    return data, body


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def is_placeholder(text):
    """
    Return True if text is an unfilled template placeholder.

    Examples that are placeholders:
        [Yes/No/Location]
        [Number and Location]
        [Describe how to get help]
    """
    if not text:
        return True
    return bool(re.search(
        r"\[[^\]]*?(?:"
        r"Yes|No|Location|Number|Type|Describe|Name|Date|Distance|"
        r"If applicable|Available|Link|Email|Phone|Area|Feature|"
        r"Reason|Loop|IR|FM|Left|Right|Dimension|Width|Depth"
        r")[^\]]*?\]",
        text,
        re.IGNORECASE,
    ))


def strip_placeholders(text):
    """
    Return text with all [...] placeholder blocks removed.

    Prevents placeholder content from being mistaken for real feature values
    during fallback body searches.
    """
    return re.sub(r"\[[^\]]*\]", " ", text)


def parse_value(raw):
    """
    Map a raw field value to "true", "false", or "unknown".

    Conservative:
    - Explicit "No"/"not available" → "false"
    - Explicit "Yes" or substantive content → "true"
    - Placeholder or ambiguous → "unknown"
    """
    if not raw or not raw.strip():
        return "unknown"

    stripped = raw.strip()

    if is_placeholder(stripped):
        return "unknown"

    lower = stripped.lower()

    # Explicit negatives
    if re.match(r"^no\b", lower):
        return "false"
    if lower in ("none", "n/a", "not available", "not applicable", "unavailable"):
        return "false"
    if re.search(
        r"\bnot\s+(?:available|present|provided|installed|accessible|applicable)\b",
        lower,
    ):
        return "false"

    # Explicit positives
    if re.match(r"^yes\b", lower):
        return "true"

    # Substantive content that isn't a placeholder
    if len(stripped) > 4 and not re.search(r"\[.*?\]", stripped):
        return "true"

    return "unknown"


def extract_section(body, heading_pattern):
    """
    Return the text of a section matching heading_pattern, up to the next
    same-or-higher-level heading or end of document.
    """
    m = re.search(heading_pattern, body, re.DOTALL | re.IGNORECASE)
    if not m:
        return ""
    return m.group(0)


def get_field_from_summary(body, field_label):
    """
    Extract raw value and parsed value for a bold-label field in the
    Quick Visitor Summary section (or anywhere in the body as fallback).

    Returns (raw_str, value_str).
    """
    # Try the Quick Visitor Summary section first
    summary = extract_section(
        body,
        r"##\s+(?:\d+\.\s+)?Quick Visitor Summary.*?(?=\n##\s|\Z)",
    )
    search_text = summary if summary else body

    pattern = rf"\*\*{re.escape(field_label)}:?\*\*\s*:?\s*(.+?)(?:\n|$)"
    m = re.search(pattern, search_text, re.IGNORECASE)
    if not m:
        return "", "unknown"

    raw = m.group(1).strip()
    return raw, parse_value(raw)


# ---------------------------------------------------------------------------
# Feature detectors
# ---------------------------------------------------------------------------

def detect_step_free_entrance(body):
    """
    Detect step-free entrance.
    Returns (value, hours_or_None).
    """
    raw, value = get_field_from_summary(body, "Step-free entrance")

    # Fallback: look for step-free mentions in the Entry section
    if value == "unknown":
        entry = extract_section(
            body,
            r"##\s+(?:\d+\.\s+)?Entry.*?(?=\n##\s|\Z)",
        )
        search_text = entry if entry else body
        main_door_m = re.search(
            r"\*\*Main Entrance:?\*\*\s*:?\s*(.+?)(?:\n|$)",
            search_text,
            re.IGNORECASE,
        )
        if main_door_m:
            raw = main_door_m.group(1).strip()
            if not is_placeholder(raw):
                if re.search(r"\bstep[- ]free\b|\blevel\s+access\b|\bramp\b", raw, re.IGNORECASE):
                    value = "true"
                elif re.search(r"\bstep\b|\bstairs\b", raw, re.IGNORECASE):
                    value = "false"

    # Check for step-free mentions in body text (evaluation files)
    if value == "unknown":
        clean_body = strip_placeholders(body)
        if re.search(r"\bstep[- ]free\s+entrance\b", clean_body, re.IGNORECASE):
            value = "unknown"  # mentioned but not confirmed

    hours = None
    if value == "true":
        hours_m = re.search(
            r"\b(?:open|available|accessible)\s+(?:from\s+)?(?:Mon(?:day)?|Mo)"
            r"[-–](?:Fri(?:day)?|Fr)\s+\d{1,2}[:.]\d{2}[-–]\d{1,2}[:.]\d{2}",
            body,
            re.IGNORECASE,
        )
        if hours_m:
            hours = hours_m.group(0)

    return value, hours


def detect_accessible_toilet(body):
    """
    Detect accessible toilet presence.
    Returns (value, description_or_None).
    """
    raw, value = get_field_from_summary(body, "Accessible toilets")
    if value == "unknown":
        raw, value = get_field_from_summary(body, "Accessible toilet")

    description = None
    if value == "true" and raw and not is_placeholder(raw) and len(raw) > 5:
        description = raw

    # Fallback: search Facilities section
    if value == "unknown":
        facilities = extract_section(
            body,
            r"##\s+(?:\d+\.\s+)?Facilities.*?(?=\n##\s|\Z)",
        )
        search_text = facilities if facilities else body
        toilet_m = re.search(
            r"\*\*Accessible Toilets?:?\*\*\s*:?\s*(.+?)(?:\n|$)",
            search_text,
            re.IGNORECASE,
        )
        if toilet_m:
            raw = toilet_m.group(1).strip()
            value = parse_value(raw)
            if value == "true" and not is_placeholder(raw) and len(raw) > 5:
                description = raw

    return value, description


def detect_changing_places(body):
    """
    Detect Changing Places toilet.
    Returns (value, description_or_None).
    """
    facilities = extract_section(
        body,
        r"##\s+(?:\d+\.\s+)?Facilities.*?(?=\n##\s|\Z)",
    )
    search_text = facilities if facilities else body

    cp_m = re.search(
        r"\*\*Changing\s+Places:?\*\*\s*:?\s*(.+?)(?:\n|$)",
        search_text,
        re.IGNORECASE,
    )
    if cp_m:
        raw = cp_m.group(1).strip()
        if is_placeholder(raw):
            return "unknown", None
        value = parse_value(raw)
        description = raw if value == "true" and len(raw) > 5 else None
        return value, description

    # Check for any Changing Places mention
    if re.search(r"\bchanging\s+places\b", body, re.IGNORECASE):
        return "unknown", None

    return "unknown", None


def detect_accessible_parking(body):
    """
    Detect accessible parking.
    Returns (value, description_or_None).
    """
    raw, value = get_field_from_summary(body, "Accessible parking")

    description = None
    if value == "true" and raw and not is_placeholder(raw) and len(raw) > 5:
        description = raw

    # Also look for a numeric spaces count anywhere in the document (outside placeholders)
    if value in ("true", "unknown"):
        clean_body = strip_placeholders(body)
        spaces_m = re.search(
            r"(\d+)\s+accessible\s+(?:parking\s+)?spaces?",
            clean_body,
            re.IGNORECASE,
        )
        if spaces_m:
            value = "true"
            if not description:
                count = spaces_m.group(1)
                description = f"{count} accessible parking space(s)"

    return value, description


def detect_assistive_listening(body):
    """
    Detect assistive listening system (hearing loop, IR, FM).
    Returns (value, description_or_None).
    """
    programs = extract_section(
        body,
        r"##\s+(?:\d+\.\s+)?Programs?\s*(?:and\s+Services?)?.*?(?=\n##\s|\Z)",
    )
    search_text = programs if programs else body

    listening_m = re.search(
        r"\*\*Assistive\s+Listening:?\*\*\s*:?\s*(.+?)(?:\n|$)",
        search_text,
        re.IGNORECASE,
    )
    if listening_m:
        raw = listening_m.group(1).strip()
        if is_placeholder(raw):
            return "unknown", None
        value = parse_value(raw)
        if value == "false":
            return "false", None
        listening_type = _classify_listening_type(raw)
        return "true", listening_type or (raw if len(raw) > 5 else None)

    # Fallback: search for hearing loop / induction loop / assistive listening
    clean_body = strip_placeholders(body)
    for pattern, label in (
        (r"\bhearing\s+loop\b", "Hearing loop"),
        (r"\binduction\s+loop\b", "Hearing loop (induction)"),
        (r"\bIR\s+(?:system|listening)\b|\binfrared\s+(?:system|listening)\b", "IR system"),
        (r"\bFM\s+(?:system|listening)\b", "FM system"),
    ):
        if re.search(pattern, clean_body, re.IGNORECASE):
            return "true", label

    if re.search(r"\bassistive\s+listening\b", clean_body, re.IGNORECASE):
        return "unknown", None

    return "unknown", None


def _classify_listening_type(raw):
    """Return a short type label for an assistive listening system."""
    if re.search(r"\bloop\b", raw, re.IGNORECASE):
        return "Hearing loop"
    if re.search(r"\bIR\b|\binfrared\b", raw, re.IGNORECASE):
        return "IR (infrared) system"
    if re.search(r"\bFM\b", raw, re.IGNORECASE):
        return "FM system"
    return None


def detect_quiet_space(body):
    """
    Detect quiet space.
    Returns (value, description_or_None).
    """
    raw, value = get_field_from_summary(body, "Quiet space")

    if value == "unknown":
        facilities = extract_section(
            body,
            r"##\s+(?:\d+\.\s+)?Facilities.*?(?=\n##\s|\Z)",
        )
        search_text = facilities if facilities else body
        quiet_m = re.search(
            r"\*\*Quiet\s+Spaces?:?\*\*\s*:?\s*(.+?)(?:\n|$)",
            search_text,
            re.IGNORECASE,
        )
        if quiet_m:
            raw = quiet_m.group(1).strip()
            value = parse_value(raw)

    description = None
    if value == "true" and raw and not is_placeholder(raw) and len(raw) > 5:
        description = raw

    return value, description


def detect_power_doors(body):
    """
    Detect power-assisted or automatic doors.
    Returns value string.
    """
    entry = extract_section(
        body,
        r"##\s+(?:\d+\.\s+)?Entry.*?(?=\n##\s|\Z)",
    )
    search_text = entry if entry else body

    main_door_m = re.search(
        r"\*\*Main Entrance:?\*\*\s*:?\s*(.+?)(?:\n|$)",
        search_text,
        re.IGNORECASE,
    )
    if main_door_m:
        raw = main_door_m.group(1).strip()
        if not is_placeholder(raw):
            if re.search(
                r"\b(?:automatic|power[- ]assisted|powered)\b", raw, re.IGNORECASE
            ):
                return "true"
            if re.search(r"\bmanual\b", raw, re.IGNORECASE):
                return "false"

    # Fallback: search full body (excluding placeholder text)
    clean_body = strip_placeholders(body)
    if re.search(
        r"\b(?:automatic|power[- ]assisted|powered)\s+door", clean_body, re.IGNORECASE
    ):
        return "true"

    return "unknown"


def detect_lift(body):
    """
    Detect lift / elevator availability.
    Returns (value, description_or_None).
    """
    nav = extract_section(
        body,
        r"##\s+(?:\d+\.\s+)?Navigation.*?(?=\n##\s|\Z)",
    )
    search_text = nav if nav else body

    lift_m = re.search(
        r"\*\*Lifts?:?\*\*\s*:?\s*(.+?)(?:\n|$)",
        search_text,
        re.IGNORECASE,
    )
    if lift_m:
        raw = lift_m.group(1).strip()
        if is_placeholder(raw):
            return "unknown", None
        value = parse_value(raw)
        if value == "false":
            return "false", None
        description = raw[:120] if len(raw) > 5 else None
        return "true", description

    # Fallback: check for any lift/elevator mention
    clean_body = strip_placeholders(body)
    if re.search(r"\blift\b|\belevator\b", clean_body, re.IGNORECASE):
        return "unknown", None

    return "unknown", None


# ---------------------------------------------------------------------------
# Building name extraction
# ---------------------------------------------------------------------------

def extract_building_name(front_matter, body):
    """
    Return the building name, or None if it cannot be determined.

    Checks front matter title first, then the first heading.
    """
    title = front_matter.get("title", "")
    if title:
        # Remove common suffixes
        name = re.sub(
            r"\s*(?:Building\s+)?Access\s+Guide\s*(?:Template)?\s*$",
            "",
            str(title),
            flags=re.IGNORECASE,
        ).strip()
        if name and not re.search(r"\[.*?\]", name) and len(name) > 3:
            return name

    # Try the first heading in the body
    heading_m = re.search(
        r"^#\s+(.+?)(?:\s+Access\s+Guide)?\s*$", body, re.MULTILINE
    )
    if heading_m:
        name = heading_m.group(1).strip()
        if not re.search(r"\[.*?\]", name) and len(name) > 3:
            return name

    return None


# ---------------------------------------------------------------------------
# JSON-LD assembly
# ---------------------------------------------------------------------------

def build_amenity_feature(name, value, description=None, hours_available=None):
    """Build a single LocationFeatureSpecification dict."""
    entry = {
        "@type": "LocationFeatureSpecification",
        "name": name,
        "value": value,
    }
    if description:
        entry["description"] = description
    if hours_available:
        entry["hoursAvailable"] = hours_available
    return entry


def generate_jsonld(building_name, amenity_features):
    """
    Assemble a schema.org CivicStructure + LocationFeatureSpecification JSON-LD dict.

    amenity_features: list of pre-built LocationFeatureSpecification dicts.
    """
    doc = {"@context": "https://schema.org", "@type": "CivicStructure"}
    if building_name:
        doc["name"] = building_name
    doc["amenityFeature"] = amenity_features
    return doc


# ---------------------------------------------------------------------------
# Per-file processing
# ---------------------------------------------------------------------------

def process_file(filepath, content):
    """
    Parse a building access guide (or example evaluation) and generate JSON-LD.
    Returns a markdown string ready to post as a PR comment.
    """
    front_matter, body = parse_front_matter(content)
    building_name = extract_building_name(front_matter, body)

    # Detect all features
    step_free_value, step_free_hours = detect_step_free_entrance(body)
    toilet_value, toilet_desc = detect_accessible_toilet(body)
    changing_places_value, changing_places_desc = detect_changing_places(body)
    parking_value, parking_desc = detect_accessible_parking(body)
    listening_value, listening_desc = detect_assistive_listening(body)
    quiet_value, quiet_desc = detect_quiet_space(body)
    power_doors_value = detect_power_doors(body)
    lift_value, lift_desc = detect_lift(body)

    features = [
        build_amenity_feature(
            "Step-free entrance", step_free_value,
            hours_available=step_free_hours,
        ),
        build_amenity_feature(
            "Accessible toilet", toilet_value,
            description=toilet_desc,
        ),
        build_amenity_feature(
            "Changing Places toilet", changing_places_value,
            description=changing_places_desc,
        ),
        build_amenity_feature(
            "Assistive listening system", listening_value,
            description=listening_desc,
        ),
        build_amenity_feature(
            "Accessible parking", parking_value,
            description=parking_desc,
        ),
        build_amenity_feature(
            "Quiet space", quiet_value,
            description=quiet_desc,
        ),
        build_amenity_feature("Power-assisted doors", power_doors_value),
        build_amenity_feature("Lift", lift_value, description=lift_desc),
    ]

    jsonld = generate_jsonld(building_name, features)
    jsonld_str = json.dumps(jsonld, indent=2)

    display_name = building_name or os.path.basename(filepath)

    lines = [
        COMMENT_MARKER,
        f"### 🤖 Suggested schema.org JSON-LD for {display_name}",
        "",
        "The following structured data was generated from the access guide content.",
        "Add it inside a `<script type=\"application/ld+json\">` block in the"
        " `<head>` of your published access page.",
        "",
        "<details>",
        "<summary>View generated JSON-LD</summary>",
        "",
        "```json",
        jsonld_str,
        "```",
        "",
        "**Review before publishing:** Verify each `value` field matches the current"
        " state of the building. Set any uncertain features to `\"unknown\"`."
        " Features not mentioned in the guide default to `\"unknown\"`"
        " rather than `\"false\"`.",
        "",
        "</details>",
        "",
        "---",
        "",
        "*Generated automatically using the vocabulary defined in"
        " [`framework/machine-readable.md`](framework/machine-readable.md).*  ",
        "*Never asserts compliance or certification status.*",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    if len(argv) >= 2 and argv[0] == "--files-from":
        with open(argv[1], encoding="utf-8") as fh:
            argv = [line.rstrip("\n") for line in fh if line.strip()]

    if not argv:
        return 0

    # Filter to existing .md files in the relevant paths
    relevant = []
    for f in argv:
        if not f.endswith(".md") or not os.path.isfile(f):
            continue
        if f.startswith("examples/_examples/") or (
            f.startswith("templates/")
            and os.path.basename(f) == "building-access-guide.md"
        ):
            relevant.append(f)

    if not relevant:
        return 0

    output_parts = []
    for filepath in relevant:
        with open(filepath, encoding="utf-8") as fh:
            content = fh.read()
        output_parts.append(process_file(filepath, content))

    print("\n\n---\n\n".join(output_parts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
