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

n, x = MII()
apbq = [LMII() for _ in range(n)]


def isOK(mid):
    sum_cost = 0
    for i in range(n):
        min_cost = inf
        for a_cnt in range(apbq[i][2] + 1):
            tmp = a_cnt * apbq[i][1]
            nokori = max(0, mid - a_cnt * apbq[i][0])
            tmp += apbq[i][3] * -(-nokori // apbq[i][2])
            min_cost = min(min_cost, tmp)
        for b_cnt in range(apbq[i][0] + 1):
            tmp = b_cnt * apbq[i][3]
            nokori = max(0, mid - b_cnt * apbq[i][2])
            tmp += apbq[i][1] * -(-nokori // apbq[i][0])
            min_cost = min(min_cost, tmp)
        sum_cost += min_cost

    # print(mid, sum_cost)
    return sum_cost <= x


def meguru(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = meguru(x * 100 + 1, 0)
print(ans)
