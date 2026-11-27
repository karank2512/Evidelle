# Evidelle web app: on-device C2PA evidence check

A static page that checks JPEG, PNG or WebP images (up to 25 MB) for C2PA Content Credentials —
**entirely in the browser**. The file never leaves the device: verification runs in the pinned
`@contentauth/c2pa-web` WebAssembly build, vendored under `vendor/`, and the page declares
`connect-src 'self'` so it can fetch only this site's own files — no request can reach a third party.

Labels are the repo's fixed honest set — **Intact · Doesn't match · Fails validation · No credential ·
Unknown** — plus a trust result against two pinned lists:

- the official **C2PA conformance trust list** (what Adobe's Inspect uses), and
- the frozen **CAI interim trust list** (what verify.contentauthenticity.org uses) — shown as a separate
  result, as the list's own header asks.

Files signed with the public C2PA test credential are labelled "TEST credential" instead of trusted:
its private key is published, so it proves a valid signature only.

## What it does not do

- It does **not** say whether an image is real or fake. An **optional experimental AI-image check**
  (section 4 of each report) runs the pinned `OwensLab/commfor-model-384` detector — exported by this
  repo to fp16 ONNX, run by `onnxruntime-web` on-device — and shows its probability score with its
  measured error rates. It is evidence, never a verdict: it misses about 1 in 3 images from the newest
  generator tested, catches only ~2 in 5 after a JPEG re-save, and wrongly flags ~1 in 28 real photos
  (`RESULTS_DETECTOR.md`). The ~60 MB of model + runtime download only happens if the check is run.
- It does not fetch certificate revocation (OCSP off) or remote/cloud manifests, so a file whose only
  credential lives outside the file shows "No credential".
- Many platforms strip credentials on upload: "No credential" is the common honest answer.

## Run it

It is a static site — any static file server or static host works. Locally:

```sh
cd web && python3 -m http.server 8077     # then open http://localhost:8077/
```

On a phone: open the deployed URL, choose an image from the photo library or files. "Add to Home
Screen" installs it as an app icon; `sw.js` precaches everything so it then works fully offline.

Requirements: a browser with WebAssembly, module workers and ES module import support (any current
Safari/Chrome/Firefox). The first check loads ~12 MB of vendored verifier code once per visit.

## Files

- `index.html`, `styles.css`, `app.js` — the page and the check/rendering logic. The label rules and
  the "can and cannot conclude" readings are ported unchanged in spirit from `viewer/src/template.html`.
- `vendor/` — pinned, integrity-recorded copies of the verifier and its dependencies, plus the
  `onnxruntime-web` WASM runtime for the experimental detector. See `PINS.md` for package versions,
  npm integrity hashes, the four specifier patches applied, and how to re-vendor.
- `detector-model.fp16.onnx` — fp16 ONNX export of `OwensLab/commfor-model-384`, produced by
  `detector_eval/export_onnx.py` and verified logit-faithful to the PyTorch original (zero sign flips
  on 120 eval images). Fetched on demand and cached by the service worker — never precached.
- `trust/` + `trust-anchors.js` — the pinned trust lists (PEMs on disk + generated module). Regenerate
  the module after updating PEMs: `python3 web/build_trust_module.py`.
- `sw.js`, `manifest.webmanifest`, `icon-*.png` — PWA installability/offline caching.
- `_pkgs/` — acquisition intermediates (npm tarballs); gitignored, never shipped.

`PINS.md` also records the one honest verifier difference: this build (c2pa-wasm / c2pa-rs 0.9x) is
stricter on some legacy manifests than the repo's pinned c2patool 0.27.23 — the official Truepic 2023
sample reports `assertion.dataHash.mismatch` here where the older tool reported `Valid`.
