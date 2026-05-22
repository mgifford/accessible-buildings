import importlib.util
import json
import pathlib
import re
import unittest


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "scripts" / "generate-jsonld.py"
FIXTURE_PATH = pathlib.Path(__file__).resolve().parent / "fixtures" / "realistic-building-guide.md"


def load_module():
    spec = importlib.util.spec_from_file_location("generate_jsonld", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def extract_jsonld(comment_markdown):
    match = re.search(r"```json\n(.*?)\n```", comment_markdown, re.DOTALL)
    if not match:
        raise AssertionError("JSON-LD block was not found in generated comment")
    return json.loads(match.group(1))


class GenerateJsonLdTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module()

    def test_realistic_fixture_generates_expected_features(self):
        content = FIXTURE_PATH.read_text(encoding="utf-8")
        comment = self.mod.process_file("examples/_examples/realistic-building-guide.md", content)
        jsonld = extract_jsonld(comment)

        self.assertEqual(jsonld["@context"], "https://schema.org")
        self.assertEqual(jsonld["@type"], "CivicStructure")

        features = {f["name"]: f for f in jsonld["amenityFeature"]}
        self.assertEqual(features["Step-free entrance"]["value"], "true")
        self.assertIn("08:00-18:00", features["Step-free entrance"]["hoursAvailable"])
        self.assertIn("intercom", features["Step-free entrance"]["description"].lower())
        self.assertEqual(features["Accessible toilet"]["value"], "true")
        self.assertEqual(features["Changing Places toilet"]["value"], "false")
        self.assertEqual(features["Assistive listening system"]["value"], "true")
        self.assertIn("loop", features["Assistive listening system"]["description"].lower())
        self.assertEqual(features["Accessible parking"]["value"], "true")
        self.assertIn("2 accessible parking spaces", features["Accessible parking"]["description"])
        self.assertEqual(features["Quiet space"]["value"], "true")
        self.assertEqual(features["Power-assisted doors"]["value"], "true")
        self.assertEqual(features["Lift"]["value"], "false")

    def test_ambiguous_and_unfilled_values_stay_unknown(self):
        body = """
## 1. Quick Visitor Summary
- **Step-free entrance:** Available on request.
- **Accessible toilets:** [Yes/No/Location]
- **Accessible parking:** N/A
"""
        comment = self.mod.process_file("examples/_examples/minimal.md", body)
        jsonld = extract_jsonld(comment)
        features = {f["name"]: f for f in jsonld["amenityFeature"]}

        self.assertEqual(features["Step-free entrance"]["value"], "unknown")
        self.assertEqual(features["Accessible toilet"]["value"], "unknown")
        self.assertEqual(features["Accessible parking"]["value"], "unknown")


if __name__ == "__main__":
    unittest.main()
