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


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LMII():
    return list(map(int, input().split()))


def is_not_Index_Er(x, y, h, w):
    return 0 <= x < h and 0 <= y < w  # 範囲外参照


n, x, y = MII()
a = LMII()

# grundy数の計算
num = 10**5
dp = [0] * (num + 1)
for i in range(num + 1):
    tmp = set()
    if i - x >= 0:
        tmp.add(dp[i - x])
    if i - y >= 0:
        tmp.add(dp[i - y])
    if tmp:
        if 0 in tmp:
            if max(tmp) == 1:
                dp[i] = 2
            else:
                dp[i] = 1


tmp = 0
for i in a:
    grundy = dp[i]
    tmp ^= grundy

if tmp == 0:
    print("Second")
else:
    print("First")
