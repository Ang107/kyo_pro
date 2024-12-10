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
a = LMII()
na = []
tmp = []
for i in a:
    if tmp and tmp[-1] != i:
        na.append(tmp)
        tmp = [i]
    else:
        tmp.append(i)
if tmp:
    na.append(tmp)

d = defaultdict(int)
d[1] = 0
d[3] = 1
for i in range(5, 200000 + 1, 2):
    d[i] = d[i - 2] * (i - 2) % mod
kaizyou = [1]
for i in range(1, 200001):
    kaizyou.append(kaizyou[-1] * i % mod)
kaizyou_inv = []
for i in kaizyou:
    kaizyou_inv.append(pow(i, -1, mod))
ans = 1
cnt = 0
if n == 1:
    if a[0] == 1:
        print(1)
        exit()
    else:
        print(0)
        exit()

for index, i in enumerate(na):
    if len(i) % 2 == 0:
        print(0)
        exit()
    if len(i) == 1 and index % 2 == i[0]:
        print(0)
        exit()

    if len(i) == 1:
        continue
    ans *= d[len(i)]
    ans %= mod
    ans *= kaizyou_inv[len(i) // 2]
    ans %= mod
    cnt += len(i) // 2
ans *= kaizyou[cnt]
ans %= mod
print(ans)
