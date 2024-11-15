import sys
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


# N, W = MII()

# dp = [[-inf] * (W + 1) for _ in range(N + 1)]
# dp[0][0] = 0

# UV = [LMII() for _ in range(N)]
# # pprint(UV)
# for i in range(1, N + 1):
#     for j in range(W + 1):
#         # not use
#         dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#         # use
#         w, v = UV[i - 1]
#         if w <= j:
#             dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)
# # pprint(dp)
# print(dp[N][W])

from collections import deque, defaultdict

inf = float("inf")

n, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
# i 番目のアイテムまでで重さの総和が j になるときの価値の総和の最大値
dp = [[-inf] * (W + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    new_w, new_v = wv[i]
    for j in range(W + 1):
        # アイテムを入れる場合
        if j + new_w <= W:
            dp[i + 1][j + new_w] = max(dp[i + 1][j + new_w], dp[i][j] + new_v)
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
ans = max(dp[n])
print(ans)

# 一次元 ndp(nextDP,in_place_DP)
dp = [-inf] * (W + 1)
dp[0] = 0
for i in range(n):
    new_w, new_v = wv[i]
    for j in reversed(range(W + 1)):
        if j + new_w <= W:
            dp[j + new_w] = max(dp[j + new_w], dp[j] + new_v)
ans = max(dp)
print(ans)


# dp = defaultdict(lambda: -inf)
# # dp[i] : 重さの総和が i になるときの価値の総和の最大値
# dp[0] = 0
# for i in range(n):
#     ndp = defaultdict(lambda: -inf)
#     new_w, new_v = wv[i]
#     for w, v in dp.items():
#         # i 番目のアイテムを入れた場合
#         if w + new_w <= W:
#             ndp[w + new_w] = max(ndp[w + new_w], v + new_v)
#         # 入れない場合
#         ndp[w] = max(ndp[w], dp[w])
#     dp = ndp
# ans = max(dp.values())
# print(ans)
