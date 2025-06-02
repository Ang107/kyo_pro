from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
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
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

h, w = MII()
a = [LMII() for _ in range(w)]
dp = [[[-inf] * 3 for _ in range(w)] for _ in range(h)]
dp[0][0][0] = a[0][0]
dp[0][0][1] = 0
dp[0][0][2] = 0
for i in range(h):
    for j in range(w):
        if i == j == 0:
            continue
        if i - 1 >= 0:
            dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][1])
            dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][0] + a[i][j])
            dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][2] + a[i][j])
        if j - 1 >= 0:
            dp[i][j][0] = max(dp[i][j][0], dp[i][j - 1][2])
            dp[i][j][0] = max(dp[i][j][0], dp[i][j - 1][0] + a[i][j])
            dp[i][j][0] = max(dp[i][j][0], dp[i][j - 1][1] + a[i][j])

        if i < h - 1:
            dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][0])
            dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][2])
            dp[i][j][1] = max(dp[i][j][1], dp[i][j - 1][0])
            dp[i][j][1] = max(dp[i][j][1], dp[i][j - 1][1])

        if j < w - 1:
            dp[i][j][2] = max(dp[i][j][2], dp[i][j - 1][0])
            dp[i][j][2] = max(dp[i][j][2], dp[i][j - 1][1])
            dp[i][j][2] = max(dp[i][j][2], dp[i - 1][j][0])
            dp[i][j][2] = max(dp[i][j][2], dp[i - 1][j][2])
print(max(dp[-1][-1]))
print(dp)
