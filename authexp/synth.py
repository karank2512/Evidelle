"""Deterministic synthetic test images: procedural landscapes and geometric shapes.

These are algorithmic images, not photographs and not outputs of a trained generative model.
They contain no people. Two separate "generator families" let the experiment test what a
missing watermark from one family does or does not say about images from the other.
"""

import math

from .imageio import Image
from .prng import SplitMix64, seed_from_text

SIZE = 256


def _lerp(a, b, t):
    return a + (b - a) * t


def _clamp(v):
    return 0 if v < 0 else 255 if v > 255 else int(v)


def landscape(index: int, size: int = SIZE) -> Image:
    rng = SplitMix64(seed_from_text("landscape:%d" % index))
    w = h = size
    sky_top = (rng.randint(20, 80), rng.randint(60, 140), rng.randint(140, 230))
    sky_low = (rng.randint(170, 255), rng.randint(150, 220), rng.randint(120, 200))
    horizon = int(h * (0.50 + 0.12 * rng.uniform()))
    sun_x = rng.randint(30, w - 30)
    sun_y = rng.randint(20, max(21, horizon - 40))
    sun_r = rng.randint(10, 22)
    sun_col = (255, rng.randint(200, 245), rng.randint(120, 190))
    ridges = []
    for k in range(3):
        base = horizon - 45 + 22 * k + rng.randint(-8, 8)
        a1, a2 = 8 + 18 * rng.uniform(), 3 + 7 * rng.uniform()
        f1, f2 = 1 + 2 * rng.uniform(), 4 + 5 * rng.uniform()
        p1, p2 = 6.2832 * rng.uniform(), 6.2832 * rng.uniform()
        shade = 0.35 + 0.2 * k
        col = (int(40 * shade + rng.randint(0, 40)), int(90 * shade + rng.randint(20, 60)), int(120 * shade + rng.randint(0, 50)))
        heights = [base + a1 * math.sin(f1 * 6.2832 * x / w + p1) + a2 * math.sin(f2 * 6.2832 * x / w + p2) for x in range(w)]
        ridges.append((heights, col))
    ground_top = (rng.randint(60, 110), rng.randint(110, 160), rng.randint(40, 80))
    ground_low = (rng.randint(30, 60), rng.randint(60, 100), rng.randint(20, 50))
    ground_y = int(h * 0.82)
    rgb = bytearray(w * h * 3)
    o = 0
    for y in range(h):
        t_sky = min(1.0, y / max(1, horizon))
        sky = tuple(_lerp(sky_top[c], sky_low[c], t_sky) for c in range(3))
        for x in range(w):
            col = sky
            dx, dy = x - sun_x, y - sun_y
            if dx * dx + dy * dy <= sun_r * sun_r:
                col = sun_col
            for heights, rcol in ridges:
                if y >= heights[x]:
                    depth = min(1.0, (y - heights[x]) / 60.0)
                    col = tuple(rcol[c] * (1.0 - 0.35 * depth) for c in range(3))
            if y >= ground_y:
                t = (y - ground_y) / max(1, h - ground_y)
                col = tuple(_lerp(ground_top[c], ground_low[c], t) for c in range(3))
            rgb[o] = _clamp(col[0])
            rgb[o + 1] = _clamp(col[1])
            rgb[o + 2] = _clamp(col[2])
            o += 3
    return Image(w, h, rgb)


def shapes(index: int, size: int = SIZE) -> Image:
    rng = SplitMix64(seed_from_text("shapes:%d" % index))
    w = h = size
    top = (rng.randint(0, 255), rng.randint(0, 255), rng.randint(0, 255))
    low = (rng.randint(0, 255), rng.randint(0, 255), rng.randint(0, 255))
    figures = []
    for _ in range(rng.randint(5, 9)):
        kind = "circle" if rng.uniform() < 0.5 else "rect"
        cx, cy = rng.randint(0, w - 1), rng.randint(0, h - 1)
        s = rng.randint(12, 60)
        col = (rng.randint(0, 255), rng.randint(0, 255), rng.randint(0, 255))
        figures.append((kind, cx, cy, s, col))
    rgb = bytearray(w * h * 3)
    o = 0
    for y in range(h):
        t = y / (h - 1)
        bg = tuple(_lerp(top[c], low[c], t) for c in range(3))
        for x in range(w):
            col = bg
            for kind, cx, cy, s, fcol in figures:
                if kind == "circle":
                    if (x - cx) * (x - cx) + (y - cy) * (y - cy) <= s * s:
                        col = fcol
                elif abs(x - cx) <= s and abs(y - cy) <= s // 2:
                    col = fcol
            rgb[o] = _clamp(col[0])
            rgb[o + 1] = _clamp(col[1])
            rgb[o + 2] = _clamp(col[2])
            o += 3
    return Image(w, h, rgb)
