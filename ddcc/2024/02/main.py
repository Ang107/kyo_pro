import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


# 各入力に対する処理
def main(n):
    tmp = []
    hms = [0] * 3
    ans = [0] * 3
    prv = 1
    for i in n:
        if i != "h" and i != "m" and i != "s" and i != "+" and i != "-":
            tmp.append(i)
        if i == "h":
            hms[0] = int("".join(tmp))
            tmp = []
        if i == "m":
            hms[1] = int("".join(tmp))
            tmp = []
        if i == "s":
            hms[2] = int("".join(tmp))
            tmp = []
        if i == "+":
            for i in range(3):
                if prv == 1:
                    ans[i] += hms[i]
                else:
                    ans[i] -= hms[i]
            prv = 1
        if i == "-":
            for i in range(3):
                if prv == 1:
                    ans[i] += hms[i]
                else:
                    ans[i] -= hms[i]
            prv = -1
        # print(ans, hms, tmp)
    for i in range(3):
        if prv == 1:
            ans[i] += hms[i]
        else:
            ans[i] -= hms[i]

    tmp = ans[0] * 3600 + ans[1] * 60 + ans[2]
    tmp %= 24 * 60 * 60
    h = tmp // 3600
    m = (tmp - h * 3600) // 60
    s = tmp - h * 3600 - m * 60
    return f'"{h}h{m}m{s}s"'


if __name__ == "__main__":
    # 入力をここに追加
    Input = [
        "0h0m0s-0h41m6s+20h54m10s+23h59m59s-1h23m13s+15h4m7s+14h46m10s",
        "16h13m37s-17h15m28s+10h51m31s-0h0m0s+15h39m56s-18h35m25s+19h17m42s-20h32m46s+22h21m31s",
        "0h4m7s-23h19m2s-19h47m15s-23h31m23s-22h45m58s-19h27m58s-21h9m59s-22h14m57s-19h39m36s-23h59m59s",
    ]

    Output = []
    for i in Input:
        Output.append(main(i))
    print(f"{Output[0]},{Output[1]},{Output[2]}")
