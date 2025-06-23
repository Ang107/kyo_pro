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
    abc = [LMII() for _ in range(n)]
    cnt = [0, 0]
    # (合計の最大値, ハードの最大値, イージーの最大値)
    tmp = []
    for a, b, c in abc:
        if a + c <= b:
            cnt[0] += a
            cnt[1] += c
        else:
            tmp.append((b, min(a, b), min(c, b)))
    # div1重視
    for sum_max, a_max, c_max in tmp:
        cnt[0] += a_max
        cnt[1] += sum_max - a_max

    # div2に調整
    for sum_max, a_max, c_max in tmp:
        if cnt[0] > cnt[1]:
            diff = cnt[0] - cnt[1]
            c = min(a_max, c_max - (sum_max - a_max), diff // 2)
            cnt[0] -= c
            cnt[1] += c
    print(min(cnt))
