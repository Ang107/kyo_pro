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
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x):
    return print(x)


def PY():
    return print("Yes")


def PN():
    return print("No")


def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LMII():
    return list(map(int, input().split()))


def is_not_Index_Er(x, y, h, w):
    return 0 <= x < h and 0 <= y < w  # 範囲外参照


n, m = MII()
A = [input().split() for _ in range(m)]
dp = [[inf] * (2**n) for _ in range(m + 1)]
# i個目までのクーポンの中で、集合jを無料にするときの必要クーポン枚数の最小値
dp[0][0] = 0

for i in range(1, m + 1):
    for j in range(2**n):
        # dont use
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        # use
        dp[i][int("".join(A[i - 1]), 2) | j] = min(
            dp[i][int("".join(A[i - 1]), 2) | j], dp[i - 1][j] + 1
        )
        print(dp)
        # for k in A[i-1]:
        #     if k == 1:

if dp[m][2**n - 1] == inf:
    print(-1)
else:
    print(dp[m][2**n - 1])
