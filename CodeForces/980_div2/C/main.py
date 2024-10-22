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
# setrecursionlimit(10**7)
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


t = II()
ans = []
import random

xor = random.randrange(1 << 63)
for _ in range(t):
    n = II()
    a = [LMII() for _ in range(n)]
    tmp = set()
    for i in range(n):
        for j in range(2):
            tmp.add(a[i][j])
    tmp = sorted(tmp)
    d = {}
    for i in range(len(tmp)):
        d[tmp[i] ^ xor] = i

    a.sort(key=lambda x: d[x[0] ^ xor] + d[x[1] ^ xor])
    # for x in a:
    #     print(d[x[0]] + d[x[1]])
    # print(a)
    # print(d)
    res = []
    for i in a:
        for j in i:
            res.append(j)
    ans.append(res)
    pass
for i in ans:
    print(*i)
