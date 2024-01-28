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


# 最長共通部分列の長さのみ取得（高速）
def get_most_long_subsequence(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
            if s[i - 1] == t[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
    return dp[n][m]


n = II()
s = input()
# ans = 0
# for i in range(n):
#     ans = max(ans, get_most_long_subsequence(s[:i], s[i::-1]))
# for i in range(n):
#     ans = max(ans, 1 + get_most_long_subsequence(s[:i], s[i + 1 :: -1]))

# print(ans)
# ~i j~に含まれる回文の長さ
dp = [[0] * (n + 2) for _ in range(n + 2)]

for i in range(n):
    for j in range(i, n)[::-1]:
        # print(i, j)
        if s[i] == s[j]:
            if i == j:
                c = 1
            else:
                c = 2
        else:
            c = 0
        dp[i][j] = max(dp[i - 1][j], dp[i][j + 1], dp[i - 1][j + 1] + c)

pprint(dp)
print(max([max(i) for i in dp]))
