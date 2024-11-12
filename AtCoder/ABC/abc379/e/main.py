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


def solve(n, s):

    tmp = 0
    ns = []
    for index, i in enumerate(s, start=1):
        m = int(i)
        tmp += index * m
        ns.append(tmp)
    ans = 0
    for index, i in enumerate(ns[::-1]):
        ans += i * 10**index
    return ans
    # ans = [0] * (n * 2)
    # for index, i in enumerate(ns[::-1]):
    #     for j, k in enumerate(str(i)[::-1]):
    #         if ans[index + j] + int(k) >= 10:
    #             ans[index + j] += int(k)
    #             ans[index + j] %= 10
    #             ans[index + j + 1] += 1
    #         else:
    #             ans[index + j] += int(k)
    # return int("".join(map(str, ans))[::-1])


if 1:
    n = II()
    s = input()
    print(solve(n, s))
else:
    import random

    while 1:
        n = random.randrange(1, 10**5)
        s = "".join(map(str, [random.randrange(1, 10) for _ in range(n)]))
        print(solve(n, s))
