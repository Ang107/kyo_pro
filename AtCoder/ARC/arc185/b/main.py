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


def solve(n: int, a: list[int]):
    # r = 1

    pref = list(accumulate(a))
    for i in range(1, n - 1):
        if a[i - 1] > a[i]:
            a[i + 1] -= a[i - 1] - a[i]
            a[i] = a[i - 1]
        else:
            a[i] = (pref[i]) // (i + 1) + (pref[i] % (i + 1) != 0)
        # sum_ += tmp
        # print(sum_)
        # print(a)

    # print(a)
    if a == sorted(a):
        return "Yes"
    else:
        return "No"

    # tmp = []
    # for i in range(n - 1):
    #     print(i, a[i], a[i + 1], a[i] < a[i + 1])
    #     if a[i] < a[i + 1]:
    #         tmp.append(i)
    # print(tmp)
    # for i in reversed(range(0, n - 1)):
    #     while tmp and tmp[-1] > i:
    #         tmp.pop()
    #     while a[i] > a[i + 1]:
    #         if not tmp:
    #             return "No"
    #         print(a, tmp)
    #         min_ = min(a[i] - a[i + 1], a[tmp[-1] + 1] - a[tmp[-1]])
    #         a[i] -= min_
    #         a[tmp[-1]] += min_
    #         if a[tmp[-1]] == a[tmp[-1] + 1] or tmp[-1] == i - 1:
    #             tmp.pop()

    # if a == sorted(a):
    #     return "Yes"
    # else:
    #     return "No"


t = II()
for _ in range(t):
    n = II()
    a = LMII()
    print(solve(n, a))

# import random

# for _ in range(10):
#     n = random.randrange(2, 11)
#     a = [random.randrange(0, 100) for _ in range(n)]
#     print(n, a)
#     print(solve(n, a))
