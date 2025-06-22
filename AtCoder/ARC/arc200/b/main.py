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

"""
max(a1,a2) <= a3 <= a1+a2
l
a1 = l * p
a2 = l * q
a3 = l * p * q
p,qは互いに素
prime = [2,3,5,7, 11,23,53, 101,211,503, 1009,2003,5003, 10007,20011,50021, 100003,200003,500009, 1000003,2000003,5000011, 10000019,20000003, 50000017, 100000007,200000033, 500000003, 1000000007,2000000011,5000000029, 10000000019,20000000089,50000000021, 100000000003,200000000041,500000000023, 1000000000039,2000000000003,5000000000053, 10000000000037, 20000000000021,50000000000053, 100000000000031,200000000000027,500000000000057, 1000000000000037,2000000000000021,5000000000000023, 10000000000000061,20000000000000003,50000000000000051]
"""
prime = [
    2,
    3,
    5,
    7,
    11,
    23,
    53,
    101,
    211,
    503,
    1009,
    2003,
    5003,
    10007,
    20011,
    50021,
    100003,
    200003,
    500009,
    1000003,
    2000003,
    5000011,
    10000019,
    20000003,
    50000017,
    100000007,
    200000033,
    500000003,
    1000000007,
    2000000011,
    5000000029,
    10000000019,
    20000000089,
    50000000021,
    100000000003,
    200000000041,
    500000000023,
    1000000000039,
    2000000000003,
    5000000000053,
    10000000000037,
    20000000000021,
    50000000000053,
    100000000000031,
    200000000000027,
    500000000000057,
    1000000000000037,
    2000000000000021,
    5000000000000023,
    10000000000000061,
    20000000000000003,
    50000000000000051,
]
ans = [[[(-1, -1)] * 18 for _ in range(18)] for _ in range(18)]
for l in range(18):
    l = 10**l
    for m in range(18):
        m = 10**m
        for i in prime:
            for j in prime:
                lcm_ = lcm(l * i, m * j)
                a1 = len(str(l * i))
                a2 = len(str(m * j))
                a3 = len(str(lcm_))
                if max(a1, a2, a3) < 18:
                    ans[a1][a2][a3] = (l * i, m * j)

# for i in range(1, 18):
#     for j in range(1, 18):
#         for k in range(1, 18):
#             if ans[i][j][k] != (-1, -1):
#                 print(i, j, k, ans[i][j][k])
#             if max(i, j) <= k <= i + j:
#                 assert ans[i][j][k] != (-1, -1)
t = II()
for _ in range(t):
    i, j, k = MII()
    if ans[i][j][k] == (-1, -1):
        PN()
    else:
        PY()
        print(*ans[i][j][k])
