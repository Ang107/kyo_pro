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


n, m, k = MII()
ab = [LMII() for _ in range(m)]
# i番目までにj個のグループを確定させたときの、小説の良さの最大値
dp = [[-inf] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 0
from functools import cache


@cache
def f(l, r):
    cnt = 0
    for a, b in ab:
        if l <= a and b <= r:
            cnt += 1
    return cnt


for i in range(1, n + 1):
    for j in range(i):
        for l in range(k):
            dp[i][l + 1] = max(dp[i][l + 1], dp[j][l] + f(j + 1, i))
print(dp[n][k])
