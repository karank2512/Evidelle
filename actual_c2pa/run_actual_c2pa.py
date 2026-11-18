#!/usr/bin/env python3
"""Actual C2PA experiment. It is separate from the toy preparation in authexp/ and run_experiment.py.

It uses the official `c2patool` binary (contentauth/c2pa-rs release c2patool-v0.27.23) on:
- a few official C2PA public test files (non-intimate; CC-BY-SA-4.0), and
- deterministic synthetic images signed here with the TEST credentials bundled with c2patool
  (certificates marked "FOR TESTING ONLY").

Offline only:
- every c2patool run is wrapped in a macOS sandbox that denies all network access;
- remote-manifest and OCSP fetching are disabled in actual_c2pa/settings/offline.toml;
- trust anchors are local files only;
- no timestamp-authority URL is used when signing.

Validation states describe signatures, bindings and trust configuration. They are not verdicts on
whether a scene is real.

Usage (from the repository root):  python3 actual_c2pa/run_actual_c2pa.py
Requires: the extracted c2patool folder (default tools/c2patool-dl/extracted/c2patool, or set
AUTHEXP_C2PATOOL_DIR), the official sample files in samples/official/, libjpeg-turbo (cjpeg,
djpeg, jpegtran) and macOS sandbox-exec. Optionally macOS sips.
"""

import hashlib
import json
import os
import shutil
import struct
import subprocess
import sys
import zlib

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

from authexp import synth  # noqa: E402
from authexp.imageio import PNG_SIGNATURE, decode_png, write_png, write_ppm  # noqa: E402

TOOL_DIR = os.environ.get("AUTHEXP_C2PATOOL_DIR", os.path.join(HERE, "tools", "c2patool-dl", "extracted", "c2patool"))
TOOL = os.path.join(TOOL_DIR, "c2patool")
TEST_CREDS = os.path.join(TOOL_DIR, "sample")
OFFICIAL = os.path.join(HERE, "samples", "official")
SETTINGS = os.path.join(HERE, "actual_c2pa", "settings", "offline.toml")
OUT_DIR = os.path.join(HERE, "results", "actual_c2pa")
WORK = os.path.join(OUT_DIR, "work")
SANDBOX_PROFILE = "(version 1)(allow default)(deny network*)"

TOOL_SOURCE = {
    "name": "c2patool",
    "version": "0.27.23",
    "release_url": "https://github.com/contentauth/c2pa-rs/releases/tag/c2patool-v0.27.23",
    "asset": "c2patool-v0.27.23-universal-apple-darwin.zip",
    "asset_size_bytes": 20800495,
    "asset_sha256_recorded_by_github": "380647e657ed16bb7e61982bd52f6c0b49a1cd92f09dbef49febd0f4c439a673",
    "license": "MIT OR Apache-2.0 (LICENSE-MIT and LICENSE-APACHE in contentauth/c2pa-rs)",
    "signing": "ad-hoc linker signature; no Developer ID or notarization (integrity relies on the GitHub-recorded digest)",
}

SAMPLES_REPO = "https://github.com/c2pa-org/public-testfiles"
SAMPLES_PATH = "legacy/1.4/image/jpeg"
OFFICIAL_SAMPLES = [
    # (file, git blob sha recorded by GitHub, documented expectation from the folder README)
    ("adobe-20220124-CA.jpg", "c0fc9ac13155427f8111e7b1d24bdbcebf59a8a3",
     "Valid claim with one ingredient; signed with C2PA Tool's test certificate"),
    ("adobe-20220124-E-sig-CA.jpg", "142f6dc7ba854af189b84ee58859de732aa3efef", "Invalid credentials: invalid signature"),
    ("adobe-20220124-E-dat-CA.jpg", "6284416b5a226538817f10996245b78f6eaa2b5c", "Invalid credentials: hard binding hash mismatch"),
    ("adobe-20220124-E-uri-CA.jpg", "8f57168cc9e41b348f01fb24425ab9c9e6c1da42", "Invalid credentials: assertion URI hash mismatch"),
    ("truepic-20230212-landscape.jpg", "42dd569a4e4f18d6c7bab4ccebab3096b0f24865",
     "Example of camera capture details (production signer, not the test certificate)"),
]
BUNDLED_SAMPLES = [
    ("C.jpg", "Bundled with c2patool (sample/); expectation not documented, observed only"),
    ("image.jpg", "Bundled with c2patool (sample/); expectation not documented, observed only"),
]

IPTC = "http://cv.iptc.org/newscodes/digitalsourcetype/"

MEANING = {
    "Trusted": "The signature is valid and chains to the configured trust anchors. Here those are C2PA TEST anchors "
               "(FOR TESTING ONLY) unless stated otherwise. The signed claims are the signer's declarations; this does "
               "not establish that the depicted scene is real.",
    "Valid": "The manifest is intact and the signature is valid, but the signer does not chain to a configured trust "
             "anchor (see signingCredential.untrusted). The signer's identity is not established.",
    "Invalid": "The manifest fails validation (see the failure codes). No conclusion about origin is supported.",
    "NO_MANIFEST": "c2patool found no C2PA manifest. Absence is not evidence either way.",
    "ERROR": "The tool reported an error. The result is unknown.",
}


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def git_blob_sha(path):
    with open(path, "rb") as f:
        data = f.read()
    return hashlib.sha1(b"blob %d\x00" % len(data) + data).hexdigest()


def rel(path):
    return os.path.relpath(path, HERE)


def run_tool(args, cwd):
    cmd = ["sandbox-exec", "-p", SANDBOX_PROFILE, TOOL, "--settings", SETTINGS] + args
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, timeout=180)
    return res.returncode, res.stdout.decode("utf-8", "replace"), res.stderr.decode("utf-8", "replace")


def _sanitize(text):
    return text.replace(HERE, "<repo>").strip()


def summarize_report(rc, stdout, stderr):
    """Turn c2patool output into a compact, path-free summary."""
    if rc != 0:
        first = _sanitize(stderr).splitlines()[0] if stderr.strip() else "(no stderr)"
        state = "NO_MANIFEST" if "No claim found" in stderr else "ERROR"
        return {"state": state, "exit_code": rc, "message": first}
    try:
        d = json.loads(stdout)
    except ValueError:
        return {"state": "ERROR", "exit_code": rc, "message": "unparseable tool output"}
    am = (d.get("validation_results") or {}).get("activeManifest") or {}
    summary = {
        "state": d.get("validation_state") or "ERROR",
        "exit_code": rc,
        "failure_codes": [x.get("code") for x in am.get("failure", [])],
        "informational_codes": [x.get("code") for x in am.get("informational", [])],
        "success_codes": sorted({x.get("code") for x in am.get("success", [])}),
    }
    active = (d.get("manifests") or {}).get(d.get("active_manifest") or "", {})
    sig = active.get("signature_info") or {}
    summary["signature_issuer"] = sig.get("issuer")
    summary["signature_common_name"] = sig.get("common_name")
    gen = active.get("claim_generator_info") or []
    summary["claim_generator"] = [g.get("name") for g in gen if isinstance(g, dict)] or active.get("claim_generator")
    dst = []
    for a in active.get("assertions", []) or []:
        if str(a.get("label", "")).startswith("c2pa.actions"):
            for act in (a.get("data") or {}).get("actions", []) or []:
                if act.get("digitalSourceType"):
                    dst.append(act["digitalSourceType"].replace(IPTC, ""))
    summary["declared_digital_source_types"] = dst
    summary["ingredient_count"] = len(active.get("ingredients", []) or [])
    return summary


def validate(path, cwd, trust):
    args = [os.path.relpath(path, cwd)]
    if trust:
        args += ["trust", "--trust_anchors", os.path.join(TEST_CREDS, "trust_anchors.pem"),
                 "--trust_config", os.path.join(TEST_CREDS, "store.cfg")]
    return summarize_report(*run_tool(args, cwd))


def sign(src, dst, title, source_type):
    manifest = {
        "claim_generator_info": [{"name": "authexp-actual-c2pa", "version": "0.1"}],
        "title": title,
        "alg": "es256",
        "sign_cert": os.path.join(TEST_CREDS, "es256_certs.pem"),
        "private_key": os.path.join(TEST_CREDS, "es256_private.key"),
        "assertions": [{"label": "c2pa.actions", "data": {"actions": [
            {"action": "c2pa.created", "digitalSourceType": IPTC + source_type}]}}],
    }
    mpath = os.path.join(WORK, "manifest_%s.json" % title.replace(" ", "_"))
    with open(mpath, "w") as f:
        json.dump(manifest, f)
    rc, _out, err = run_tool([os.path.relpath(src, WORK), "-m", os.path.relpath(mpath, WORK),
                              "-o", os.path.relpath(dst, WORK), "-f"], WORK)
    if rc != 0:
        raise RuntimeError("signing failed: " + _sanitize(err)[:300])


# --- PNG chunk-level helpers (keep, drop or move C2PA chunks without touching pixels) ---

def png_chunks(path):
    with open(path, "rb") as f:
        data = f.read()
    assert data[:8] == PNG_SIGNATURE
    pos, out = 8, []
    while pos < len(data):
        (n,) = struct.unpack(">I", data[pos:pos + 4])
        out.append((data[pos + 4:pos + 8], data[pos + 8:pos + 8 + n]))
        pos += 12 + n
    return out


def png_build(chunks):
    out = bytearray(PNG_SIGNATURE)
    for ctype, data in chunks:
        out += struct.pack(">I", len(data)) + ctype + data + struct.pack(">I", zlib.crc32(ctype + data) & 0xFFFFFFFF)
    return bytes(out)


def _replace_idat(chunks, raw_scanlines, level, ihdr=None):
    new, done = [], False
    for ctype, data in chunks:
        if ctype == b"IHDR" and ihdr is not None:
            new.append((ctype, ihdr))
        elif ctype == b"IDAT":
            if not done:
                new.append((b"IDAT", zlib.compress(raw_scanlines, level)))
                done = True
        else:
            new.append((ctype, data))
    return new


def png_recompress(src, dst, level=1):
    """Same pixels, different IDAT bytes; all other chunks (including C2PA) kept in place."""
    ch = png_chunks(src)
    raw = zlib.decompress(b"".join(d for t, d in ch if t == b"IDAT"))
    with open(dst, "wb") as f:
        f.write(png_build(_replace_idat(ch, raw, level)))


def png_change_one_value(src, dst):
    """Change one colour value by 1 (filter-0 scanlines as written by authexp); keep other chunks."""
    ch = png_chunks(src)
    raw = bytearray(zlib.decompress(b"".join(d for t, d in ch if t == b"IDAT")))
    raw[1] = (raw[1] + 1) % 256  # first pixel's red value (byte 0 is the row's filter type)
    with open(dst, "wb") as f:
        f.write(png_build(_replace_idat(ch, bytes(raw), 9)))


def png_crop_keep_chunks(src, dst, dx=8, dy=8):
    ch = png_chunks(src)
    with open(src, "rb") as f:
        img, _t, _o = decode_png(f.read())
    nw, nh = img.width - dx, img.height - dy
    raw = bytearray()
    for y in range(nh):
        raw.append(0)
        s = ((y + dy) * img.width + dx) * 3
        raw += img.rgb[s:s + nw * 3]
    ihdr = struct.pack(">IIBBBBB", nw, nh, 8, 2, 0, 0, 0)
    with open(dst, "wb") as f:
        f.write(png_build(_replace_idat(ch, bytes(raw), 9, ihdr=ihdr)))


def png_strip(src, dst):
    keep = (b"IHDR", b"PLTE", b"IDAT", b"IEND")
    with open(dst, "wb") as f:
        f.write(png_build([(t, d) for t, d in png_chunks(src) if t in keep]))


def png_transplant(manifest_src, pixels_src, dst):
    """Move the C2PA chunk(s) from one signed PNG into a different, unsigned PNG."""
    c2pa = [(t, d) for t, d in png_chunks(manifest_src) if t == b"caBX"]
    target = png_chunks(pixels_src)
    with open(dst, "wb") as f:
        f.write(png_build(target[:1] + c2pa + target[1:]))


def png_has_chunk(path, ctype=b"caBX"):
    return any(t == ctype for t, _ in png_chunks(path))


def run(cmd):
    subprocess.run(cmd, check=True, capture_output=True)


def cert_dates(pem_path):
    res = subprocess.run(["openssl", "x509", "-in", pem_path, "-noout", "-subject", "-dates"], capture_output=True)
    return [l.strip() for l in res.stdout.decode().splitlines()]


def main():
    for need in (TOOL, SETTINGS):
        if not os.path.exists(need):
            sys.exit("missing: %s" % rel(need))
    os.makedirs(WORK, exist_ok=True)
    results = {"tool": TOOL_SOURCE, "environment": {}, "offline_controls": {
        "sandbox_profile": SANDBOX_PROFILE, "settings_file": rel(SETTINGS),
        "remote_manifest_fetch": False, "ocsp_fetch": False, "allowed_network_hosts": [],
        "trust_anchor_sources": "local files only (c2patool sample/trust_anchors.pem and sample/store.cfg)",
        "timestamp_authority": "none used when signing"}}
    rc, out, _ = run_tool(["-V"], HERE)
    results["environment"]["c2patool_version_reported"] = out.strip()
    results["environment"]["tool_binary_sha256"] = sha256(TOOL)
    results["environment"]["test_signing_certificate"] = cert_dates(os.path.join(TEST_CREDS, "es256_certs.pem"))

    # 1. Official samples, with and without the TEST trust anchors.
    official = []
    for name, blob, expected in OFFICIAL_SAMPLES:
        p = os.path.join(OFFICIAL, name)
        entry = {"file": name, "source": "%s/blob/main/%s/%s" % (SAMPLES_REPO, SAMPLES_PATH, name),
                 "license": "CC-BY-SA-4.0", "documented_expectation": expected,
                 "git_blob_sha_matches_github": git_blob_sha(p) == blob, "sha256": sha256(p),
                 "no_trust_anchors": validate(p, OFFICIAL, trust=False),
                 "test_trust_anchors": validate(p, OFFICIAL, trust=True)}
        official.append(entry)
    for name, expected in BUNDLED_SAMPLES:
        p = os.path.join(TEST_CREDS, name)
        official.append({"file": "c2patool sample/" + name, "source": TOOL_SOURCE["release_url"], "license": TOOL_SOURCE["license"],
                         "documented_expectation": expected, "sha256": sha256(p),
                         "no_trust_anchors": validate(p, TEST_CREDS, trust=False),
                         "test_trust_anchors": validate(p, TEST_CREDS, trust=True)})
    results["official_samples"] = official

    # 2. Synthetic images signed with the bundled TEST credentials, then processed.
    cases = []

    def record(case_id, description, path):
        cases.append({"id": case_id, "description": description, "file": rel(path),
                      "c2pa_chunk_present": png_has_chunk(path) if path.endswith(".png") else None,
                      "no_trust_anchors": validate(path, WORK, trust=False),
                      "test_trust_anchors": validate(path, WORK, trust=True)})

    w = lambda n: os.path.join(WORK, n)  # noqa: E731
    write_png(w("L0.png"), synth.landscape(0))
    write_png(w("S0.png"), synth.shapes(0))
    sign(w("L0.png"), w("L0_signed.png"), "synthetic landscape 0", "algorithmicMedia")
    record("A01_png_signed_intact", "Synthetic landscape signed with TEST credentials, declared algorithmicMedia; unchanged.", w("L0_signed.png"))
    png_recompress(w("L0_signed.png"), w("A02.png"), level=1)
    record("A02_png_lossless_recompress", "Same pixels, IDAT re-compressed (zlib level 1); C2PA chunk kept in place.", w("A02.png"))
    png_change_one_value(w("L0_signed.png"), w("A03.png"))
    record("A03_png_one_value_changed", "One colour value changed by 1; C2PA chunk kept.", w("A03.png"))
    png_crop_keep_chunks(w("L0_signed.png"), w("A04.png"))
    record("A04_png_crop_8px", "Cropped by 8 px; C2PA chunk kept.", w("A04.png"))
    png_strip(w("L0_signed.png"), w("A05.png"))
    record("A05_png_c2pa_chunk_removed", "C2PA chunk removed; pixels and IDAT bytes unchanged.", w("A05.png"))
    png_transplant(w("L0_signed.png"), w("S0.png"), w("A06.png"))
    record("A06_png_manifest_transplanted", "C2PA chunk from the signed landscape inserted into a different synthetic image.", w("A06.png"))
    if shutil.which("sips"):
        run(["sips", "-s", "format", "png", w("L0_signed.png"), "--out", w("A07.png")])
        record("A07_png_sips_resave", "Signed PNG re-saved as PNG by macOS sips.", w("A07.png"))
    sign(w("L0.png"), w("L0_false_capture.png"), "synthetic landscape false capture", "digitalCapture")
    record("A08_png_false_capture_claim", "The same synthetic landscape signed with TEST credentials but declared digitalCapture "
           "(a false claim, made deliberately).", w("L0_false_capture.png"))

    # JPEG path.
    write_ppm(w("L1.ppm"), synth.landscape(1))
    run(["cjpeg", "-quality", "90", "-outfile", w("L1.jpg"), w("L1.ppm")])
    sign(w("L1.jpg"), w("L1_signed.jpg"), "synthetic landscape 1 jpeg", "algorithmicMedia")
    record("B01_jpeg_signed_intact", "Synthetic landscape JPEG signed with TEST credentials; unchanged.", w("L1_signed.jpg"))
    run(["jpegtran", "-copy", "all", "-optimize", "-outfile", w("B02.jpg"), w("L1_signed.jpg")])
    record("B02_jpeg_lossless_transcode_markers_kept", "jpegtran -copy all -optimize (lossless; all markers copied).", w("B02.jpg"))
    run(["jpegtran", "-copy", "none", "-outfile", w("B03.jpg"), w("L1_signed.jpg")])
    record("B03_jpeg_lossless_transcode_markers_dropped", "jpegtran -copy none (lossless; extra markers dropped).", w("B03.jpg"))
    run(["djpeg", "-ppm", "-outfile", w("B04.ppm"), w("L1_signed.jpg")])
    run(["cjpeg", "-quality", "75", "-outfile", w("B04.jpg"), w("B04.ppm")])
    record("B04_jpeg_reencode_q75", "Decoded and re-encoded at JPEG quality 75 (libjpeg-turbo).", w("B04.jpg"))
    if shutil.which("sips"):
        run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "80", w("L1_signed.jpg"), "--out", w("B05.jpg")])
        record("B05_jpeg_sips_resave_q80", "Signed JPEG re-saved as JPEG (quality 80) by macOS sips.", w("B05.jpg"))
    results["synthetic_cases"] = cases
    results["state_meanings"] = MEANING

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "actual_c2pa_results.json"), "w") as f:
        json.dump(results, f, indent=1, sort_keys=True)
    write_md(results, os.path.join(HERE, "RESULTS_ACTUAL_C2PA.md"))
    for e in official:
        print("%-36s no-trust=%-11s test-trust=%-11s %s" % (e["file"], e["no_trust_anchors"]["state"],
                                                          e["test_trust_anchors"]["state"],
                                                          e["no_trust_anchors"].get("failure_codes", e["no_trust_anchors"].get("message"))))
    for c in cases:
        print("%-42s no-trust=%-11s test-trust=%-11s %s" % (c["id"], c["no_trust_anchors"]["state"],
                                                          c["test_trust_anchors"]["state"],
                                                          c["no_trust_anchors"].get("failure_codes", c["no_trust_anchors"].get("message"))))


def _codes(s):
    if s["state"] in ("NO_MANIFEST", "ERROR"):
        return s.get("message", "")
    return ", ".join(s.get("failure_codes") or []) or "none"


def write_md(r, path):
    L = []
    a = L.append
    a("# Actual C2PA results (official c2patool; offline)")
    a("")
    a("This is separate from the toy preparation in RESULTS.md. It uses the official `c2patool` %s binary "
      "(release %s; asset SHA-256 `%s`, matching GitHub's recorded digest)." % (
          r["tool"]["version"], r["tool"]["release_url"], r["tool"]["asset_sha256_recorded_by_github"]))
    a("")
    a("**Offline controls:** every run is in a macOS sandbox that denies all network access. Remote-manifest and OCSP "
      "fetching are disabled. Trust anchors are local files only, and no timestamp authority was used when signing.")
    a("")
    a("**Trust conditions:**")
    a("- *No trust anchors:* nothing is configured as trusted.")
    a("- *Test trust anchors:* the C2PA **test** root bundled with c2patool (FOR TESTING ONLY). \"Trusted\" therefore "
      "means \"chains to the test root\" here, not to any production trust list.")
    a("")
    a("**These states describe signatures, bindings and trust configuration. They are not verdicts on whether a scene "
      "is real.** AI-image detectors, SynthID and production watermarks remain unevaluated.")
    a("")
    a("## 1. Official C2PA test files and bundled samples")
    a("")
    a("| File | Documented expectation | No trust anchors | Failure codes (no anchors) | Test trust anchors |")
    a("|---|---|---|---|---|")
    for e in r["official_samples"]:
        a("| %s | %s | `%s` | %s | `%s` |" % (e["file"], e["documented_expectation"], e["no_trust_anchors"]["state"],
                                              _codes(e["no_trust_anchors"]), e["test_trust_anchors"]["state"]))
    a("")
    a("Sources: %s (`%s`, CC-BY-SA-4.0), plus the `sample/` folder in the c2patool release zip. Each downloaded test "
      "file matched the git blob hash GitHub records for it." % (SAMPLES_REPO, SAMPLES_PATH))
    a("")
    a("## 2. Synthetic images signed with TEST credentials, then processed")
    a("")
    a("| Case | What was done | C2PA chunk present (PNG) | No trust anchors | Failure codes (no anchors) | Test trust anchors | Declared source type |")
    a("|---|---|---|---|---|---|---|")
    for c in r["synthetic_cases"]:
        s = c["no_trust_anchors"]
        a("| %s | %s | %s | `%s` | %s | `%s` | %s |" % (
            c["id"], c["description"], "" if c["c2pa_chunk_present"] is None else c["c2pa_chunk_present"], s["state"],
            _codes(s), c["test_trust_anchors"]["state"], ", ".join(s.get("declared_digital_source_types") or []) or "-"))
    a("")
    a("## 3. What each state supports")
    a("")
    for k, v in r["state_meanings"].items():
        a("- **%s:** %s" % (k, v))
    a("")
    a("Test signing certificate used for the synthetic cases: %s." % "; ".join(r["environment"]["test_signing_certificate"]))
    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
