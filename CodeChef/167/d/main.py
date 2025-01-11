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

t = II()
anss = []
for _ in range(t):
    n = II()
    a = LMII()
    plus = deque()
    minus = deque()
    for index, i in enumerate(a):
        if i > 0:
            plus.append([index, i])
        elif i < 0:
            minus.append([index, -i])
    ans = 0
    while plus:
        # print(plus, minus)
        p = plus[0][1]
        m = minus[0][1]
        dis = abs(plus[0][0] - minus[0][0])
        min_ = min(p, m)
        ans += min_ * dis
        plus[0][1] -= min_
        minus[0][1] -= min_
        if plus[0][1] == 0:
            plus.popleft()
        if minus[0][1] == 0:
            minus.popleft()
    anss.append(ans)
for ans in anss:
    print(ans)
