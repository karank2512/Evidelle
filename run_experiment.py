#!/usr/bin/env python3
"""Run the offline authenticity-signal experiment and write results/results.json and RESULTS.md.

Usage:  python3 run_experiment.py            (full run)
        python3 run_experiment.py --quick    (fewer images and keys, for a fast check)

Synthetic, non-intimate images only. No network access, no AI-image detector, and no C2PA tool.
"""

import argparse
import hashlib
import json
import math
import os
import platform
import statistics
import sys
import tempfile

from authexp import __version__, evidence, keys, synth, transforms as tf, watermark as wm
from authexp import manifest as mf
from authexp.imageio import read_png, write_png

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(HERE, "results")
ARTIFACT_DIR = os.path.join(RESULTS_DIR, "artifacts")
WM_KEY = "generator-A-watermark-key"


def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def environment():
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "openssl": keys.openssl_version(),
        "tools": tf.tool_versions(),
        "authexp_version": __version__,
        "c2pa_tool": "not installed (C2PA verification unevaluated)",
        "ai_image_detector": "none available offline (detection unevaluated)",
    }


def provenance_cases(work, land, shp, key):
    """Each case: id, description, observed state(s), and what the state supports."""
    gen, cam, rev, forger = key["trusted-generator"], key["trusted-camera"], key["revoked-signer"], key["forger"]
    trust = {gen["key_id"], cam["key_id"], rev["key_id"]}
    revoked = {rev["key_id"]}
    claims_synth = {"claim_generator": "procedural-landscape/1.0", "digital_source_type": "algorithmicMedia",
                    "note": "synthetic test image"}
    L0, L1, L2, S0 = land[0], land[1], land[2], shp[0]
    signed_L0 = mf.build_manifest(L0, claims_synth, gen)
    cases = []

    def run(case_id, description, img, chunks, check_revocation=True, extra=None, text=None):
        path = os.path.join(work, case_id + ".png")
        write_png(path, img, text=text or {"Software": "authexp synthetic"}, extra_chunks=chunks)
        res = mf.verify_png(path, trust_list=trust, revoked=revoked, check_revocation=check_revocation)
        entry = {"id": case_id, "description": description, "state": res["state"],
                 "supported_statement": evidence.PROVENANCE[res["state"]][1],
                 "claims_as_signed": res.get("claims")}
        if extra:
            entry.update(extra)
        cases.append(entry)
        return res

    run("P01_intact", "Trusted generator key signs a synthetic landscape; file unchanged.", L0, [mf.manifest_chunk(signed_L0)])
    run("P02_stripped", "Same pixels, manifest removed (as when a converter drops unknown chunks).", L0, [])
    run("P03_jpeg90_manifest_kept", "Pixels re-encoded as JPEG q90 and decoded; manifest copied across unchanged.",
        tf.jpeg(L0, 90), [mf.manifest_chunk(signed_L0)])
    run("P04_webp80_manifest_kept", "Pixels re-encoded as WebP q80; manifest copied across unchanged.",
        tf.webp(L0, 80), [mf.manifest_chunk(signed_L0)])
    run("P05_crop_manifest_kept", "Image cropped by 8 px; manifest copied across unchanged.",
        tf.crop(L0, 8, 8), [mf.manifest_chunk(signed_L0)])
    run("P06_one_pixel_manifest_kept", "One colour value changed by 1; manifest copied across unchanged.",
        tf.nudge_one_pixel(L0), [mf.manifest_chunk(signed_L0)])
    run("P07_text_metadata_edited", "Unsigned text metadata changed; pixels and manifest unchanged.",
        L0, [mf.manifest_chunk(signed_L0)], text={"Software": "edited after signing", "Make": "ExampleCam"})
    cases[-1]["note"] = "The manifest covers pixels and its own claims only; unsigned metadata can change without affecting it."
    run("P08_manifest_transplanted", "Valid manifest from image L0 attached to a different image (S0).", S0, [mf.manifest_chunk(signed_L0)])
    forged = mf.build_manifest(S0, {"claim_generator": "ExampleCam firmware", "digital_source_type": "digitalCapture",
                                    "note": "false capture claim"}, forger)
    run("P09_self_signed_forgery", "An unknown key self-signs a false 'camera capture' claim for a synthetic image.",
        S0, [mf.manifest_chunk(forged)])
    spoof_id = mf.build_manifest(S0, {"claim_generator": "procedural-landscape/1.0", "digital_source_type": "algorithmicMedia"},
                                 forger, claimed_key_id=gen["key_id"])
    run("P10_key_id_spoof", "Forger claims the trusted generator's key id but signs with its own key.",
        S0, [mf.manifest_chunk(spoof_id)])
    false_capture = mf.build_manifest(L1, {"claim_generator": "ExampleCam firmware", "digital_source_type": "digitalCapture",
                                           "note": "trusted pipeline signed content it did not capture"}, cam)
    run("P11_trusted_key_false_claim", "A trust-listed 'camera' key signs a synthetic image as a capture "
        "(analogous to a signing pipeline being fed non-camera content).", L1, [mf.manifest_chunk(false_capture)])
    rev_manifest = mf.build_manifest(L2, claims_synth, rev)
    run("P12_revoked_key_checked", "Key on the trust list but also revoked; validator checks revocation.", L2,
        [mf.manifest_chunk(rev_manifest)], check_revocation=True)
    run("P13_revoked_key_unchecked", "Same file; validator does not check revocation.", L2,
        [mf.manifest_chunk(rev_manifest)], check_revocation=False)
    tampered = json.loads(signed_L0.decode())
    tampered["claims"]["digital_source_type"] = "digitalCapture"
    run("P14_claims_tampered", "Signed claims edited after signing (synthetic relabelled as capture).",
        L0, [mf.manifest_chunk(json.dumps(tampered, sort_keys=True, indent=1).encode())])
    # Real conversions through the operating system's image tool.
    sips_note = {}
    if tf.tool_available("sips"):
        src = os.path.join(work, "P15_source.png")
        write_png(src, L0, text={"Make": "ExampleCam"}, extra_chunks=[mf.manifest_chunk(signed_L0)])
        img, text, chunks = tf.sips_png_resave(src)
        res = mf.verify_image(img, chunks, trust, revoked)
        cases.append({"id": "P15_sips_png_resave", "description": "Signed PNG re-saved as PNG by macOS sips.",
                      "state": res["state"], "supported_statement": evidence.PROVENANCE[res["state"]][1],
                      "text_metadata_after": text, "chunks_after": [c.decode("latin-1") for c, _ in chunks]})
        img, text, chunks = tf.sips_jpeg_roundtrip(src, "80")
        res = mf.verify_image(img, chunks, trust, revoked)
        cases.append({"id": "P16_sips_jpeg_roundtrip", "description": "Signed PNG converted to JPEG (q80) and back by macOS sips.",
                      "state": res["state"], "supported_statement": evidence.PROVENANCE[res["state"]][1],
                      "text_metadata_after": text, "chunks_after": [c.decode("latin-1") for c, _ in chunks]})
    else:
        sips_note = {"sips": "not available; P15-P16 not run"}
    return cases, sips_note


def wm_summary(scores):
    det = sum(1 for z in scores if z >= wm.THRESHOLD)
    return {"n": len(scores), "detected": det, "detection_rate": det / len(scores),
            "z_min": round(min(scores), 2), "z_median": round(statistics.median(scores), 2), "z_max": round(max(scores), 2)}


def watermark_experiments(work, land, shp, n_null_keys):
    marked = [wm.embed(img, WM_KEY) for img in land]
    transforms = [
        ("none", lambda im: im),
        ("jpeg_q90", lambda im: tf.jpeg(im, 90)),
        ("jpeg_q75", lambda im: tf.jpeg(im, 75)),
        ("jpeg_q50", lambda im: tf.jpeg(im, 50)),
        ("jpeg_q30", lambda im: tf.jpeg(im, 30)),
        ("jpeg_q15", lambda im: tf.jpeg(im, 15)),
        ("webp_q80", lambda im: tf.webp(im, 80)),
        ("webp_q50", lambda im: tf.webp(im, 50)),
        ("webp_q20", lambda im: tf.webp(im, 20)),
        ("half_then_double", tf.half_then_double),
        ("crop_1px", lambda im: tf.crop(im, 1, 1)),
        ("crop_8px", lambda im: tf.crop(im, 8, 8)),
    ]
    robustness = {}
    for name, fn in transforms:
        robustness[name] = wm_summary([wm.detect(fn(im), WM_KEY) for im in marked])
    if tf.tool_available("sips"):
        scores = []
        for i, im in enumerate(marked):
            p = os.path.join(work, "wm_%02d.png" % i)
            write_png(p, im)
            scores.append(wm.detect(tf.sips_jpeg_roundtrip(p, "80")[0], WM_KEY))
        robustness["sips_jpeg80_roundtrip"] = wm_summary(scores)
    # Unmarked images, true key: should not be detected.
    unmarked_true_key = {
        "landscapes_unmarked": wm_summary([wm.detect(im, WM_KEY) for im in land]),
        "shapes_unmarked_other_generator": wm_summary([wm.detect(im, WM_KEY) for im in shp]),
    }
    # Null calibration: unmarked images scored against many unrelated keys.
    null_scores = []
    residuals = [(wm.residual(im), im.width, im.height) for im in land + shp]
    for k in range(n_null_keys):
        key = "null-key-%03d" % k
        for res, w, h in residuals:
            null_scores.append(wm.score_residual(res, w, h, key))
    n = len(null_scores)
    false_pos = sum(1 for z in null_scores if z >= wm.THRESHOLD)
    null = {"trials": n, "false_positives_at_threshold": false_pos, "threshold": wm.THRESHOLD,
            "empirical_fpr": false_pos / n, "rule_of_three_95pct_upper_bound": (3.0 / n) if false_pos == 0 else None,
            "z_mean": round(statistics.mean(null_scores), 3), "z_sd": round(statistics.pstdev(null_scores), 3),
            "z_max": round(max(null_scores), 2),
            "theoretical_one_sided_fpr_if_normal": 0.5 * math.erfc(wm.THRESHOLD / math.sqrt(2))}
    # Copy attack: mark estimated from a marked landscape, stamped onto unmarked shapes images.
    spoofed = [wm.copy_attack(m, s) for m, s in zip(marked, shp)]
    copy_attack = {"description": "Mark estimated from marked generator-A images and stamped onto unmarked images "
                                  "from a different generator, without the key.",
                   "result": wm_summary([wm.detect(im, WM_KEY) for im in spoofed])}
    return {"key_label": WM_KEY, "alpha": wm.ALPHA, "threshold": wm.THRESHOLD, "robustness": robustness,
            "unmarked_with_true_key": unmarked_true_key, "null_calibration": null, "copy_attack": copy_attack}


def metadata_experiments(work, land):
    claims = {"Make": "ExampleCam", "Model": "X-100", "DigitalSourceType": "digitalCapture",
              "DateTimeOriginal": "2026:01:01 12:00:00"}
    src = os.path.join(work, "M01_text_claims.png")
    write_png(src, land[3], text=claims)
    _img, text, _chunks = read_png(src)
    out = {"M01_forged_text_claims": {
        "description": "Camera-style text metadata written onto a synthetic landscape with ordinary file writing.",
        "claims_written": claims, "claims_read_back": text,
        "verification_available": "none: plain text metadata carries no signature or binding"}}
    if tf.tool_available("sips"):
        _i, t1, c1 = tf.sips_png_resave(src)
        _i, t2, c2 = tf.sips_jpeg_roundtrip(src, "80")
        out["M02_survival_sips_png_resave"] = {"text_after": t1, "chunks_after": [c.decode("latin-1") for c, _ in c1]}
        out["M03_survival_sips_jpeg_roundtrip"] = {"text_after": t2, "chunks_after": [c.decode("latin-1") for c, _ in c2]}
    out["M04_survival_libjpeg_ppm_path"] = {"note": "The cjpeg/djpeg path used here goes through PPM, which cannot carry "
                                                    "metadata; any PNG text or manifest chunk is dropped by construction."}
    return out


def evidence_examples():
    examples = {
        "trusted_valid_and_watermark_detected": evidence.summarize(mf.VALID_TRUSTED, True),
        "no_manifest_no_watermark": evidence.summarize(mf.NO_MANIFEST, False),
        "binding_mismatch_watermark_detected": evidence.summarize(mf.BINDING_MISMATCH, True),
        "untrusted_valid_no_watermark": evidence.summarize(mf.VALID_UNTRUSTED, False),
    }
    for ex in examples.values():
        for s in ex["statements"]:
            assert not evidence.contains_verdict_language(s["statement"]), s
    return examples


def write_results_md(results, path):
    r = results
    lines = []
    a = lines.append
    a("# Prep results: toy mechanisms only (not an evaluation of actual signals)")
    a("")
    a("Generated by `run_experiment.py` (%s run). All images are synthetic, non-intimate procedural landscapes and "
      "geometric shapes. **No real/fake verdicts are issued.** The manifest is a toy format (not C2PA) and the "
      "watermark is a toy scheme (not SynthID or any product). These results are preparation only. They do not "
      "evaluate actual provenance, watermark or detector signals; see docs/ACTUAL_SIGNAL_ROUTES.md." % r["mode"])
    a("")
    a("## Unevaluated")
    a("")
    a("- **AI-image detectors:** none available offline. No detector scores were produced or estimated.")
    a("- **C2PA verification:** no C2PA tool installed. C2PA conformance was not evaluated.")
    a("")
    a("## 1. Provenance (toy signed manifest)")
    a("")
    a("| Case | What was done | Verification state | Strongest supported statement |")
    a("|---|---|---|---|")
    for c in r["provenance"]["cases"]:
        a("| %s | %s | `%s` | %s |" % (c["id"], c["description"], c["state"], c["supported_statement"]))
    a("")
    for c in r["provenance"]["cases"]:
        if "chunks_after" in c:
            a("- %s: text metadata after conversion = `%s`; chunks after = `%s`." % (c["id"], c["text_metadata_after"], c["chunks_after"]))
    a("")
    w = r["watermark"]
    a("## 2. Watermark (toy keyed spread-spectrum scheme; alpha = %d, threshold z >= %.1f)" % (w["alpha"], w["threshold"]))
    a("")
    a("### 2.1 Detection on marked images after processing (%d marked landscapes)" % w["robustness"]["none"]["n"])
    a("")
    a("| Processing | Detected | z min | z median | z max |")
    a("|---|---|---|---|---|")
    for name, s in w["robustness"].items():
        a("| %s | %d/%d | %.2f | %.2f | %.2f |" % (name, s["detected"], s["n"], s["z_min"], s["z_median"], s["z_max"]))
    a("")
    a("### 2.2 Unmarked images and the false-positive rate")
    a("")
    for name, s in w["unmarked_with_true_key"].items():
        a("- %s, scored with the watermark key: %d/%d detected (z max %.2f)." % (name, s["detected"], s["n"], s["z_max"]))
    n = w["null_calibration"]
    ub = n["rule_of_three_95pct_upper_bound"]
    a("- Null calibration: %d trials (unmarked images x unrelated keys); %d at or above the threshold; "
      "empirical false-positive rate %.4f%s. Null z mean %.3f, sd %.3f, max %.2f. Theoretical one-sided rate if the score were "
      "exactly standard normal: %.1e." % (n["trials"], n["false_positives_at_threshold"], n["empirical_fpr"],
                                         ("; 95%% upper bound about %.4f (rule of three)" % ub) if ub else "",
                                         n["z_mean"], n["z_sd"], n["z_max"], n["theoretical_one_sided_fpr_if_normal"]))
    a("")
    ca = w["copy_attack"]["result"]
    a("### 2.3 Copy attack (spoofing without the key)")
    a("")
    a("- %s Detected on %d/%d spoofed images (z median %.2f)." % (w["copy_attack"]["description"], ca["detected"], ca["n"], ca["z_median"]))
    a("")
    a("## 3. Plain metadata")
    a("")
    for k, v in r["metadata"].items():
        a("- **%s**: `%s`" % (k, json.dumps(v, sort_keys=True)))
    a("")
    a("## 4. Evidence-to-statement mapping (examples)")
    a("")
    for name, ex in r["evidence_examples"].items():
        a("- **%s** -> overall: `%s`; real/fake verdict: %s." % (name, ex["overall"], ex["real_or_fake_verdict"]))
    a("")
    a("See README.md for interpretation, counterexamples and coverage limits.")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    n_images = 4 if args.quick else 12
    n_null_keys = 5 if args.quick else 40
    os.makedirs(ARTIFACT_DIR, exist_ok=True)
    land = [synth.landscape(i) for i in range(n_images)]
    shp = [synth.shapes(i) for i in range(n_images)]
    artifact_hashes = {}
    for i, im in enumerate(land):
        p = os.path.join(ARTIFACT_DIR, "landscape_%02d.png" % i)
        write_png(p, im)
        artifact_hashes[os.path.basename(p)] = {"file_sha256": sha256_file(p), "pixel_sha256": im.pixel_digest()}
    for i, im in enumerate(shp):
        p = os.path.join(ARTIFACT_DIR, "shapes_%02d.png" % i)
        write_png(p, im)
        artifact_hashes[os.path.basename(p)] = {"file_sha256": sha256_file(p), "pixel_sha256": im.pixel_digest()}
    with tempfile.TemporaryDirectory() as work:
        key = {name: keys.make_test_key(name, work) for name in ("trusted-generator", "trusted-camera", "revoked-signer", "forger")}
        cases, sips_note = provenance_cases(work, land, shp, key)
        results = {
            "mode": "quick" if args.quick else "full",
            "environment": environment(),
            "parameters": {"images_per_family": n_images, "image_size": synth.SIZE, "null_keys": n_null_keys,
                           "watermark_alpha": wm.ALPHA, "watermark_threshold": wm.THRESHOLD},
            "test_key_ids": {k: v["key_id"] for k, v in key.items()},
            "provenance": {"cases": cases, "notes": sips_note,
                           "trust_list": ["trusted-generator", "trusted-camera", "revoked-signer"],
                           "revocation_list": ["revoked-signer"]},
            "watermark": watermark_experiments(work, land, shp, n_null_keys),
            "metadata": metadata_experiments(work, land),
            "evidence_examples": evidence_examples(),
            "unevaluated": {"ai_image_detectors": evidence.DETECTOR[1], "c2pa": evidence.C2PA[1]},
            "artifact_hashes": artifact_hashes,
        }
    out_json = os.path.join(RESULTS_DIR, "results.json" if not args.quick else "results_quick.json")
    with open(out_json, "w") as f:
        json.dump(results, f, indent=1, sort_keys=True)
    if not args.quick:
        write_results_md(results, os.path.join(HERE, "RESULTS.md"))
    print("wrote", os.path.relpath(out_json, HERE))
    for c in results["provenance"]["cases"]:
        print("%-28s %s" % (c["id"], c["state"]))
    for name, s in results["watermark"]["robustness"].items():
        print("wm %-22s %d/%d  z_med=%.2f" % (name, s["detected"], s["n"], s["z_median"]))
    print("null:", results["watermark"]["null_calibration"])
    print("copy attack:", results["watermark"]["copy_attack"]["result"])


if __name__ == "__main__":
    main()
