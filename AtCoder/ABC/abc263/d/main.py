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


n, l, r = MII()
a = LMII()
a_r = a[::-1]
prf_a = list(accumulate(a))
prf_a_rev = list(accumulate(a_r))
tmp = [l] * n
prf_l = list(accumulate(tmp))
prf_l = [0] + prf_l
tmp = [r] * n
prf_r = list(accumulate(tmp))

max_gensyou = [0] * (n + 1)
idx = 1
for i, j in zip(prf_a_rev, prf_r):
    max_gensyou[idx] = max(max_gensyou[idx - 1], i - j)
    idx += 1


max_gensyou = max_gensyou[::-1]

ans = 0
index = 0
prf_a = [0] + prf_a
# print([i - j for i, j in zip(prf_a, prf_l)])
# print(prf_l)
# print(max_gensyou)
for i, j, k in zip(prf_a, prf_l, max_gensyou):
    ans = max(ans, i - j + k)

# x, y = 0, 0
# tmp_l = [i - j for i, j in zip(prf_a, prf_l)]
# tmp_r = [i - j for i, j in zip(prf_a, prf_r)]

print(sum(a) - ans)
