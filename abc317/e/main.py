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


h, w = MII()
a = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if a[i][j] == "S":
            sx, sy = i, j
        elif a[i][j] == "G":
            gx, gy = i, j
        elif a[i][j] == ">":
            tmp = j + 1
            while 0 <= tmp < w and (a[i][tmp] == "." or a[i][tmp] == "*"):
                a[i][tmp] = "*"
                tmp += 1

        elif a[i][j] == "<":
            tmp = j - 1
            while 0 <= tmp < w and (a[i][tmp] == "." or a[i][tmp] == "*"):
                a[i][tmp] = "*"
                tmp -= 1

        elif a[i][j] == "v":
            tmp = i + 1
            while 0 <= tmp < h and (a[tmp][j] == "." or a[tmp][j] == "*"):
                a[tmp][j] = "*"
                tmp += 1

        elif a[i][j] == "^":
            tmp = i - 1
            while 0 <= tmp < h and (a[tmp][j] == "." or a[tmp][j] == "*"):
                a[tmp][j] = "*"
                tmp -= 1
# for i in a:
#     print(*i)


def bfs():
    deq = deque()
    visited = [[-1] * w for _ in range(h)]
    deq.append((sx, sy))
    visited[sx][sy] = 0
    while deq:
        x, y = deq.popleft()
        for i, j in around4:
            if (
                x + i in range(h)
                and y + j in range(w)
                and (a[x + i][y + j] == "." or a[x + i][y + j] == "G")
                and visited[x + i][y + j] == -1
            ):
                visited[x + i][y + j] = visited[x][y] + 1
                deq.append((x + i, y + j))
    # for i in visited:
    #     print(*i)
    return visited[gx][gy]


print(bfs())
