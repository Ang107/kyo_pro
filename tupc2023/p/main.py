import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n, m = MII()
LR = [LMII() for _ in range(m)]
LR.sort()
print(LR)
ed = [set() for _ in range(m)]


# 連結成分の計算
for i in range(m):
    l, r = LR[i]
    for j in range(m):
        if i == j:
            continue
        p, q = LR[j]
        if r < p or (l % 2 == p % 2 and l <= p):
            ed[i].add(j)


print(ed)


def dfs(graph, start, visited=None, depth=0):
    if visited is None:
        visited = set()
    visited.add(start)
    max_depth = depth
    for next in graph[start] - visited:
        current_depth = dfs(graph, next, visited.copy(), depth + 1)
        max_depth = max(max_depth, current_depth)
    return max_depth


max_length = 0
for start in range(m):
    length = dfs(ed, start)
    max_length = max(max_length, length)

print(max_length + 1)


# print(sorted(LR, key=lambda x: x[1]))
# for i in range(n):
#     l,r = MII()


# g, k = 0, 0
# for i in range(m):
#     l, r = MII()
#     if l % 2 == 0:
#         g += 1
#     else:
#         k += 1
# print(g, k)
# tmp = [LMII() for _ in range(m)]
# tmp.sort(key=lambda x: x[1] - x[0], reverse=True)
# print(tmp)
# LR = defaultdict(int)
# for l, r in tmp:
#     flag = False
#     for j, k in LR:
#         if l <= j and k <= r and l % 2 == j % 2:
#             flag = True
#             LR[(j, k)] += 1
#     if not flag:
#         LR[(l, r)] += 1

# print(LR)
# j文字目までの中での満たす条件数の最大値
# dp = [[0](n+1) for _ in range(m+1)]

# for i in range(1,m+1):
#     for j in range(1,n+1):
#         # not use
#         dp[i][j] = dp[i-1][j]
#         dp[i][]
