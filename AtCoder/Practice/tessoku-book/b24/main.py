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


n = II()
XY = [LMII() for _ in range(n)]

XY.sort(key=lambda x: x[0])
XY.sort(key=lambda x: x[1])
# pprint(XY)

XY.sort(key=lambda x: (x[1], -x[0]))
# pprint(XY)

X = [i for i, j in XY]

# i個目までの箱で、重ねられる最大数
dp = [-inf] * (n + 1)
dp[0] = 0
dp[1] = 1
# 重ねられる最大数がiの時の縦の長さの最小値
h = [inf] * (n + 1)
h[0] = 0
h[1] = X[0]
# print(dp)
# print(h)
for i in range(1, n):
    # X[i]を使用して重ねられる最大数

    tmp = bisect_left(h, X[i])
    # print(X[i])
    # print(tmp)
    # print(dp)
    # print(h)
    dp[i + 1] = max(dp[i], tmp)
    h[tmp] = min(h[tmp], X[i])

print(dp[n])
