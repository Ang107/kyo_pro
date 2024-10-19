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

n, m, q = MII()
dis = [[inf] * n for _ in range(n)]
for i in range(n):
    dis[i][i] = 0
abc = [LMII() for _ in range(m)]
for i in range(m):
    abc[i][0] -= 1
    abc[i][1] -= 1
querys = []
for _ in range(q):
    tmp = LMII()
    if tmp[0] == 1:
        tmp[1] -= 1
    else:
        tmp[1] -= 1
        tmp[2] -= 1
    querys.append(tmp)
out = set()
for i in querys:
    if i[0] == 1:
        out.add(i[1])
for i in range(m):
    if i not in out:
        a, b, c = abc[i]
        dis[a][b] = min(dis[a][b], c)
        dis[b][a] = min(dis[b][a], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
# print(dis)
ans = []
for q in querys[::-1]:
    if q[0] == 1:
        i = q[1]
        a, b, c = abc[i]
        for i in range(n):
            for j in range(n):
                dis[i][j] = min(
                    dis[i][j], dis[i][a] + c + dis[b][j], dis[i][b] + c + dis[a][j]
                )
        # print(dis)
    else:
        x, y = q[1:]
        if dis[x][y] == inf:
            ans.append(-1)
        else:
            ans.append(dis[x][y])
for i in ans[::-1]:
    print(i)
