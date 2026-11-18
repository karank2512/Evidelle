"""Unit tests for the offline experiment (standard library unittest).

Run from the repository root:  python3 -m unittest discover -s tests -v
"""

import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from authexp import evidence, keys, synth, transforms as tf, watermark as wm  # noqa: E402
from authexp import manifest as mf  # noqa: E402
from authexp.imageio import Image, read_png, read_ppm, write_png, write_ppm  # noqa: E402

HAS_OPENSSL = shutil.which("openssl") is not None
HAS_CJPEG = shutil.which("cjpeg") is not None and shutil.which("djpeg") is not None


class TestImageIO(unittest.TestCase):
    def test_png_roundtrip_with_text_and_chunk(self):
        img = synth.shapes(1)
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.png")
            write_png(p, img, text={"Make": "ExampleCam"}, extra_chunks=[(b"prVn", b"{}")])
            back, text, chunks = read_png(p)
        self.assertEqual(back.rgb, img.rgb)
        self.assertEqual(text, {"Make": "ExampleCam"})
        self.assertIn((b"prVn", b"{}"), chunks)

    def test_ppm_roundtrip(self):
        img = synth.landscape(1)
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.ppm")
            write_ppm(p, img)
            self.assertEqual(read_ppm(p).rgb, img.rgb)


class TestDeterminism(unittest.TestCase):
    def test_same_index_same_pixels(self):
        self.assertEqual(synth.landscape(3).pixel_digest(), synth.landscape(3).pixel_digest())
        self.assertEqual(synth.shapes(3).pixel_digest(), synth.shapes(3).pixel_digest())

    def test_different_index_different_pixels(self):
        self.assertNotEqual(synth.landscape(3).pixel_digest(), synth.landscape(4).pixel_digest())

    def test_watermark_pattern_is_deterministic(self):
        wm._pattern_cache.clear()
        a = wm.pattern("k")[:100]
        wm._pattern_cache.clear()
        self.assertEqual(a, wm.pattern("k")[:100])


@unittest.skipUnless(HAS_OPENSSL, "openssl not available")
class TestManifest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = tempfile.mkdtemp()
        cls.gen = keys.make_test_key("trusted-generator", cls.dir)
        cls.forger = keys.make_test_key("forger", cls.dir)
        cls.rev = keys.make_test_key("revoked-signer", cls.dir)
        cls.trust = {cls.gen["key_id"], cls.rev["key_id"]}
        cls.revoked = {cls.rev["key_id"]}
        cls.img = synth.landscape(0)
        cls.claims = {"claim_generator": "procedural-landscape/1.0", "digital_source_type": "algorithmicMedia"}
        cls.signed = mf.build_manifest(cls.img, cls.claims, cls.gen)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.dir)

    def verify(self, img, chunks, **kw):
        return mf.verify_image(img, chunks, self.trust, self.revoked, **kw)["state"]

    def test_test_keys_are_deterministic(self):
        again = keys.make_test_key("trusted-generator", tempfile.mkdtemp())
        self.assertEqual(again["key_id"], self.gen["key_id"])

    def test_intact_is_valid_trusted(self):
        self.assertEqual(self.verify(self.img, [mf.manifest_chunk(self.signed)]), mf.VALID_TRUSTED)

    def test_absent_manifest(self):
        self.assertEqual(self.verify(self.img, []), mf.NO_MANIFEST)

    def test_any_pixel_change_breaks_binding(self):
        self.assertEqual(self.verify(tf.nudge_one_pixel(self.img), [mf.manifest_chunk(self.signed)]), mf.BINDING_MISMATCH)

    def test_transplant_breaks_binding(self):
        self.assertEqual(self.verify(synth.shapes(0), [mf.manifest_chunk(self.signed)]), mf.BINDING_MISMATCH)

    def test_self_signed_is_valid_but_untrusted(self):
        forged = mf.build_manifest(self.img, {"digital_source_type": "digitalCapture"}, self.forger)
        self.assertEqual(self.verify(self.img, [mf.manifest_chunk(forged)]), mf.VALID_UNTRUSTED)

    def test_key_id_spoof_fails(self):
        spoof = mf.build_manifest(self.img, self.claims, self.forger, claimed_key_id=self.gen["key_id"])
        self.assertEqual(self.verify(self.img, [mf.manifest_chunk(spoof)]), mf.SIGNATURE_INVALID)

    def test_tampered_claims_fail(self):
        m = json.loads(self.signed.decode())
        m["claims"]["digital_source_type"] = "digitalCapture"
        self.assertEqual(self.verify(self.img, [mf.manifest_chunk(json.dumps(m).encode())]), mf.SIGNATURE_INVALID)

    def test_malformed(self):
        self.assertEqual(self.verify(self.img, [mf.manifest_chunk(b"not json")]), mf.MALFORMED)

    def test_revocation_only_matters_if_checked(self):
        m = mf.build_manifest(self.img, self.claims, self.rev)
        self.assertEqual(self.verify(self.img, [mf.manifest_chunk(m)], check_revocation=True), mf.VALID_REVOKED)
        self.assertEqual(self.verify(self.img, [mf.manifest_chunk(m)], check_revocation=False), mf.VALID_TRUSTED)


class TestWatermark(unittest.TestCase):
    def test_marked_detected_unmarked_not(self):
        img = synth.landscape(5)
        self.assertGreaterEqual(wm.detect(wm.embed(img, "k"), "k"), wm.THRESHOLD)
        self.assertLess(wm.detect(img, "k"), wm.THRESHOLD)

    def test_wrong_key_not_detected(self):
        marked = wm.embed(synth.landscape(5), "k")
        self.assertLess(wm.detect(marked, "other-key"), wm.THRESHOLD)

    def test_copy_attack_spoofs_detection(self):
        marked = wm.embed(synth.landscape(6), "k")
        target = synth.shapes(6)
        self.assertLess(wm.detect(target, "k"), wm.THRESHOLD)
        self.assertGreaterEqual(wm.detect(wm.copy_attack(marked, target), "k"), wm.THRESHOLD)

    def test_misaligned_crop_defeats_origin_detector(self):
        marked = wm.embed(synth.landscape(7), "k")
        self.assertLess(wm.detect(tf.crop(marked, 8, 8), "k"), wm.THRESHOLD)

    @unittest.skipUnless(HAS_CJPEG, "libjpeg tools not available")
    def test_jpeg_reduces_score(self):
        marked = wm.embed(synth.landscape(8), "k")
        self.assertLess(wm.detect(tf.jpeg(marked, 30), "k"), wm.detect(marked, "k"))


class TestEvidence(unittest.TestCase):
    def test_no_state_produces_verdict_language(self):
        for state in mf.STATES:
            for detected in (True, False, None):
                out = evidence.summarize(state, detected)
                self.assertEqual(out["real_or_fake_verdict"], "not issued")
                for s in out["statements"]:
                    self.assertFalse(evidence.contains_verdict_language(s["statement"]), s)

    def test_absence_states_abstain(self):
        out = evidence.summarize(mf.NO_MANIFEST, False)
        self.assertEqual(out["overall"], "abstain")

    def test_guard_catches_verdicts(self):
        self.assertTrue(evidence.contains_verdict_language("This image is real."))
        self.assertTrue(evidence.contains_verdict_language("The metadata proves capture."))
        self.assertFalse(evidence.contains_verdict_language("This does not establish that the depicted scene is real."))

    def test_detectors_and_c2pa_reported_unevaluated(self):
        signals = {s["signal"]: s["state"] for s in evidence.summarize()["statements"]}
        self.assertEqual(signals["AI-image detector"], "UNEVALUATED")
        self.assertEqual(signals["C2PA verification"], "UNEVALUATED")


if __name__ == "__main__":
    unittest.main()
