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


t = input()
n = II()
s = []
for i in range(n):
    tmp = input().split()
    s.append(tmp[1:])

# i個目まででj文字目までにかかるお金の最小値
dp = [[inf] * (len(t) + 1) for i in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(0, len(t) + 1):
        for k in s[i - 1]:
            # use
            # print(k, t[j : j + len(k)])
            if k == t[j : j + len(k)]:
                dp[i][j + len(k)] = min(dp[i][j + len(k)], dp[i - 1][j] + 1)
            # not use

            dp[i][j] = min(dp[i][j], dp[i - 1][j])

# print(dp)
if dp[n][len(t)] == inf:
    print(-1)
else:
    print(dp[n][len(t)])
