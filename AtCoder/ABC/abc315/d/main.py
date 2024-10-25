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

h, w = MII()
c = [list(input()) for _ in range(h)]
cnt_h = [[0] * h for _ in range(26)]
cnt_w = [[0] * w for _ in range(26)]
for i in range(h):
    for j in range(w):
        a = ord(c[i][j]) - ord("a")
        cnt_h[a][i] += 1
        cnt_w[a][j] += 1
change = True
height = h
width = w
delled_h = [False] * h
delled_w = [False] * w
while change:
    change = False
    for i in range(h):
        if delled_h[i]:
            continue
        for c in range(26):
            if cnt_h[c][i] == width and width >= 2:
                change = True
                height -= 1
                delled_h[i] = True
                cnt_h[c][i] = 0
                for j in range(w):
                    cnt_w[c][j] -= 1
                    if cnt_w[c][j] == height == 1:
                        cnt_w[c][j] = 0
                        width -= 1
                        delled_w[j] = True

    for j in range(w):
        if delled_w[j]:
            continue
        for c in range(26):
            if cnt_w[c][j] == height and height >= 2:
                change = True
                width -= 1
                delled_w[j] = True
                cnt_w[c][j] = 0
                for i in range(h):
                    cnt_h[c][i] -= 1
                    if cnt_h[c][i] == width == 1:
                        cnt_h[c][i] = 0
                        height -= 1
                        delled_h[i] = True
# print(height, width)
print(height * width)
