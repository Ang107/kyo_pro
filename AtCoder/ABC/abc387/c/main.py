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


# n進数->10進数
def base_10(num_n, n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


# 10進数->n進数
def base_n(num_10, n, **kwargs):
    trans = kwargs.get("trans", list(map(str, range(n))))
    # print(trans)
    if num_10 == 0:
        return 0
    str_n = ""
    while num_10:
        str_n += trans[num_10 % n]
        num_10 //= n
    return str_n[::-1]


def f(x):
    if x < 10:
        return 0
    keta = len(str(x))
    ans = 0
    for i in range(2, keta):
        for head in range(1, 10):
            ans += head ** (i - 1)

    for head in range(1, int(str(x)[0])):
        ans += head ** (keta - 1)

    head = int(str(x)[0])
    ans += (head) ** (keta - 1)

    sx = [min(int(i), head - 1) for i in str(x)[1:]]
    mx = [head - 1] * (keta - 1)
    sx_h = int("".join(map(str, sx)), base=head)
    mx_h = int("".join(map(str, sx)), base=head)
    deff = mx_h - sx_h
    deff_h = base_n(deff, head)
    ans -= deff_h

    # ans -=

    # if mxi <= sxi:
    #     pass
    # else:
    #     tmp = keta - 1
    #     d = 0
    #     for i, j in zip(mx, sx):
    #         tmp -= 1
    #         # print(tmp)
    #         # print(i, j)
    #         if head <= j:
    #             break
    #         if i >= j:
    #             ans -= (i - j) * (head) ** tmp
    #             d += (i - j) * (head) ** tmp
    #         # for k in range(j + 1, i + 1):
    #         #     d += (head - 1) ** tmp
    #         #     ans -= (head - 1) ** tmp
    #     # print(f"{d=}")
    return ans


# print(f(r), f(l))


def native(x):
    ans = 0
    for i in range(10, x + 1):
        s = str(i)
        l = s[0]
        r = max(s[1:])
        if l > r:
            ans += 1
    return ans


if 1:
    l, r = MII()
    ans = f(r) - f(l - 1)
    print(ans)
else:
    import random

    while 1:
        x = random.randrange(10, 10000)
        r1, r2 = native(x), f(x)
        print(x)
        assert r1 == r2, (x, r1, r2)
