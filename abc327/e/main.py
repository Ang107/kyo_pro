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
p = LMII()
# i番目のコンテストまでに、j回出場したときのその時点でのレートの最大値
dp = [[-inf] * 5010 for _ in range(5010)]

dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(0, 5001):
        # rated
        dp[i][j + 1] = max(dp[i][j + 1], dp[i - 1][j] * 0.9 + p[i - 1])
        # unrated
        dp[i][j] = max(dp[i][j], dp[i - 1][j])
ans = -inf
bunbo = [1]
for i in range(1, 5002):
    bunbo.append(bunbo[-1] + 0.9**i)
# print(bunbo)
for i in range(1, 5001):
    ans = max(ans, dp[n][i] / bunbo[i - 1] - 1200 / i**0.5)
print(ans)
