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

n, q = MII()
a = LMII()
b = LMII()


import random

zobrist_hash = [random.randrange(1 << 63) for _ in range(n + 1)]
pref_a = [0]
pref_b = [0]
for i in range(n):
    pref_a.append(pref_a[-1] + zobrist_hash[a[i]])
    pref_b.append(pref_b[-1] + zobrist_hash[b[i]])

for _ in range(q):
    l, r, L, R = MII()
    l -= 1
    r -= 1
    L -= 1
    R -= 1
    if pref_a[r + 1] - pref_a[l] == pref_b[R + 1] - pref_b[L]:
        PY()
    else:
        PN()
