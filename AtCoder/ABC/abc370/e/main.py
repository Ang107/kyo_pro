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

n, k = MII()
a = LMII()
d = defaultdict(int)
pref = [0] + list(accumulate(a))
sum_ = 1
for i in range(n):
    tmp = sum_ - d[k - a[i]]
    tmp %= mod
    d[pref[i + 1]] += tmp
    sum_ = tmp
    print(tmp, sum_, d[k - a[i]], pref[i + 1])
print(tmp)
# pref = [0] + list(accumulate(a))
# dp = [0] * (n + 1)
# dp[0] = 1
# for i in range(n):
#     for j in range(i, n):
#         if pref[j + 1] - pref[i] != k:
#             dp[j + 1] += dp[i]
# # print(dp)
# print(dp[n])
