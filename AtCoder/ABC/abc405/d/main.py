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
deq = deque()
visited = [[False] * w for _ in range(h)]
# frm = [[-1] * w for _ in range(h)]
ans = [list(i) for i in s]
for i in range(h):
    for j in range(w):
        if s[i][j] == "E":
            deq.append((i, j))
            visited[i][j] = True
vec = "v^><"
while deq:
    x, y = deq.popleft()
    for idx, (dx, dy) in enumerate(dxy4):
        nx = x + dx
        ny = y + dy
        if (
            nx in range(h)
            and ny in range(w)
            and s[nx][ny] == "."
            and visited[nx][ny] == False
        ):
            deq.append((nx, ny))
            visited[nx][ny] = True
            ans[nx][ny] = vec[idx]
for i in ans:
    print("".join(i))
