import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def solve():
    visited = [[0] * w for i in range(h)]
    # print(visited, h, w)
    que = deque()
    que.append((0, 0))
    visited[0][0] = 1
    while que:
        x, y = que.popleft()
        for idx, (i, j) in enumerate(around4):
            nx = x + i
            ny = y + j
            if idx == 0:
                if nx > 0 and ww[x - 1][y] == 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
            elif idx == 1:
                # print(nx < h - 1, ww[nx][ny] == 0, visited[nx][ny], x, y)
                if x < h - 1 and ww[x][y] == 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

            elif idx == 2:
                if y > 0 and wh[x][y - 1] == 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
            else:
                if y < w - 1 and wh[x][y] == 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    # print(visited)
    return visited[-1][-1]


ans = []

while 1:
    w, h = MII()
    if h == w == 0:
        break
    wh = []
    ww = []
    for i in range(h * 2 - 1):
        if i % 2 == 0:
            wh.append(LMII())
        else:
            ww.append(LMII())
    # for i in wh:
    #     print(i)
    # print()
    # for i in ww:
    #     print(i)
    ans.append(solve())

for i in ans:
    print(i)
