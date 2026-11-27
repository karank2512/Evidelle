"""Tests for the evidence viewer's summary label.

The page labels each file with overall() in src/template.html. These tests take that exact function from the
template source and run it under node, on the SYNTHETIC state/code patterns in tests/fixtures/ (hand-written; not
measured validation results and not evidence of accuracy). They also rebuild the previous overall() by reverting the
fix as an exact text edit, and check that the previous version breaks the label rule that the current one keeps.

Run from the viewer folder (Python 3 standard library and node; nothing is installed or downloaded):
  python3 -I -B -m unittest discover -s tests -v
"""
import json
import os
import shutil
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from derived_facts import derive  # noqa: E402

TEMPLATE = os.path.join(ROOT, "src", "template.html")
FIXTURE = os.path.join(ROOT, "tests", "fixtures", "synthetic_state_code_patterns.json")
LABELS = {"intact": ("intact", "Intact"), "no-credential": ("none", "No credential"),
          "doesnt-match": ("broken", "Doesn't match"), "fails-validation": ("broken", "Fails validation"),
          "unknown": ("unknown", "Unknown")}
# The fix, as an exact text edit of overall(). Reverting it rebuilds the previous label logic.
FIX_LINE = ('    if (d.state === "Invalid") { return { cls: "broken", text: "Credential fails c2patool validation '
            '(see the failure codes)", short: "Fails validation" }; }\n')
FIXED_CONDITION = '((d.state === "Valid" || d.state === "Trusted") && d.binding === "match"'
PREVIOUS_CONDITION = '(d.binding === "match"'
CONTROLS = ("valid-untrusted-signer", "trusted", "no-manifest", "tool-error", "binding-mismatch",
            "valid-without-signature-code")


def label_source():
    """derivedA() and overall(), exactly as the template defines them."""
    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()
    return tpl[tpl.index("function derivedA(c)"):tpl.index("function trustChip(")]


def previous_label_source():
    src = label_source()
    if src.count(FIX_LINE) != 1 or src.count(FIXED_CONDITION) != 1:
        raise AssertionError("the fix is not present exactly once in src/template.html")
    return src.replace(FIX_LINE, "").replace(FIXED_CONDITION, PREVIOUS_CONDITION)


def run_overall(js, derived):
    """Evaluate overall() from the given source on Policy-A derived facts; returns [{cls, text, short}]."""
    node = shutil.which("node")
    if node is None:
        raise RuntimeError("these tests need node")
    script = (js + "\nconst input = JSON.parse(require('fs').readFileSync(0, 'utf8'));\n"
              "process.stdout.write(JSON.stringify(input.map(function (d) {"
              " return overall({ policies: { no_trust_anchors: { derived: d } } }); })));")
    res = subprocess.run([node, "-e", script], input=json.dumps(derived), capture_output=True, text=True,
                         timeout=60, check=True)
    return json.loads(res.stdout)


class OverallLabelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(FIXTURE, encoding="utf-8") as f:
            fixture = json.load(f)
        cls.about, cls.items = fixture["about"], fixture["patterns"]
        cls.derived = [derive(p["summary"]) for p in cls.items]
        cls.current = run_overall(label_source(), cls.derived)

    def previous(self):
        return run_overall(previous_label_source(), self.derived)

    def test_fixture_is_synthetic_state_and_codes_only(self):
        self.assertIn("SYNTHETIC", self.about)
        for p in self.items:
            self.assertEqual(sorted(p["summary"]), ["failure_codes", "state", "success_codes"], p["id"])

    def test_current_labels(self):
        got = {p["id"]: (lab["cls"], lab["short"]) for p, lab in zip(self.items, self.current)}
        self.assertEqual(got, {p["id"]: LABELS[p["expected"]] for p in self.items})

    def test_current_never_intact_without_valid_or_trusted_state(self):
        for p, d, lab in zip(self.items, self.derived, self.current):
            if lab["cls"] == "intact":
                self.assertIn(d["state"], ("Valid", "Trusted"), p["id"])
                self.assertEqual((d["binding"], d["signature"]), ("match", "validated"), p["id"])

    def test_previous_logic_breaks_that_rule(self):
        wrong = sorted(p["id"] for p, d, lab in zip(self.items, self.derived, self.previous())
                       if lab["cls"] == "intact" and d["state"] not in ("Valid", "Trusted"))
        self.assertEqual(wrong, ["invalid-other-failure", "unrecognised-state"])

    def test_controls_unchanged_by_the_fix(self):
        for p, cur, prev in zip(self.items, self.current, self.previous()):
            if p["id"] in CONTROLS:
                self.assertEqual(cur, prev, p["id"])


if __name__ == "__main__":
    unittest.main()
