"""Evaluate an AI-image detector on pinned public test sets, offline.

Model: OwensLab/commfor-model-384 (MIT licence) — the official PyTorch checkpoint of
"Community Forensics: Using Thousands of Generators to Train Fake Image Detectors"
(Park & Owens, CVPR 2025): timm vit_small_patch16_384, single logit, sigmoid -> P(fake),
real:0/fake:1. Preprocessing per the authors' CommForImageProcessor: resize shorter edge
to 440 (aspect preserved), centre-crop 384, ImageNet mean/std.

Also run, for comparison, the onnx-community auto-converted ONNX build
(onnx-community/CommunityForensics-DeepfakeDet-ViT-ONNX) — it is the only browser-ready
export of this model and, as shown here, it is defective: outputs are nearly constant.

Datasets (gitignored under samples/; fetch + hashes in RESULTS_DETECTOR.md):
- --dataset cifake: CIFAKE test split via the dragonintelligence HF parquet mirror
  (dataset MIT; REAL = CIFAR-10 32x32 photos, FAKE = Stable Diffusion 1.4). The model was
  not trained on CIFAKE, but CIFAKE is far below its native resolution.
- --dataset synthbuster: marco-willi/synthbuster-plus test shards (real = RAISE-1k photos,
  fake = 13 generators incl. FLUX, SD3, DALL-E 3, Midjourney v5, Firefly, Imagen-3, Glide).
  Dataset lineage CC-BY-NC-SA-4.0 (Synthbuster) / RAISE academic; evaluation use only.

    ../.venv/bin/python run_detector_eval.py --dataset cifake --n 1000
    ../.venv/bin/python run_detector_eval.py --dataset synthbuster
"""

import argparse
import glob
import io
import json
import os
import time

import numpy as np
import onnxruntime as ort
import pyarrow.parquet as pq
import timm
import torch
from PIL import Image
from safetensors.torch import load_file

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
CIFAKE = os.path.join(ROOT, "samples", "cifake", "test.parquet")
SYNTH = sorted(glob.glob(os.path.join(ROOT, "samples", "synthbuster-plus-*.parquet")))
TORCH_WEIGHTS = os.path.join(ROOT, "samples", "detector", "commfor384.safetensors")
ONNX_MODEL = os.path.join(ROOT, "samples", "detector", "model_int8.onnx")

# authors' test-time preprocessing (dataloader.py get_transform mode="test")
RESIZE, CROP = 440, 384
IMAGENET_MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
IMAGENET_STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)
# what the broken ONNX repo's preprocessor_config advertised (kept for the comparison)
CLIP_MEAN = np.array([0.48145466, 0.4578275, 0.40821073], dtype=np.float32)
CLIP_STD = np.array([0.26862954, 0.26130258, 0.27577711], dtype=np.float32)


def preprocess(blob: bytes) -> np.ndarray:
    im = Image.open(io.BytesIO(blob)).convert("RGB")
    w, h = im.size
    s = RESIZE / min(w, h)                       # torchvision Resize(int): shorter edge -> 440
    im = im.resize((round(w * s), round(h * s)), Image.BICUBIC)
    x0 = (im.width - CROP) // 2
    y0 = (im.height - CROP) // 2
    a = np.asarray(im.crop((x0, y0, x0 + CROP, y0 + CROP)), dtype=np.float32) / 255.0
    return ((a - IMAGENET_MEAN) / IMAGENET_STD).transpose(2, 0, 1)


def preprocess_onnx_style(blob: bytes) -> np.ndarray:
    """The (wrong) preprocessing the ONNX export's config implied: square resize + CLIP std."""
    im = Image.open(io.BytesIO(blob)).convert("RGB").resize((440, 440), Image.BICUBIC)
    a = np.asarray(im, dtype=np.float32)[56:56 + 384, 56:56 + 384] / 255.0
    return ((a - CLIP_MEAN) / CLIP_STD).transpose(2, 0, 1)


def load_torch_model():
    m = timm.create_model("vit_small_patch16_384", num_classes=1, pretrained=False)
    sd = {k[len("vit."):]: v for k, v in load_file(TORCH_WEIGHTS).items()}
    missing, unexpected = m.load_state_dict(sd, strict=False)
    assert not missing and not unexpected, (missing[:3], unexpected[:3])
    return m.eval()


def scores_torch(sess, batch):
    x = torch.from_numpy(np.stack(batch))
    with torch.no_grad():
        return sess(x).reshape(-1).numpy()           # logit; sigmoid -> P(fake)


def scores_onnx(sess, batch):
    out = sess.run(None, {"pixel_values": np.stack(batch)})[0]   # (B,2) — broken export
    return out[:, 1] - out[:, 0]                    # log-odds "class1" as a scalar score


def jpeg_roundtrip(blob: bytes, q: int) -> bytes:
    im = Image.open(io.BytesIO(blob)).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=q)
    return buf.getvalue()


def load_cifake(n):
    rows = pq.read_table(CIFAKE).to_pylist()
    fakes = [r["image"]["bytes"] for r in rows if r["label"] == 0][:n]
    reals = [r["image"]["bytes"] for r in rows if r["label"] == 1][:n]
    return [(b, True, "sd-1.4-cifake") for b in fakes] + [(b, False, "cifar10") for b in reals]


def load_synthbuster():
    items = []
    for p in SYNTH:
        t = pq.read_table(p, columns=["image", "label", "source"]).to_pylist()
        for r in t:
            items.append((r["image"]["bytes"], r["label"] == 1, r["source"]))
    return items


def evaluate(run, items, batch, prep):
    out = np.zeros(len(items), dtype=np.float32)
    buf, idx = [], []
    t0 = time.time()
    for i, (blob, _, _) in enumerate(items):
        buf.append(prep(blob))
        idx.append(i)
        if len(buf) == batch:
            out[idx] = run(buf)
            buf, idx = [], []
    if buf:
        out[idx] = run(buf)
    return out, time.time() - t0


def summarize(name, s_fake, s_real):
    sens = float(np.mean(s_fake > 0)) if len(s_fake) else float("nan")
    spec = float(np.mean(s_real <= 0)) if len(s_real) else float("nan")
    res = {"n_fake": int(len(s_fake)), "n_real": int(len(s_real)),
           "accuracy_at_0": (sens + spec) / 2,
           "sens_fake": sens, "spec_real": spec,
           "fake_score_pct": {str(p): float(np.percentile(s_fake, p)) for p in (5, 25, 50, 75, 95)} if len(s_fake) else {},
           "real_score_pct": {str(p): float(np.percentile(s_real, p)) for p in (5, 25, 50, 75, 95)} if len(s_real) else {}}
    print("%-12s acc %.4f  sens %.4f spec %.4f (fake %d real %d)"
          % (name, res["accuracy_at_0"], sens, spec, len(s_fake), len(s_real)))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", choices=["cifake", "synthbuster"], required=True)
    ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--batch", type=int, default=16)
    args = ap.parse_args()

    items = load_cifake(args.n) if args.dataset == "cifake" else load_synthbuster()
    is_fake = np.array([f for _, f, _ in items])
    print("%s: %d images (%d fake / %d real)" % (args.dataset, len(items),
          int(is_fake.sum()), int((~is_fake).sum())))

    results = {"dataset": args.dataset, "models": {}}

    model = load_torch_model()
    run_t = lambda buf: scores_torch(model, buf)
    sc, secs = evaluate(run_t, items, args.batch, preprocess)
    r = summarize("torch-fp32", sc[is_fake], sc[~is_fake]); r["seconds"] = round(secs, 1)
    results["models"]["torch-fp32"] = r

    sess = ort.InferenceSession(ONNX_MODEL, providers=["CPUExecutionProvider"])
    run_o = lambda buf: scores_onnx(sess, buf)
    sco, secs = evaluate(run_o, items, args.batch, preprocess_onnx_style)
    r = summarize("onnx-int8", sco[is_fake], sco[~is_fake]); r["seconds"] = round(secs, 1)
    results["models"]["onnx-int8(broken-export)"] = r

    # per-generator breakdown (torch model)
    sources = sorted({s for _, _, s in items})
    gen = {}
    for s in sources:
        fidx = np.array([it[2] == s and it[1] for it in items])
        ridx = np.array([it[2] == s and not it[1] for it in items])
        if fidx.any():
            gen[s] = {"n": int(fidx.sum()), "detected": float(np.mean(sc[fidx] > 0)),
                      "median_logit": float(np.median(sc[fidx]))}
        elif ridx.any():
            gen[s] = {"n": int(ridx.sum()), "real_rate": float(np.mean(sc[ridx] <= 0))}
    results["per_source_torch"] = gen
    for s, g in gen.items():
        print("  %-22s %s" % (s, g))

    # JPEG-laundering robustness (torch model, 200 fake + 200 real)
    sub = [it for it in items if it[1]][:200] + [it for it in items if not it[1]][:200]
    sub_fake = np.array([f for _, f, _ in sub])
    for q in (90, 75, 50):
        laundered = [(jpeg_roundtrip(b, q), f, s) for b, f, s in sub]
        scq, _ = evaluate(run_t, laundered, args.batch, preprocess)
        results.setdefault("jpeg_laundering", {})[str(q)] = summarize(
            "jpeg_q%d" % q, scq[sub_fake], scq[~sub_fake])

    out_path = os.path.join(ROOT, "results", "detector",
                            "detector_results_%s.json" % args.dataset)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as fh:
        json.dump(results, fh, indent=2)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
