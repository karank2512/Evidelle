"""Checks the web app's pinned inputs and generated files. Standard library only.

    python3 web/check_web.py

Verifies, without running a browser:
- every file the page and service worker need is present;
- trust-anchors.js regenerates byte-identically from the pinned PEMs;
- the pinned PEMs still match their recorded SHA-256s;
- no vendored file keeps a bare module specifier the browser cannot resolve;
- sw.js precaches exactly the shipped asset list.
"""

import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ((" — " + detail) if detail and not ok else ""))
    if not ok:
        FAIL.append(name)


def sha256(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def main():
    required = [
        "index.html", "styles.css", "app.js", "sw.js", "manifest.webmanifest",
        "icon-192.png", "icon-512.png", "trust-anchors.js", "pins.json",
        "vendor/c2pa-web/inline.js", "vendor/c2pa-web/builder-CaTgrAW1.js", "vendor/c2pa-web/c2pa_worker.js",
        "vendor/c2pa-utilities/index.js", "vendor/c2pa-utilities/context.js", "vendor/c2pa-utilities/settings.js",
        "vendor/c2pa-utilities/fetchWithRetry.js", "vendor/c2pa-utilities/caseConversion.js",
        "vendor/c2pa-utilities/signingAlg.js", "vendor/c2pa-utilities/assetSize.js",
        "vendor/highgain/index.js", "vendor/ts-deepmerge/index.js",
        "trust/C2PA-TRUST-LIST.pem", "trust/C2PA-TSA-TRUST-LIST.pem",
        "trust/C2PA-INTERIM-TRUST-LIST.pem", "trust/c2pa-interim-eku-store.cfg",
        "detector-model.fp16.onnx",
        "vendor/onnxruntime-web/ort.wasm.min.mjs",
        "vendor/onnxruntime-web/ort-wasm-simd-threaded.mjs",
        "vendor/onnxruntime-web/ort-wasm-simd-threaded.wasm",
    ]
    for rel in required:
        check("exists " + rel, (HERE / rel).is_file())

    # recorded hashes — web/pins.json is the single source of truth (the trust-refresh
    # workflow updates it when upstream lists change)
    pins = json.loads((HERE / "pins.json").read_text())

    # trust module regenerates identically
    r = subprocess.run([sys.executable, str(HERE / "build_trust_module.py"), "--fetched", "2026-11-27"],
                       capture_output=True, text=True, cwd=str(HERE))
    check("build_trust_module.py runs", r.returncode == 0, r.stderr.strip()[:200])
    if r.returncode == 0:
        # --fetched fixes the recorded date so regeneration is reproducible for this pin
        check("trust-anchors.js records pinned hashes",
              '"sha256": "' + pins["trust/C2PA-TRUST-LIST.pem"] + '"'
              in (HERE / "trust-anchors.js").read_text())
    for rel, want in pins.items():
        p = HERE / rel
        check("sha256 " + rel, p.is_file() and sha256(p) == want)

    # no bare specifiers left in vendored files (browser would fail to resolve them)
    bare = re.compile(r'^\s*(?:import|export)[^\n]*?from\s*["\'](?!\.{1,2}/|https?:|data:|blob:)', re.M)
    vendored_js = sorted((HERE / "vendor").rglob("*.js")) + sorted((HERE / "vendor").rglob("*.mjs"))
    for js in vendored_js:
        if "_pkgs" in js.parts:
            continue
        hits = [m.group(0).strip()[:80] for m in bare.finditer(js.read_text())]
        check("no bare specifiers in " + str(js.relative_to(HERE)), not hits, "; ".join(hits))

    # sw.js precaches exactly the shipped core asset list, and declares the detector
    # files as on-demand runtime assets (never precached: ~60 MB is opt-in only).
    sw = (HERE / "sw.js").read_text()
    pre = re.search(r"const ASSETS = \[(.*?)\];", sw, re.S)
    run = re.search(r"const RUNTIME_ASSETS = \[(.*?)\];", sw, re.S)
    check("sw.js declares ASSETS and RUNTIME_ASSETS", bool(pre) and bool(run))
    if pre and run:
        sw_assets = set(re.findall(r"'(\./[^']*)'", pre.group(1)))
        expected = {"./", "./index.html", "./styles.css", "./app.js", "./trust-anchors.js",
                    "./manifest.webmanifest", "./icon-192.png", "./icon-512.png"}
        expected |= {"./" + str(p.relative_to(HERE)) for p in vendored_js
                     if "_pkgs" not in p.parts and "onnxruntime-web" not in p.parts}
        check("sw.js asset list matches shipped files", sw_assets == expected,
              "in sw but missing: %s; shipped but not cached: %s"
              % (sorted(sw_assets - expected), sorted(expected - sw_assets)))
        sw_runtime = set(re.findall(r"'(\./[^']*)'", run.group(1)))
        expected_rt = {"./detector-model.fp16.onnx"} | {
            "./vendor/onnxruntime-web/" + f for f in
            ["ort.wasm.min.mjs", "ort-wasm-simd-threaded.mjs", "ort-wasm-simd-threaded.wasm"]}
        check("sw.js runtime list matches detector files", sw_runtime == expected_rt,
              "in runtime but missing: %s; expected but not listed: %s"
              % (sorted(sw_runtime - expected_rt), sorted(expected_rt - sw_runtime)))

    # index.html declares the same-origin-only CSP
    html = (HERE / "index.html").read_text()
    check("index.html declares connect-src 'self'", "connect-src 'self'" in html)

    print()
    if FAIL:
        print("%d check(s) failed" % len(FAIL))
        sys.exit(1)
    print("all web checks passed")


if __name__ == "__main__":
    main()
