"""Evaluate the production `invisible-watermark` package on this repository's own
synthetic images, under the same transforms used in the toy run.

Schemes under test (from the pinned `invisible-watermark==0.2.0` wheel):
- `dwtDctSvd`: classical DWT+DCT+SVD mark, 64-bit payload ("bytes" mode).
- `rivaGan`: neural encoder/decoder shipped as ONNX inside the wheel, 32-bit payload.

Detection criterion is honest and simple: the decoder always returns bits/bytes;
"detected" means they exactly equal what was embedded. Bit agreement is reported too.
"No verdict" — this measures whether a known mark survives processing. It does not
say whether any unmarked image is real or fake.

    ../.venv/bin/python run_watermark_eval.py            (from this folder)
"""

import base64
import hashlib
import json
import os
import sys

import cv2
import numpy as np
from imwatermark import WatermarkDecoder, WatermarkEncoder

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from authexp.imageio import Image, write_png          # noqa: E402
from authexp.synth import landscape, shapes           # noqa: E402
from authexp import transforms as T                   # noqa: E402

N_IMAGES = 12
PAYLOAD = b"evidelle"                                # 64 bits for dwtDctSvd
RIVA_BITS = [int(b) for b in np.unpackbits(np.frombuffer(
    hashlib.sha256(b"evidelle:rivagan").digest()[:4], dtype=np.uint8))]              # 32 bits

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..", "results", "watermark")


def to_bgr(img: Image) -> np.ndarray:
    rgb = np.frombuffer(img.rgb, dtype=np.uint8).reshape(img.height, img.width, 3)
    return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)


def to_img(arr: np.ndarray) -> Image:
    rgb = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)
    return Image(rgb.shape[1], rgb.shape[0], rgb.tobytes())


def make_encoders():
    e_dwt = WatermarkEncoder()
    e_dwt.set_watermark("bytes", PAYLOAD)
    WatermarkEncoder.loadModel()                     # loads the bundled ONNX rivaGan models
    e_riva = WatermarkEncoder()
    e_riva.set_watermark("bits", RIVA_BITS)
    return e_dwt, e_riva


DEC_DWT = WatermarkDecoder("bytes", len(PAYLOAD) * 8)
DEC_RIVA = WatermarkDecoder("bits", 32)


def decode_dwt(arr):
    try:
        got = DEC_DWT.decode(arr, "dwtDctSvd")
        return got == PAYLOAD, None
    except Exception as e:
        return False, "%s: %s" % (type(e).__name__, e)


def decode_riva(arr):
    try:
        bits = DEC_RIVA.decode(arr, "rivaGan")
        agree = float(np.mean(np.array(bits) == np.array(RIVA_BITS)))
        return bool(np.all(np.array(bits) == np.array(RIVA_BITS))), agree
    except Exception as e:
        return False, "refused: %s" % e


def transforms_for(img: Image):
    cases = {
        "none": img,
        "jpeg_q90": T.jpeg(img, 90), "jpeg_q75": T.jpeg(img, 75),
        "jpeg_q50": T.jpeg(img, 50), "jpeg_q30": T.jpeg(img, 30),
        "jpeg_q15": T.jpeg(img, 15),
        "webp_q80": T.webp(img, 80), "webp_q50": T.webp(img, 50),
        "webp_q20": T.webp(img, 20),
        "half_then_double": T.half_then_double(img),
        "crop_1px": T.crop(img, 1, 1), "crop_8px": T.crop(img, 8, 8),
    }
    # sips JPEG round-trip (needs a real PNG on disk)
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "m.png")
        write_png(p, img)
        cases["sips_jpeg_rt_q80"] = T.sips_jpeg_roundtrip(p)[0]
    return cases


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    e_dwt, e_riva = make_encoders()
    results = {"payload_dwtDctSvd": base64.b16encode(PAYLOAD).decode(),
               "riva_bits": RIVA_BITS, "images": N_IMAGES, "families": {}}

    for fam_name, gen in (("landscape", landscape), ("shapes", shapes)):
        fam = {"dwtDctSvd": {}, "rivaGan": {}, "diff": {"dwtDctSvd": [], "rivaGan": []},
               "fp": {"dwtDctSvd": [], "rivaGan": []}, "copy_attack": {"dwtDctSvd": [], "rivaGan": []}}
        for i in range(N_IMAGES):
            img = gen(i)
            arr = to_bgr(img)
            marked = {"dwtDctSvd": e_dwt.encode(arr, "dwtDctSvd"),
                      "rivaGan": e_riva.encode(arr, "rivaGan")}
            for scheme, marr in marked.items():
                diff = np.abs(marr.astype(int) - arr.astype(int))
                fam["diff"][scheme].append({"mean_abs": float(diff.mean()), "max": int(diff.max())})

                for tname, timg in transforms_for(to_img(marr)).items():
                    tarr = to_bgr(timg)
                    if scheme == "dwtDctSvd":
                        det, err = decode_dwt(tarr)
                    else:
                        det, err = decode_riva(tarr)
                    fam[scheme].setdefault(tname, {"detected": 0, "refused": 0, "agree": []})
                    fam[scheme][tname]["detected"] += int(det)
                    if isinstance(err, str) and err.startswith("refused"):
                        fam[scheme][tname]["refused"] += 1
                    if isinstance(err, float):
                        fam[scheme][tname]["agree"].append(round(err, 3))

                # copy attack: add the mark's pixel residual to an image from the OTHER family
                other = to_bgr((shapes if fam_name == "landscape" else landscape)(i))
                spoofed = np.clip(other.astype(int) + (marr.astype(int) - arr.astype(int)),
                                  0, 255).astype(np.uint8)
                if scheme == "dwtDctSvd":
                    det, _ = decode_dwt(spoofed)
                else:
                    det, _ = decode_riva(spoofed)
                fam["copy_attack"][scheme].append({"detected": det})

            # false positives: decode the UNMARKED image
            d_det, _ = decode_dwt(arr)
            fam["fp"]["dwtDctSvd"].append({"detected": d_det})
            r_det, r_agree = decode_riva(arr)
            fam["fp"]["rivaGan"].append({"detected": r_det, "agree": round(r_agree or 0, 3)})
        results["families"][fam_name] = fam

    path = os.path.join(OUT_DIR, "watermark_results.json")
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    print("wrote", path)

    for fam_name, fam in results["families"].items():
        print("\n==", fam_name)
        for scheme in ("dwtDctSvd", "rivaGan"):
            diffs = fam["diff"][scheme]
            print(" %s  mark diff: mean %.2f max %d"
                  % (scheme, np.mean([d["mean_abs"] for d in diffs]),
                     max(d["max"] for d in diffs)))
            for tname, r in fam[scheme].items():
                ag = (" agree %.2f" % np.mean(r["agree"])) if r["agree"] else ""
                rf = (" refused %d" % r["refused"]) if r["refused"] else ""
                print("   %-16s %d/%d%s%s" % (tname, r["detected"], N_IMAGES, rf, ag))
            fp = fam["fp"][scheme]
            print("   unmarked detect %d/%d" % (sum(f["detected"] for f in fp), N_IMAGES))
            ca = fam["copy_attack"][scheme]
            print("   copy-attack detect %d/%d" % (sum(c["detected"] for c in ca), N_IMAGES))


if __name__ == "__main__":
    main()
