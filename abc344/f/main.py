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


n = II()
p = [LMII() for _ in range(n)]
r = [LMII() for _ in range(n)]
d = [LMII() for _ in range(n - 1)]


deq = deque()
deq.append((0, 0, p[0][0], 0, 0))
visited = [[inf] * n for _ in range(n)]
visited[0][0] = 0

while deq:
    x, y, max_p, zankin, num = deq.popleft()

    if visited[x][y] < num:
        continue

    i, j = 0, 1
    if x + i in range(n) and y + j in range(n):
        tmp = math.ceil((r[x][y] - zankin) / max_p)
        if r[x][y] - zankin >= 0:
            zankin = (r[x][y] - zankin) % max_p
        else:
            zankin -= r[x][y]

        if visited[x + i][y + j] > visited[x][y] + tmp + 1:
            deq.append(
                (
                    x + i,
                    y + j,
                    max(
                        max_p,
                        p[x + i][y + j],
                    ),
                    zankin,
                    visited[x][y] + tmp + 1,
                )
            )
            visited[x + i][y + j] = visited[x][y] + tmp + 1

    i, j = 1, 0
    if x + i in range(n) and y + j in range(n):
        tmp = math.ceil((d[x][y] - zankin) / max_p)
        if (d[x][y] - zankin) >= 0:
            zankin = (d[x][y] - zankin) % max_p
        else:
            zankin -= d[x][y]

        if visited[x + i][y + j] > visited[x][y] + tmp + 1:
            deq.append(
                (
                    x + i,
                    y + j,
                    max(
                        max_p,
                        p[x + i][y + j],
                    ),
                    zankin,
                    visited[x][y] + tmp + 1,
                )
            )
            visited[x + i][y + j] = visited[x][y] + tmp + 1

print(visited[n - 1][n - 1])
