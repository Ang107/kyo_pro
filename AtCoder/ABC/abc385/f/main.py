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
import decimal

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
xh = [tuple(LMII()) for _ in range(n)]
xh.sort(key=lambda x: x[0])
ans = -inf
for i in range(n - 1):
    x, h = xh[i]
    b = ((xh[i + 1][0] - xh[i][0]) * h - (xh[i + 1][1] - xh[i][1]) * x) / (
        xh[i + 1][0] - xh[i][0]
    )
    ans = max(ans, b)
if ans < 0:
    ans = -1
print(ans)
# tmp = [h / x for x, h in xh]
# if tmp == sorted(tmp) and len(set(tmp)) == n:
#     print(-1)
#     exit()

# ans = -inf
# max_ = -inf
# maxx, maxh = -inf, -inf
# tmp = deque()
# tmp.append(xh[0])

# for x, h in xh[1:]:
#     while len(tmp) >= 2:
#         if decimal.Decimal(h - tmp[0][1]) / decimal.Decimal(
#             x - tmp[0][0]
#         ) <= decimal.Decimal(h - tmp[1][1]) / decimal.Decimal(x - tmp[1][0]):
#             tmp.popleft()
#         else:
#             break
#     b = decimal.Decimal(h) - decimal.Decimal((h - tmp[0][1]) * x) / decimal.Decimal(
#         (x - tmp[0][0])
#     )
#     ans = max(ans, b)
#     if tmp[0][1] <= h:
#         tmp = deque()
#         tmp.append((x, h))
#     else:
#         tmp.append((x, h))
# if ans < 0:
#     ans = -1
# print(ans)
