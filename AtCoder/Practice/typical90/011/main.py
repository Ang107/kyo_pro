import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string

# import pypyjit

# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = II()
dcs = [LMII() for _ in range(n)]
dcs.sort(key=lambda x: x[0])
# i個目の仕事までの中で、j日まで予定が埋まっているときの、利得の総計の最大値
dp = [[-inf] * 5001 for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(5001):
        # 仕事をしない場合
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        # 仕事をする場合
        if j + dcs[i][1] <= dcs[i][0]:
            dp[i + 1][j + dcs[i][1]] = max(
                dp[i + 1][j + dcs[i][1]], dp[i][j] + dcs[i][2]
            )
print(max(dp[n]))


# start_lim = []
# for d, c, s in dcs:
#     start_lim.append(d - c + 1)
# # print(start_lim)
# ans = 0
# for mask in range(1 << n):
#     tmp = []
#     p = 0
#     for i in range(n):
#         if mask >> i & 1:
#             tmp.append(i)
#             p += dcs[i][2]

#     tmp.sort(key=lambda x: dcs[x][0])
#     now = 1
#     res = 0
#     for i in tmp:
#         if now <= start_lim[i]:
#             now += dcs[i][1]
#             res += dcs[i][2]
#         # print(now)
#     ans = max(ans, res)
#     # print(p, tmp, res)
# print(ans)
