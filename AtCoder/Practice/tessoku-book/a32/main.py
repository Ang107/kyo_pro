import sys

# from collections import deque, defaultdict
# from itertools import (
#     accumulate,
#     product,
#     permutations,
#     combinations,
#     combinations_with_replacement,
# )
# import math
# from bisect import bisect_left, insort_left, bisect_right, insort_right
# from pprint import pprint
# from heapq import heapify, heappop, heappush

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
# deq = deque()
# dd = defaultdict()
mod = 998244353


def Pr(x):
    return print(x)


def PY():
    return print("Yes")


def PN():
    return print("No")


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LMII():
    return list(map(int, input().split()))


def is_not_Index_Er(x, y, h, w):
    return 0 <= x < h and 0 <= y < w  # 範囲外参照


n, a, b = MII()
from functools import cache


@cache
def f(turn, num):

    if num < min(a, b):
        if turn % 2 == 0:
            return -1
        else:
            return 1

    if turn % 2 == 0:
        rslt = -1
        if num >= a:
            rslt = max(rslt, f((turn + 1) % 2, num - a))
        if num >= b:
            rslt = max(rslt, f((turn + 1) % 2, num - b))
        return rslt
    else:
        rslt = 1
        if num >= a:
            rslt = min(rslt, f((turn + 1) % 2, num - a))
        if num >= b:
            rslt = min(rslt, f((turn + 1) % 2, num - b))
        return rslt


ans = f(0, n)
if ans == 1:
    print("First")
else:
    print("Second")

# a, b = min(a, b), max(a, b)

# # 先行にとって負け->false
# dp = [False] * (n + 1)
# for i in range(1, n + 1):
#     if i - a >= 0:
#         dp[i] |= not dp[i - a]
#     if i - b >= 0:
#         dp[i] |= not dp[i - b]


# # print(dp)
# if dp[n]:
#     print("First")
# else:
#     print("Second")
