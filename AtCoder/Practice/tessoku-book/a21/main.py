import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x):
    return print(x)


def PY():
    return print("Yes")


def PN():
    return print("No")


def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LMII():
    return list(map(int, input().split()))


def is_not_Index_Er(x, y, h, w):
    return 0 <= x < h and 0 <= y < w  # 範囲外参照


# n = II()
# PA = [LMII() for _ in range(n)]
# # i = 左端j = 右端
# dp = [[0] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n - 1, i - 1, -1):
#         if i >= 1:
#             if i <= PA[i - 1][0] - 1 <= j:
#                 dp[i][j] = max(dp[i][j], dp[i - 1][j] + PA[i - 1][1])
#             else:
#                 dp[i][j] = max(dp[i][j], dp[i - 1][j])

#         if j < n - 1:
#             if i <= PA[j + 1][0] - 1 <= j:
#                 dp[i][j] = max(dp[i][j], dp[i][j + 1] + PA[j + 1][1])
#             else:
#                 dp[i][j] = max(dp[i][j], dp[i][j + 1])
# print(max([max(i) for i in dp]))

n = II()
pa = []
for _ in range(n):
    tmp = LMII()
    tmp[0] -= 1
    pa.append(tmp)
# # dp[l][r] : l~r番目まで残っているときのスコアの最大値
# dp = [[-inf] * n for _ in range(n)]
# dp[0][n - 1] = 0
# for l in range(n):
#     for r in reversed(range(l + 1, n)):
#         s = dp[l][r]
#         if l <= pa[l][0] <= r:
#             s += pa[l][1]
#         dp[l + 1][r] = max(dp[l + 1][r], s)
#         s = dp[l][r]
#         if l <= pa[r][0] <= r:
#             s += pa[r][1]
#         dp[l][r - 1] = max(dp[l][r - 1], s)
# ans = -inf
# for i in range(n):
#     ans = max(ans, dp[i][i])
# print(ans)

# from functools import cache
memo = [[-1] * n for _ in range(n)]


# @cache
def f(l, r):
    if memo[l][r] != -1:
        return memo[l][r]
    if l == r:
        return 0
    res = 0
    if l <= pa[l][0] <= r:
        res = max(res, pa[l][1] + f(l + 1, r))
    else:
        res = max(res, f(l + 1, r))

    if l <= pa[r][0] <= r:
        res = max(res, pa[r][1] + f(l, r - 1))
    else:
        res = max(res, f(l, r - 1))
    memo[l][r] = res
    return res


print(f(0, n - 1))
