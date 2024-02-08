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
s = [input() for _ in range(n)]
P = []
# ed = [
#     [[[set() for i in range(n)] for i in range(n)] for i in range(n)] for i in range(n)
# ]
# for i in range(n):
#     for j in range(n):
#         for p in range(n):
#             for q in range(n):
#                 if s[i][j] == "P" and s[p][q] == "P" and (i, j) != (p, q):
#                     P = i, j, p, q
#                 for a, b in around4:
#                     x1, y1, x2, y2 = i, j, p, q
#                     if (
#                         i + a in range(n)
#                         and j + b in range(n)
#                         and s[i + a][j + b] != "#"
#                     ):
#                         x1 += a
#                         y1 += b
#                     if (
#                         p + a in range(n)
#                         and q + b in range(n)
#                         and s[p + a][q + b] != "#"
#                     ):
#                         x2 += a
#                         y2 += b
#                     ed[i][j][p][q].add((x1, y1, x2, y2))
#                     x1, y1, x2, y2 = i, j, p, q


# pprint(ed)


def bfs():
    deq = deque()
    visited = dlist(n, n, n, n, fill=-1)
    P = []
    for i in range(n):
        for j in range(n):
            if s[i][j] == "P":
                P.extend((i, j))
    deq.append(P)
    x1, y1, x2, y2 = P
    visited[x1][y1][x2][y2] = 0
    while deq:
        # print(visited)

        x1, y1, x2, y2 = deq.popleft()
        if (x1, y1) == (x2, y2):
            print(visited[x1][y1][x2][y2])
            exit()
        # print(x1, y1, x2, y2)
        # pprint(ed[x1][y1][x2][y2])
        for a, b in around4:
            i, j, p, q = x1, y1, x2, y2
            if i + a in range(n) and j + b in range(n) and s[i + a][j + b] != "#":
                i += a
                j += b
            if p + a in range(n) and q + b in range(n) and s[p + a][q + b] != "#":
                p += a
                q += b

            if visited[i][j][p][q] == -1:
                deq.append((i, j, p, q))
                visited[i][j][p][q] = visited[x1][y1][x2][y2] + 1


# print(ed[0][0][0][0])
bfs()
print(-1)
