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
a = LMII()

dp = [inf] * (n + 1)
dp[0] = 0
dp[1] = min(a[0], a[-1])
for i in range(2, n + 1):
    # dp[i] = min(dp[i + 1], dp[i - 1] + a[i - 1])
    # if i >= 2:
    dp[i] = min(dp[i], dp[i - 1] + a[i - 1], dp[i - 2] + a[i - 2])
    # else:
    #     dp[i] = a[0]
print(dp)
dp_ano = dp[:]

dp = [inf] * (n + 1)
dp[0] = 0
dp[1] = 0
dp[2] = min(a[0], a[1])
for i in range(3, n):
    dp[i] = min(dp[i], dp[i - 1] + a[i - 1], dp[i - 2] + a[i - 2])

print(dp)

# print(dp_0[-1], dp[-1] + a[-1])
print(min(dp_ano[-1], dp_ano[-2] + a[-1], dp[-2] + a[-1]))
