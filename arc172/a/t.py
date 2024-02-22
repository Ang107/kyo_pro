import sys

from itertools import (
    accumulate,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）


sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict

II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
PY = lambda: print("Yes")
PN = lambda: print("No")
h, w, n = MII()
a = LMII()
a.sort(reverse=True)

# 面積が足りるか
S = 0
for i in a:
    S += (2**i) ** 2

# print(S)
if S > h * w:
    PN()
    exit()


def solve(h, w):
    tmp = defaultdict(int)
    if h == 0 or w == 0:
        return tmp
    if h == w:
        tmp[h] += 1
        return tmp
    while True:
        # print(h, w)
        if h == 0 or w == 0:
            break
        elif h > w:
            num = h // w
            amari = h % w
            tmp[w] += num
            h = amari
        elif h < w:
            num = w // h
            amari = w % h
            tmp[h] += num
            w = amari
    return tmp


dd = solve(h, w)
size = SortedSet()

for i in dd:
    size.add(i)
# print(size)
# print(dd)
for i in a:

    I = 2**i

    idx = size.bisect_left(I)
    if idx == len(size):
        PN()
        exit()

    tmp = size[idx]
    dd[tmp] -= 1

    if dd[tmp] == 0:
        size.remove(tmp)

    if tmp != I:
        # print(tmp - I, I)
        dd_n = solve(tmp - I, I)

        for p, q in dd_n.items():
            if dd[p] == 0:
                size.add(p)
            dd[p] += 2 * q

        if dd[tmp - I] == 0:
            size.add(tmp - I)
        dd[tmp - I] += 1

    # print(size)
    # print(dd)

    # print(I)


PY()
