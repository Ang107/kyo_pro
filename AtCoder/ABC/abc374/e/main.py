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
        # お金をi円使ったときの仕事量の最大値
        dp = defaultdict(int)
        for j in range(x + 2):
            if apbq[i][1] <= j:
                dp[j] = max(dp[j], dp[j - apbq[i][1]] + apbq[i][0])
            if apbq[i][3] <= j:
                dp[j] = max(dp[j], dp[j - apbq[i][3]] + apbq[i][2])
            if dp[j] >= mid:
                break
            # print(dp)
        sum_cost += j
        if sum_cost > x:
            break

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
