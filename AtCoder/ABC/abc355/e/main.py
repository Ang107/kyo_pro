import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353

pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
import typing

n, l, r = MII()


def calc(l, r):
    rslt = []
    while l < r:
        num = 0
        while l % 2**num == 0 and l + 2**num <= r + 1:
            num += 1
        rslt.append(("?", num - 1, l // 2 ** (num - 1)))
        # t = II()
        # ans += t
        l += 2 ** (num - 1)
        # print(l)
    return rslt


p1 = calc(l, r)
p2 = []
num = 0
while (r - l + 1) > 2**num:
    num += 1
# 内包
if r < (l // (2**num) + 1) * 2**num:

    p2.extend(calc((l // (2**num)) * 2**num, (l // (2**num) + 1) * 2**num - 1))
    print(p2)
    p2.extend(calc((l // (2**num)) * 2**num, l - 1))
    print(p2)

    p2.extend(calc(r + 1, (l // (2**num) + 1) * 2**num - 1))
    print(p2)


# またぎ
else:
    p2.extend(calc((l // (2**num)) * 2**num, (l // (2**num) + 1) * 2**num - 1))
    p2.extend(calc((l // (2**num) + 1) * 2**num, (l // (2**num) + 2) * 2**num - 1))
    p2.extend(calc((l // (2**num)) * 2**num, l - 1))
    p2.extend(calc(r + 1, (l // (2**num) + 2) * 2**num - 1))
print(p1)
print(p2)
if r < (l // (2**num) + 1) * 2**num:
    print("A")
    if len(p2) >= len(p1):
        print("A-1")

        ans = 0
        for i in p1:
            print(*i)
            ans += II()
            ans %= 100
    else:
        print("A-2")

        ans = 0
        for i in calc((l // (2**num)) * 2**num, (l // (2**num) + 1) * 2**num - 1):
            print(*i)
            ans += II()
            ans %= 100
        for i in calc((l // (2**num)) * 2**num, l - 1):
            print(*i)
            ans -= II()
            ans %= 100

        for i in calc(r + 1, (l // (2**num) + 1) * 2**num - 1):
            print(*i)
            ans -= II()
            ans %= 100

else:
    print("B")
    ans = 0
    if (
        len(calc(l, (l // (2**num) + 1) * 2**num - 1))
        < len(calc((l // (2**num)) * 2**num, l - 1)) + 1
    ):
        for i in calc(l, (l // (2**num) + 1) * 2**num - 1):
            print(*i)
            ans += II()
            ans %= 100
    else:
        for i in calc((l // (2**num)) * 2**num, (l // (2**num) + 1) * 2**num - 1):
            print(*i)
            ans += II()
            ans %= 100
        for i in calc((l // (2**num)) * 2**num, l - 1):
            print(*i)
            ans -= II()
            ans %= 100

    if len(calc((l // (2**num) + 1) * 2**num, r)) < calc(
        r + 1, (l // (2**num) + 2) * 2**num - 1
    ):
        for i in calc((l // (2**num) + 1) * 2**num, r):
            print(*i)
            ans += II()
            ans %= 100
    else:
        for i in calc((l // (2**num) + 1) * 2**num, (l // (2**num) + 2) * 2**num - 1):
            print(*i)
            ans += II()
            ans %= 100
        for i in calc(r + 1, (l // (2**num) + 2) * 2**num - 1):
            print(*i)
            ans -= II()
            ans %= 100


# while l < r:
#     num = 0
#     while l % 2**num == 0 and l + 2**num <= r + 1:
#         num += 1
#     p1.append("?", num - 1, l // 2 ** (num - 1))
#     # t = II()
#     # ans += t
#     l += 2 ** (num - 1)
#     # print(l)


print("!", ans % 100)
