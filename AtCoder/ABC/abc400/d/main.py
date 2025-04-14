from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

h, w = MII()
s = [input() for _ in range(h)]
a, b, c, d = [i - 1 for i in LMII()]

deq = deque()
deq.append((a, b))
visited = [[inf] * w for _ in range(h)]
visited[a][b] = 0

while deq:
    x, y = deq.popleft()
    for i, j in dxy4:
        nx = x + i
        ny = y + j
        if (
            nx in range(h)
            and ny in range(w)
            and s[nx][ny] == "."
            and visited[nx][ny] > visited[x][y]
        ):
            deq.appendleft((nx, ny))
            visited[nx][ny] = visited[x][y]
    for i, j in dxy4:
        nx = x + i
        ny = y + j
        if nx in range(h) and ny in range(w) and visited[nx][ny] > visited[x][y] + 1:
            deq.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
        nx += i
        ny += j
        if nx in range(h) and ny in range(w) and visited[nx][ny] > visited[x][y] + 1:
            deq.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
print(visited[c][d])
