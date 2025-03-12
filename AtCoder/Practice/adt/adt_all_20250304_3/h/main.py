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


class Inter:
    def __init__(self):
        import random

        self.n = random.randrange(3, 5)
        self.a = [random.randrange(100) for _ in range(2**self.n)]
        self.pref = [0] + list(accumulate(self.a))
        self.l = random.randrange(2**self.n)
        self.r = random.randrange(self.l, 2**self.n)
        self.ans_ = (self.pref[self.r + 1] - self.pref[self.l]) % 100

    def query(self, i, j):
        print(i, j, (self.pref[2**i * (j + 1) - 1] - self.pref[2**i * j]) % 100)
        return (self.pref[2**i * (j + 1)] - self.pref[2**i * j]) % 100

    def ans(self, ans):
        print(ans)
        return self.ans_ == ans


def query(i, j):
    print("?", i, j, flush=True)
    res = int(input())
    return res


ans = []


def f(l, r):
    if l > r:
        return []
    nl = l
    tmp = []
    while nl <= r:
        i = 0
        while nl % 2**i == 0 and nl + 2**i <= r + 1:
            i += 1
        i -= 1
        # print(nl // 2**i)
        tmp.append((i, nl // 2**i))
        nl += 2**i
        # print(i, nl)
    return tmp


if not DEBUG:
    n, l, r = MII()
else:
    inter = Inter()
    n = inter.n
    l = inter.l
    r = inter.r
    print(inter.n)
    print(inter.l)
    print(inter.r)
    print(inter.a)
    print(inter.ans_)

a = f(l, r)

b = f(0, r)

c = f(0, l - 1)
# print(a)
# print(b)
# print(c)
if len(a) < len(b) + len(c):
    ans = 0
    for i, j in a:
        if not DEBUG:
            ans += query(i, j)
        else:
            ans += inter.query(i, j)
        ans %= 100
else:
    ans = 0
    for i, j in b:
        if not DEBUG:
            ans += query(i, j)
        else:
            ans += inter.query(i, j)
        ans %= 100
    for i, j in c:
        if not DEBUG:
            ans -= query(i, j)
        else:
            ans -= inter.query(i, j)
        ans %= 100
if not DEBUG:
    print("!", ans, flush=True)
else:
    print(inter.ans(ans))
