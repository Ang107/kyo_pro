from sys import stdin, setrecursionlimit
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
# setrecursionlimit(10**7)
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

import random

t = II()
ans = []
xor = random.randrange(1 << 60)
for _ in range(t):
    n, m = MII()
    x = LMII()
    r = LMII()
    xr = [(i, j) for i, j in zip(x, r)]
    xr.sort()
    h = defaultdict(lambda: -1)
    for i, j in xr:
        for k in range(-j, j + 1):
            key = (i + k) ^ xor
            if key not in h:
                h[key] = 0
            h[key] = max(h[key], int((j * j - k * k) ** 0.5))
    res = 0
    for i in h.values():
        res += 1 + 2 * i
    ans.append(res)
for i in ans:
    print(i)
