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
a = LMII()
b = LMII()
dp = [inf] * n
dp[0] = 0
b.append(inf)
idx = 0
for i, j in zip(a, b):
    dp[idx + 1] = min(dp[idx + 1], dp[idx] + i)
    if idx + 2 in range(n):
        dp[idx + 2] = min(dp[idx + 2], dp[idx] + j)
    idx += 1
print(dp[n - 1])
# for i in range(1,n):
#     if i >= 2:
#         dp[i] = min(dp[i],dp[i-2]+b[i-2])
#     dp[i] = min(dp[i],dp[i-1]+a[i-1])
# print(dp[-1])
