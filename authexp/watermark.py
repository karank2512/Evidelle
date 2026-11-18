"""A toy keyed spread-spectrum watermark. It is NOT SynthID or any production scheme, and its
robustness numbers say nothing about production watermarks.

Embedding adds +/-ALPHA to every pixel's R, G and B values, following a +/-1 pattern drawn from a
keyed pseudo-random generator on a fixed 256x256 grid. Detection correlates the image's
high-pass residual (luminance minus its 3x3 local mean) with the key's pattern and reports a
z-like score. Under the null hypothesis (no mark for this key) the score is approximately
standard normal, so THRESHOLD = 4.0 targets a one-sided false-positive rate of about 3e-5.
The experiment also measures the false-positive rate empirically.
"""

import math

from .imageio import Image
from .prng import SplitMix64, seed_from_text

GRID = 256
ALPHA = 3
THRESHOLD = 4.0

_pattern_cache = {}


def pattern(key: str):
    if key not in _pattern_cache:
        rng = SplitMix64(seed_from_text("wm-pattern:" + key))
        _pattern_cache[key] = [1 if (rng.next_u64() >> 63) else -1 for _ in range(GRID * GRID)]
    return _pattern_cache[key]


def _clamp(v):
    return 0 if v < 0 else 255 if v > 255 else v


def embed(img: Image, key: str, alpha: int = ALPHA) -> Image:
    p = pattern(key)
    out = bytearray(img.rgb)
    w = img.width
    for y in range(min(img.height, GRID)):
        for x in range(min(w, GRID)):
            d = alpha * p[y * GRID + x]
            i = (y * w + x) * 3
            out[i] = _clamp(out[i] + d)
            out[i + 1] = _clamp(out[i + 1] + d)
            out[i + 2] = _clamp(out[i + 2] + d)
    return Image(img.width, img.height, out)


def luminance(img: Image):
    rgb = img.rgb
    return [0.299 * rgb[i] + 0.587 * rgb[i + 1] + 0.114 * rgb[i + 2] for i in range(0, len(rgb), 3)]


def residual(img: Image):
    """Luminance minus its 3x3 box mean (edges clamped)."""
    w, h = img.width, img.height
    lum = luminance(img)
    rows = []
    for y in range(h):
        r = lum[y * w:(y + 1) * w]
        rows.append([r[max(x - 1, 0)] + r[x] + r[min(x + 1, w - 1)] for x in range(w)])
    res = [0.0] * (w * h)
    for y in range(h):
        up, mid, dn = rows[max(y - 1, 0)], rows[y], rows[min(y + 1, h - 1)]
        base = y * w
        for x in range(w):
            res[base + x] = lum[base + x] - (up[x] + mid[x] + dn[x]) / 9.0
    return res


def score_residual(res, w: int, h: int, key: str) -> float:
    """Correlation score of a precomputed residual against the key's pattern at origin (0, 0)."""
    p = pattern(key)
    num = 0.0
    den = 0.0
    for y in range(min(h, GRID)):
        base = y * w
        pbase = y * GRID
        for x in range(min(w, GRID)):
            r = res[base + x]
            num += r * p[pbase + x]
            den += r * r
    return num / math.sqrt(den) if den > 0 else 0.0


def detect(img: Image, key: str) -> float:
    return score_residual(residual(img), img.width, img.height, key)


def copy_attack(marked: Image, target: Image, alpha: int = ALPHA) -> Image:
    """Estimate the mark from a marked image's residual sign and stamp it onto another image
    without knowing the key (a 'copy attack')."""
    res = residual(marked)
    out = bytearray(target.rgb)
    w = min(marked.width, target.width)
    h = min(marked.height, target.height)
    for y in range(h):
        for x in range(w):
            r = res[y * marked.width + x]
            d = alpha if r > 0 else (-alpha if r < 0 else 0)
            i = (y * target.width + x) * 3
            out[i] = _clamp(out[i] + d)
            out[i + 1] = _clamp(out[i + 1] + d)
            out[i + 2] = _clamp(out[i + 2] + d)
    return Image(target.width, target.height, out)
