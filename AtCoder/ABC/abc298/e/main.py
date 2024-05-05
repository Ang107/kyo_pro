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

n, a, b, p, q = MII()
mod_p = pow(p, -1, mod)
mod_q = pow(q, -1, mod)

from functools import cache


@cache
def f(t, a, turn):
    if turn == 0:
        if a >= n:
            return 0
        result = 0
        for i in range(1, p + 1):
            result += f(t + i, a, turn ^ 1) * mod_p
            result %= mod
        return result
    else:
        if t >= n:
            return 1
        result = 0
        for i in range(1, q + 1):
            result += f(t, a + i, turn ^ 1) * mod_q
            result %= mod
        return result


print(f(a, b, 0))

# dp_t = [[0] * (n + 1) for _ in range(n + 1)]
# dp_a = [[0] * (n + 1) for _ in range(n + 1)]

# dp_t[0][a] = 1
# dp_a[0][b] = 1
# mod_p = pow(p, -1, mod)
# mod_q = pow(q, -1, mod)

# for i in range(n):
#     for j in range(1, n + 1):
#         for k in range(1, p + 1):
#             dp_t[i + 1][min(j + k, n)] += dp_t[i][j] * mod_p
#             dp_t[i + 1][min(j + k, n)] %= mod

# for i in range(n):
#     for j in range(1, n + 1):
#         for k in range(1, q + 1):
#             dp_a[i + 1][min(j + k, n)] += dp_a[i][j] * mod_q
#             dp_a[i + 1][min(j + k, n)] %= mod
# # print(dp_t)
# # print(dp_a)
# ans = 0
# cnt = 0
# for i in range(1, n + 1):
#     if dp_t[i][n] * (1 - dp_a[i - 1][n]) != 0:
#         cnt += 1
#         ans += dp_t[i][n] * (1 - dp_a[i - 1][n])
#         ans %= mod
# print(ans * pow(cnt, -1, mod) % mod)
