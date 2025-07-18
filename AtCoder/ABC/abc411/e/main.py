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
a = [deque(sorted(LMII())) for _ in range(n)]
values = set()
idxs = defaultdict(set)
for i in range(n):
    for j in a[i]:
        idxs[j].add(i)
        values.add(j)
den = [-1] * 7
for i in range(1, 7):
    den[i] = pow(i, -1, mod)
values = sorted(values)
cnt = 0
p = [1]
ans = 0
for i in values:
    p.append(p[-1])
    if cnt < n:
        p[-2] = 0
    for j in idxs[i]:
        before_len = len(a[j])
        while a[j] and a[j][0] == i:
            a[j].popleft()
        after_len = len(a[j])
        if before_len == 6:
            cnt += 1
        else:
            p[-1] *= 6 * den[(6 - before_len)]
            p[-1] %= mod
        p[-1] *= (6 - after_len) * den[6]
        p[-1] %= mod
    if cnt == n:
        if len(p) == 2:
            ans += i * p[-1]
            ans %= mod
        else:
            ans += i * (p[-1] - p[-2])
            ans %= mod
# print(p)
print(ans)
