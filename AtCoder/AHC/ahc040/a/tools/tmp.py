import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import os
from itertools import combinations

# データの準備 (ここではランダムデータを使用しています。実際のデータを適用する場合は読み込み部分を修正してください)
# データリストの準備


# データ読み込み処理
for i in range(100):
    ws = []
    new_ws = []
    hs = []
    new_hs = []
    whs = []
    new_whs = []
    with open(f"err/{i:04}.txt", "r") as file:
        for line in file:
            if "before:" in line:
                _, w, h = line.split()
                w = int(w)
                h = int(h)
                ws.append(w)
                hs.append(h)
                whs.append(min(w, h) / max(w, h))
            elif "after: " in line:
                _, w, h = line.split()
                w = int(w)
                h = int(h)
                new_ws.append(w)
                new_hs.append(h)
                new_whs.append(w + h)

    print(len(ws))
    plt.scatter(ws, new_ws)
    plt.savefig(f"plot_w/{i:04}.png")
    plt.close()
    plt.scatter(hs, new_hs)
    plt.savefig(f"plot_h/{i:04}.png")
    plt.close()
    plt.scatter(whs, new_whs)
    plt.savefig(f"plot_wh/{i:04}.png")
    plt.close()
