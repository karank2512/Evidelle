# Results: production invisible-watermark evaluation

One production watermark package — `invisible-watermark` 0.2.0 (PyPI, MIT licence) — evaluated
on this repository's own synthetic images under the same transforms as the toy run, so the
numbers sit next to the toy numbers in `RESULTS.md`. Same discipline: fully offline, recorded
dependency hashes, no real-or-fake verdicts.

**What "detected" means here:** the decoder always returns bits or bytes, whether or not a mark
was embedded. "Detected" means the returned payload **exactly equals** what was embedded. For a
64-bit (dwtDctSvd) or 32-bit (rivaGan) payload, a chance exact match is ~2⁻⁶⁴ / ~2⁻³² — so the
meaningful questions are *robustness* and *domain sensitivity*, not random false positives.

## Inputs (pinned)

- `watermark_eval/run_watermark_eval.py` — the harness. Run: `../.venv/bin/python run_watermark_eval.py`.
- `.venv/` (gitignored): `invisible-watermark==0.2.0` (wheel SHA-256 `644311beed9cfe4a9a5a4a46c740f47800cef184fe2e1297f3f4542e2d992f8b`),
  `onnxruntime==1.32.0` (`27bf5dad46355a8a435c9c4e1556464d99ca834ea44e0f452909712068b8821b`),
  `opencv-python==5.1.0.95`, `numpy==2.5.5`, `PyWavelets==1.10.0`, `pillow==13.0.0`, `torch==2.15.0`.
  Full wheel hashes: the 19-file list was recorded at install time 2026-11-27; regenerate with
  `pip download` + `shasum -a 256`.
- Images: `authexp.synth.landscape(0..11)` and `.shapes(0..11)` — the same 256×256 synthetic
  families as the toy run. Deterministic; no dataset fetched.
- Transforms: `authexp.transforms` — libjpeg-turbo `cjpeg`/`djpeg`, libwebp `cwebp`/`dwebp`,
  macOS `sips`. Identical stand-ins to the toy run; not a model of any platform's pipeline.
- Payloads: `b"evidelle"` (64 bits) for dwtDctSvd; first 32 bits of `sha256("evidelle:rivagan")` for rivaGan.
- Machine-readable output: `results/watermark/watermark_results.json`.

## Results

### dwtDctSvd (classical; mark diff mean ≈1.5 LSB, up to ±203 at a few pixels)

| Transform | landscape (n=12) | shapes (n=12) |
|---|---|---|
| none (intact) | 12/12 | 12/12 |
| JPEG q90 | 5/12 | 3/12 |
| JPEG q75 / q50 / q30 / q15 | 0/12 at every quality | 0/12 at every quality |
| WebP q80 / q50 / q20 | 0/12 at every quality | 0/12 at every quality |
| half → double resize | 12/12 | 12/12 |
| crop 1 px / 8 px | 0/12 | 0/12 |
| `sips` PNG→JPEG(q80)→PNG | 12/12 | 10/12 |
| unmarked images decoded | 0/12 | 0/12 |
| copy attack onto other family | 0/12 | 0/12 |

### rivaGan (neural ONNX mark; mark diff ≤3 LSB, mean ≈2.2)

| Transform | landscape exact (n=12) | landscape bit-agreement | shapes exact (n=12) | shapes bit-agreement |
|---|---|---|---|---|
| none (intact) | 6/12 | 0.97 | 0/12 | 0.70 |
| JPEG q90 | 2/12 | 0.94 | 0/12 | 0.66 |
| JPEG q75 → q15 | 0/12 | 0.89 → 0.62 | 0/12 | 0.62 → 0.58 |
| WebP q80 / q50 / q20 | 1/12 / 0/12 / 0/12 | 0.83 / 0.71 / 0.61 | 0/12 | 0.59 / 0.57 / 0.52 |
| half → double resize | 3/12 | 0.96 | 0/12 | 0.68 |
| crop 1 px / 8 px | decoder refused (12/12) | — | decoder refused (12/12) | — |
| `sips` PNG→JPEG(q80)→PNG | 2/12 | 0.94 | 0/12 | 0.67 |
| unmarked images decoded | 0/12 | ~0.5 | 0/12 | ~0.5 |
| copy attack onto other family | 0/12 | — | 0/12 | — |

## What these numbers support — and what they do not

- **The classical mark is fragile where it matters most.** dwtDctSvd survives a lossless or
  near-lossless path (intact, resize, the `sips` round-trip) but fails at ordinary JPEG q75 and
  every tested WebP quality, and any crop breaks alignment. A platform that re-compresses at
  typical settings erases it. Absence of the mark says nothing.
- **The neural mark is domain-sensitive.** On the "natural-looking" landscape family rivaGan
  reached 0.97 bit-agreement intact; on flat geometric shapes only 0.70 and zero exact matches —
  the same mark, the same payload, a different image distribution. Its published robustness
  numbers do not transfer to off-domain content. Note also that even intact, exact-match recovery
  was only 6/12 on landscapes: the decoder threshold returns *approximately* correct bits, so
  deployments need fuzzy matching, which trades against false positives.
- **Small images and crops are a hard limit.** The production decoder refuses anything below
  256×256 pixels outright — including the 1-px-cropped 255×255 case. Real crops are not
  "lower confidence"; they are unprocessable.
- **The marks did not transfer.** Adding a marked image's pixel residual to an unmarked image
  from the other family yielded zero detections for both schemes — the marks are embedded
  adaptively into image structure, not as a constant additive pattern. (The toy mark *did*
  transfer, which is one way a toy and a production scheme differ.)
- **Zero false positives is the expected, uninteresting result** here: detection requires an
  exact payload match. It does not generalize to deployments that use fuzzy thresholds.
- **`sips` survived where libjpeg did not** (12/12 landscape vs 0/12 at cjpeg q75): the `sips`
  "80" quality scale is not IJG's — encoder choice changes the outcome as much as the named
  quality does.

## Limits

- 256×256 synthetic procedural images, 12 per family, one machine, one package version — not
  real photographs and not model-generated images. rivaGan's domain sensitivity cuts both ways:
  it may do *better* on real photos than on our shapes.
- These specific tools and qualities only; platform pipelines were not tested.
- Only `invisible-watermark`'s two strongest schemes. TrustMark, Stable Signature, Video Seal
  and SynthID were not evaluated; SynthID verification requires uploading to Google and remains
  out of scope for the offline rule.
- A positive detection would establish only that a specific mark was embedded — never that an
  image is real.
