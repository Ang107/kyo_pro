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

DEBUG = True
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
pv = [LMII() for _ in range(q)]
v = [j for i, j in pv]
tmp = {j: i for i, j in enumerate([0] + sorted(set(v)))}
# 座圧
for i in range(q):
    pv[i][0] -= 1
    pv[i][1] = tmp[pv[i][1]]
# 左からi番目までで、最大値がj
dp_l = [[0] * len(tmp) for _ in range(n)]
dp_r = [[0] * len(tmp) for _ in range(n)]
for i in range(n):
    dp_l[i][0] = 1
    dp_r[i][0] = 1
print(pv)
for p, v in pv:
    # 左側を採用する場合
    cnt1 = 0
    for i in range(v + 1):
        cnt1 += dp_l[p][i]
        cnt1 %= mod

    # 右側を採用する場合
    cnt2 = 0
    for i in range(v + 1):
        cnt2 += dp_r[p][i]
        cnt2 %= mod
    for i in range(p + 1):
        dp_l[i][v] += cnt1
        dp_l[i][v] %= mod

    for i in range(p, n):
        dp_r[i][v] += cnt2
        dp_r[i][v] %= mod

    for i in range(v):

        for j in range(p, n):
            dp_l[j][i] = 0
        for j in range(p + 1):
            dp_r[j][i] = 0

    deb(dp_l)
    deb(dp_r)
ans = 0
for i in range(n):
    tmp = 0
    tmp = sum(dp_l[i]) * sum(dp_r[i])
    # for j in range(len(dp_l[0])):
    #     tmp += min(dp_l[i][j], dp_r[i][j])
    #     tmp %= mod
    ans = max(ans, tmp)
print(ans)
