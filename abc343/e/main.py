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
# from sortedcontainers import SortedSet, SortedList, SortedDict
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


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


v1, v2, v3 = MII()
if v1 + v2 * 2 + v3 * 3 != 3 * 7**3:
    PN()
    exit()


def solve(x, y, z, a, b, c):
    return (
        max(0, (7 - abs(x - a))) * max(0, (7 - abs(y - b))) * max(0, (7 - abs(z - c)))
    )


for i in range(0, 8):
    for j in range(0, 8):
        for k in range(0, 8):
            for p in range(-7, 8):
                for q in range(-7, 8):
                    for r in range(-7, 8):
                        kasanari = [0] * 3

                        tmp = [0, i, p]
                        tmp.sort()
                        kasanari[0] = max(0, tmp[0] + 7 - tmp[2])
                        tmp = [0, j, q]
                        tmp.sort()
                        kasanari[1] = max(0, tmp[0] + 7 - tmp[2])
                        tmp = [0, k, r]
                        tmp.sort()
                        kasanari[2] = max(0, tmp[0] + 7 - tmp[2])

                        tmp2 = (
                            solve(0, 0, 0, p, q, r)
                            + solve(i, j, k, p, q, r)
                            + solve(i, j, k, 0, 0, 0)
                        )
                        tmp3 = kasanari[0] * kasanari[1] * kasanari[2]

                        if tmp2 - tmp3 * 3 == v2 and tmp3 == v3:
                            PY()
                            print(0, 0, 0, i, j, k, p, q, r)
                            exit()
PN()
# XYZ2 = []
# for i in range(8):
#     for j in range(i, 8):
#         for k in range(j, 8):
#             if i * j * k <= v2:
#                 XYZ2.append((i, j, k))

# tmp = []
# for i in range(len(XYZ2)):
#     for j in range(i, len(XYZ2)):
#         x1, y1, z1 = XYZ2[i]
#         x2, y2, z2 = XYZ2[j]
#         if x1 * y1 * z1 + x2 * y2 * z2 == v2:
#             tmp.append(((x1, y1, z1), (x2, y2, z2)))
# XYZ2 = tmp

# XYZ3 = []
# for i in range(8):
#     for j in range(i, 8):
#         for k in range(j, 8):
#             if i * j * k == v3:
#                 XYZ3.append((i, j, k))
