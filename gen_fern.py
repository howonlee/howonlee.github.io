#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy", "Pillow"]
# ///

import numpy as np
from PIL import Image
import time

W, H = 1200, 280
N = 8_000_000

# Site colors: background #111111, brand #c0c0c0
BG = np.array([17, 17, 17], dtype=np.float64)
FG = np.array([192, 192, 192], dtype=np.float64)


def make_bismuth_ifs(rng, n):
    """IFS mimicking bismuth hopper crystal patterns.

    Bismuth forms stepped rectangular hopper crystals with 4-fold symmetry.
    We restrict to 90°-increment rotations and quantize translations to a grid
    so the attractor inherits that angular, staircase-stepped character.
    """
    tfms, wts = [], []
    base_scale = rng.uniform(0.40, 0.62)
    step = rng.uniform(0.20, 0.55)  # grid step for staircase quantization

    for _ in range(n):
        # Only rotations by multiples of 90° — no diagonal shear
        rot = rng.integers(0, 4) * (np.pi / 2)
        cos_r = round(np.cos(rot))
        sin_r = round(np.sin(rot))

        # Slight anisotropic scaling (orthorhombic crystal structure)
        sx = base_scale * rng.uniform(0.75, 1.25)
        sy = base_scale * rng.uniform(0.75, 1.25)
        sv_max = max(abs(sx), abs(sy))
        if sv_max > 0.88:
            sx *= 0.88 / sv_max
            sy *= 0.88 / sv_max

        a =  cos_r * sx
        b = -sin_r * sy
        c =  sin_r * sx
        d =  cos_r * sy

        # Snap translations to grid — produces visible staircase steps
        e = round(rng.uniform(-2.5, 2.5) / step) * step
        f = round(rng.uniform(-2.5, 2.5) / step) * step

        tfms.append((a, b, c, d, e, f))
        wts.append(abs(a * d - b * c) + rng.uniform(0.02, 0.15))

    wts = np.array(wts)
    wts /= wts.sum()
    return tfms, np.cumsum(wts)


seed = int(time.time())
rng = np.random.default_rng(seed)
n_tfms = int(rng.integers(4, 9))
tfms, cumwts = make_bismuth_ifs(rng, n_tfms)

rs = rng.random(N)
choices = np.searchsorted(cumwts, rs)

x, y = 0.0, 0.0
xs, ys = np.empty(N), np.empty(N)
for i in range(N):
    a, b, c, d, e, f = tfms[choices[i]]
    x, y = a * x + b * y + e, c * x + d * y + f
    xs[i], ys[i] = x, y

x0, x1 = np.percentile(xs, 1), np.percentile(xs, 99)
y0, y1 = np.percentile(ys, 1), np.percentile(ys, 99)
mask = (xs >= x0) & (xs <= x1) & (ys >= y0) & (ys <= y1)
xs, ys = xs[mask], ys[mask]

col = np.clip(((xs - x0) / (x1 - x0) * (W - 1)).astype(int), 0, W - 1)
row = np.clip(((y1 - ys) / (y1 - y0) * (H - 1)).astype(int), 0, H - 1)

density = np.zeros((H, W), dtype=np.int64)
np.add.at(density, (row, col), 1)
density = np.log1p(density.astype(np.float64))
density /= density.max()

img = (BG + density[..., None] * (FG - BG)).astype(np.uint8)
Image.fromarray(img, "RGB").save("img/barnsley_fern.png")
print(f"Saved img/barnsley_fern.png (seed={seed}, {n_tfms} transforms)")
