import matplotlib.pyplot as plt
from typing import List, Tuple
from dataclasses import dataclass
from functools import reduce


@dataclass
class Action:
    p: int
    r: int
    d: str
    b: int


def get_pos(
    w: int,
    h: int,
    action: Action,
    vertical: List[Tuple[int, int, int]],
    horizon: List[Tuple[int, int, int]],
) -> Tuple[int, int, int, int]:
    """
    各長方形の位置を計算する関数。
    """
    if action.r == 1:
        w, h = h, w  # 回転

    l, r, u, d = 0, 0, 0, 0
    if action.d == "U":
        if action.b == -1:
            l = 0
            r = l + w
        else:
            l = horizon[action.b][1]
            r = l + w

        u = 0
        for x, y, z in horizon:
            if l <= y and x <= r:
                u = max(u, z)
        d = u + h

    else:  # action.d == "L"
        if action.b == -1:
            u = 0
            d = u + h
        else:
            u = vertical[action.b][1]
            d = u + h

        l = 0
        for x, y, z in vertical:
            if u <= y and x <= d:
                l = max(l, z)
        r = l + w

    return u, d, l, r


def get_wh(
    actions: List[Action], cand: List[Tuple[int, int]]
) -> Tuple[int, int, List[Tuple[int, int, int, int]]]:
    """
    長方形の幅、高さ、そしてすべての位置情報を返す関数。
    """
    assert len(actions) == len(cand)

    vertical = []
    horizon = []
    W, H = 0, 0
    positions = []

    for action, (w, h) in zip(actions, cand):
        u, d, l, r = get_pos(w, h, action, vertical, horizon)
        vertical.append((u, d, r))
        horizon.append((l, r, d))
        W = max(W, r)
        H = max(H, d)
        positions.append((u, d, l, r))

    return W, H, positions


def visualize(actions: List[Action], cand: List[Tuple[int, int]]):
    """
    長方形の配置を可視化する関数。
    """
    _, _, positions = get_wh(actions, cand)

    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="box")

    # 描画範囲を設定
    W, H = 0, 0
    for u, d, l, r in positions:
        W = max(W, r)
        H = max(H, d)

    ax.set_xlim(0, W + 10)
    ax.set_ylim(0, H + 10)

    # 長方形を描画
    for (u, d, l, r), (w, h) in zip(positions, cand):
        rect = plt.Rectangle((l, u), r - l, d - u, edgecolor="blue", facecolor="none")
        ax.add_patch(rect)

    plt.savefig("tmp.png")


# サンプルデータ
n = int(input("長方形の数: "))
rectangles = [tuple(map(int, input("幅と高さ: ").split())) for _ in range(n)]
actions = []
for _ in range(n):
    p_, r_, d_, b_ = input("アクション (p r d b): ").split()
    p_ = int(p_)
    r_ = int(r_)
    b_ = int(b_)
    actions.append(Action(p_, r_, d_, b_))

# 可視化
visualize(actions, rectangles)
