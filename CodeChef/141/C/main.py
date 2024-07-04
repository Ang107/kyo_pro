import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

t = II()
ans = []

for _ in range(t):
    n = II()
    p = LMII()
    g = []
    max_ = 0
    for i in range(0, n - 1, 2):
        if i + 1 == max(max_, p[i + 1]):
            g.append(1)
        elif i + 1 == max(max_, p[i]):
            g.append(-1)
        else:
            g.append(0)

        max_ = max(max_, p[i], p[i + 1])

    k = []
    max_ = p[0]
    for i in range(1, n - 1, 2):
        if i + 1 == max(max_, p[i + 1]):
            k.append(1)
        elif i + 1 == max(max_, p[i]):
            k.append(-1)
        else:
            k.append(0)
        max_ = max(max_, p[i], p[i + 1])

    rslt = 0
    max_ = 0
    for i in range(n):
        max_ = max(max_, p[i])
        if max_ == i + 1:
            rslt += 1

    g_max = [0] * (len(g) + 1)
    for i in range(len(g)):
        g_max[i + 1] = max(g[i], g_max[i] + g[i])

    k_max = [0] * (len(k) + 1)
    for i in range(len(k)):
        k_max[i + 1] = max(k[i], k_max[i] + k[i])

    ans.append(rslt + max(max(g_max), max(k_max)))

    pass
for i in ans:
    print(i)
