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


def solve(n, w, d, ps: list[list[int]]):
    b = [[0] * w for _ in range(d)]
    for index, (p, s) in enumerate(ps, start=1):
        p -= 1
        minx, miny = inf, inf
        maxx, maxy = -inf, -inf
        for i in range(d):
            for j in range(w):
                if b[i][j] == p:
                    minx = min(minx, i)
                    miny = min(miny, j)
                    maxx = max(maxx, i)
                    maxy = max(maxy, j)
                elif b[i][j] > p:
                    b[i][j] -= 1
        width = maxy - miny + 1
        height = maxx - minx + 1
        s %= (width + height) * 2
        if 0 < s < width:
            if s <= width - s:
                for x in range(minx, maxx + 1):
                    for y in range(miny + s, maxy + 1):
                        b[x][y] = index
                for x in range(minx, maxx + 1):
                    for y in range(miny, miny + s):
                        b[x][y] = index - 1
            else:
                for x in range(minx, maxx + 1):
                    for y in range(miny, miny + s):
                        b[x][y] = index
                for x in range(minx, maxx + 1):
                    for y in range(miny + s, maxy + 1):
                        b[x][y] = index - 1

        elif width < s < width + height:
            s -= width
            if s >= height - s:
                for x in range(minx, minx + s):
                    for y in range(miny, maxy + 1):
                        b[x][y] = index
                for x in range(minx + s, maxx + 1):
                    for y in range(miny, maxy + 1):
                        b[x][y] = index - 1
            else:
                for x in range(minx + s, maxx + 1):
                    for y in range(miny, maxy + 1):
                        b[x][y] = index
                for x in range(minx, minx + s):
                    for y in range(miny, maxy + 1):
                        b[x][y] = index - 1

        elif width + height < s < width * 2 + height:
            s -= width + height
            s = width - s
            if s <= width - s:
                for x in range(minx, maxx + 1):
                    for y in range(miny + s, maxy + 1):
                        b[x][y] = index
                for x in range(minx, maxx + 1):
                    for y in range(miny, miny + s):
                        b[x][y] = index - 1
            else:
                for x in range(minx, maxx + 1):
                    for y in range(miny, miny + s):
                        b[x][y] = index
                for x in range(minx, maxx + 1):
                    for y in range(miny + s, maxy + 1):
                        b[x][y] = index - 1

        elif width * 2 + height < s < width * 2 + height * 2:
            s -= width * 2 + height
            s = height - s
            if s >= height - s:
                for x in range(minx, minx + s):
                    for y in range(miny, maxy + 1):
                        b[x][y] = index
                for x in range(minx + s, maxx + 1):
                    for y in range(miny, maxy + 1):
                        b[x][y] = index - 1
            else:
                for x in range(minx + s, maxx + 1):
                    for y in range(miny, maxy + 1):
                        b[x][y] = index
                for x in range(minx, minx + s):
                    for y in range(miny, maxy + 1):
                        b[x][y] = index - 1
        # print(index)
        # for i in range(d):
        #     print(b[i])

    s = [0] * (n + 1)
    # print(b)
    for i in range(d):
        for j in range(w):
            s[b[i][j]] += 1
    return " ".join(map(str, sorted(s)))

    # 処理を記入
    pass


ans = []
if 1:
    while 1:
        # 入力を記入
        n, w, d = MII()
        if n == w == d == 0:
            break
        ps = [LMII() for _ in range(n)]
        ans.append(solve(n, w, d, ps))
        pass

    for i in ans:
        print(i)
else:
    import random

    while 1:
        n = random.randrange(10)
        w = random.randrange(1, 10)
        d = random.randrange(1, 10)
    ps = []
    for i in range(n):
        p = random.randrange(1, i + 2)
        s = random.randrange(1, 1001)
        ps.append((p, s))
    r1 = solve(n, w, d, ps)
