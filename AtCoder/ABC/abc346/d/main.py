import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n = II()
s = list(map(int, list(input())))
c = LMII()

# i番目がjで、それまでに連続の部分がk個存在する場合のコストの最小値
dp = [[[inf] * 2 for _ in range(2)] for _ in range(n)]
dp[0][s[0]][0] = 0
dp[0][(s[0] + 1) % 2][0] = c[0]

for i in range(n - 1):
    if s[i + 1] == 0:
        # no change
        dp[i + 1][0][0] = min(dp[i + 1][0][0], dp[i][1][0])
        dp[i + 1][0][1] = min(dp[i + 1][0][1], dp[i][1][1])
        dp[i + 1][0][1] = min(dp[i + 1][0][1], dp[i][0][0])

        # change
        dp[i + 1][1][0] = min(dp[i + 1][1][0], dp[i][0][0] + c[i + 1])
        dp[i + 1][1][1] = min(dp[i + 1][1][1], dp[i][0][1] + c[i + 1])
        dp[i + 1][1][1] = min(dp[i + 1][1][1], dp[i][1][0] + c[i + 1])

    else:
        # no change
        dp[i + 1][1][0] = min(dp[i + 1][1][0], dp[i][0][0])
        dp[i + 1][1][1] = min(dp[i + 1][1][1], dp[i][0][1])
        dp[i + 1][1][1] = min(dp[i + 1][1][1], dp[i][1][0])

        # change
        dp[i + 1][0][0] = min(dp[i + 1][0][0], dp[i][1][0] + c[i + 1])
        dp[i + 1][0][1] = min(dp[i + 1][0][1], dp[i][1][1] + c[i + 1])
        dp[i + 1][0][1] = min(dp[i + 1][0][1], dp[i][0][0] + c[i + 1])

ans = inf
# pprint(dp)
ans = min(
    ans,
    dp[n - 1][0][1],
    dp[n - 1][1][1],
)
print(ans)
