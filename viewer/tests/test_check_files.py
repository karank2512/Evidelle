"""Tests for src/check_files.py, which checks your own files with c2patool and builds a local viewer page.

A stub c2patool, written into a temporary folder by these tests, stands in for the real tool. It prints SYNTHETIC,
hand-written reports chosen by the input file's name: they are not measured results and not evidence of accuracy. The
checker runs the stub exactly as it runs the real tool, inside the macOS network-denied sandbox. The checker accepts
only the files of the tested c2patool release, so these tests run it through a small wrapper that swaps in the
stub's file hashes. The labels and the fixed readings are then computed by the template's own functions under node,
on the data embedded in the page, and the page's own script is run on a minimal fake DOM.

One optional test runs the real c2patool on the two sample images bundled with it. It runs only when
EVIDELLE_C2PATOOL_DIR points to the extracted c2patool 0.27.23 release folder; otherwise it is skipped.

Run from the viewer folder (Python 3 standard library, node and macOS sandbox-exec; nothing is installed or
downloaded). The checker starts its own sandbox, so do not run these tests inside another sandbox-exec:
  python3 -I -B -m unittest discover -s tests -v
"""
import base64
import hashlib
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
import check_files  # noqa: E402

CHECK = os.path.join(ROOT, "src", "check_files.py")
TEMPLATE = os.path.join(ROOT, "src", "template.html")
PLACEHOLDER = "/*__EVIDENCE_DATA__*/null"
HAVE_SANDBOX = os.path.isfile(check_files.SANDBOX_EXEC)
NODE = shutil.which("node")
REAL_TOOL_DIR = os.environ.get("EVIDELLE_C2PATOOL_DIR", "")
# With EVIDELLE_KEEP_TEST_FILES=1 these tests delete nothing: remove_tree() is the only place that removes files, and it
# then leaves every temporary folder in place.
KEEP_TEST_FILES = os.environ.get("EVIDELLE_KEEP_TEST_FILES") == "1"
if KEEP_TEST_FILES:
    # Left to itself, tempfile first checks its folder by creating and deleting a probe file; naming the folder skips that.
    tempfile.tempdir = os.environ.get("TMPDIR") or "/tmp"


def remove_tree(path):
    if not KEEP_TEST_FILES:
        shutil.rmtree(path, ignore_errors=True)


STUB_BODY = r'''"""Test stub for c2patool: prints SYNTHETIC reports chosen by the input file's name. Not measured results."""
import json
import os
import sys

args = sys.argv[1:]
if args == ["--version"]:
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fail-version")):
        sys.exit("stub: --version fails in this folder")
    print("c2patool 0.0.0 (test stub)")
    sys.exit(0)
if len(args) < 3 or args[0] != "--settings" or not os.path.isfile(args[1]):
    sys.exit("stub: unexpected arguments %r" % (args,))
name = os.path.basename(args[2])
trust = args[3:4] == ["trust"]
if trust and not (os.path.isfile(args[5]) and os.path.isfile(args[7])):
    sys.exit("stub: trust files missing")
kind = name.split(".")[0].split(" ")[0]
if kind in ("nomanifest", "found", "o"):
    sys.stderr.write("Error: No claim found\n")
    sys.exit(1)
if kind == "toolerror":
    sys.stderr.write("Error: synthetic failure while reading %s\n" % os.path.abspath(args[2]))
    sys.exit(1)
if kind == "nulljson":
    print("null")
    sys.exit(0)
if kind == "deepjson":
    print("[" * 100000 + "]" * 100000)
    sys.exit(0)
if kind == "selfmodify":
    with open(args[2], "ab") as f:
        f.write(b"changed while it was being checked")
state, succ, fail = "Valid", ["assertion.dataHash.match", "assertion.hashedURI.match", "claimSignature.validated"], []
if kind == "mismatch":
    state, succ, fail = "Invalid", ["assertion.hashedURI.match", "claimSignature.validated"], ["assertion.dataHash.mismatch"]
elif kind == "mismatchbadsig":
    state, succ, fail = ("Invalid", ["assertion.hashedURI.match"],
                         ["assertion.dataHash.mismatch", "claimSignature.mismatch"])
elif kind == "invaliduri":
    state, fail = "Invalid", ["assertion.hashedURI.mismatch"]
elif kind == "missingassertion":
    state, fail = "Invalid", ["assertion.missing"]
elif kind == "oddexplanation":
    state, fail = "Invalid", ["assertion.hashedURI.mismatch", "assertion.hashedURI.mismatch"]
elif kind == "oddstate":
    state = "Unrecognised"
if trust and kind in ("intact", "mismatch", "invaliduri"):
    succ = succ + ["signingCredential.trusted"]
    state = "Trusted" if state == "Valid" else state
else:
    fail = fail + ["signingCredential.untrusted"]
generator = {"name": "synthetic-test-stub"} if kind == "oddclaims" else [{"name": "synthetic-test-stub", "version": "0"}]
report = {
    "active_manifest": "urn:synthetic:1",
    "manifests": {"urn:synthetic:1": {
        "title": os.path.abspath(args[2]) if kind == "pathintitle" else name, "format": "image/png",
        "claim_generator_info": generator,
        "signature_info": {"issuer": "Synthetic Test Issuer", "common_name": "Synthetic Test Signer", "alg": "Es256"},
        "assertions": [{"label": "c2pa.actions.v2", "data": {"actions": [
            {"action": "c2pa.created",
             "digitalSourceType": "http://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia"}]}}],
        "ingredients": []}},
    "validation_results": {"activeManifest": {
        "success": [{"code": c, "explanation": "synthetic"} for c in succ],
        "informational": [],
        "failure": [{"code": c, "explanation": 7 if kind == "oddexplanation" else "synthetic"} for c in fail]}},
    "validation_state": state,
}
if kind == "warning":
    sys.stderr.write("synthetic warning on standard error\n")
print(json.dumps(report, indent=2))
'''

# Runs the checker with the stub folder's file hashes in place of the tested c2patool release's.
WITH_STUB_RELEASE = r'''
import os
import sys
src, reference = sys.argv[1], sys.argv[2]
sys.path.insert(0, src)
import check_files as cf
cf.TESTED_RELEASE = {"name": "the synthetic test stub",
                     "sha256": {rel: cf.sha256_file(os.path.join(reference, rel)) for rel in cf.TESTED_RELEASE["sha256"]}}
sys.exit(cf.main(sys.argv[3:]))
'''


def png_bytes(width=3, height=2, seed=0):
    """A small, valid RGB PNG with synthetic pixels."""
    rows = b"".join(b"\x00" + bytes((seed + x * 40 + y * 90) % 256 for x in range(width * 3)) for y in range(height))

    def chunk(kind, body):
        return struct.pack(">I", len(body)) + kind + body + struct.pack(">I", zlib.crc32(kind + body) & 0xFFFFFFFF)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(rows)) + chunk(b"IEND", b""))


def make_stub_folder(folder):
    os.makedirs(os.path.join(folder, "sample"))
    stub = os.path.join(folder, "c2patool")
    with open(stub, "w") as f:
        f.write("#!" + sys.executable + " -I\n" + STUB_BODY)
    os.chmod(stub, 0o755)
    for name in ("trust_anchors.pem", "store.cfg"):
        with open(os.path.join(folder, "sample", name), "w") as f:
            f.write("synthetic placeholder %s; only the stub reads it\n" % name)


def run_check(tool_dir, out, files, reference=None):
    """Run the checker as a command. With `reference`, it accepts the stub files in that folder as the tested release."""
    args = ["--c2patool-dir", tool_dir, "--out", out] + list(files)
    if reference is None:
        cmd = [sys.executable, "-I", "-B", CHECK] + args
    else:
        cmd = [sys.executable, "-I", "-B", "-c", WITH_STUB_RELEASE, os.path.join(ROOT, "src"), reference] + args
    return subprocess.run(cmd, capture_output=True, text=True, timeout=300)


def payload_bounds(html):
    start = html.index("var DATA = ") + len("var DATA = ")
    return start, html.index(";\n", start)


def embedded_data(html):
    start, end = payload_bounds(html)
    return json.loads(html[start:end])


def page_functions():
    """derivedA(), overall(), trustChip(), trustMeaning() and localReading(), exactly as the template defines them."""
    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()
    return re.search(r"var POL_SHORT = \{[^}]*\};", tpl).group(0) + "\n" + \
        tpl[tpl.index("function derivedA(c)"):tpl.index("function selectCase(")]


def run_page_functions(cases):
    script = (page_functions() + "\nconst input = JSON.parse(require('fs').readFileSync(0, 'utf8'));\n"
              "process.stdout.write(JSON.stringify(input.map(function (c) { return { overall: overall(c),"
              " trustB: trustChip(c, 'test_trust_anchors'), meaningB: trustMeaning(c, 'test_trust_anchors'),"
              " reading: localReading(c) }; })));")
    res = subprocess.run([NODE, "-e", script], input=json.dumps(cases), capture_output=True, text=True, timeout=60,
                         check=True)
    return json.loads(res.stdout)


# A minimal stand-in for the browser DOM: enough for the page script to render, and for its text to be read back.
FAKE_DOM = r'''
class FakeNode {
  constructor(tag) { this.tagName = tag; this.children = []; this.attrs = {}; this.listeners = {}; this.own = ""; this.style = {}; }
  appendChild(c) { this.children.push(c); return c; }
  setAttribute(k, v) { this.attrs[k] = String(v); }
  getAttribute(k) { return this.attrs[k]; }
  addEventListener(t, f) { this.listeners[t] = f; }
  focus() {}
  set textContent(v) { this.children = []; this.own = String(v); }
  get textContent() { return this.own + this.children.map(function (c) { return c.textContent + " "; }).join(""); }
}
global.Node = FakeNode;
const ids = {};
global.document = {
  title: "",
  createElement: function (t) { return new FakeNode(t); },
  createTextNode: function (t) { const n = new FakeNode("#text"); n.own = String(t); return n; },
  getElementById: function (id) { return ids[id] || (ids[id] = new FakeNode("div")); },
  querySelectorAll: function () { return []; },
  querySelector: function () { return new FakeNode("div"); }
};
global.location = { hash: "" };
global.history = { replaceState: function (a, b, h) { location.hash = h; } };
global.window = { addEventListener: function () {}, scrollTo: function () {} };
'''
READ_BACK = r'''
const texts = [];
(function walk(n) {
  if (n.tagName === "button" && n.listeners.click) { n.listeners.click(); texts.push(document.getElementById("case").textContent); }
  n.children.forEach(walk);
})(document.getElementById("case-list"));
process.stdout.write(JSON.stringify({ cases: texts, heading: document.getElementById("cases-heading").textContent,
                                      about: document.getElementById("about").textContent }));
'''


READ_FIRST_VIEW = r'''
process.stdout.write(JSON.stringify({ first: document.getElementById("case").textContent }));
'''


def render_page(html, initial_hash="", read_back=READ_BACK):
    """Run the page's own script on a fake DOM; by default returns the rendered text of every file, the heading and
    the footer."""
    script = html[html.index("<script>") + len("<script>"):html.index("</script>")]
    dom = FAKE_DOM.replace('global.location = { hash: "" };', "global.location = { hash: %s };" % json.dumps(initial_hash))
    res = subprocess.run([NODE, "-"], input=dom + script + read_back, capture_output=True, text=True, timeout=120,
                         check=True)
    return json.loads(res.stdout)


def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


class HelpersTest(unittest.TestCase):
    def test_png_and_jpeg_headers(self):
        self.assertEqual(check_files.image_kind(png_bytes(5, 4)), ("PNG", "image/png", 5, 4))
        jpeg = (b"\xff\xd8" + b"\xff\xe0" + struct.pack(">H", 4) + b"\x00\x00"
                + b"\xff\xc0" + struct.pack(">HBHHB", 11, 8, 30, 40, 1) + b"\x01\x11\x00" + b"\xff\xd9")
        self.assertEqual(check_files.image_kind(jpeg), ("JPEG", "image/jpeg", 40, 30))
        self.assertIsNone(check_files.image_kind(b"GIF89a" + b"\x00" * 32))

    def test_tested_binary_is_the_one_the_runner_recorded(self):
        with open(os.path.join(os.path.dirname(ROOT), "results", "actual_c2pa", "actual_c2pa_results.json")) as f:
            recorded = json.load(f)
        self.assertEqual(check_files.TESTED_RELEASE["sha256"]["c2patool"], recorded["environment"]["tool_binary_sha256"])

    def test_root_level_folders_are_not_replaced(self):
        self.assertEqual(check_files.sanitizer([("/a", "<x>")])("see https://host/a/b and /a"),
                         "see https://host/a/b and /a")
        self.assertEqual(check_files.sanitizer([("/a/b", "<x>")])("/a/b/c"), "<x>/c")

    def test_printable_replaces_characters_utf8_cannot_hold(self):
        shown = check_files.printable("a\udcffb.png")
        self.assertTrue(shown.startswith("a") and shown.endswith("b.png") and "�" in shown)
        shown.encode("utf-8")

    def test_only_a_path_to_the_file_is_masked(self):
        self.assertEqual(check_files.summarize(1, "", "Error: No claim found\n", "found")["state"], "NO_MANIFEST")
        self.assertEqual(check_files.summarize(1, "", "Error: No claim found\n", "o")["state"], "NO_MANIFEST")
        self.assertEqual(check_files.summarize(1, "", "Error: cannot read ./x No claim found.png\n",
                                               "x No claim found.png")["state"], "ERROR")


@unittest.skipUnless(HAVE_SANDBOX and NODE, "these tests need macOS sandbox-exec and node")
class CheckFilesTest(unittest.TestCase):
    NAMES = ["intact.png", "nomanifest.png", "mismatch.png", "invaliduri.png", "oddstate.png", "toolerror.png",
             "nulljson.png", "pathintitle.png", "missingassertion.png", "oddclaims.png", "warning.png",
             "found", "o", "deepjson.png", "oddexplanation.png", "mismatchbadsig.png"]

    @classmethod
    def setUpClass(cls):
        cls.made = tempfile.mkdtemp(prefix="evidelle_check_")
        cls.tmp = os.path.realpath(cls.made)
        cls.tool_dir = os.path.join(cls.tmp, "c2patool-stub")
        make_stub_folder(cls.tool_dir)
        os.makedirs(os.path.join(cls.tmp, "files"))
        cls.paths = []
        for i, name in enumerate(cls.NAMES):
            cls.paths.append(os.path.join(cls.tmp, "files", name))
            with open(cls.paths[-1], "wb") as f:
                f.write(png_bytes(seed=i))
        cls.out = os.path.join(cls.tmp, "report.html")
        cls.res = run_check(cls.tool_dir, cls.out, cls.paths, reference=cls.tool_dir)
        if cls.res.returncode != 0:
            raise AssertionError("check_files failed: " + cls.res.stderr)
        with open(cls.out, encoding="utf-8") as f:
            cls.html = f.read()
        cls.data = embedded_data(cls.html)
        cls.page = run_page_functions(cls.data["cases"])
        cls.rendered = render_page(cls.html)

    @classmethod
    def tearDownClass(cls):
        remove_tree(cls.tmp)

    def case(self, name):
        return self.data["cases"][self.NAMES.index(name)]

    def test_terminal_summary_and_page_file(self):
        self.assertIn("1. intact.png: PNG, ", self.res.stdout)
        self.assertIn("policy B: c2patool state Trusted; binding match, signature validated, signer trusted",
                      self.res.stdout)
        self.assertIn("Wrote %s (" % self.out, self.res.stdout)
        self.assertEqual(os.stat(self.out).st_mode & 0o777, 0o600)

    def test_labels_from_the_template_functions(self):
        got = {c["image"]["original_name"]: (r["overall"]["short"], r["trustB"]["short"])
               for c, r in zip(self.data["cases"], self.page)}
        self.assertEqual(got, {
            "intact.png": ("Intact", "TEST root"),
            "nomanifest.png": ("No credential", "Trust n/a"),
            "mismatch.png": ("Doesn't match", "TEST root"),
            "invaliduri.png": ("Fails validation", "TEST root"),
            "oddstate.png": ("Unknown", "Untrusted"),
            "toolerror.png": ("Unknown", "Trust unknown"),
            "nulljson.png": ("Unknown", "Trust unknown"),
            "pathintitle.png": ("Intact", "Untrusted"),
            "missingassertion.png": ("Fails validation", "Untrusted"),
            "oddclaims.png": ("Intact", "Untrusted"),
            "warning.png": ("Intact", "Untrusted"),
            "found": ("No credential", "Trust n/a"),
            "o": ("No credential", "Trust n/a"),
            "deepjson.png": ("Unknown", "Trust unknown"),
            "oddexplanation.png": ("Fails validation", "Untrusted"),
            "mismatchbadsig.png": ("Doesn't match", "Untrusted"),
        })
        meaning = {c["image"]["original_name"]: r["meaningB"] for c, r in zip(self.data["cases"], self.page)}
        self.assertTrue(meaning["mismatch.png"].endswith("The overall state is still Invalid because the binding check failed."))
        self.assertTrue(meaning["invaliduri.png"].endswith("The overall state is still Invalid (see the failure codes)."))
        self.assertEqual(meaning["nomanifest.png"], "No manifest, so there was no signer to check.")
        self.assertEqual(meaning["toolerror.png"], "c2patool did not produce a usable result, so the signer was not checked.")

    def test_page_is_the_template_plus_data(self):
        with open(TEMPLATE, encoding="utf-8") as f:
            template = f.read()
        start, end = payload_bounds(self.html)
        self.assertEqual(self.html[:start] + PLACEHOLDER + self.html[end:], template)
        self.assertNotIn("<", self.html[start:end])
        self.assertEqual(self.data["mode"], "local_check")
        self.assertEqual([c["id"] for c in self.data["cases"]], ["file-%d" % i for i in range(1, len(self.NAMES) + 1)])
        self.assertEqual(self.data["run"]["tool"]["reported_version"], "c2patool 0.0.0 (test stub)")
        self.assertEqual(self.data["run"]["tool"]["tested_release"], "the synthetic test stub")

    def test_embeds_the_exact_checked_bytes(self):
        for c, path in zip(self.data["cases"], self.paths):
            with open(path, "rb") as f:
                data = f.read()
            prefix = "data:image/png;base64,"
            self.assertTrue(c["image"]["data_uri"].startswith(prefix))
            self.assertEqual(base64.b64decode(c["image"]["data_uri"][len(prefix):]), data)
            self.assertEqual(c["image"]["sha256"], hashlib.sha256(data).hexdigest())
            self.assertEqual((c["image"]["format"], c["image"]["width"], c["image"]["height"]), ("PNG", 3, 2))

    def test_no_local_paths_in_the_page(self):
        for path in {self.made, self.tmp, os.path.expanduser("~"), os.path.dirname(ROOT)}:
            self.assertNotIn(path, self.html)
        err = self.case("toolerror.png")["policies"]["no_trust_anchors"]
        self.assertIn("synthetic failure while reading <input-folder>/toolerror.png", err["report_text"])
        self.assertEqual(err["runner_summary"]["message"],
                         "Error: synthetic failure while reading <input-folder>/<file>")
        self.assertEqual(self.case("pathintitle.png")["claims"]["title"], "<input-folder>/pathintitle.png")
        cmd = self.data["cases"][0]["policies"]["test_trust_anchors"]["command"]
        self.assertEqual(cmd, ["/usr/bin/sandbox-exec", "-p", "(version 1)(allow default)(deny network*)",
                               "<c2patool>/c2patool", "--settings", "<evidelle>/actual_c2pa/settings/offline.toml",
                               "./intact.png", "trust", "--trust_anchors", "<c2patool>/sample/trust_anchors.pem",
                               "--trust_config", "<c2patool>/sample/store.cfg"])

    def test_unreadable_output_and_stderr_are_kept_as_data(self):
        null = self.case("nulljson.png")["policies"]["no_trust_anchors"]
        self.assertEqual((null["derived"]["state"], null["exit_code"]), ("ERROR", 0))
        self.assertTrue(null["report_text"].startswith("c2patool exit code 0\n--- stdout ---\nnull"))
        deep = self.case("deepjson.png")["policies"]["no_trust_anchors"]
        self.assertEqual((deep["derived"]["state"], deep["exit_code"]), ("ERROR", 0))
        warn = self.case("warning.png")["policies"]["no_trust_anchors"]
        self.assertEqual(warn["stderr_text"], "synthetic warning on standard error\n")
        self.assertIsNone(self.case("intact.png")["policies"]["no_trust_anchors"]["stderr_text"])

    def test_fixed_readings(self):
        by_name = {c["image"]["original_name"]: r["reading"] for c, r in zip(self.data["cases"], self.page)}
        self.assertIn("A missing credential is not evidence either way.", " ".join(by_name["nomanifest.png"]["cannot"]))
        self.assertIn("It is not production trust.", " ".join(by_name["intact.png"]["can"]))
        self.assertIn("there is no usable result", " ".join(by_name["toolerror.png"]["cannot"]))
        self.assertIn("with these failure codes: assertion.missing.", " ".join(by_name["missingassertion.png"]["can"]))
        self.assertIn("These are not the bytes the credential was signed for", " ".join(by_name["mismatch.png"]["can"]))
        bad_sig = " ".join(by_name["mismatchbadsig.png"]["can"])
        self.assertIn("and the claim signature did not validate", bad_sig)
        self.assertNotIn("signed for", bad_sig)
        for name, reading in by_name.items():
            self.assertEqual((reading["label"], reading["title"]), (name, name))
            self.assertTrue(reading["what"] and reading["cannot"] and reading["unknown"], name)
            for line in reading["can"]:
                self.assertNotRegex(line.lower(), r"\b(real|fake|authentic|genuine|ai-generated|probability)\b", name)
                self.assertNotIn("changed after signing", line, name)

    def test_every_file_renders_with_the_page_script(self):
        self.assertEqual(self.rendered["heading"], "Files")
        self.assertIn("Fileschecked%d" % len(self.NAMES), self.rendered["about"].replace(" ", ""))
        text = dict(zip(self.NAMES, self.rendered["cases"]))
        self.assertEqual(len(text), len(self.NAMES))
        for name, t in text.items():
            self.assertIn("Fixed reading rules applied to the results above", t, name)
            self.assertIn("Your file, read on this computer. It was not uploaded anywhere.", t, name)
        self.assertIn("no longer matches its recorded hash (assertion.hashedURI.mismatch)", text["invaliduri.png"])
        self.assertIn("this alone does not show that the bytes are unchanged since signing", text["invaliduri.png"])
        self.assertIn("The claim signature validates, and the assertions it lists are unchanged.", text["intact.png"])
        self.assertIn("so the bound bytes have not changed since signing", text["intact.png"])
        self.assertIn("these are not the bytes that were signed", text["mismatch.png"])
        self.assertIn("but it does not bind to these bytes", text["mismatch.png"])
        self.assertIn("c2patool still reports the credential as Invalid", text["missingassertion.png"])
        self.assertNotIn("the assertions it lists are unchanged", text["missingassertion.png"])
        self.assertIn("Nothing to check: there is no manifest", text["nomanifest.png"])
        self.assertIn("Claim generator not reported", text["oddclaims.png"])
        self.assertIn("--- stderr ---\nsynthetic warning on standard error", text["warning.png"])
        self.assertIn("it is unknown what the credential was signed for", text["mismatchbadsig.png"])
        self.assertIn("is not Valid or Trusted", text["oddstate.png"])
        self.assertNotIn("so the bound bytes have not changed since signing", text["oddstate.png"])
        self.assertIn("assertion.hashedURI.mismatch", text["oddexplanation.png"])
        self.assertIn("c2patool exited with code 1.", text["nomanifest.png"])
        self.assertIn("SHA-256 of the text below", text["nomanifest.png"])
        for name in ("found", "o"):
            self.assertIn("Nothing to check: there is no manifest", text[name])
        for name in ("toolerror.png", "nulljson.png", "deepjson.png"):
            self.assertIn("c2patool did not produce a usable result for this file (see the raw output), so the "
                          "binding was not checked.", text[name])
            self.assertIn("no usable result (exit code", text[name])
            self.assertNotIn("no manifest", text[name].lower())

    def test_a_malformed_hash_does_not_stop_the_page(self):
        first = render_page(self.html, initial_hash="#case=%", read_back=READ_FIRST_VIEW)["first"]
        self.assertTrue(first.startswith(self.NAMES[0]), first[:80])

    def test_refusals_write_nothing(self):
        gif = os.path.join(self.tmp, "picture.gif")
        with open(gif, "wb") as f:
            f.write(b"GIF89a" + b"\x00" * 32)
        big = os.path.join(self.tmp, "big.png")
        with open(big, "wb") as f:
            f.write(png_bytes())
            f.truncate(check_files.MAX_BYTES + 1)
        refused = os.path.join(self.tmp, "refused.html")
        for tool_dir, files, message in [
                (self.tool_dir, [gif], "not a JPEG or PNG file"),
                (self.tool_dir, [big], "larger than 25 MB"),
                (self.tool_dir, [self.paths[0], self.paths[0]], "listed twice"),
                (self.tool_dir, [os.path.join(self.tmp, "missing.png")], "not a file"),
                (os.path.join(self.tmp, "no-such-folder"), self.paths[:1], "no c2patool folder at")]:
            res = run_check(tool_dir, refused, files, reference=self.tool_dir)
            self.assertEqual(res.returncode, 2, message)
            self.assertIn(message, res.stderr)
            self.assertFalse(os.path.exists(refused), message)
        before = sha256_file(self.out)
        res = run_check(self.tool_dir, self.out, self.paths[:1], reference=self.tool_dir)
        self.assertEqual(res.returncode, 2)
        self.assertIn("will not overwrite", res.stderr)
        self.assertEqual(sha256_file(self.out), before)

    def test_more_refusals_write_nothing(self):
        work = os.path.join(self.tmp, "more-refusals")
        os.makedirs(work)
        out = os.path.join(work, "page.html")
        locked = os.path.join(work, "read-only")
        os.makedirs(locked)
        os.chmod(locked, 0o555)
        try:
            res = run_check(self.tool_dir, os.path.join(locked, "page.html"), self.paths[:1], reference=self.tool_dir)
        finally:
            os.chmod(locked, 0o755)
        self.assertEqual(res.returncode, 2)
        self.assertIn("cannot create", res.stderr)
        not_executable = os.path.join(work, "stub-not-executable")
        shutil.copytree(self.tool_dir, not_executable)
        os.chmod(os.path.join(not_executable, "c2patool"), 0o644)
        bad_version = os.path.join(work, "stub-bad-version")
        shutil.copytree(self.tool_dir, bad_version)
        open(os.path.join(bad_version, "fail-version"), "w").close()
        changing = os.path.join(work, "selfmodify.png")
        with open(changing, "wb") as f:
            f.write(png_bytes())
        for tool_dir, page, files, message in [
                (self.tool_dir, os.path.join(work, "no-such-folder", "page.html"), self.paths[:1], "does not exist"),
                (not_executable, out, self.paths[:1], "is not executable"),
                (bad_version, out, self.paths[:1], "could not run c2patool --version"),
                (self.tool_dir, out, [changing], "changed or disappeared while it was being checked")]:
            res = run_check(tool_dir, page, files, reference=self.tool_dir)
            self.assertEqual(res.returncode, 2, message)
            self.assertIn(message, res.stderr)
            self.assertFalse(os.path.exists(page), message)

    def test_only_the_tested_release_is_accepted(self):
        refused = os.path.join(self.tmp, "refused-release.html")
        res = run_check(self.tool_dir, refused, self.paths[:1])
        self.assertEqual(res.returncode, 2)
        self.assertIn("is not the file from c2patool 0.27.23", res.stderr)
        no_store = os.path.join(self.tmp, "stub-without-store")
        shutil.copytree(self.tool_dir, no_store, ignore=shutil.ignore_patterns("store.cfg"))
        res = run_check(no_store, refused, self.paths[:1], reference=self.tool_dir)
        self.assertEqual(res.returncode, 2)
        self.assertIn("sample/store.cfg is missing", res.stderr)
        other_anchors = os.path.join(self.tmp, "stub-other-anchors")
        shutil.copytree(self.tool_dir, other_anchors)
        with open(os.path.join(other_anchors, "sample", "trust_anchors.pem"), "w") as f:
            f.write("a different synthetic anchors file\n")
        res = run_check(other_anchors, refused, self.paths[:1], reference=self.tool_dir)
        self.assertEqual(res.returncode, 2)
        self.assertIn("sample/trust_anchors.pem in", res.stderr)
        self.assertIn("is not the file from the synthetic test stub", res.stderr)
        self.assertFalse(os.path.exists(refused))

    def test_unusual_file_names_stay_data(self):
        folder = os.path.join(self.tmp, "unusual")
        os.makedirs(folder)
        names = ['intact <b>&"x\'.png', "-intact.png"]
        for name in names:
            with open(os.path.join(folder, name), "wb") as f:
                f.write(png_bytes())
        out = os.path.join(self.tmp, "unusual.html")
        res = run_check(self.tool_dir, out, [os.path.join(folder, n) for n in names], reference=self.tool_dir)
        self.assertEqual(res.returncode, 0, res.stderr)
        with open(out, encoding="utf-8") as f:
            html = f.read()
        start, end = payload_bounds(html)
        self.assertNotIn("<", html[start:end])
        data = json.loads(html[start:end])
        self.assertEqual([c["image"]["original_name"] for c in data["cases"]], names)
        self.assertEqual(data["cases"][1]["policies"]["no_trust_anchors"]["command"][6], "./-intact.png")


@unittest.skipUnless(REAL_TOOL_DIR and HAVE_SANDBOX and NODE,
                     "set EVIDELLE_C2PATOOL_DIR to the extracted c2patool 0.27.23 release folder to run this test")
class RealC2patoolTest(unittest.TestCase):
    def test_bundled_sample_images(self):
        tmp = tempfile.mkdtemp(prefix="evidelle_real_")
        try:
            out = os.path.join(tmp, "report.html")
            res = run_check(REAL_TOOL_DIR, out, [os.path.join(REAL_TOOL_DIR, "sample", n) for n in ("C.jpg", "image.jpg")])
            self.assertEqual(res.returncode, 0, res.stderr)
            with open(out, encoding="utf-8") as f:
                data = embedded_data(f.read())
            self.assertEqual(data["run"]["tool"]["reported_version"], "c2patool 0.27.23")
            states = [(c["policies"]["no_trust_anchors"]["derived"]["state"],
                       c["policies"]["test_trust_anchors"]["derived"]["state"]) for c in data["cases"]]
            # As recorded for c2patool 0.27.23 in results/actual_c2pa/actual_c2pa_results.json (bundled samples).
            self.assertEqual(states, [("Valid", "Trusted"), ("NO_MANIFEST", "NO_MANIFEST")])
            self.assertEqual([r["overall"]["short"] for r in run_page_functions(data["cases"])], ["Intact", "No credential"])
        finally:
            remove_tree(tmp)


if __name__ == "__main__":
    unittest.main()
