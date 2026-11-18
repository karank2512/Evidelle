# Evaluating actual signals: routes and decisions needed

Status, 18 November 2026:
- **Route A (C2PA) was approved narrowly and has been run.** The approval covered the official `c2patool` binary and a few official test files, used offline inside the experiment folder. See [`../RESULTS_ACTUAL_C2PA.md`](../RESULTS_ACTUAL_C2PA.md).
- **Routes B, C and D were not approved.** Actual watermark, SynthID and AI-detector signals therefore remain unevaluated.
- The toy experiment is still preparation only. Its results do not settle questions about actual signals.

The rest of this note is the route assessment as written before route A was approved.

This note identifies the smallest real route to evaluating each kind of signal. It records what each route would need, and what stays unevaluated if it is skipped. The sources are the projects' public repositories, release pages and model metadata, read on 18 November 2026. Versions and sizes are as listed there on that date.

## What is available without any new install, download or upload

Nothing that can evaluate an actual signal.

- **Installed:** Python 3.13 (standard library only), OpenSSL 4.0.3, libjpeg-turbo 3.1.0, libwebp 1.5.0, ffmpeg and macOS `sips`. None of these reads or validates C2PA, detects a production watermark, or classifies AI-generated images.
- **Not installed:**
  - Python packages: C2PA, watermark or detector packages, PyTorch, numpy or OpenCV.
  - Command-line tools: `c2patool`, `exiftool`, ImageMagick.
  - Desktop apps: no Content Credentials-capable editor (for example Photoshop or Lightroom).
- **Package managers are present** (`pip`, `uv`, `cargo`, `npm`, Homebrew, Docker). Using any of them to add a tool is an install, so it needs a decision.

## Smallest real route for each signal

### A. C2PA / Content Credentials (actual validation)

- **Smallest route:** the official `c2patool` command-line tool, as a prebuilt universal macOS binary.
  - Release `c2patool-v0.27.23`, published 2026-11-10: `c2patool-v0.27.23-universal-apple-darwin.zip`, 19.8 MB. Source: https://github.com/contentauth/c2pa-rs/releases/tag/c2patool-v0.27.23
  - Alternatives:
    - Homebrew formula `c2patool`, listed at 0.29.0 (https://formulae.brew.sh/formula/c2patool). The GitHub tag and the Homebrew version differ; confirm before use.
    - Python bindings, `pip install c2pa-python`, v0.39.0, published 2026-11-12, in an isolated virtual environment (https://github.com/contentauth/c2pa-python).
- **Test material:** a few official sample files from https://github.com/c2pa-org/public-testfiles. The repository is about 170 MB and licensed CC-BY-SA-4.0; only a handful of files would be needed. Our own synthetic images could also be signed with the tool's test credentials.
- **Cost and setup:** $0. About 20 MB plus the selected samples. No account and no upload; it runs offline once downloaded.
- **What it would enable:**
  - real manifest reading and validation states on official valid and invalid samples;
  - signing our synthetic images and measuring what our re-encodes, crops and metadata stripping do to *real* manifests;
  - checking whether validation reports untrusted signers differently from trusted ones.
- **If skipped:** actual C2PA validation stays unevaluated. Only the toy manifest illustrates the logic.

### B. An actual open watermark

- **Smallest route:** `invisible-watermark` (MIT), https://github.com/ShieldMnt/invisible-watermark, installed with `pip install invisible-watermark` into an isolated virtual environment.
  - Its default `dwtDct` method is classical, CPU-only, and needs no model download.
  - It pulls in numpy, OpenCV and PyWavelets (tens of MB).
  - The library describes itself as experimental.
- **Heavier alternative:** Adobe TrustMark, https://github.com/adobe/trustmark, via `pip install trustmark`.
  - It needs PyTorch, and the model weights are fetched from S3 on first use. ONNX runners exist for JavaScript, Rust and C++.
  - Several hundred MB in total.
  - TrustMark is the watermark associated with "durable" Content Credentials, so it is more relevant to C2PA.
- **Video alternative:** Meta Video Seal, https://github.com/facebookresearch/videoseal (MIT). PyTorch, and checkpoints download automatically.
- **Cost:** $0. No account and no upload.
- **What it would enable:** how an actual watermark survives the same JPEG, WebP, resize and crop steps used in the toy experiment, and whether copy or removal attacks transfer.
- **If skipped:** actual watermark robustness stays unevaluated. Only the toy watermark illustrates the mechanisms.

### C. SynthID (Google)

- **No offline route exists.** Only SynthID *Text* is open source (https://github.com/google-deepmind/synthid-text). Image and video SynthID detection is available only through Google's services, such as verification in the Gemini app (https://support.google.com/gemini/answer/16722517).
- **What that route needs:**
  - A Google sign-in.
  - Uploading test media into Gemini chats. Under Gemini's published terms, a subset of chats is reviewed by humans, and reviewed chats are kept for up to 3 years (https://support.google.com/gemini/answer/13594961).
  - Daily check limits, reported as about 10 per media type.
  - SynthID-marked test content would also have to come from Google's own generators.
- **Decision needed:** whether to allow uploading synthetic, non-intimate test images to Google under those terms.
- **If skipped:** SynthID behaviour stays entirely unevaluated.

### D. AI-image detectors

- **Smallest offline route:** one open-source detector with published weights, for example:
  - Community Forensics (MIT), https://github.com/JeongsooP/Community-Forensics. The 224-input checkpoint is `model.safetensors`, 82.7 MB, at https://huggingface.co/OwensLab/commfor-model-224.
  - UniversalFakeDetect (MIT), https://github.com/WisconsinAIVision/UniversalFakeDetect. It uses CLIP features.
  - Both need PyTorch and torchvision (several hundred MB) plus the weights.
- **A lawful test set is also required, and it is a separate decision.** The procedural images here are not outputs of generative models, and there are no permitted real photographs. A meaningful test would need:
  - real photographs supplied with explicit permission, or taken from an openly licensed dataset;
  - non-intimate AI-generated images, either from a licensed dataset or generated locally (another model download).
- **Hosted alternatives** (Sightengine, Hive, AI or Not) need an account and uploads. Their published data handling varies (see the report's section 8.3), and pricing was not verified in this pass.
- **Cost:** $0 for the open-source route, but a few hundred MB to about 1 GB of downloads, plus test-set curation.
- **If skipped:** detector false-positive and false-negative behaviour stays entirely unevaluated. No detector scores will be produced or estimated.

## Suggested order of decisions

1. **A (C2PA tool and samples).** The largest gain in real-signal coverage for the smallest change: no account, no upload, about 20 MB.
2. **B (`invisible-watermark` in a disposable virtual environment).** A small, offline route to one actual watermark.
3. **C and D only by separate, explicit approval.** They involve uploads, accounts or heavy downloads, plus a licensed test set.

None of these steps has been started. The toy experiment remains labelled as preparation.
