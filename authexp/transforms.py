"""Image processing steps that stand in for ordinary sharing. They use locally installed
command-line tools (libjpeg-turbo, libwebp, macOS sips) or pure Python. They are NOT a model of any
specific platform's pipeline."""

import os
import shutil
import subprocess
import tempfile

from .imageio import Image, read_png, read_ppm, write_png, write_ppm


def tool_available(name: str) -> bool:
    return shutil.which(name) is not None


def tool_versions() -> dict:
    out = {}
    if tool_available("cjpeg"):
        out["cjpeg"] = subprocess.run(["cjpeg", "-version"], capture_output=True).stderr.decode().strip().splitlines()[0]
    if tool_available("cwebp"):
        out["cwebp"] = subprocess.run(["cwebp", "-version"], capture_output=True).stdout.decode().strip()
    out["sips"] = "available" if tool_available("sips") else "not available"
    return out


def jpeg(img: Image, quality: int) -> Image:
    with tempfile.TemporaryDirectory() as d:
        src, mid, dst = (os.path.join(d, n) for n in ("in.ppm", "mid.jpg", "out.ppm"))
        write_ppm(src, img)
        subprocess.run(["cjpeg", "-quality", str(quality), "-outfile", mid, src], check=True, capture_output=True)
        subprocess.run(["djpeg", "-ppm", "-outfile", dst, mid], check=True, capture_output=True)
        return read_ppm(dst)


def webp(img: Image, quality: int) -> Image:
    with tempfile.TemporaryDirectory() as d:
        src, mid, dst = (os.path.join(d, n) for n in ("in.png", "mid.webp", "out.ppm"))
        write_png(src, img)
        subprocess.run(["cwebp", "-quiet", "-q", str(quality), src, "-o", mid], check=True, capture_output=True)
        subprocess.run(["dwebp", "-quiet", "-ppm", mid, "-o", dst], check=True, capture_output=True)
        return read_ppm(dst)


def half_then_double(img: Image) -> Image:
    """2x2 box downscale, then nearest-neighbour upscale back to the original size."""
    w, h = img.width, img.height
    hw, hh = w // 2, h // 2
    small = bytearray(hw * hh * 3)
    for y in range(hh):
        for x in range(hw):
            for c in range(3):
                s = (img.rgb[((2 * y) * w + 2 * x) * 3 + c] + img.rgb[((2 * y) * w + 2 * x + 1) * 3 + c]
                     + img.rgb[((2 * y + 1) * w + 2 * x) * 3 + c] + img.rgb[((2 * y + 1) * w + 2 * x + 1) * 3 + c])
                small[(y * hw + x) * 3 + c] = (s + 2) // 4
    out = bytearray(w * h * 3)
    for y in range(h):
        for x in range(w):
            si = ((min(y // 2, hh - 1)) * hw + min(x // 2, hw - 1)) * 3
            oi = (y * w + x) * 3
            out[oi:oi + 3] = small[si:si + 3]
    return Image(w, h, out)


def crop(img: Image, dx: int, dy: int) -> Image:
    """Remove the first dx columns and dy rows."""
    w, h = img.width, img.height
    nw, nh = w - dx, h - dy
    out = bytearray(nw * nh * 3)
    for y in range(nh):
        src = ((y + dy) * w + dx) * 3
        out[y * nw * 3:(y + 1) * nw * 3] = img.rgb[src:src + nw * 3]
    return Image(nw, nh, out)


def nudge_one_pixel(img: Image) -> Image:
    out = img.copy()
    out.rgb[0] = (out.rgb[0] + 1) % 256
    return out


def sips_convert(src_path: str, fmt: str, dst_path: str, quality: str = None) -> None:
    args = ["sips", "-s", "format", fmt]
    if quality is not None:
        args += ["-s", "formatOptions", quality]
    args += [src_path, "--out", dst_path]
    subprocess.run(args, check=True, capture_output=True)


def sips_png_resave(src_png: str):
    """Re-save a PNG as PNG with sips; return (Image, text, other_chunks) of the result."""
    with tempfile.TemporaryDirectory() as d:
        dst = os.path.join(d, "resaved.png")
        sips_convert(src_png, "png", dst)
        return read_png(dst)


def sips_jpeg_roundtrip(src_png: str, quality: str = "80"):
    """PNG -> JPEG -> PNG with sips; return (Image, text, other_chunks) of the final PNG."""
    with tempfile.TemporaryDirectory() as d:
        mid = os.path.join(d, "mid.jpg")
        dst = os.path.join(d, "back.png")
        sips_convert(src_png, "jpeg", mid, quality)
        sips_convert(mid, "png", dst)
        return read_png(dst)
