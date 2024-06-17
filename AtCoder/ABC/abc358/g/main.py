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

h, w, k = MII()
x, y = MII()
x -= 1
y -= 1
a = [LMII() for _ in range(h)]
dp = [[0] * w for _ in range(h)]


def bfs(x, y):
    deq = deque([(x, y, -1, -1)])
    visited = [[False] * w for _ in range(h)]
    visited[x][y] = True
    while deq:
        x, y, fx, fy = deq.popleft()
        for i, j in around4:
            if (
                x + i in range(h)
                and y + j in range(w)
                and visited[x + i][y + j] == False
            ):
                dp[x + i][y + j] = max(dp[x + i][y + j], dp[x][y] + a[x + i][y + j])
                deq.append((x + i, y + j, x, y))
                visited[x + i][y + j] = True


bfs(x, y)
# print(dp)
ans = 0
for i in range(h):
    for j in range(w):
        # print(dp[i][j], (k - (abs(x - i) + abs(y - j))))
        ans = max(ans, (k - (abs(x - i) + abs(y - j))) * a[i][j] + dp[i][j])
print(ans)
