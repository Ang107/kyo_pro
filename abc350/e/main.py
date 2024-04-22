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
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n, a, x, y = MII()

from functools import cache


@cache
def f(num):
    if num == 0:
        return 0
    else:

        x_cost = x + f(num // a)
        y_cost = 6 * y / 5

        for i in range(2, 7):
            y_cost += f(num // i) / 5

            # print(x, x_cost)
        return min(x_cost, y_cost)


print(f(n))


# while s:
#     tmp = set()
#     print(s)
#     for i in s:
#         y_score = 0
#         for j in range(1, 7):
#             y_score += 6 * i // j

#         if dp[y_score] > dp[i] + y:
#             dp[y_score] = dp[i] + y
#             tmp.add(y_score)

#         x_score = i // a
#         if dp[x_score] > dp[i] + x:
#             dp[x_score] = dp[i] + x
#             tmp.add(x_score)
#     s = tmp
# print(dp[0])
