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

a = [LMII() for _ in range(n)]
if n == 1:
    print(a[0][0] % m)
    exit()
cand = [[] for _ in range(2 * n - 1)]
na = [[-1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        na[i][j] = a[i][j] * pow(10, 2 * n - 2 - i - j, m) % m
        cand[i + j].append(a[i][j] * pow(10, 2 * n - 2 - i - j, m) % m)
kaizyou = [1]
for i in range(1, 41):
    kaizyou.append(kaizyou[-1] * i)
print(kaizyou[20] / kaizyou[10] / kaizyou[10])
ans = [[set() for _ in range(n)] for _ in range(n)]
ans[0][0].add(na[0][0])
for i in range(n):
    for j in range(n):
        if i + j >= n - 1:
            continue
        ni = i + 1
        nj = j
        if ni in range(n):
            for k in ans[i][j]:
                ans[ni][nj].add((k + na[ni][nj]) % m)
        ni = i
        nj = j + 1
        if nj in range(n):
            for k in ans[i][j]:
                ans[ni][nj].add((k + na[ni][nj]) % m)
ans2 = [[set() for _ in range(n)] for _ in range(n)]
ans2[n - 1][n - 1].add(na[n - 1][n - 1])

for i in reversed(range(n)):
    for j in reversed(range(n)):
        if i + j <= n - 1:
            continue
        ni = i - 1
        nj = j
        if ni in range(n):
            for k in ans2[i][j]:
                ans2[ni][nj].add((k + na[ni][nj]) % m)
        ni = i
        nj = j - 1
        if nj in range(n):
            for k in ans2[i][j]:
                ans2[ni][nj].add((k + na[ni][nj]) % m)

for i in range(n):
    for j in range(n):
        ans2[i][j] = sorted(ans2[i][j])


res = 0
for i in range(n):
    j = n - 1 - i
    for x in ans[i][j]:
        for di, dj in [(1, 0), (0, 1)]:
            ni = i + di
            nj = j + dj
            if ni in range(n) and nj in range(n):
                idx = bisect_left(ans2[ni][nj], m - 1 - x)
                for k in range(idx - 10, idx + 10):
                    res = max(res, (x + ans2[ni][nj][k % len(ans2[ni][nj])]) % m)
print(res)

# s = set()
# print(cand)
# for i in cand:
#     if not s:
#         s = set(i)
#     else:
#         new_s = set()
#         for j in s:
#             for k in i:
#                 new_s.add((j + k) % m)
#         s = new_s
# print(max(s))
