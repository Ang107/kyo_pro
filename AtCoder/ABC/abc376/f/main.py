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
# n = 998244353
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
n, q = MII()
l = 0
r = 1
ans = 0
# (左手、右手):コスト
cand = defaultdict(lambda: inf)
cand[0 * l + r] = 0


def dis_r(f, t):
    if f <= t:
        return t - f
    else:
        return t + n - f


def dis_l(f, t):
    if f >= t:
        return f - t
    else:
        return f + n - t


for _ in range(q):
    h, t = input().split()
    t = int(t) - 1
    ncand = defaultdict(lambda: inf)
    if h == "R":
        for lr, c in cand.items():
            l, r = lr // n, lr % n
            # print(l, r)
            # 時計回り
            if r <= l:
                # ぶつかる場合
                if r <= l <= t:
                    ncost = c
                    nl = (t + 1) % n
                    nr = t
                    ncost += dis_r(l, nl) + dis_r(r, nr)
                    assert dis_r(l, nl) + dis_r(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)
                else:
                    ncost = c
                    nl = l
                    nr = t
                    ncost += dis_r(l, nl) + dis_r(r, nr)
                    assert dis_r(l, nl) + dis_r(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)

            elif r >= l:
                # ぶつかる場合
                if l <= t <= r:
                    ncost = c
                    # ncost += (t - l + 1) + t + (n - r)
                    nl = (t + 1) % n
                    nr = t
                    ncost += dis_r(l, nl) + dis_r(r, nr)
                    assert dis_r(l, nl) + dis_r(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)
                else:
                    ncost = c
                    nl = l
                    nr = t
                    ncost += dis_r(l, nl) + dis_r(r, nr)
                    # print(l, r, nl, nr, dis_r(l, nl) + dis_r(r, t))
                    assert dis_r(l, nl) + dis_r(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)

            # 反時計回り
            if r >= l:
                # ぶつかる場合
                if r >= l >= t:
                    ncost = c
                    nl = (t - 1) % n
                    nr = t
                    ncost += dis_l(l, nl) + dis_l(r, nr)
                    assert dis_l(l, nl) + dis_l(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)
                else:
                    ncost = c
                    nl = l
                    nr = t
                    ncost += dis_l(l, nl) + dis_l(r, nr)
                    assert dis_l(l, nl) + dis_l(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)

            elif r <= l:
                # ぶつかる場合
                if l >= t >= r:
                    ncost = c
                    nl = (t - 1) % n
                    nr = t
                    ncost += dis_l(l, nl) + dis_l(r, nr)
                    assert dis_l(l, nl) + dis_l(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)
                else:
                    ncost = c
                    nl = l
                    nr = t
                    ncost += dis_l(l, nl) + dis_l(r, nr)
                    assert dis_l(l, nl) + dis_l(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)
    else:
        for lr, c in cand.items():
            l, r = lr // n, lr % n
            # 時計回り
            if l <= r:
                # ぶつかる場合
                if l <= r <= t:
                    ncost = c
                    nr = (t + 1) % n
                    nl = t
                    ncost += dis_r(l, nl) + dis_r(r, nr)
                    assert dis_r(l, nl) + dis_r(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)
                else:
                    ncost = c
                    nr = r
                    nl = t
                    ncost += dis_r(l, nl) + dis_r(r, nr)
                    assert dis_r(l, nl) + dis_r(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)

            elif l >= r:
                # ぶつかる場合
                if r <= t <= l:
                    ncost = c
                    nr = (t + 1) % n
                    nl = t
                    ncost += dis_r(l, nl) + dis_r(r, nr)
                    assert dis_r(l, nl) + dis_r(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)
                else:
                    ncost = c
                    nr = r
                    nl = t
                    ncost += dis_r(l, nl) + dis_r(r, nr)
                    assert dis_r(l, nl) + dis_r(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)

            # 反時計回り
            if l >= r:
                # ぶつかる場合
                if l >= r >= t:
                    ncost = c
                    nr = (t - 1) % n
                    nl = t
                    ncost += dis_l(l, nl) + dis_l(r, nr)
                    assert dis_l(l, nl) + dis_l(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)
                else:
                    ncost = c
                    nr = r
                    nl = t
                    ncost += dis_l(l, nl) + dis_l(r, nr)
                    assert dis_l(l, nl) + dis_l(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)

            elif l <= r:
                # ぶつかる場合
                if r >= t >= l:
                    ncost = c
                    nr = (t - 1) % n
                    nl = t
                    ncost += dis_l(l, nl) + dis_l(r, nr)
                    assert dis_l(l, nl) + dis_l(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)
                else:
                    ncost = c
                    nr = r
                    nl = t
                    ncost += dis_l(l, nl) + dis_l(r, nr)
                    assert dis_l(l, nl) + dis_l(r, nr) >= 0
                    ncand[nl * n + nr] = min(ncand[nl * n + nr], ncost)
    cand = ncand
    print(cand)
    for i in cand:
        print((i // n, i % n), cand[i])
ans = min(cand.values())
# for i in cand:
#     print(i // n, i % n)
print(ans)
