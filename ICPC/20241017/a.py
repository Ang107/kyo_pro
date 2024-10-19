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
import inspect

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


def solve(n, sx, sy, gx, gy, xyr: list[list[int]]):
    # 初期スポーン位置を含むセンサーは最初に壊す

    side_wall = [[0] * 1010 for _ in range(1010)]
    vertical_wall = [[0] * 1010 for _ in range(1010)]
    cost = 0
    for x, y, r in xyr:
        left = max(0, x - r)
        right = min(1000, x + r)
        up = max(0, y - r)
        down = min(1000, y + r)
        if left <= sx <= right and up <= sy <= down:
            cost += 1
        # print(left, right, up, down)
        if sx < gx:
            side_wall[left][up] += 1
            side_wall[left][down + 1] -= 1
        else:
            side_wall[right][up] += 1
            side_wall[right][down + 1] -= 1
        if sy < gy:
            vertical_wall[left][up] += 1
            vertical_wall[right + 1][up] -= 1
        else:
            vertical_wall[left][down] += 1
            vertical_wall[right + 1][down] -= 1

    for i in range(1010):
        side_wall[i] = list(accumulate(side_wall[i]))
    for i in range(1009):
        for j in range(1010):
            vertical_wall[i + 1][j] += vertical_wall[i][j]

    dp = [[inf] * 1010 for _ in range(1010)]
    dp[sx][sy] = cost
    deq = deque()
    deq.append((sx, sy))
    # cnt = 0
    while deq:
        # # print(deq)
        # cnt += 1

        x, y = deq.popleft()
        if x > 1000 or y > 1000 or x < 0 or y < 0:
            continue
        if sx < gx:
            if dp[x + 1][y] == inf:
                deq.append((x + 1, y))
            dp[x + 1][y] = min(dp[x + 1][y], dp[x][y] + side_wall[x + 1][y])

        elif sx > gx:
            if dp[x - 1][y] == inf:
                deq.append((x - 1, y))
            dp[x - 1][y] = min(dp[x - 1][y], dp[x][y] + side_wall[x - 1][y])
        if sy < gy:
            if dp[x][y + 1] == inf:
                deq.append((x, y + 1))
            dp[x][y + 1] = min(dp[x][y + 1], dp[x][y] + vertical_wall[x][y + 1])
        elif sy > gy:
            if dp[x][y - 1] == inf:
                deq.append((x, y - 1))
            dp[x][y - 1] = min(dp[x][y - 1], dp[x][y] + vertical_wall[x][y - 1])
    # print(dp[gx][gy])
    # for i in range(10):
    #     print(dp[i][:10])
    return dp[gx][gy]

    # for i in range(10):
    #     print(side_wall[i][:10])
    # for i in range(10):
    #     print(vertical_wall[i][:10])


ans = []

while 1:
    n = II()
    if n == 0:
        break
    sx, sy, gx, gy = MII()
    xyr = [LMII() for _ in range(n)]
    ans.append(solve(n, sx, sy, gx, gy, xyr))
    pass


for i in ans:
    print(i)
