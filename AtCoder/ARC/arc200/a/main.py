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
import random
import time

t = II()
for _ in range(t):
    n = II()
    a = LMII()
    b = LMII()
    ab = [(i, j, idx) for idx, (i, j) in enumerate(zip(a, b))]

    tmp1 = max(ab, key=lambda x: x[1] / x[0])
    tmp2 = max(ab, key=lambda x: x[0] / x[1])
    ai, bi, idxi = tmp1
    aj, bj, idxj = tmp2
    if aj * bi <= ai * bj:
        print("No")
        continue
    ans = [0] * n
    # bj/bi < -p/q < aj/ai
    start_t = time.perf_counter()
    while time.perf_counter() - start_t < 3 / t:
        rnd = random.uniform(bj / bi, aj / ai)
        q = random.randrange(1, min(10**8, floor(10**8 // rnd)) + 1)
        if random.randrange(2):
            p = floor(rnd * q)
        else:
            p = ceil(rnd * q)
        if bj / bi < p / q < aj / ai:
            break
    if not (bj / bi < p / q < aj / ai):
        print("No")
        continue
    print("Yes")

    p = -p
    ans[idxi] = p
    ans[idxj] = q
    print(*ans)
    sum_a = 0
    sum_b = 0
    for i, j, k in zip(a, b, ans):
        sum_a += i * k
        sum_b += j * k
    # print(sum_a, sum_b)
    assert sum_a > 0 and sum_b < 0
