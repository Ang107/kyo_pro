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
# from scipy.special import comb

k = II()
c = LMII()
kaizyou = [None] * 1001
kaizyou[0] = 1
kaizyou[1] = 1
for i in range(2, 1001):
    kaizyou[i] = kaizyou[i - 1] * i
    kaizyou[i] %= mod

kaizyou_gyakugen = [None] * 1001
kaizyou_gyakugen[0] = pow(kaizyou[0], -1, mod)
kaizyou_gyakugen[1] = pow(kaizyou[1], -1, mod)
for i in range(2, 1001):
    kaizyou_gyakugen[i] = pow(kaizyou[i], -1, mod)


def comb(a, b):
    return kaizyou[a] * kaizyou_gyakugen[a - b] * kaizyou_gyakugen[b] % mod


# print(kaizyou)
# print(kaizyou_gyakugen)
# while True:
#     a, b = MII()
#     print(comb(a, b))
# i文字目までで合計j個使用したときの、通り数
dp = [[0] * 1001 for _ in range(27)]
dp[0][0] = 1

for i in range(26):
    for j in range(k + 1):
        for l in range(min(c[i] + 1, k - j + 1)):
            dp[i + 1][j + l] += dp[i][j] * comb(j + l, l) % mod
            dp[i + 1][j + l] %= mod
# print(dp)
print(sum(dp[-1][1:]) % mod)


# 使用した個数を持ってDP
# i番目まででjをk個
# 使用した数の総計はK以下、即ち1000以下
# dp = [[0] * 26 for _ in range(i + 1)]
# dp[0]

# memo = {}


# def f(l: list[int], length: int):
#     # print(l, length)
#     tmp = tuple(sorted(l))
#     if tmp in memo:
#         # print(l, length, memo[tmp])
#         return memo[tmp]

#     if length == 0:
#         # print(l, length, 1)
#         return 1

#     rslt = 1
#     for i in range(26):
#         if l[i] > 0:
#             l_new = l[:]
#             l_new[i] -= 1
#             rslt += f(l_new, length - 1)
#             rslt %= mod
#     # print(l, length, rslt)

#     memo[tuple(sorted(l))] = rslt
#     return rslt


# pritn(f([0] * 26, 1))
# pritn(f(c, k) - 1)

# i個目の要素にj個割り当てて、総和がkのときの通り数
# dp = [[[0] * (k + 1) for _ in range(k + 1)] for _ in range(26)]
# for i in range(26):
#     dp[i][0][0] = 1
# ans = 0
# for i in range(26):
#     for j in range(c[i] + 1):
#         for l in range(k + 1):
#             if l + j <= k:
#                 dp[i + 1][j][l + j] += dp[i][0][l]
