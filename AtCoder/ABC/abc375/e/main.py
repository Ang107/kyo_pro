# from sys import stdin, setrecursionlimit
# from collections import deque, defaultdict
# from itertools import accumulate
# from itertools import permutations
# from itertools import product
# from itertools import combinations
# from itertools import combinations_with_replacement
# from math import ceil, floor, log, log2, sqrt, gcd, lcm
# from bisect import bisect_left, bisect_right
# from heapq import heapify, heappop, heappush
# from functools import cache
# from string import ascii_lowercase, ascii_uppercase

# DEBUG = False
# # import pypyjit
# # pypyjit.set_param("max_unroll_recursion=-1")
# # 外部ライブラリ
# # from sortedcontainers import SortedSet, SortedList, SortedDict
# setrecursionlimit(10**7)
# alph_s = ascii_lowercase
# alph_l = ascii_uppercase
# around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
# around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
# inf = float("inf")
# mod = 998244353
# input = lambda: stdin.readline().rstrip()
# pritn = lambda *x: print(*x)
# deb = lambda *x: print(*x) if DEBUG else None
# PY = lambda: print("Yes")
# PN = lambda: print("No")
# SI = lambda: input()
# IS = lambda: input().split()
# II = lambda: int(input())
# MII = lambda: map(int, input().split())
# LMII = lambda: list(map(int, input().split()))

# # n = II()
# # sum_ = 0
# # ab = []
# # for _ in range(n):
# #     a, b = MII()
# #     a -= 1
# #     ab.append((a, b))
# #     sum_ += b


# def solve(ab, sum_):
#     if sum_ % 3 != 0:
#         return -1
#     t = sum_ // 3
#     dp = [[[inf] * (t + 1) for _ in range(t + 1)] for _ in range(n + 1)]
#     dp[0][0][0] = 0

#     for i in range(n):
#         a, b = ab[i]
#         for j in range(t + 1):
#             for k in range(t + 1):
#                 if dp[i][j][k] == inf:
#                     continue
#                 if j + b <= t:
#                     if a == 0:
#                         dp[i + 1][j + b][k] = min(dp[i + 1][j + b][k], dp[i][j][k])
#                     else:
#                         dp[i + 1][j + b][k] = min(dp[i + 1][j + b][k], dp[i][j][k] + 1)

#                 if k + b <= t:
#                     if a == 1:
#                         dp[i + 1][j][k + b] = min(dp[i + 1][j][k + b], dp[i][j][k])
#                     else:
#                         dp[i + 1][j][k + b] = min(dp[i + 1][j][k + b], dp[i][j][k] + 1)

#                 if a == 2:
#                     dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
#                 else:
#                     dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k] + 1)
#     if
#     return dp[n][t][t]


# def native(ab, sum_):
#     ret = inf
#     n = len(ab)
#     for p in product(range(3), repeat=len(ab)):
#         ans = 0
#         tmp = [0] * 3
#         for i in range(n):
#             tmp[p[i]] += ab[i][1]
#             if p[i] == ab[i][0]:
#                 pass
#             else:
#                 ans += 1
#         if len(set(tmp)) == 1:
#             print(tmp)
#             ret = min(ret, ans)
#     if ret == inf:
#         ret = -1
#     return ret


# import random

# while 1:
#     ab = []
#     n = random.randrange(3, 5)
#     sum_ = 0
#     for _ in range(n):
#         a = random.randrange(3)
#         b = random.randrange(1, 100)
#         ab.append((a, b))
#         sum_ += b
#     if sum_ % 3 == 0:
#         r1 = solve(ab, sum_)
#         r2 = native(ab, sum_)
#         print(r1, r2)
#         if r1 != r2:
#             print(ab, sum_)
#             exit()
from sys import stdin, setrecursionlimit
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = II()
team = [[] for _ in range(3)]
sum_ = 0
ab = []
for _ in range(n):
    a, b = MII()

    a -= 1
    ab.append((a, b))
    sum_ += b
    team[a].append(b)
for i in range(3):
    team[i].sort()
if sum_ % 3 != 0:
    print(-1)
    exit()

t = sum_ // 3
dp = [[[inf] * (t + 1) for _ in range(t + 1)] for _ in range(n + 1)]
dp[0][0][0] = 0
# print(t)
# print(dp)
for i in range(n):
    a, b = ab[i]
    for j in range(t + 1):
        for k in range(t + 1):
            if dp[i][j][k] == inf:
                continue
            if j + b <= t:
                if a == 0:
                    dp[i + 1][j + b][k] = min(dp[i + 1][j + b][k], dp[i][j][k])
                else:
                    dp[i + 1][j + b][k] = min(dp[i + 1][j + b][k], dp[i][j][k] + 1)

            if k + b <= t:
                if a == 1:
                    dp[i + 1][j][k + b] = min(dp[i + 1][j][k + b], dp[i][j][k])
                else:
                    dp[i + 1][j][k + b] = min(dp[i + 1][j][k + b], dp[i][j][k] + 1)

            if a == 2:
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            else:
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k] + 1)


# print(dp)
if dp[n][t][t] != inf:
    print(dp[n][t][t])
else:
    print(-1)
