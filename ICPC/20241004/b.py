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
setrecursionlimit(10**7)
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
ans = []
while 1:
    n, m = MII()
    if n == m == 0:
        break
    a = LMII()
    w = LMII()
    for i in range(m):
        w.append(-w[i])
    cand = set()
    for mask in range(1 << (2 * m)):
        weight = 0
        for i in range(2 * m):
            if mask >> i & 1:
                weight += w[i]
        # if weight > 0:
        cand.add(weight)
    na = set()
    for i in a:
        if i in cand:
            pass
        else:
            na.add(i)
    if not na:
        ans.append(0)
        continue

    prv_s = set()
    now_s = set()
    # print(cand)
    f = True
    # print(na)
    for i in na:
        for j in cand:
            if f:
                now_s.add(abs(i - j))
            else:
                if abs(i - j) in prv_s:
                    now_s.add(abs(i - j))
        # print(prv_s, now_s)
        prv_s = now_s
        now_s = set()
        f = False
    if prv_s:
        ans.append(min(prv_s))
    else:
        ans.append(-1)

for i in ans:
    print(i)
