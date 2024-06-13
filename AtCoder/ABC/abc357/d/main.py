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
# 10000000000
#   998244353
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
ans = 0
n_len = len(str(n))
r = 10**n_len
print(n * (pow(r, n, mod) - 1) * pow(r - 1, -1, mod) % mod)

# def mod_sum(n, j, mod=998244353):
#     k = pow(10, j, mod)  # 10^j % mod
#     k_n = pow(k, n, mod)  # (10^j)^n % mod
#     numerator = (k_n - 1) % mod
#     denominator = (k - 1) % mod
#     # Compute the modular inverse of the denominator
#     denominator_inv = pow(denominator, mod - 2, mod)
#     result = (numerator * denominator_inv) % mod
#     return result


# print((n % mod * mod_sum(n, n_len)) % mod)
