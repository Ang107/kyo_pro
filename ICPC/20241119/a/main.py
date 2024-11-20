from sys import stdin, setrecursionlimit, set_int_max_str_digits
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
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def modinv(a, m):
    b = m
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    if u < 0:
        u += m
    return u


def get_dis(x, y, a, b):
    return abs(-b * x / a + y)


def native(a, b):
    dis = inf
    gcd_ = gcd(a, b)
    a //= gcd_
    b //= gcd_
    if a == 1:
        return (0, 1)

    ans = -1
    for x in range(1, a):
        tmp = x * b / a
        if abs(tmp - int(tmp)) <= abs(int(tmp + 1) - tmp):
            y = int(tmp)
        else:
            y = int(tmp + 1)
        if get_dis(x, y, a, b) < dis:
            dis = get_dis(x, y, a, b)
            ans = (x, y)
    return ans


def solve(a, b):
    gcd_ = gcd(a, b)
    a //= gcd_
    b //= gcd_
    # print(a, b)
    if a == 1:
        x = 0
        y = 1
    # elif a == 1:

    else:
        # x = pow(b, a - 2, a)
        x = pow(b, -1, a)
        mid = a / 2
        if x >= mid:
            x = int(mid - (x - mid))
        tmp = x * b / a
        # print(tmp, abs(tmp - int(tmp)), abs(int(tmp + 1) - tmp))
        if abs(tmp - int(tmp)) <= abs(int(tmp + 1) - tmp):
            y = int(tmp)
        else:
            y = int(tmp + 1)
    return x, y


if 1:
    while 1:
        a, b = MII()
        if a == b == 0:
            break
        print(*solve(a, b))
else:
    import random

    while 1:
        a = random.randrange(1, 1000)
        b = random.randrange(1, 1000)
        print(a, b)
        if solve(a, b) != native(a, b):
            x, y = solve(a, b)
            print(solve(a, b), native(a, b))
            print(get_dis(x, y, a, b))
            x, y = native(a, b)
            print(get_dis(x, y, a, b))
            exit()
