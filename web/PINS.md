# Pinned inputs for the web app

Everything the page uses is vendored under `web/` — fetched from this same site only (the page declares
`connect-src 'self'`), so no request can reach a third party and the checked image never leaves the
device. This file records what each artifact is, where it came from, and how to verify or refresh it.
Regenerate `trust-anchors.js` with `python3 web/build_trust_module.py` after updating PEMs.

## Verifier: @contentauth/c2pa-web 0.17.1

- npm package `@contentauth/c2pa-web@0.17.1`, published 2026-11-16, licence MIT.
- Tarball integrity (npm registry): `sha512-3JBoLhmffbUX1aQk9iolKsff+J6xOWgHvNshLvWQAbeJKDtL6OjRlOD9O9rJajYYUrguSOfJCiRSfchZ5IdS3Q==`
- Embeds `@contentauth/c2pa-wasm@0.15.1` (the official c2pa-rs WebAssembly build).
- Version note: 0.17.2 was published 2026-11-23, too recent to pin on that date; 0.17.1 was the newest
  release at least 7 days old.
- Runtime deps bundled in `vendor/`: `@contentauth/c2pa-utilities@0.5.2`, `highgain@0.1.0`,
  `ts-deepmerge@8.0.0` (peer of utilities).

Re-vendor:

```sh
npm pack @contentauth/c2pa-web@0.17.1 @contentauth/c2pa-utilities@0.5.2 highgain@0.1.0 ts-deepmerge@8.0.0
# copy dist files into vendor/, then re-apply the specifier patches below
```

### Specifier patches applied to vendored files

The page uses no bundler and no import map, so bare module specifiers were rewritten to relative paths.
Only the `from` strings changed:

| File | Original | Now |
|---|---|---|
| `vendor/c2pa-web/inline.js` | `from "@contentauth/c2pa-utilities"` | `from "../c2pa-utilities/index.js"` |
| `vendor/c2pa-web/builder-CaTgrAW1.js` | `from "@contentauth/c2pa-utilities"` | `from "../c2pa-utilities/index.js"` |
| `vendor/c2pa-web/builder-CaTgrAW1.js` | `from "highgain"` | `from "../highgain/index.js"` |
| `vendor/c2pa-utilities/settings.js` | `from 'ts-deepmerge'` | `from '../ts-deepmerge/index.js'` |

## Trust lists (fetched once, pinned by SHA-256, fetched 2026-11-27)

| File | Source | SHA-256 | Contents |
|---|---|---|---|
| `trust/C2PA-TRUST-LIST.pem` | `github.com/c2pa-org/conformance-public` | `62673a9e68e30f953eda65b4171e980ee111e1f12385989b1230fdfe787bfae8` | 34 signing CAs — official conformance list (Adobe Inspect) |
| `trust/C2PA-TSA-TRUST-LIST.pem` | same repo | `eca8347ee71e31d226e00c85b15aca356116fefe6c26ed8c0ee1f954115b1990` | 24 timestamp authorities |
| `trust/C2PA-INTERIM-TRUST-LIST.pem` | `contentcredentials.org/trust/anchors.pem` | `db57e50b9bd4e4c786cbb91f38fd85e2af6a9d5412438a8cddcc42688df07ae5` | 27 CAs — frozen interim list (what verify.contentauthenticity.org uses) |
| `trust/c2pa-interim-eku-store.cfg` | fetched by pinned `c2patool init trust --legacy` | `1044c30a906b0c9cbe28b4a4c0002ca56a718f0ae22b9af83238543a07d0e718` | EKU store for the interim list |

Cross-checks recorded 2026-11-27: `c2patool init trust` (pinned binary 0.27.23) fetched the same official
list byte-for-byte (same SHA-256); `c2patool init trust --legacy` fetched the same interim list
byte-for-byte as `contentcredentials.org/trust/anchors.pem`.

The interim list's own header says it is frozen and that validators "should distinguish" credentials
signed under it from those under the official list — which is why the app runs and shows both passes.
Verify's extra end-entity "allowed list" is not applied; a few more signers may show trusted there.

## Verifier differences to keep honest

- The verifier is c2pa-wasm (c2pa-rs 0.9x-era), **not** the c2patool 0.27.23 binary the repo's recorded
  run used. It is stricter on some legacy (1.x) manifests: the official Truepic 2023 sample reports
  `assertion.dataHash.mismatch` ("exclusion does not match the manifest location") → state `Invalid`,
  where c2patool 0.27.23 reported `Valid`. Both are shown; this is a validator-version difference, not a
  contradiction.
- Timestamp authorities are checked against the pinned TSA list (the repo's c2patool run did not
  configure one).
- `remoteManifestFetch` and `ocspFetch` are off; `connect-src 'self'` allows only same-origin fetches
  (the on-demand detector files), so no third party can be reached.

## Experimental detector: onnxruntime-web 1.31.1 + commfor-model-384 (fp16)

Loaded **on demand only** (section 4 "Experimental: AI-image check") — never precached; `sw.js` caches
the files after first use.

- npm package `onnxruntime-web@1.31.1`, published 2026-10-26, licence MIT.
- Tarball integrity (npm registry): `sha512-5GeH+bWQ+HxM10z7erGlsWqryrwMbSvm/1tkIsKTT48g0fI19VXVVC435t4t7VsPdSQeS7NmuZPXrQ73k82URw==`
- Vendored files (unmodified, from `dist/`): `ort.wasm.min.mjs` (WASM-only ESM entry),
  `ort-wasm-simd-threaded.mjs`, `ort-wasm-simd-threaded.wasm` (SHA-256s:
  `c21d9c32…`, `30ed0b5c…`, `4b884c20…` — full values in `check_web.py` history / `shasum -a 256`).
- Runs with `env.wasm.numThreads = 1` — GitHub Pages sends no cross-origin isolation headers, so
  SharedArrayBuffer threading is unavailable anyway.

Re-vendor:

```sh
npm pack onnxruntime-web@1.31.1
# copy dist/ort.wasm.min.mjs, dist/ort-wasm-simd-threaded.{mjs,wasm} into vendor/onnxruntime-web/
```

### `detector-model.fp16.onnx` (43.7 MB, committed binary)

- Source weights: `OwensLab/commfor-model-384` (Community Forensics ViT-Small, MIT) — the same pinned
  checkpoint the detector arm evaluated (`RESULTS_DETECTOR.md`); source SHA-256 `b89f3627…`.
- Exported by `detector_eval/export_onnx.py` (torch → ONNX fp32 → repacked single file → fp16 with
  `keep_io_types`, opset 17). File SHA-256 `78cc1dc6c49a3a5d68fbc8d160e2799ec21837d12662d5b3f9d978c7bb44c52f`.
- Parity measured on 120 eval images vs the PyTorch original: fp32 max |Δlogit| 0.0002 (0 flips);
  fp16 max |Δ| 0.057 (**0 sign flips** — shipped); int8-dynamic 5 flips and int8-static 39 flips
  (rejected). The published onnx-community int8 export of this model was already shown defective
  (~0.51 accuracy) in `RESULTS_DETECTOR.md`.
- Browser-vs-torch check (Playwright, canvas preprocessing): a midjourney-v5 eval image scored
  logit 2.46–2.92 vs torch 3.07, and a RAISE real photo scored 2.92 vs torch 2.76 — a true
  borderline false positive (the model's documented ~3.5% FPR tail), same reading both ways.
