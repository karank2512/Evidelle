"""Export the Community Forensics checkpoint to ONNX for the web app, and verify parity.

    ../.venv/bin/python export_onnx.py

Produces /tmp/commfor384_*.onnx candidates and reports logit parity against the
PyTorch original on a mixed eval sample. The shipped artifact (fp16) is chosen by the
parity numbers below, not by size alone — quantization candidates that flip signs at
the decision threshold are rejected regardless of how small they are.
"""

import os
import sys

import numpy as np
import onnx
import onnxruntime as ort
import pyarrow.parquet as pq
import torch

sys.path.insert(0, os.path.dirname(__file__))
from run_detector_eval import load_torch_model, preprocess, scores_torch  # noqa: E402

OUT = "/tmp"


def export_fp32(m):
    x = torch.from_numpy(np.zeros((1, 3, 384, 384), dtype=np.float32))
    torch.onnx.export(m, x, f"{OUT}/commfor384_fp32.onnx",
                      input_names=["pixel_values"], output_names=["logits"],
                      dynamic_axes={"pixel_values": {0: "batch"}, "logits": {0: "batch"}},
                      opset_version=17)
    m_onnx = onnx.load(f"{OUT}/commfor384_fp32.onnx")
    onnx.save_model(m_onnx, f"{OUT}/commfor384_fp32_packed.onnx",
                    save_as_external_data=False, convert_attribute=True)


def to_fp16():
    from onnxconverter_common import float16
    m = onnx.load(f"{OUT}/commfor384_fp32_packed.onnx")
    onnx.save_model(float16.convert_float_to_float16(m, keep_io_types=True),
                    f"{OUT}/commfor384_fp16.onnx")


def to_int8_dynamic():
    from onnxruntime.quantization import QuantType, quantize_dynamic
    quantize_dynamic(f"{OUT}/commfor384_fp32_packed.onnx",
                     f"{OUT}/commfor384_int8.onnx", weight_type=QuantType.QInt8)


def parity(ref_logits, path, xs):
    l = ort.InferenceSession(path, providers=["CPUExecutionProvider"]).run(
        None, {"pixel_values": xs})[0].reshape(-1)
    d = np.abs(l - ref_logits)
    flips = int(np.sum(np.sign(l) != np.sign(ref_logits)))
    mb = os.path.getsize(path) / 1e6
    print("%-36s %6.1fMB  max|d|=%.4f  flips=%d/%d" % (path, mb, d.max(), flips, len(l)))


def main():
    m = load_torch_model()
    export_fp32(m)
    to_fp16()
    to_int8_dynamic()
    t = pq.read_table(os.path.join(HERE, "../samples/synthbuster-plus-test6.parquet"),
                      columns=["image", "label"]).to_pylist()
    blobs = [r["image"]["bytes"] for r in t[:120]]
    xs = np.stack([preprocess(b) for b in blobs])
    lt = scores_torch(m, list(xs))
    parity(lt, f"{OUT}/commfor384_fp32_packed.onnx", xs)
    parity(lt, f"{OUT}/commfor384_fp16.onnx", xs)
    parity(lt, f"{OUT}/commfor384_int8.onnx", xs)
    print("\nShip the smallest file with zero sign flips.")


HERE = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    main()
