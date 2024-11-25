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
# setrecursionlimit(10**7)
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
x = II()
for i in range(20):
    print(x * i ^ x)
t = II()
for _ in range(t):

    x, m = MII()
    ans = 0

    if m <= x:
        for y in range(1, m + 1):
            tmp = y ^ x
            if tmp % x == 0 or tmp % y == 0:
                ans += 1
        pass
    else:
        for y in range(1, x):
            tmp = y ^ x
            if tmp % x == 0 or tmp % y == 0:
                ans += 1
        syuki = 1 << len(bin(x)[2:])
        l = []
        for i in range(1, syuki + 1):
            l.append(x * i ^ x)
        k = x * syuki

        ans += syuki * (m // k + 1)
        i = syuki * (m // k + 1)
        cnt = 0
        # print(i, syuki)
        while cnt <= syuki:
            if x * i ^ x > m:
                ans -= 1
                cnt = 0
            else:
                cnt += 1
            i -= 1

    print(ans)


# for i in range(20):
#     print(i, bin(i)[2:])
