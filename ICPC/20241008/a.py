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


ans_l = []
while 1:
    h, w = MII()
    if h == w == 0:
        break
    e = [LMII() for _ in range(h)]

    def isok(a, b, c, d):
        out_min = inf
        in_max = -inf
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                if i == a or i == c or j == b or j == d:
                    out_min = min(out_min, e[i][j])
                else:
                    in_max = max(in_max, e[i][j])
        return (in_max < out_min, out_min)

    def calc(a, b, c, d, out_min):
        res = 0
        for i in range(a + 1, c):
            for j in range(b + 1, d):
                res += out_min - e[i][j]
        return res

    ans = 0
    for i in range(h):
        for j in range(w):
            for ii in range(i + 2, h):
                for jj in range(j + 2, w):
                    ok, out_min = isok(i, j, ii, jj)
                    if ok:
                        ans = max(ans, calc(i, j, ii, jj, out_min))
    ans_l.append(ans)

for i in ans_l:
    print(i)
