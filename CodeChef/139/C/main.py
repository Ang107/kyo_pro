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

for _ in range(t):
    n, c = MII()
    a = LMII()
    tmp = [[0, i] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            tmp[i][0] += a[i] * a[j]
    if tmp[0][0] <= c:
        ans.append(1)
    else:
        result = 0
        tmp.sort()
        tmp = [i for _, i in tmp]
        for i in range(1, n + 1):
            rem = set(tmp[:i])
            cost = 0
            for j in rem:
                for k in range(n):
                    if k not in rem:
                        cost += a[j] * a[k]
            if cost <= c:
                result = i
            else:
                break
        ans.append(n - result)

        # ok = set(range(n))
        # print(tmp)
        # while tmp and tmp[-1][0] <= c:
        #     cost, idx = tmp.pop()
        #     ok.remove(idx)
        #     c -= cost
        #     for i in range(len(tmp)):
        #         tmp[i][0] -= a[tmp[i][1]] * a[idx]
        #     tmp.sort(reverse=True)
        #     print(ok)
        #     print(tmp)
        # ans.append(len(ok))

    pass
for i in ans:
    print(i)
