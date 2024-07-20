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

alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

t = II()
ans = []

for _ in range(t):
    n, x = MII()
    a = LMII()
    r = n
    # dp[i] = l=iとしたときに、f(l,r) == 0を満たすrの個数
    dp = [0] * (n + 1)
    sum_ = 0
    rslt = 0
    for i in reversed(range(n)):
        sum_ += a[i]
        print(sum_)
        while sum_ - a[r - 1] > x:
            print(i, sum_, r)
            r -= 1
            sum_ -= a[r]
        if sum_ <= x:
            dp[i] = 0
        else:
            dp[i] = dp[r] + 1
        rslt += n - i - dp[i]
        print(dp)
    ans.append(rslt)
    # acc = [0] + list(accumulate(a))
    # to = []
    # start = [0] * n
    # end = [0] * n
    # for i in range(n):
    #     tmp = bisect_right(acc, x + acc[i]) - 1
    #     to.append(tmp)

    # rslt = (n + 1) * n // 2
    # for i in range(n):
    #     if to[i] < n:
    #         end[to[i]] += 1
    #         start[i] += 1
    #         rslt -= 1

    # for i in range(n - 1):
    #     rslt -= end[i] * start[i + 1]
    #     if to[i + 1] < n:
    #         end[to[i + 1]] += end[i]

    # ans.append(rslt)


for i in ans:
    print(i)
