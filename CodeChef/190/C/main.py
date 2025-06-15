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

t = II()
ans = []
for _ in range(t):
    n, x = MII()
    a = LMII()
    b = LMII()
    # 貪欲でMを求める
    m = 0
    max_a = [0]
    for i in reversed(a):
        max_a.append(max(max_a[-1], i))
    max_a = max_a[::-1]
    for i in range(n):
        if b[i] - m - 1 >= max_a[i + 1] and b[i] - m >= b[i]:
            m += 1
    print(f"{m=}")
    # max_ab = [0]
    # for i in reversed(range(n)):
    #     max_ab.append(max(min(a[i], b[i]), max_ab[-1]))
    # max_ab = max_ab[::-1]
    # res = []
    # print(max_ab)
    # t = 0  # そこまでにパリィ必須の回数
    # ok = True
    # for i in range(n):
    #     if ok and x - t - 1 >= max_ab[i + 1] and x - t >= b[i]:
    #         res.append("1")
    #     else:
    #         res.append("0")
    #     if x - t < a:
    #         ok = False
    #     elif x-t <=
    # ans.append("".join(res))
    pass
for i in ans:
    pritn(i)
