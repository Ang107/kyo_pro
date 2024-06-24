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

t = II()
ans = []


def dis(a, b):
    return min(abs(i - j) for i, j in zip(a, b))


for _ in range(t):
    n = II()
    tmp = [i + 1 for i in range(n)]
    ans.append(tmp)
    rslt = []
    rslt.extend(tmp[n // 2 :])
    rslt.extend(tmp[: n // 2])
    ans.append(rslt)

    # a = list(range(n))
    # max_dis = 0
    # for b in permutations(a):
    #     dis_ = dis(a, b)
    #     if max_dis < dis_:
    #         max_dis = dis_

    #         print(max_dis, list(b))

    pass
for i in ans:
    print(*i)
