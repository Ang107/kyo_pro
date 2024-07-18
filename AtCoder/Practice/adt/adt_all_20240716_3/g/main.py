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
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
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

n = II()
a = LMII()
ans = 0
# i個目まででj個選んだ時にmod k が l になる通り数
dp = [[[[0] * 101 for _ in range(101)] for _ in range(101)] for _ in range(n + 1)]

for i in range(n + 1):
    dp[0][0][i][0] = 1

for i in range(n):
    for j in range(i + 1):
        for k in range(n + 1):
            for l in range(k):
                num = a[i]
                # use
                dp[i + 1][j + 1][k][(l + num) % k] += dp[i][j][k][l]
                dp[i + 1][j + 1][k][(l + num) % k] %= mod
                # not use
                dp[i + 1][j][k][l] += dp[i][j][k][l]
                dp[i + 1][j][k][l] %= mod

for i in range(1, n + 1):
    ans += dp[n][i][i][0]
    ans %= mod

print(ans)
