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

h, w = MII()
a = [LMII() for _ in range(h)]
p = LMII()


def isOK(mid):
    # (i,j)の時点での所持コインの最大値
    dp = [[-inf] * w for _ in range(h)]
    dp[0][0] = mid + a[0][0] - p[0]
    if dp[0][0] < 0:
        return False
    for i in range(h):
        for j in range(w):
            if i + 1 in range(h):
                if dp[i][j] + a[i + 1][j] - p[i + j + 1] >= 0:
                    dp[i + 1][j] = max(
                        dp[i + 1][j], dp[i][j] + a[i + 1][j] - p[i + j + 1]
                    )
            if j + 1 in range(w):
                if dp[i][j] + a[i][j + 1] - p[i + j + 1] >= 0:
                    dp[i][j + 1] = max(
                        dp[i][j + 1], dp[i][j] + a[i][j + 1] - p[i + j + 1]
                    )
    return dp[h - 1][w - 1] >= 0


def meguru(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        # print(mid, isOK(mid))
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = meguru(-1, sum(p))
print(ans)
