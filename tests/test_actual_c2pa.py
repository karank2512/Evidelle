"""Tests for the actual-C2PA experiment helpers.

The unit tests need no external tool. The integration tests run the official c2patool binary
(offline, network-denied sandbox) and are skipped when it or sandbox-exec is not available.
"""

import json
import os
import shutil
import struct
import sys
import tempfile
import unittest
import zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "actual_c2pa"))

import run_actual_c2pa as rac  # noqa: E402
from authexp import synth  # noqa: E402
from authexp.imageio import read_png, write_png  # noqa: E402

HAVE_TOOL = os.path.exists(rac.TOOL) and shutil.which("sandbox-exec") is not None


class TestReportSummary(unittest.TestCase):
    def test_no_manifest_error_maps_to_absence(self):
        s = rac.summarize_report(1, "", "Error: No claim found\n")
        self.assertEqual(s["state"], "NO_MANIFEST")

    def test_other_error_maps_to_error(self):
        self.assertEqual(rac.summarize_report(1, "", "Error: something else")["state"], "ERROR")

    def test_validation_fields_are_read(self):
        report = {"validation_state": "Valid", "active_manifest": "m1",
                  "validation_results": {"activeManifest": {"success": [{"code": "claimSignature.validated"}],
                                                            "failure": [{"code": "signingCredential.untrusted"}],
                                                            "informational": []}},
                  "manifests": {"m1": {"signature_info": {"issuer": "Example"},
                                       "assertions": [{"label": "c2pa.actions", "data": {"actions": [
                                           {"action": "c2pa.created", "digitalSourceType": rac.IPTC + "algorithmicMedia"}]}}]}}}
        s = rac.summarize_report(0, json.dumps(report), "")
        self.assertEqual(s["state"], "Valid")
        self.assertEqual(s["failure_codes"], ["signingCredential.untrusted"])
        self.assertEqual(s["declared_digital_source_types"], ["algorithmicMedia"])
        self.assertEqual(s["signature_issuer"], "Example")


class TestPngChunkHelpers(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.src = os.path.join(self.d, "src.png")
        write_png(self.src, synth.shapes(2), extra_chunks=[(b"caBX", b"placeholder")])

    def tearDown(self):
        shutil.rmtree(self.d)

    def test_recompress_keeps_pixels_and_chunk_but_changes_bytes(self):
        dst = os.path.join(self.d, "re.png")
        rac.png_recompress(self.src, dst, level=1)
        self.assertEqual(read_png(dst)[0].rgb, read_png(self.src)[0].rgb)
        self.assertTrue(rac.png_has_chunk(dst))
        with open(self.src, "rb") as a, open(dst, "rb") as b:
            self.assertNotEqual(a.read(), b.read())

    def test_strip_removes_chunk_keeps_pixels(self):
        dst = os.path.join(self.d, "st.png")
        rac.png_strip(self.src, dst)
        self.assertFalse(rac.png_has_chunk(dst))
        self.assertEqual(read_png(dst)[0].rgb, read_png(self.src)[0].rgb)

    def test_one_value_change_and_crop(self):
        one = os.path.join(self.d, "one.png")
        rac.png_change_one_value(self.src, one)
        a, b = read_png(self.src)[0].rgb, read_png(one)[0].rgb
        self.assertEqual(sum(1 for x, y in zip(a, b) if x != y), 1)
        crop = os.path.join(self.d, "crop.png")
        rac.png_crop_keep_chunks(self.src, crop, 8, 8)
        img = read_png(crop)[0]
        self.assertEqual((img.width, img.height), (248, 248))
        self.assertTrue(rac.png_has_chunk(crop))


@unittest.skipUnless(HAVE_TOOL, "official c2patool or sandbox-exec not available")
class TestActualC2paIntegration(unittest.TestCase):
    """Runs the official binary offline with the bundled TEST credentials."""

    @classmethod
    def setUpClass(cls):
        os.makedirs(rac.WORK, exist_ok=True)
        cls.src = os.path.join(rac.WORK, "t_in.png")
        cls.signed = os.path.join(rac.WORK, "t_signed.png")
        write_png(cls.src, synth.landscape(9))
        rac.sign(cls.src, cls.signed, "unit test landscape", "algorithmicMedia")

    def test_intact_untrusted_then_trusted_with_test_anchors(self):
        self.assertEqual(rac.validate(self.signed, rac.WORK, trust=False)["state"], "Valid")
        self.assertEqual(rac.validate(self.signed, rac.WORK, trust=True)["state"], "Trusted")

    def test_lossless_recompress_invalidates_binding(self):
        dst = os.path.join(rac.WORK, "t_re.png")
        rac.png_recompress(self.signed, dst, level=1)
        s = rac.validate(dst, rac.WORK, trust=True)
        self.assertEqual(s["state"], "Invalid")
        self.assertIn("assertion.dataHash.mismatch", s["failure_codes"])

    def test_stripped_reports_absence(self):
        dst = os.path.join(rac.WORK, "t_strip.png")
        rac.png_strip(self.signed, dst)
        self.assertEqual(rac.validate(dst, rac.WORK, trust=True)["state"], "NO_MANIFEST")


if __name__ == "__main__":
    unittest.main()
