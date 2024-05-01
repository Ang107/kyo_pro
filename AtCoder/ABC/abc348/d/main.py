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


h, w = MII()
a = [input() for _ in range(h)]
n = II()
E = [[None] * w for _ in range(h)]
for i in range(n):
    r, c, e = MII()
    r -= 1
    c -= 1
    E[r][c] = e


for i in range(h):
    for j in range(w):
        if a[i][j] == "S":
            S = (i, j)
        if a[i][j] == "T":
            T = (i, j)


def bfs():
    deq = deque()
    deq.append((S[0], S[1], 0))
    visited = [[-100] * w for _ in range(h)]
    visited[S[0]][S[1]] = 0
    while deq:

        x, y, p = deq.popleft()
        if p < visited[x][y]:
            continue
        if E[x][y] != None:
            visited[x][y] = max(visited[x][y], E[x][y])
            E[x][y] = None
        # pprint(visited)
        # pprint(E)
        for i, j in around4:
            if (
                x + i in range(h)
                and y + j in range(w)
                and visited[x + i][y + j] < visited[x][y] - 1
                and a[x + i][y + j] != "#"
                and visited[x][y] > 0
            ):
                visited[x + i][y + j] = max(visited[x + i][y + j], visited[x][y] - 1)
                deq.append((x + i, y + j, visited[x + i][y + j]))
                if a[x + i][y + j] == "T":
                    return True
    return False


# pprint(visited)
ans = bfs()
if ans:
    PY()
else:
    PN()
