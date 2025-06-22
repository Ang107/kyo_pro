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

n = II()
a = [LMII() for _ in range(n)]
# 目がiのサイコロの集合について，目がiの個数
b = defaultdict(list)
c = []
for i in a:
    tmp = defaultdict(int)
    for j in i:
        tmp[j] += 1
        c.append(j)
    for k, v in tmp.items():
        b[k].append(v)
c = sorted(set(c), reverse=True)
ans = 0
sum_ = 0
inv_6 = pow(6, -1, mod)
print(b)
print(c)
sum2 = 0
min_ = min(c)
for i in c:
    tmp = 1 - sum_
    tmp2 = 1
    tmp3 = 1
    tmp4 = 1 - sum2
    for j in b[i]:
        tmp2 *= (6 - j) * inv_6 % mod
        tmp3 *= (6 - j) / 6
        tmp2 %= mod
    tmp *= 1 - tmp2
    tmp4 *= 1 - tmp3
    tmp %= mod
    print(tmp3, tmp4, sum2)
    ans += tmp * i % mod
    ans %= mod
    sum_ += tmp
    sum2 += tmp4
print(ans)


# cnt = defaultdict(lambda: 1)
# cnt2 = defaultdict(lambda: 1)
# p6 = pow(6, -1, mod)
# for i in a:
#     tmp = defaultdict(int)
#     tmp2 = defaultdict(int)
#     for j in i:
#         tmp[j] += p6
#         tmp2[j] += 1 / 6
#     for k, v in tmp.items():
#         cnt[k] *= 1 - v
#         cnt[k] %= mod
#     print(cnt2)
#     print(tmp2)
#     for k, v in tmp2.items():
#         cnt2[k] *= 1 - v
# print(cnt)
# print(cnt2)
# b = sorted(cnt.keys(), reverse=True)
# ans = 0
# print(n, -1, mod)
# c = pow(6 * n, -1, mod)
# tmp = 1
# ans2 = 0
# tmp2 = 1
# for i in b:
#     print(1 - cnt2[i], tmp2)
#     ans += i * (1 - cnt[i]) % mod * (tmp)
#     tmp *= cnt[i]
#     tmp2 *= cnt2[i]
#     print(tmp)
#     # print(i, cnt[i] / (6 * n))
#     ans %= mod
#     print(ans)
# print(ans)
# # i個目までで出目の最大値がjの確立
# dp = [defaultdict(int) for _ in range(n + 1)]
# dp[0][0] = 1
# p = pow(6, -1, mod)
# for i in range(n):
#     for j in range(7):
#         for k in range(6):
#             # print(i + 1, max(j, a[i][k]), j)
#             dp[i + 1][max(j, a[i][k])] += dp[i][j] * p
#             dp[i + 1][max(j, a[i][k])] %= mod

# ans = 0
# for i in dp[n]:
#     ans += dp[n][i] * i
#     ans %= mod
# print(ans)
