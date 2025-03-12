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
if n == 3:
    if a.count(0) == 3:
        PN()
    else:
        PY()
    exit()

# cnt = 0
# max_cnt = 0
# for i in a:
#     if i == 0:
#         cnt += 1
#     else:
#         cnt = 0
#     max_cnt = max(max_cnt, cnt)
ans = "No"
for i in range(min(15, n)):
    dp = [[False] * 2 for _ in range(n)]
    if a[2] == 1:
        dp[0][0] = True
        dp[0][1] = True
    for j in range(n):
        for k in range(2):
            if not dp[j][k]:
                continue
            if j + 2 < n and a[j + 2] == 1:
                dp[j + 2][k ^ 1] = True
            elif j + 2 == n:
                ans = "Yes"
            elif j + 2 >= n and all(a[l] == 1 for l in range(j + 1, n)):
                ans = "Yes"

            if j + 3 < n and a[j + 3] == 1:
                dp[j + 3][k ^ 0] = True
                dp[j + 3][k ^ 1] = True
            elif j + 3 == n:
                ans = "Yes"
            elif j + 3 >= n and all(a[l] == 1 for l in range(j + 1, n)):
                ans = "Yes"
    # print(ans)
    # print(a, dp)
    if any(dp[n - 1]):
        ans = "Yes"
    a.append(a.pop(0))
print(ans)
# if n == 3:
#     if a.count(0) == 6:
#         PN()
#     else:
#         PY()
#     exit()
# ok = [0, 0, 0, 0, 1] * (-(-2 * n // 5))
# ans = "No"
# for _ in range(5):
#     f = True
#     for index in range(5 * -(-n // 5)):
#         # print(index)
#         i = a[index]
#         j = ok[index]
#         if i == 1 or j == 0:
#             pass
#         else:
#             f = False
#     ok.append(ok.pop(0))
#     if f:
#         ans = "Yes"
# print("Yes")
