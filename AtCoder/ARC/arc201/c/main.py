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

n = II()


dd = defaultdict(int)
cnt = [0] * 500001
cnt[0] = 1
child_cnt = defaultdict(int)
ans = 0
tmp = defaultdict(int)
used = set()
for _ in range(n):
    s = II()
    if s[-1] == "A":
        other = s[:-1] + "B"
    else:
        other = s[:-1] + "A"

    cnt[len(s)] += 1
    ans *= 2
    if cnt[len(s)] == 1 << len(s):
        ans += 1
    parent = s[:-1]
    tmp[s] = 1
    child_cnt[parent] += 1
    if parent in used:
        tmp[parent] = tmp[s] * tmp[other]
        if tmp[s] > 0 and tmp[other] > 0:
            tmp[parent] += 1

    used.add(s)
