#!/usr/bin/env python3
"""
tools/err/0000.txt, 0001.txt, … を読み込み，
 1. 第 2 列 × 第 3 列の散布図
 2. 第 2 列（≒誤差?）のヒストグラム

をファイルごとに 2 画面 (scatter + histogram) で保存します。
出力は同じディレクトリに PNG で生成されます。
"""

import glob
import os
import numpy as np
import matplotlib.pyplot as plt

ERR_DIR = "tools/err"  # データフォルダ
PATTERN = os.path.join(ERR_DIR, "*.txt")


def main():
    files = sorted(glob.glob(PATTERN))
    if not files:
        print("No files found. Check ERR_DIR.")
        return

    for path in files:
        # 読み込み（列数は 3 以上想定。空白区切り）
        data = np.loadtxt(path)  # shape = (1000, 3)
        if data.shape[1] < 3:
            print(f"Skip {path}: not enough columns")
            continue

        x = data[:, 1]  # 第 2 列
        y = data[:, 2]  # 第 3 列

        fig, axes = plt.subplots(1, 2, figsize=(10, 4))

        # ── 散布図 ───────────────────────────────
        ax0 = axes[0]
        ax0.scatter(x, y, s=8, alpha=0.6)
        ax0.set_xlabel("2nd column")
        ax0.set_ylabel("3rd column")
        ax0.set_title("Scatter")

        # ── ヒストグラム ────────────────────────
        ax1 = axes[1]
        ax1.hist(x, bins=50)
        ax1.set_xlabel("2nd column")
        ax1.set_ylabel("Frequency")
        ax1.set_title("Histogram of 2nd col")

        # ── 仕上げ ──────────────────────────────
        fig.suptitle(os.path.basename(path))
        fig.tight_layout()

        out_png = path + ".png"
        fig.savefig(out_png, dpi=150)
        plt.close(fig)
        print(f"Wrote {out_png}")


if __name__ == "__main__":
    main()
