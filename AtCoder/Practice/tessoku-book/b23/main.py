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
distance = {}
for i in range(n):
    for j in range(i + 1, n):
        x1, y1, x2, y2 = *XY[i], *XY[j]
        distance[(i, j)] = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        distance[(j, i)] = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# print(distance)
dp = [[inf] * n for _ in range(2**n)]
dp[1][0] = 0
ans = inf
for s in range(1, 2**n):
    for u in range(n):
        for v in range(n):
            if s == (1 << n) - 1 and v == 0 and u != v:
                # print("s")
                ans = min(ans, dp[s][u] + distance[(u, v)])
            if s >> u & 1 and not s >> v & 1:
                dis = distance[(u, v)]
                dp[s | (1 << v)][v] = min(dp[s | 1 << v][v], dp[s][u] + dis)
# pprint(dp)
print(ans)

# dp[0] = [0] * n
# deq = deque()
# deq.append(1)
# dp[1] = [0] * n
# visited = set()
# visited.add(0)
# ans = inf
# while deq:
#     i = deq.pop()
#     for j in range(n):
#         print(i, bin(i), j)
#         # print((i >> j) & 1)
#         if i == 2**n - 1:
#             PY()
#             exit()
#         # if (i >> j) & 1 == 1:
#         #     continue
#         for k in range(n):
#             print(i, j, k)
#             # if i | 2**j == 2**n - 1:
#             #     ans = min(ans, dp[i][j]+)
#             if (i >> k) & 1 == 0 and j != k:
#                 print(i, j, k)
#                 dis = distance[(j, k)]
#                 # print(dp[i | 2**j][k], dp[i][j] + dis)

#                 # if dp[i | 2**j][k] > dp[i][j] + dis:
#                 dp[i | 2**j][k] = min(dp[i | 2**j][k], dp[i][j] + dis)
#                 # if i | 2**j not in visited:
#                 visited.add(i | 2**j)
#                 deq.append(i | 2**j)
#                 # print(i | 2**j)
#     print(visited)
#     # print(deq)
# pprint(dp)
