from sys import stdin, setrecursionlimit
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
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
# for n in range(2, 4):
#     print(n)
#     # 存在の有無
#     ans = [False] * (n * n + 1)
#     same = defaultdict(list)
#     # 似ているグループに分ける
#     for mask in range(1 << (n * n)):
#         tmp = [[-1] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 tmp[i][j] = mask >> (i * n + j) & 1
#         sum_l = []
#         for i in range(n):
#             sum_l.append(sum(tmp[i]))
#         for j in range(n):
#             cnt = 0
#             for i in range(n):
#                 cnt += tmp[i][j]
#             sum_l.append(cnt)
#         sum_l = tuple(sum_l)
#         same[sum_l].append(tmp)

#     # 似ているグループの中で固定されている個数を求める。
#     for k, v in same.items():
#         tmp = [[{0, 1} for _ in range(n)] for _ in range(n)]
#         for cand in v:
#             for i in range(n):
#                 for j in range(n):
#                     tmp[i][j].discard(cand[i][j])
#         cnt = 0
#         for i in range(n):
#             for j in range(n):
#                 if len(tmp[i][j]) == 1:
#                     cnt += 1
#         if cnt != 0 and cnt != n**2:
#             print(k)
#             print(cnt)
#             for i in range(n):
#                 print([1 if len(j) == 1 else 0 for j in tmp[i]])
#                 # print(tmp[i])

#         ans[cnt] = True

#     for i in range(n * n + 1):
#         if ans[i]:
#             print(i)
#     print(ans)

n, q = map(int, input().split())
ans = set()
s = n * n
ans.add(0)
ans.add(n * n)
for i in range(2, n + 1):
    for j in range(i, n + 1):
        ans.add(s - i * j)
ans = sorted(ans)
# print(ans)
for _ in range(q):
    k = int(input())
    if k in ans:
        print("Yes")
    else:
        print("No")
