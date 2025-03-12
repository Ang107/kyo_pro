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
s = list(map(int, input()))
cnt = s.count(1)

l = 0
r = n - cnt


def f(m):
    now = m
    res = 0
    for i in range(n):
        if s[i]:
            res += abs(now - i)
            now += 1
    return res
    pass


while r - l > 2:
    m1 = (l * 2 + r) // 3
    m2 = (l + r * 2) // 3
    if f(m1) > f(m2):
        l = m1
    else:
        r = m2
ans = inf
for i in range(l, r + 1):
    ans = min(ans, f(i))
print(ans)
# indexs = []
# cnt = s.count(1)
# for i in range(n):
#     if s[i]:
#         indexs.append(i)
# # print(s)
# sum_ = sum(indexs)
# avr = sum_ // cnt
# ans = inf
# for i in range(-10, 10):
#     l = avr - cnt // 2 + i
#     r = l + cnt
#     # print(avr, cnt, avr - cnt // 2 + i)
#     # print(l, r)
#     if l in range(n) and r in range(n + 1):
#         now = l
#         tmp = 0
#         for j in range(n):
#             if s[j] == 1:
#                 tmp += abs(j - now)
#                 now += 1
#         # print(l, r, tmp)
#         ans = min(tmp, ans)
# print(ans)
