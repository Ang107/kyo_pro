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
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n, c = MII()
a = LMII()

# iまでで追加で貰えるポイントの最大値
# dp = [0] * n
# for i in range(n):
#     num = a[i]
#     add = num * c - num
#     if i == 0:
#         dp[i] = max(add, dp[i])

#     else:
#         dp[i] = max(add, dp[i - 1] + add)
# print(sum(a) + max(dp))

if c >= 1:
    # iを終点とする任意区間の総和の最大値
    dp = [-inf] * n

    for i in range(n):
        num = a[i]
        if i == 0:
            dp[i] = max(dp[i], num)
        else:
            dp[i] = max(dp[i], num, dp[i - 1] + num)
    print(dp)
    print(max(sum(a), sum(a) + max(dp) * (c - 1)))
else:
    # iを終点とする任意区間の総和の最小値
    dp = [inf] * n
    for i in range(n):
        num = a[i]
        if i == 0:
            dp[i] = min(dp[i], num)
        else:
            dp[i] = min(dp[i], num, dp[i - 1] + num)
    # print(dp)
    print(max(sum(a), sum(a) + min(dp) * (c - 1)))
