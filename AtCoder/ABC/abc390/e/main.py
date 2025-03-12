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

DEBUG = False
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

n, x = MII()
vac = [[] for _ in range(3)]
for _ in range(n):
    tmp = LMII()
    tmp[0] -= 1
    vac[tmp[0]].append((tmp[1], tmp[2]))
# print(vac)
dp = [[-inf] * (x + 1) for _ in range(3)]
dp[0][0] = 0
dp[1][0] = 0
dp[2][0] = 0
for i in range(3):
    for j in range(len(vac[i])):
        for k in reversed(range(x)):
            # print(i, j, k, vac[i][j][1], k + vac[i][j][1] <= x, dp[i][j], vac[i][j][0])
            if k + vac[i][j][1] <= x:
                dp[i][k + vac[i][j][1]] = max(
                    dp[i][k + vac[i][j][1]], dp[i][k] + vac[i][j][0]
                )
for i in range(3):
    for j in range(x):
        dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
# print(dp)
ans = 0
for i in range(x + 1):
    for j in range(x + 1):
        if i + j > x:
            break
        k = x - i - j
        # print(i, j, k, dp[0][i], dp[1][j], dp[2][k])
        ans = max(ans, min(dp[0][i], dp[1][j], dp[2][k]))
print(ans)
# dp = [[-inf] * 3 for _ in range(x + 1)]
# dp[0] = [0, 0, 0]
# for i in range(n):
#     ndp = [[-(1 << 60)] * 3 for _ in range(x + 1)]
#     for j in range(x):
#         tmp = dp[j][:]
#         if min(ndp[j]) < min(tmp):
#             ndp[j] = tmp
#         if j + vac[i][2] <= x:
#             tmp = dp[j][:]
#             tmp[vac[i][0] - 1] += vac[i][1]
#             print(j, min(ndp[j + vac[i][2]]), min(tmp))
#             if min(ndp[j + vac[i][2]]) < min(tmp):
#                 ndp[j + vac[i][2]] = tmp
#     dp = ndp
# ans = 0
# print(dp)
# for i in dp:
#     ans = max(ans, min(i))
# print(ans)
