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

n, k, x = MII()
t = LMII()
ans = 0
tmp = []
for i in range(n):
    tmp.append(t[i])
    # 出荷する。
    if i == n - 1 or t[i] + x <= t[i + 1] or len(tmp) >= k:
        for j in tmp:
            ans += t[i] - j
        tmp = []

# dp[i] = i個目までの荷物で、j個目から貯めてるときの、前回の出荷日が総和の最小値
dp = [[inf] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(i + 1):
        # 貯める場合
        if j - i + 1 < k:
            dp[i + 1][j] = dp[i][j] + (j - i) * (t[i] - t[i - 1])
            
        # 

    # tmp.append(t[i])
    # # 出荷する場合
    # if i == n - 1 or t[i] + x <= t[i + 1] or len(tmp) >= k:
    #     for j in tmp:
    #         ans += t[i] - j
    #     tmp = []
