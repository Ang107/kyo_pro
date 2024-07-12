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
    n, m, k = MII()
    a = "L" + input() + "L"
    # i地点にいる時に、水中に存在した時間の最小値
    dp = [inf] * (n + 2)
    dp[0] = 0
    for i in range(n + 1):

        if dp[i] > k:
            continue

        if a[i] == "L":
            for j in range(m + 1):
                if i + j >= n + 2:
                    continue

                if a[i + j] == "L":
                    dp[i + j] = min(dp[i + j], dp[i])
                elif a[i + j] == "W":
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        elif a[i] == "W":
            if a[i + 1] == "L":
                dp[i + 1] = min(dp[i + 1], dp[i])
            elif a[i + 1] == "W":
                dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    # print(dp)
    if dp[-1] <= k:
        ans.append("Yes")
    else:
        ans.append("No")
    pass
for i in ans:
    print(i)
