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

n, m = MII()
ab = [[i - 1 for i in LMII()] for _ in range(m)]
ans = m * (m - 1) // 2
# if n % 2 == 0:
#     cnt1 = [0] * n // 2
#     cnt2 = [0] * n // 2
# else:
cnt = [0] * n
for a, b in ab:
    # if n % 2 == 0:
    #     if (a + b) % 2 == 0:
    #         cnt1[(a + b) // 2 % (n // 2)] += 1
    #     else:
    #         cnt2[(a + b) // 2 % (n // 2)] += 1
    # else:
    cnt[(a + b) % n] += 1
for i in cnt:
    ans -= i * (i - 1) // 2
print(ans)
