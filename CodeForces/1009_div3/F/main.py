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
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(3 * 10**5)
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


ans = []
cnt = 0


@cache
def f(x1, y1, x2, y2):
    global cnt
    # print(cnt)

    cnt += 1
    if x1 == x2 or y1 == y2:
        # print(x1, y1, x2, y2, 0)

        return 0
    res = 0
    i = 0
    while (
        x1 % 2 ** (i + 1) == 0
        and y1 % 2 ** (i + 1) == 0
        and x1 + 2 ** (i + 1) <= x2
        and y1 + 2 ** (i + 1) <= y2
    ):
        i += 1
    # res += (x2 - x1) // (2**i)
    # res += (y2 - y1) // (2**i)
    nx = x1 + 2**i
    ny = y1 + 2**i
    r1 = f(nx, ny, x2, y2)
    xx = (x2 - x1) // (2**i)
    yy = (y2 - y1) // (2**i)
    r1 += xx
    r1 += yy
    r -= 1
    nnx = nx + (x2 - nx) // (2**i) * 2**i
    nny = ny + (y2 - ny) // (2**i) * 2**i
    r1 += f(nnx, ny, x2, y2)
    r1 += f(nx, nny, x2, y2)

    r2 = f(nnx, ny, x2, y2)
    r2 += f(x1, ny, x2, y2)
    r2 += xx

    r3 = f(nx, nny, x2, y2)
    r3 += f(nx, y1, x2, y2)
    r3 += yy
    return min(r1, r2, r3)
    # if nx == x2:
    #     res += (y2 - ny) // (2**i)
    #     ny += (y2 - ny) // (2**i) * 2**i
    # if ny == y2:
    #     res += (x2 - nx) // (2**i)
    #     nx += (x2 - nx) // (2**i) * 2**i
    assert x1 < nx
    assert y1 < ny

    if ny < y2:
        res += f(x1, ny, x2, y2)
    if nx < x2:
        res += f(nx, y1, x2, y2)
    if nx < x2 and ny < y2:
        res -= f(nx, ny, x2, y2)
    # print(x1, y1, x2, y2, nx, ny)
    # print(x1, y1, x2, y2, res)
    return res


import random

for _ in range(1000):
    x1 = random.randrange(0, 10**6)
    y1 = random.randrange(0, 10**6)
    x2 = random.randrange(x1 + 1, 10**6)
    y2 = random.randrange(y1 + 1, 10**6)
    print(x1, y1, x2, y2)
    print(f(x1, y1, x2, y2))
# t = II()

# for _ in range(t):
#     x1, x2, y1, y2 = map(int, input().split())
#     ans.append(f(x1, y1, x2, y2))
# for i in ans:
#     print(i)
