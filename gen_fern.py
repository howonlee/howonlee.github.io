#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy", "Pillow"]
# ///

import numpy as np
from PIL import Image

W, H = 1200, 280
N = 8_000_000

def generate_fern(n):
    rng = np.random.default_rng(42)
    rs = rng.random(n)
    xs = np.empty(n)
    ys = np.empty(n)
    x, y = 0.0, 0.0
    for i in range(n):
        r = rs[i]
        if r < 0.01:
            x, y = 0.0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        xs[i] = x
        ys[i] = y
    return xs, ys

xs, ys = generate_fern(N)

x_min, x_max = xs.min(), xs.max()
y_min, y_max = ys.min(), ys.max()

col = np.clip(((xs - x_min) / (x_max - x_min) * (W - 1)).astype(int), 0, W - 1)
row = np.clip(((y_max - ys) / (y_max - y_min) * (H - 1)).astype(int), 0, H - 1)

density = np.zeros((H, W), dtype=np.int64)
np.add.at(density, (row, col), 1)

density = np.log1p(density.astype(np.float64))
density /= density.max()

img_arr = (255 * density).astype(np.uint8)
Image.fromarray(img_arr, mode='L').save('img/barnsley_fern.png')
print("Saved img/barnsley_fern.png")
