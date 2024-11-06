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
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
YN = ("Yes", "No")
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

n, m = MII()
a = LMII()
rbc = [tuple(LMII()) for _ in range(m)]
a.sort()
rbc.sort(key=lambda x: x[0])
# i番目の部屋までで、j人の部屋が確定したときの、金額の総和の最小値
dp = [[inf] * (n + 1) for _ in range(m + 1)]
dp[0][0] = 0
for i in range(m):
    tmp = bisect_right(a, rbc[i][0])
    for j in range(n + 1):
        if dp[i][j] == inf:
            continue
        # i 番目の部屋に泊まらない場合
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        num = min(rbc[i][1], tmp - j)
        # assert num >= 0
        cost = rbc[i][2]
        # assert j + num <= n, (j, num)
        # 泊まる場合
        dp[i + 1][j + num] = min(dp[i + 1][j + num], dp[i][j] + cost)
# print(dp)
if dp[m][n] == inf:
    dp[m][n] = -1
print(dp[m][n])
