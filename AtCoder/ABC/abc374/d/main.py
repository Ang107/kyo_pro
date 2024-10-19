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

n, s, t = MII()
abcd = [LMII() for _ in range(n)]
ans = inf


def dis(abcd):
    a, b, c, d = abcd
    return ((a - c) ** 2 + (b - d) ** 2) ** 0.5


for p in permutations(abcd):
    for mask in range(1 << n):
        x, y = 0, 0
        cost = 0
        for i in range(n):
            if mask >> i & 1:
                cost += dis(p[i]) / t + dis([p[i][0], p[i][1], x, y]) / s
                x, y = p[i][2], p[i][3]
            else:
                cost += dis(p[i]) / t + dis([p[i][2], p[i][3], x, y]) / s
                x, y = p[i][0], p[i][1]
        ans = min(ans, cost)
print(ans)
