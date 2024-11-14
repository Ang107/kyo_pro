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
import inspect

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
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


def solve(k, n: int):
    if k > n:
        return 0
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 1
    for i in range(k):
        for j in range(n + 1):
            tmp = n - j
            
            if j+1 <= n:
                dp[i+1][j+1] += dp[i][j] * l % mod
                dp[i+1][j+1] %= mod
                
            for l in range(1, 256):
                dp[]
                if j + l <= n:
                    dp[i + 1][j + l] += 
                    dp[i + 1][j + l] %= mod
    # print(dp)
    return dp[k][n]


ans = []

while 1:
    # 入力を記入
    k, n = MII()
    if k == n == 0:
        break
    ans.append(solve(k, n))
    pass

for i in ans:
    print(i)
