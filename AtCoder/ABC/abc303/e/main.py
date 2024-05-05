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
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = II()
ed = defaultdict(set)
for i in range(n - 1):
    u, v = MII()
    ed[u - 1].add(v - 1)
    ed[v - 1].add(u - 1)
ans = []
visited = set()
zisu_1_set = {i for i, j in ed.items() if len(j) == 1}
while zisu_1_set:
    x = zisu_1_set.pop()
    if len(ed[x]) != 1:
        continue
    visited.add(x)
    pear = ed[x].pop()
    visited.add(pear)
    ans.append(len(ed[pear]))

    for i in ed[pear]:
        visited.add(i)
        for j in ed[i]:
            if j == pear:
                continue
            ed[j].discard(i)
            if len(ed[j]) == 1:
                zisu_1_set.add(j)
        ed[i] = set()
    ed[pear] = set()
# print(ed_sorted)
# for k, v in ed_sorted:
#     print(visited)
#     if k not in visited:
#         ans.append(len(v))
#         visited.add(k)
#         for i in v:
#             visited.add(i)

print(*sorted(ans))
