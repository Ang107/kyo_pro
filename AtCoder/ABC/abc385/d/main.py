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

n, m, sx, sy = MII()
X = defaultdict(list)
Y = defaultdict(list)
for _ in range(n):
    x, y = MII()
    X[x].append(y)
    Y[y].append(x)
for i in X:
    X[i].sort()
for i in Y:
    Y[i].sort()
iX = defaultdict(list)
iY = defaultdict(list)
for k, v in X.items():
    iX[k] = [0] * (len(v) + 1)
for k, v in Y.items():
    iY[k] = [0] * (len(v) + 1)
x, y = sx, sy
for _ in range(m):
    d, c = input().split()
    c = int(c)
    if d == "U":
        p = y
        q = y + c
        y += c
        if x in X:
            pp = bisect_left(X[x], p)
            qq = bisect_right(X[x], q)
            iX[x][pp] += 1
            iX[x][qq] -= 1
    elif d == "D":
        p = y - c
        q = y
        y -= c
        if x in X:
            pp = bisect_left(X[x], p)
            qq = bisect_right(X[x], q)
            iX[x][pp] += 1
            iX[x][qq] -= 1
    if d == "L":
        p = x - c
        q = x
        x -= c
        if y in Y:
            pp = bisect_left(Y[y], p)
            qq = bisect_right(Y[y], q)
            iY[y][pp] += 1
            iY[y][qq] -= 1
    elif d == "R":
        p = x
        q = x + c
        x += c
        if y in Y:
            pp = bisect_left(Y[y], p)
            qq = bisect_right(Y[y], q)
            iY[y][pp] += 1
            iY[y][qq] -= 1
ans = set()
for i in iX:
    iX[i] = list(accumulate(iX[i]))
for i in iY:
    iY[i] = list(accumulate(iY[i]))
for k, v in X.items():
    for j in range(len(v)):
        if iX[k][j] > 0:
            ans.add((k, v[j]))
for k, v in Y.items():
    for j in range(len(v)):
        if iY[k][j] > 0:
            ans.add((v[j], k))
print(x, y, len(ans))
