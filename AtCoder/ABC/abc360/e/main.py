import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")

input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

mod = 998244353
n, k = map(int, input().split())
if n == 1:
    print(1)
    exit()
inv_n = pow(n, -1, mod)


change_0_1 = 2 * (n - 1) * inv_n**2 % mod
change_1_0 = 2 * inv_n**2 % mod
keep_0_0 = (n - 1) ** 2 * inv_n**2 + inv_n**2 % mod
keep_1_1 = (
    (n - 1) ** 2 * inv_n**2 + inv_n**2 + 2 * (n - 1) * inv_n**2 - 2 * inv_n**2 % mod
)

dp = [[0, 0] for _ in range(k + 1)]
dp[0][0] = 1
for i in range(k):
    # 0 -> 0
    dp[i + 1][0] += dp[i][0] * keep_0_0 % mod
    dp[i + 1][0] %= mod

    # 0 -> not 0
    dp[i + 1][1] += dp[i][0] * change_0_1 % mod
    dp[i + 1][1] %= mod

    # not 0 -> not 0
    dp[i + 1][1] += dp[i][1] * keep_1_1 % mod
    dp[i + 1][1] %= mod

    # not 0 -> 0
    dp[i + 1][0] += dp[i][1] * change_1_0 % mod
    dp[i + 1][0] %= mod

ans = (
    dp[k][0] + dp[k][1] * pow(n - 1, -1, mod) * (2 + n) * (n - 1) * pow(2, -1, mod)
) % mod
print(ans)
