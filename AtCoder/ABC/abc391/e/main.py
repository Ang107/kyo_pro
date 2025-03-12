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
import random


def solve(n, a):
    dp = a
    cnt = [1] * len(a)
    for _ in range(n):
        ndp = []
        ncnt = []
        for i in range(1, len(dp), 3):
            tmp1 = dp[i - 1 : i + 2]
            cand = []
            cnt0 = tmp1.count(0)
            cnt1 = tmp1.count(1)
            ndp.append(cnt1 > cnt0)
            for j in range(i - 1, i + 2):
                if dp[j] == (cnt1 > cnt0):
                    cand.append(cnt[j])
            if abs(cnt0 - cnt1) == 3:
                ncnt.append(sum(sorted(cand)[:2]))
            else:
                ncnt.append(min(cand))
        dp = ndp
        cnt = ncnt
    return cnt[0]


def native(n, a):
    def judge(a):
        while len(a) > 1:
            next = []
            for i in range(1, len(a), 3):
                tmp = a[i - 1 : i + 2]
                if tmp.count(0) > tmp.count(1):
                    next.append(0)
                else:
                    next.append(1)
            a = next
        return a[0]

    m = 3**n
    res = judge(a)
    ans = inf
    for i in range(1 << m):
        tmp = []
        for j in range(m):
            tmp.append(i >> j & 1)
        if res != judge(tmp):
            ans = min(ans, sum([i != j for i, j in zip(a, tmp)]))
    return ans


if 1:
    # n = 13
    # a = [random.randrange(2) for _ in range(3**n)]
    n = II()
    a = list(map(int, input()))
    print(solve(n, a))
else:
    while 1:
        n = random.randrange(1, 3)
        a = [random.randrange(2) for _ in range(3**n)]
        res1 = solve(n, a)
        res2 = native(n, a)
        print(res1, res2)
        if res1 != res2:
            print(a)
            exit()
