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


def make_ifs(rng, n):
    tfms, wts = [], []
    for _ in range(n):
        # Fully random affine matrix, scaled so largest singular value < 0.9
        mat = rng.uniform(-1, 1, (2, 2))
        sv_max = np.linalg.svd(mat, compute_uv=False)[0]
        if sv_max > 0.05:
            mat *= rng.uniform(0.25, 0.88) / sv_max
        a, b, c, d = mat[0, 0], mat[0, 1], mat[1, 0], mat[1, 1]
        e, f = rng.uniform(-2.0, 2.0, 2)
        tfms.append((a, b, c, d, e, f))
        # Partially random weights — not just |det|
        wts.append(abs(a * d - b * c) + rng.uniform(0.05, 0.3))
    wts = np.array(wts)
    wts /= wts.sum()
    return tfms, np.cumsum(wts)


seed = int(time.time())
rng = np.random.default_rng(seed)
n_tfms = int(rng.integers(2, 9))
tfms, cumwts = make_ifs(rng, n_tfms)

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
