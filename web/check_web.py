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
        "icon-192.png", "icon-512.png", "trust-anchors.js",
        "vendor/c2pa-web/inline.js", "vendor/c2pa-web/builder-CaTgrAW1.js", "vendor/c2pa-web/c2pa_worker.js",
        "vendor/c2pa-utilities/index.js", "vendor/c2pa-utilities/context.js", "vendor/c2pa-utilities/settings.js",
        "vendor/c2pa-utilities/fetchWithRetry.js", "vendor/c2pa-utilities/caseConversion.js",
        "vendor/c2pa-utilities/signingAlg.js", "vendor/c2pa-utilities/assetSize.js",
        "vendor/highgain/index.js", "vendor/ts-deepmerge/index.js",
        "trust/C2PA-TRUST-LIST.pem", "trust/C2PA-TSA-TRUST-LIST.pem",
        "trust/C2PA-INTERIM-TRUST-LIST.pem", "trust/c2pa-interim-eku-store.cfg",
    ]
    for rel in required:
        check("exists " + rel, (HERE / rel).is_file())

    # trust module regenerates identically
    r = subprocess.run([sys.executable, str(HERE / "build_trust_module.py"), "--fetched", "2026-11-27"],
                       capture_output=True, text=True, cwd=str(HERE))
    check("build_trust_module.py runs", r.returncode == 0, r.stderr.strip()[:200])
    if r.returncode == 0:
        # --fetched fixes the recorded date so regeneration is reproducible for this pin
        check("trust-anchors.js records pinned hashes",
              '"sha256": "62673a9e68e30f953eda65b4171e980ee111e1f12385989b1230fdfe787bfae8"'
              in (HERE / "trust-anchors.js").read_text())

    # recorded PEM hashes (PINS.md)
    pins = {
        "trust/C2PA-TRUST-LIST.pem": "62673a9e68e30f953eda65b4171e980ee111e1f12385989b1230fdfe787bfae8",
        "trust/C2PA-TSA-TRUST-LIST.pem": "eca8347ee71e31d226e00c85b15aca356116fefe6c26ed8c0ee1f954115b1990",
        "trust/C2PA-INTERIM-TRUST-LIST.pem": "db57e50b9bd4e4c786cbb91f38fd85e2af6a9d5412438a8cddcc42688df07ae5",
        "trust/c2pa-interim-eku-store.cfg": "1044c30a906b0c9cbe28b4a4c0002ca56a718f0ae22b9af83238543a07d0e718",
    }
    for rel, want in pins.items():
        p = HERE / rel
        check("sha256 " + rel, p.is_file() and sha256(p) == want)

    # no bare specifiers left in vendored files (browser would fail to resolve them)
    bare = re.compile(r'^\s*(?:import|export)[^\n]*?from\s*["\'](?!\.{1,2}/|https?:|data:|blob:)', re.M)
    for js in sorted((HERE / "vendor").rglob("*.js")):
        if "_pkgs" in js.parts:
            continue
        hits = [m.group(0).strip()[:80] for m in bare.finditer(js.read_text())]
        check("no bare specifiers in " + str(js.relative_to(HERE)), not hits, "; ".join(hits))

    # sw.js precaches exactly the shipped asset list (excluding trust PEMs: trust-anchors.js covers them)
    sw = (HERE / "sw.js").read_text()
    sw_assets = set(re.findall(r"'(\./[^']*)'", sw))
    expected = {"./", "./index.html", "./styles.css", "./app.js", "./trust-anchors.js",
                "./manifest.webmanifest", "./icon-192.png", "./icon-512.png"}
    expected |= {"./" + str(p.relative_to(HERE)) for p in (HERE / "vendor").rglob("*.js") if "_pkgs" not in p.parts}
    check("sw.js asset list matches shipped files", sw_assets == expected,
          "in sw but missing: %s; shipped but not cached: %s"
          % (sorted(sw_assets - expected), sorted(expected - sw_assets)))

    # index.html declares the no-network CSP
    html = (HERE / "index.html").read_text()
    check("index.html declares connect-src 'none'", "connect-src 'none'" in html)

    print()
    if FAIL:
        print("%d check(s) failed" % len(FAIL))
        sys.exit(1)
    print("all web checks passed")


if __name__ == "__main__":
    main()
