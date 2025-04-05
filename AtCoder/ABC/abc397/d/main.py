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
# (x-y)^3 = x^3 - y^3 - 3x^2y + 3xy^2
# x^3 - y^3 = (x-y)^3 + 3x^2y - 3xy^2 = (x-y)^3 + 3xy(x - y) = (x-y)((x-y)^2 + 3xy)
# = (x-y)(x^2 + xy + y^2) = d((d+y)^2 + (d+y)y + y^2) = d(d^2 + 2dy + y^2 + dy + y^2 + y^2)
# = d(3y^2 + 3dy + d^2)
for d in range(1, n):
    if d**3 > n:
        break
    if n % d != 0:
        continue
    e = n // d
    a = 3
    b = 3 * d
    c = d**2 - e
    y = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    x = d + y
    x = int(x)
    y = int(y)
    if x > 0 and y > 0 and x**3 - y**3 == n:
        print(x, y)
        exit()
print(-1)
