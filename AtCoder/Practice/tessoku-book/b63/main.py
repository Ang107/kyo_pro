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
sx, sy = MII()
sx -= 1
sy -= 1
gx, gy = MII()
gx -= 1
gy -= 1
c = [input() for _ in range(h)]
deq = deque()
visited = [[-1] * w for _ in range(h)]
visited[sx][sy] = 0
deq.append((sx, sy))
while deq:
    x, y = deq.popleft()
    for i, j in around4:
        nx = x + i
        ny = y + j
        if (
            nx in range(h)
            and ny in range(w)
            and visited[nx][ny] == -1
            and c[nx][ny] == "."
        ):
            deq.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
print(visited[gx][gy])
