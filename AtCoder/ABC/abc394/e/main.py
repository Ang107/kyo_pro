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

n = II()
c = [input() for _ in range(n)]
dp = [[1 << 60] * n for _ in range(n)]
ed = [[[] for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         for ii in range(n):
#             for jj in range(n):
#                 if c[i][j] == c[ii][jj] and c[i][j] != "-":
#                     ed[j][ii].append((i, jj))
deq = deque()
for i in range(n):
    dp[i][i] = 0
    deq.append((i, i))
for i in range(n):
    for j in range(n):
        if c[i][j] != "-":
            dp[i][j] = min(dp[i][j], 1)
            deq.append((i, j))
while deq:
    i, j = deq.popleft()
    for a in range(n):
        for b in range(n):
            if c[a][i] != "-" and c[a][i] == c[j][b] and dp[a][b] > dp[i][j] + 2:
                dp[a][b] = dp[i][j] + 2
                deq.append((a, b))
for i in range(n):
    for j in range(n):
        if dp[i][j] == (1 << 60):
            dp[i][j] = -1
for i in dp:
    print(*i)
