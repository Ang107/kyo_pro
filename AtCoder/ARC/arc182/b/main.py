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
ans = []
t = II()
for _ in range(t):
    n, k = MII()
    # tmp = []
    # for i in range(k):
    #     tmp.append(1 << i)
    # def all_1(n):
    #     tmp = bin(n)[2:]
    #     return len(tmp) == tmp.count("1")
    i = 0
    rslt = []
    s = set()
    for i in range(n):
        tmp = 1 + (i << 1)
        tmp = bin(tmp)[2:]
        tmp = "0" * (k - len(tmp)) + tmp
        tmp = tmp[::-1]
        # print(tmp)
        if int(tmp, 2) == (1 << k) - 1:
            break
        r = int(tmp, 2)
        rslt.append(r)
        s.add(r)
    i = 2**k - 1
    while len(rslt) < n:
        if i <= 0:
            rslt.append(1)
        elif i not in s:
            rslt.append(i)
            s.add(i)
        i -= 1
    ans.append(" ".join(map(str, rslt)))
    tmp = set()
    for i in rslt:
        for j in range(k + 1):
            tmp.add(i // 2**j)
    # print(tmp)

for i in ans:
    print(i)
