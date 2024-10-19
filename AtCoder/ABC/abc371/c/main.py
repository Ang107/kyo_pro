from sys import stdin, setrecursionlimit
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
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = II()
mg = II()
g = [[False] * n for _ in range(n)]
for _ in range(mg):
    u, v = LMII()
    u -= 1
    v -= 1
    g[u][v] = True
    g[v][u] = True
mh = II()
h = [[False] * n for _ in range(n)]
for _ in range(mh):
    u, v = LMII()
    u -= 1
    v -= 1
    h[u][v] = True
    h[v][u] = True
a = [LMII() for _ in range(n - 1)]
min_ans = inf

for p in permutations(range(n)):
    ans = 0
    nh = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nh[i][j] = h[p[i]][p[j]]

    for i in range(n):
        for j in range(i + 1, n):
            if g[i][j] != nh[i][j]:
                # print(i, j, a[i][j - i - 1])
                ii = p[i]
                jj = p[j]
                if ii > jj:
                    ii, jj = jj, ii

                ans += a[ii][jj - ii - 1]
    # if min_ans > ans:
    #     print(ans, p)
    # print(p, ans)
    min_ans = min(ans, min_ans)

print(min_ans)
