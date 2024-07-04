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
    n, k, h = MII()
    # 一発で超える場合 A >= H
    rslt = n * max(0, (n - h + 1))
    # print(rslt)
    # 一回では超えられない場合
    # 1秒間に上がる必要のある最低距離
    tmp = -(-h // (k + 1))
    # print(tmp)
    # 初項
    # a = 1
    # 末項
    # b = max(1, min(h - 2))

    # rslt += (1 + ( h - tmp - 1)) * (h - tmp - 1) // 2
    # ans.append(rslt)
    # cnt = 0

    for a in range(1, min(h, n + 1)):

        def isOK(mid):
            return (a - mid) * (k - 1) + a >= h
            pass

        def meguru(ng, ok):
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if isOK(mid):
                    ok = mid
                else:
                    ng = mid
            return ok

        if (a - 1) * (k - 1) + a >= h:
            rslt += meguru(n + 1, 1)

    ans.append(rslt)

    pass
for i in ans:
    print(i)
