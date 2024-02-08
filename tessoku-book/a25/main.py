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


h, w = MII()
c = [input() for _ in range(h)]

dp = [[0] * w for _ in range(h)]

dp[0][0] = 1


def bfs():
    visited = [[0] * w for _ in range(h)]
    deq = deque()
    deq.append((0, 0))
    visited[0][0] = 1
    while deq:
        x, y = deq.popleft()
        if x - 1 in range(h):
            dp[x][y] += dp[x - 1][y]
        if y - 1 in range(w):
            dp[x][y] += dp[x][y - 1]

        for i, j in [(1, 0), (0, 1)]:
            if (
                x + i in range(h)
                and y + j in range(w)
                and c[x + i][y + j] == "."
                and visited[x + i][y + j] == 0
            ):
                visited[x + i][y + j] = 1
                deq.append((x + i, y + j))


# print(dp)
bfs()
print(dp[h - 1][w - 1])
