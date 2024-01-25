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


N, W = MII()
WV = [LMII() for _ in range(N)]
# dp[i品目までの中から選ぶ][利得がjになるときの]重さの最小値
dp = [[inf] * (1000 * N + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(1000 * N + 1):
        if dp[i - 1][j] != inf:
            # not use
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
            # use
            w, v = WV[i - 1]
            if dp[i - 1][j] + w <= W:
                dp[i][j + v] = min(dp[i][j + v], dp[i - 1][j] + w)
# print(dp)
ans = i
for i, j in enumerate(dp[N]):
    if j != inf:
        ans = i
print(ans)

# d = defaultdict(int)
# # v->w
# d[0] = 0
# s = set([0])
# for i in range(N):
#     w, v = MII()
#     tmp_s = set()
#     tmp_d = defaultdict(int)
#     for j in s:
#         tmp_s.add(j)
#         if tmp_d[j] == 0 or tmp_d[j] > d[j]:
#             tmp_d[j] = d[j]
#         if d[j] + w <= W:
#             tmp_s.add(j + v)
#             if tmp_d[j + v] == 0 or tmp_d[j + v] > d[j] + w:
#                 tmp_d[j + v] = d[j] + w
#     s, d = tmp_s, tmp_d
#     # print(s)

# # print(s, d)
# ans = max([i for i, j in d.items() if j <= W])
# print(ans)
