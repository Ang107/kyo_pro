import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = II()
lr = [LMII() for _ in range(n)]
min_, max_ = 0, 0
tmp = [(0, 0)]
for l, r in lr:
    min_ = min_ + l
    max_ = max_ + r
    tmp.append((min_, max_))

l = [i for i, j in lr]
r = [j for i, j in lr]
p_min = list(accumulate(l[::-1]))[::-1]
p_max = list(accumulate(r[::-1]))[::-1]

if min_ <= 0 <= max_:
    ans = []
    now = 0
    for i in range(n - 1):
        ok_l = max(-p_max[i + 1], now + lr[i][0])
        ok_r = min(-p_min[i + 1], now + lr[i][1])
        if ok_l <= ok_r:
            ans.append(ok_l - now)
            now = ok_l
    ans.append(-now)
    PY()
    # print(sum(ans))
    print(*ans)
else:
    PN()
