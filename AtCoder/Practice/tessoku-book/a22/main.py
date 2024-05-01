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
a = [i - 1 for i in a]
b = [i - 1 for i in b]
dp = [-inf] * n
dp[0] = 0

ed_a = [[] for i in range(n)]
ed_b = [[] for i in range(n)]
for i, j in enumerate(a):
    ed_a[j].append(i)

for i, j in enumerate(b):
    ed_b[j].append(i)

for i in range(1, n):
    tmp = -inf
    for j in ed_a[i]:
        tmp = max(tmp, dp[j] + 100)
    for j in ed_b[i]:
        tmp = max(tmp, dp[j] + 150)
    dp[i] = tmp
# pprint(ed_a)
# pprint(ed_b)
# def dfs():
#     deq = deque()
#     deq.append((0, 0))
#     while deq:
#         x, score = deq.pop()
#         if dp[x] > score:
#             continue
#         if dp[a[x]] < dp[x] + 100:
#             dp[a[x]] = dp[x] + 100
#             if a[x] != n - 1:
#                 deq.append((a[x], dp[a[x]]))

#         if dp[b[x]] < dp[x] + 150:
#             dp[b[x]] = dp[x] + 150
#             if b[x] != n - 1:
#                 deq.append((b[x], dp[b[x]]))
#         # print(dp)


# dfs()

# print(dp)
print(dp[n - 1])
