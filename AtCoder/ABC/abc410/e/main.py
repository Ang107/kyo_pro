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

n, h, m = MII()
# iターン目に体力がjのときに残っている魔力の最大値
dp = [[-inf] * (h + 1) for _ in range(n + 1)]
dp[0][h] = m

ab = [LMII() for _ in range(n)]
for i in range(n):
    for j in range(h + 1):
        if j >= ab[i][0]:
            dp[i + 1][j - ab[i][0]] = max(dp[i + 1][j - ab[i][0]], dp[i][j])
        if dp[i][j] >= ab[i][1]:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] - ab[i][1])
ans = 0
for i in reversed(range(n + 1)):
    if max(dp[i]) >= 0:
        ans = i
        break
print(ans)
