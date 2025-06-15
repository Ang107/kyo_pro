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


# 転置
def tenti(l):
    return [list(i) for i in zip(*l)]


t = II()
for _ in range(t):
    h, w = MII()
    s = [list(input()) for _ in range(h)]
    if h > w:
        h, w = w, h
        s = tenti(s)

    imos = [[0] * (w + 1) for _ in range(h + 1)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                imos[i + 1][j + 1] = 1
            else:
                imos[i + 1][j + 1] = -1
    for i in range(h + 1):
        for j in range(w):
            imos[i][j + 1] += imos[i][j]

    for i in range(h):
        for j in range(w + 1):
            imos[i + 1][j] += imos[i][j]

    def get(a, b, c, d):
        assert a <= c
        assert b <= d
        res = 0
        res += imos[c + 1][d + 1]
        res += imos[a][b]
        res -= imos[a][d + 1]
        res -= imos[c + 1][b]
        return res

    ans = 0

    for i in range(h):
        for j in range(i, h):
            tmp = defaultdict(int)
            tmp[0] += 1
            for k in range(w):
                tmp[get(i, 0, j, k)] += 1
            for key, k in tmp.items():
                ans += k * (k - 1) // 2
                print(key, k)

    print(ans)
