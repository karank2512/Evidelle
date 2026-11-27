# Results: production AI-image detector evaluation

One research-grade detector — **Community Forensics** (Park & Owens, CVPR 2025; ViT-Small
trained on 2.7M images from ~4,800 generators) — evaluated offline on two pinned public
test sets. No real-or-fake verdicts: these are measurements of one model on specific data.

## Inputs (pinned)

- **Model**: `OwensLab/commfor-model-384` (MIT licence) — official authors' checkpoint.
  `samples/detector/commfor384.safetensors`, SHA-256
  `b89f36275f3bf5e2b040eee36597a8f19db051bff9a473a9cf7b2466284fb387`
  (independently matches the published hash in `ADPer/verity-weights`).
  Single logit, `sigmoid` → P(fake), labels `real:0, fake:1` per the authors' repo.
- **Preprocessing** (from the authors' `commfor-data-preprocessor`, not inferred): resize
  shorter edge to 440 preserving aspect, centre-crop 384, ImageNet mean/std.
- **Also evaluated**: `onnx-community/CommunityForensics-DeepfakeDet-ViT-ONNX`
  `model_int8.onnx` SHA-256 `a504b8ea9372e8c9be9e8e3aa0a7f0f2eff5ba3df067c3d5ed2fcdfe15eaba2c`
  — the only browser-ready export of this model. **It is defective** (see below).
- **Data** (gitignored `samples/`; fetched 2026-11-27):
  - `samples/cifake/test.parquet` — CIFAKE test split via `dragonintelligence/CIFAKE-image-dataset`
    (HF parquet mirror; CIFAKE is MIT-licensed: REAL = CIFAR-10 photos, FAKE = Stable Diffusion 1.4).
    SHA-256 `7767d5285d009471175ac7985c60367d82a34088f29c67185da7af2c53b7975d`. 20,000 rows, 32×32.
  - `samples/synthbuster-plus-test{0,3,5,6}.parquet` — four test shards of
    `marco-willi/synthbuster-plus` (Synthbuster lineage CC-BY-NC-SA-4.0; real = RAISE-1k).
    SHA-256 `75284688…`, `1fc8d049…`, `d51dfaa3…`, `76c161f9…`. 1,245 rows, full resolution PNG.
    Evaluation use only, per licence.
- Harness: `detector_eval/run_detector_eval.py` in the pinned `.venv`
  (`torch==2.15.0`, `timm`, `onnxruntime==1.32.0`, `pyarrow`, `pillow==13.0.0`).
- Output: `results/detector/detector_results_{synthbuster,cifake}.json`.

## Results

### Full-resolution set (1,045 fake across 8 generators + 200 real RAISE photos)

Official PyTorch checkpoint, threshold at logit 0:

| Source | n | Detected (fake) / Called real | Median logit |
|---|---|---|---|
| stable-diffusion-1-4 | 45 | **100%** | +13.9 |
| stable-diffusion-1-3 | 200 | **99.0%** | +14.0 |
| stable-diffusion-xl | 200 | **97.5%** | +11.2 |
| midjourney-v5 | 66 | 89.4% | +7.3 |
| dalle2 | 200 | 81.0% | +4.4 |
| stable-diffusion-2 | 44 | 79.5% | +5.3 |
| dalle3 | 112 | 73.2% | +3.0 |
| **FLUX.1-schnell** | 178 | **65.7%** | +2.1 |
| raise1k (real photos) | 200 | 96.5% correctly called real | — |

Overall balanced accuracy 0.910 (sens 0.855 / spec 0.965). So 6.5% of real photographs
were called fake.

### Same detector, 32×32 images (CIFAKE test, n=2000+2000)

Accuracy **0.596** (sens 0.41 / spec 0.78). The same SD-1.x family detected ~100% at
full resolution drops to 41% at 32×32, and 22% of tiny real photos are called fake.
Detector accuracy is a property of *resolution*, not just of the generator.

### JPEG laundering (200 fake + 200 real, full-res, torch model)

| JPEG quality | Accuracy | Fake detected | Real still correct |
|---|---|---|---|
| none | 0.91 | 0.86 | 0.97 |
| q90 | 0.83 | 0.67 | 0.995 |
| q75 | 0.76 | 0.54 | 0.99 |
| q50 | 0.69 | 0.38 | 1.00 |

A single ordinary JPEG re-save removes roughly half the detections while false alarms
on real photos *fall to ~0* — the detector's fake-evidence is largely in the frequencies
JPEG destroys. Note the laundering subset is the first 200 fakes in shard order
(dalle2/dalle3 heavy); per-generator sensitivity varies.

### The only browser-ready export is broken

`onnx-community/CommunityForensics-DeepfakeDet-ViT-ONNX` scored **0.51** on the same
full-res set where the real model scored 0.91. Its outputs are nearly constant
(±0.15 logit across maximally different inputs): the auto-converted graph is degenerate,
not merely degraded. Anyone embedding this HF model in a browser would ship a coin flip
unless they re-export the ONNX themselves.

## What these numbers support — and what they do not

- A positive reading on a *recent* generator is meaningful but not decisive: spec 0.965
  means ~1 in 15 real photos is called fake at this threshold. At low real-world
  prevalence of AI images, false alarms can dominate — a point the tool's wording must
  preserve (the repo already refuses real-or-fake verdicts).
- Detection falls steeply with generator recency (FLUX 66% < DALL-E 3 73% < SD-1.x 99%+)
  and with ordinary compression (q50 → 38%). A "not detected" result on a social-media
  image is close to uninformative; a "detected" result is evidence but not proof.
- The tiny-image regime is different in kind: sub-~64px content is near-undetectable to
  this model, and real photos are *more* likely to be flagged there.
- For the web app: the browser path would require a custom ONNX export of this MIT-licensed
  checkpoint (~87MB fp32; int8/q4 could shrink it) — feasible but unproven, and model
  download size is a real mobile cost. The onnx-community export is not an option.

## Limits

- n≈1,245 full-res + 4,000 tiny; specific generator versions on specific domains (RAISE-1k
  photos and CIFAR-10; not phone photos, screenshots, memes, or edited composites).
- One detector version, one threshold (logit 0). Score percentiles are recorded in the
  JSON for other threshold choices.
- synthbuster-plus images carry no degradations by design; the laundering numbers are our
  own simple re-saves, not platform pipelines.
- This detector is one signal among many; nothing here estimates the prevalence of
  AI-generated images anywhere.
