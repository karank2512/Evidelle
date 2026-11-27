"""Regression assertions for every recorded actual-C2PA case.

Two layers:
- TestCommittedEvidence checks results/actual_c2pa/actual_c2pa_results.json against the expected states and failure
  codes below. It needs no tool.
- TestOfflineRerun re-runs every case with the official c2patool (offline, network-denied sandbox) into a temporary
  folder. It asserts the same expectations plus bounded material claims about the files. It is skipped when the
  tool, its sample/ folder, sandbox-exec, the libjpeg-turbo tools or the official sample files are missing, and the
  skip message names what is missing. AUTHEXP_C2PATOOL_DIR and AUTHEXP_OFFICIAL_DIR point to folders elsewhere.

The expectations are the recorded results of c2patool 0.27.23. They describe validation states, not whether any
scene is real.
"""

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "actual_c2pa"))

import run_actual_c2pa as rac  # noqa: E402
from authexp.imageio import read_png, read_ppm  # noqa: E402

UNTRUSTED = "signingCredential.untrusted"
DATAHASH = "assertion.dataHash.mismatch"
TEST_ISSUER = "C2PA Test Signing Cert"

# file -> (no-anchor state, no-anchor failure codes, test-anchor state, test-anchor failure codes, issuer)
EXPECTED_OFFICIAL = {
    "adobe-20220124-CA.jpg": ("Valid", [UNTRUSTED], "Trusted", [], TEST_ISSUER),
    "adobe-20220124-E-sig-CA.jpg": ("Invalid", [UNTRUSTED, "claimSignature.mismatch"], "Invalid", ["claimSignature.mismatch"], TEST_ISSUER),
    "adobe-20220124-E-dat-CA.jpg": ("Invalid", [UNTRUSTED, DATAHASH], "Invalid", [DATAHASH], TEST_ISSUER),
    "adobe-20220124-E-uri-CA.jpg": ("Invalid", [UNTRUSTED, "assertion.hashedURI.mismatch"], "Invalid", ["assertion.hashedURI.mismatch"], TEST_ISSUER),
    "truepic-20230212-landscape.jpg": ("Valid", [UNTRUSTED], "Valid", [UNTRUSTED], "Truepic"),
    "c2patool sample/C.jpg": ("Valid", [UNTRUSTED], "Trusted", [], TEST_ISSUER),
    "c2patool sample/image.jpg": ("NO_MANIFEST", None, "NO_MANIFEST", None, None),
}

# case id -> (C2PA chunk present (PNG only), no-anchor state, no-anchor codes, test-anchor state, test-anchor codes,
#             declared digital source types)
EXPECTED_SYNTHETIC = {
    "A01_png_signed_intact": (True, "Valid", [UNTRUSTED], "Trusted", [], ["algorithmicMedia"]),
    "A02_png_lossless_recompress": (True, "Invalid", [UNTRUSTED, DATAHASH], "Invalid", [DATAHASH], ["algorithmicMedia"]),
    "A03_png_one_value_changed": (True, "Invalid", [UNTRUSTED, DATAHASH], "Invalid", [DATAHASH], ["algorithmicMedia"]),
    "A04_png_crop_8px": (True, "Invalid", [UNTRUSTED, DATAHASH], "Invalid", [DATAHASH], ["algorithmicMedia"]),
    "A05_png_c2pa_chunk_removed": (False, "NO_MANIFEST", None, "NO_MANIFEST", None, None),
    "A06_png_manifest_transplanted": (True, "Invalid", [UNTRUSTED, DATAHASH], "Invalid", [DATAHASH], ["algorithmicMedia"]),
    "A07_png_sips_resave": (False, "NO_MANIFEST", None, "NO_MANIFEST", None, None),
    "A08_png_false_capture_claim": (True, "Valid", [UNTRUSTED], "Trusted", [], ["digitalCapture"]),
    "B01_jpeg_signed_intact": (None, "Valid", [UNTRUSTED], "Trusted", [], ["algorithmicMedia"]),
    "B02_jpeg_lossless_transcode_markers_kept": (None, "Invalid", [UNTRUSTED, DATAHASH], "Invalid", [DATAHASH], ["algorithmicMedia"]),
    "B03_jpeg_lossless_transcode_markers_dropped": (None, "NO_MANIFEST", None, "NO_MANIFEST", None, None),
    "B04_jpeg_reencode_q75": (None, "NO_MANIFEST", None, "NO_MANIFEST", None, None),
    "B05_jpeg_sips_resave_q80": (None, "NO_MANIFEST", None, "NO_MANIFEST", None, None),
}
SIPS_CASES = {"A07_png_sips_resave", "B05_jpeg_sips_resave_q80"}


def check_official(test, entries):
    seen = {e["file"]: e for e in entries}
    test.assertEqual(set(seen), set(EXPECTED_OFFICIAL))
    for name, (nt_state, nt_codes, tt_state, tt_codes, issuer) in EXPECTED_OFFICIAL.items():
        nt, tt = seen[name]["no_trust_anchors"], seen[name]["test_trust_anchors"]
        with test.subTest(file=name):
            test.assertEqual(nt["state"], nt_state)
            test.assertEqual(tt["state"], tt_state)
            test.assertEqual(nt.get("failure_codes"), nt_codes)
            test.assertEqual(tt.get("failure_codes"), tt_codes)
            test.assertEqual(nt.get("signature_issuer"), issuer)


def check_synthetic(test, cases, require_sips):
    seen = {c["id"]: c for c in cases}
    expected_ids = set(EXPECTED_SYNTHETIC) if require_sips else set(EXPECTED_SYNTHETIC) - SIPS_CASES
    test.assertTrue(expected_ids.issubset(seen), sorted(expected_ids - set(seen)))
    for cid in seen:
        chunk, nt_state, nt_codes, tt_state, tt_codes, dst = EXPECTED_SYNTHETIC[cid]
        c = seen[cid]
        with test.subTest(case=cid):
            test.assertEqual(c["c2pa_chunk_present"], chunk)
            test.assertEqual(c["no_trust_anchors"]["state"], nt_state)
            test.assertEqual(c["test_trust_anchors"]["state"], tt_state)
            test.assertEqual(c["no_trust_anchors"].get("failure_codes"), nt_codes)
            test.assertEqual(c["test_trust_anchors"].get("failure_codes"), tt_codes)
            test.assertEqual(c["no_trust_anchors"].get("declared_digital_source_types"), dst)
            if nt_state in ("Valid", "Invalid"):
                test.assertEqual(c["no_trust_anchors"].get("signature_issuer"), TEST_ISSUER)


class TestCommittedEvidence(unittest.TestCase):
    """The committed results JSON matches the expected states and codes (no tool needed)."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(ROOT, "results", "actual_c2pa", "actual_c2pa_results.json")) as f:
            cls.r = json.load(f)

    def test_official_samples(self):
        check_official(self, self.r["official_samples"])

    def test_synthetic_cases(self):
        check_synthetic(self, self.r["synthetic_cases"], require_sips=True)

    def test_timestamp_codes_recorded_as_observed(self):
        # Observed but not examined: official samples report timestamp codes with no anchors and no network.
        ca = next(e for e in self.r["official_samples"] if e["file"] == "adobe-20220124-CA.jpg")
        self.assertIn("timeStamp.trusted", ca["no_trust_anchors"]["success_codes"])
        self.assertIn("timeStamp.validated", ca["no_trust_anchors"]["success_codes"])
        # The synthetic signatures carry no timestamp.
        a01 = next(c for c in self.r["synthetic_cases"] if c["id"] == "A01_png_signed_intact")
        self.assertFalse([s for s in a01["no_trust_anchors"]["success_codes"] if s.startswith("timeStamp")])

    def test_offline_controls_recorded(self):
        oc = self.r["offline_controls"]
        self.assertEqual(oc["sandbox_profile"], "(version 1)(allow default)(deny network*)")
        self.assertFalse(oc["remote_manifest_fetch"])
        self.assertFalse(oc["ocsp_fetch"])
        self.assertEqual(oc["allowed_network_hosts"], [])


def _png_parts(path):
    chunks = rac.png_chunks(path)
    idat = b"".join(d for t, d in chunks if t == b"IDAT")
    cabx = [d for t, d in chunks if t == b"caBX"]
    return read_png(path)[0], idat, cabx


def _jpeg_pixels(path, tmp):
    out = os.path.join(tmp, os.path.basename(path) + ".ppm")
    subprocess.run(["djpeg", "-ppm", "-outfile", out, path], check=True, capture_output=True)
    return read_ppm(out).rgb


def _sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


MISSING_FOR_RERUN = rac.missing_prerequisites()
# With EVIDELLE_KEEP_TEST_FILES=1 this file deletes nothing: the re-run's temporary folder is left in place.
KEEP_TEST_FILES = os.environ.get("EVIDELLE_KEEP_TEST_FILES") == "1"
if KEEP_TEST_FILES:
    # Left to itself, tempfile first checks its folder by creating and deleting a probe file; naming the folder skips that.
    tempfile.tempdir = os.environ.get("TMPDIR") or "/tmp"


@unittest.skipIf(MISSING_FOR_RERUN, "missing: " + "; ".join(MISSING_FOR_RERUN))
class TestOfflineRerun(unittest.TestCase):
    """Re-run every case offline with the official tool and assert states, codes and material claims."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="c2pa_regression_")
        cls.r = rac.collect(cls.tmp)

    @classmethod
    def tearDownClass(cls):
        if not KEEP_TEST_FILES:
            shutil.rmtree(cls.tmp, ignore_errors=True)

    def p(self, name):
        return os.path.join(self.tmp, name)

    def test_official_states_and_codes(self):
        check_official(self, self.r["official_samples"])

    def test_synthetic_states_and_codes(self):
        check_synthetic(self, self.r["synthetic_cases"], require_sips=shutil.which("sips") is not None)

    def test_official_tampered_files_have_identical_pixels_but_different_bytes(self):
        ref = os.path.join(rac.OFFICIAL, "adobe-20220124-CA.jpg")
        ref_px = _jpeg_pixels(ref, self.tmp)
        for name in ("adobe-20220124-E-sig-CA.jpg", "adobe-20220124-E-dat-CA.jpg", "adobe-20220124-E-uri-CA.jpg"):
            p = os.path.join(rac.OFFICIAL, name)
            with self.subTest(file=name):
                self.assertEqual(_jpeg_pixels(p, self.tmp), ref_px)
                self.assertNotEqual(_sha256(p), _sha256(ref))

    def test_png_material_claims(self):
        a01_img, a01_idat, a01_cabx = _png_parts(self.p("L0_signed.png"))
        self.assertEqual(len(a01_cabx), 1)
        # A02: same pixels, different image-data bytes, same C2PA chunk.
        img, idat, cabx = _png_parts(self.p("A02.png"))
        self.assertEqual(img.rgb, a01_img.rgb)
        self.assertNotEqual(idat, a01_idat)
        self.assertEqual(cabx, a01_cabx)
        # A03: exactly one value changed.
        img, _idat, _cabx = _png_parts(self.p("A03.png"))
        self.assertEqual(sum(1 for x, y in zip(img.rgb, a01_img.rgb) if x != y), 1)
        # A04: cropped by 8 px in each dimension, chunk kept.
        img, _idat, cabx = _png_parts(self.p("A04.png"))
        self.assertEqual((img.width, img.height), (a01_img.width - 8, a01_img.height - 8))
        self.assertEqual(cabx, a01_cabx)
        # A05: chunk removed; pixels and image-data bytes unchanged.
        img, idat, cabx = _png_parts(self.p("A05.png"))
        self.assertEqual(cabx, [])
        self.assertEqual(idat, a01_idat)
        self.assertEqual(img.rgb, a01_img.rgb)
        # A06: the other image's pixels carrying the signed chunk.
        s0_img = read_png(self.p("S0.png"))[0]
        img, _idat, cabx = _png_parts(self.p("A06.png"))
        self.assertEqual(img.rgb, s0_img.rgb)
        self.assertEqual(cabx, a01_cabx)
        # A08: same pixels as A01, deliberately false declaration under the public test key.
        img, _idat, cabx = _png_parts(self.p("L0_false_capture.png"))
        self.assertEqual(img.rgb, a01_img.rgb)
        self.assertEqual(len(cabx), 1)
        if shutil.which("sips"):
            # A07: sips re-save kept pixels and dropped the chunk.
            img, _idat, cabx = _png_parts(self.p("A07.png"))
            self.assertEqual(cabx, [])
            self.assertEqual(img.rgb, a01_img.rgb)

    def test_jpeg_lossless_transcodes_keep_pixels(self):
        b01 = _jpeg_pixels(self.p("L1_signed.jpg"), self.tmp)
        self.assertEqual(_jpeg_pixels(self.p("B02.jpg"), self.tmp), b01)
        self.assertEqual(_jpeg_pixels(self.p("B03.jpg"), self.tmp), b01)
        self.assertNotEqual(_sha256(self.p("B02.jpg")), _sha256(self.p("L1_signed.jpg")))


if __name__ == "__main__":
    unittest.main()
