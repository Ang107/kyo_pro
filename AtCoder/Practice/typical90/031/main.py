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
# 白石がi青石がjになるときのgrudy数
dp = [[-1] * 1326 for _ in range(51)]

dp[0][0] = 0
for w in range(51):
    for b in range(1326):
        cand = set()
        if w >= 1 and b + w < 1326:
            cand.add(dp[w - 1][b + w])
        if b >= 2:
            for k in range(1, b // 2 + 1):
                cand.add(dp[w][b - k])
        for i in range(60):
            if i not in cand:
                res = i
                break
        dp[w][b] = res
n = II()
w = LMII()
b = LMII()
xor = 0
for i, j in zip(w, b):
    xor ^= dp[i][j]
if xor == 0:
    print("Second")
else:
    print("First")
