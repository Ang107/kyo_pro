from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
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

DEBUG = True
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n, k = MII()
s = input()
tmp = []
for i in s:
    if i == "A":
        tmp.append(0)
    elif i == "B":
        tmp.append(1)
    elif i == "C":
        tmp.append(2)
    else:
        tmp.append(-1)
dp_2 = [[0] * 3 for _ in range(n)]
for i in range(n):
    for j in range(3):
        if 
# dp = [[[[0] * 51 for _ in range(51)] for _ in range(51)] for _ in range(n + 1)]
# dp[0][0][0][0] = 1
# for i in range(n):
#     for a in range(50):
#         for b in range(50):
#             for c in range(50):
#                 if s[i] == "?":
#                     dp[i + 1][a + 1][b][c] += dp[i][a][b][c]
#                     dp[i + 1][a + 1][b][c] %= mod
#                     dp[i + 1][a][b + 1][c] += dp[i][a][b][c]
#                     dp[i + 1][a][b + 1][c] %= mod
#                     dp[i + 1][a][b][c + 1] += dp[i][a][b][c]
#                     dp[i + 1][a][b][c + 1] %= mod
#                 elif s[i] == "A":
#                     dp[i + 1][a + 1][b][c] += dp[i][a][b][c]
#                     dp[i + 1][a + 1][b][c] %= mod

#                 elif s[i] == "B":
#                     dp[i + 1][a][b + 1][c] += dp[i][a][b][c]
#                     dp[i + 1][a][b + 1][c] %= mod

#                 elif s[i] == "C":
#                     dp[i + 1][a][b][c + 1] += dp[i][a][b][c]
#                     dp[i + 1][a][b][c + 1] %= mod


# def ok(a, b, c):
#     if a % 2 == b % 2 == c % 2:
#         return True
#     else:
#         return False
#     pass


# ans = 0
# for a in range(51):
#     for b in range(51):
#         for c in range(51):
#             if dp[n][a][b][c] > 0:
#                 deb(a, b, c, dp[n][a][b][c])
#             if ok(a, b, c):
#                 ans += dp[n][a][b][c]
#                 ans %= mod
print(ans)
