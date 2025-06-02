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
for _ in range(t):
    n = II()
    s = input()
    cnt1l = [0]
    cnt1r = [0]
    cnt0r = [0]
    for i in s:
        cnt1l.append(cnt1l[-1])
        if i == "1":
            cnt1l[-1] += 1
    for i in reversed(s):
        cnt0r.append(cnt0r[-1])
        cnt1r.append(cnt1r[-1])
        if i == "0":
            cnt0r[-1] += 1
        else:
            cnt1r[-1] += 1
    cnt0r = cnt0r[::-1]
    cnt1r = cnt1r[::-1]
    ans = inf
    best = inf
    for i in range(n + 1):
        best = min(best, cnt1l[i] + cnt0r[i])
        ans = min(ans, cnt1r[i] + best - cnt0r[i])
    print(ans)
