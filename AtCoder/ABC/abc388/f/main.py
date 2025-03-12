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


def extended_gcd(a, b):
    """拡張ユークリッドの互除法を用いて、ax + by = gcd(a, b) を満たす整数 x, y を求める"""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def find_integer_solution(a, b, c):
    """ax + by = c を満たす整数 x, y を求める"""
    gcd, x0, y0 = extended_gcd(a, b)
    if c == -1:
        return gcd
    else:
        # c が gcd(a, b) で割り切れない場合、整数解は存在しない
        if c % gcd != 0:
            return False
        return True
    # # ax0 + by0 = gcd(a, b) の倍数が解の一つなので、両辺を c / gcd(a, b) で割る
    # factor = c // gcd
    # x = x0 * factor
    # y = y0 * factor

    # return x, y


n, m, a, b = MII()

lr = [LMII() for _ in range(m)]
for l, r in lr:
    if r - l > 20:
        PN()
        exit()
gcds = set()
for i in range(a, b + 1):
    for j in range(a, b + 1):
        # tmp = find_integer_solution(i, j, -1)
        gcds.add(gcd(i, j))


indexs = []
ng = set()
for idx, (l, r) in enumerate(lr):
    for i in range(l, r + 1):
        ng.add(i)
    tmp = []
    for i in range(r + 1 - b, l):
        if indexs and indexs[-1] and i <= indexs[-1][-1]:
            continue
        if idx < m - 1 and i >= lr[idx + 1][0]:
            continue
        if i > n:
            continue
        tmp.append(i)
    indexs.append(tmp)

now = [1]
for i in range(len(indexs)):

    next = set()
    for j in now:
        for k in indexs[i]:
            if any((k - j) % l == 0 for l in gcds) and k not in ng and (k - j) >= a:
                next.add(k)
    now = next
    next = set()
    for j in now:
        for k in range(a, b + 1):
            if j + k <= n and j + k not in ng:
                next.add(j + b)
    now = next


if any(n - i >= 0 and any((n - i) % l == 0 for l in gcds) for i in now):
    PY()
else:
    PN()
