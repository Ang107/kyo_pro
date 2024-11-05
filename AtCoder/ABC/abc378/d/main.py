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
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

h, w, k = MII()

s = [input() for _ in range(h)]
visited = []

# import time

# st = time.perf_counter()


def f(x, y):
    if len(visited) == k + 1:
        # print(visited)
        return 1
    cnt = 0
    for i, j in dxy4:
        nx = x + i
        ny = y + j
        if (
            nx in range(h)
            and ny in range(w)
            and s[nx][ny] == "."
            and (nx, ny) not in visited
        ):
            visited.append((nx, ny))
            cnt += f(nx, ny)
            visited.pop()
    return cnt


# h = 10
# w = 10
# k = 11
# s = ["." * 10 for _ in range(10)]
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            visited = [(i, j)]
            ans += f(i, j)
            # print(f(i, j))
print(ans)
# print(time.perf_counter() - st)
