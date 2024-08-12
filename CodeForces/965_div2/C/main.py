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
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
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
    n, k = MII()
    a = LMII()
    b = LMII()
    ab = [(i, j) for i, j in zip(a, b)]
    ab.sort()
    c = []
    d = []
    idx_1 = []
    for idx, (i, j) in enumerate(ab):
        if j:
            idx_1.append(idx)
            c.append(i)
        else:
            d.append(i)

    rslt = 0
    tmp = sum(max(d[0]-i,0) for i in a) 
    if (n+1)//2-2 >= 0 and sum(max(0,d[(n+1)//2-2]-i) for i in c) <= k:
        bn0 = True
    if (n+1)//2-1 >= 0 and sum(max(0,d[(n+1)//2-1]-i) for i in c) <= k: 
        bn1 = True
        
    for i in range(n):
        if i <= (n + 1) // 2 - 1:
            mean = (n + 1) // 2
        else:
            mean = (n + 1) // 2 - 1
        if b[i] == 1:
            rslt = max(rslt, a[i] + a[mean] + k)
        else:
            # ボトルネックが存在するなら
            if tmp + (a[i]-d[0]) * 
            mean = bisect_left(idx_1, mean) - 1
            if mean >= 0:
                rslt = max(rslt, a[i] + a[mean] + k)
            else:
                rslt = max(rslt, a[i] + a[mean])

    ans.append(rslt)
    # if tmp:

    #     def isOK(mid):
    #         pass

    #     def meguru(ng, ok):
    #         while abs(ok - ng) > 1:
    #             mid = (ok + ng) // 2
    #             if isOK(mid):
    #                 ok = mid
    #             else:
    #                 ng = mid
    #         return ok

    #     # 最小値の最大化
    #     tmp = meguru(tmp[-1] + k + 1, tmp[0])

    # ans.append(sum(other) + sum(tmp) + sorted(other + tmp)[(n + 1) // 2])
    pass
for i in ans:
    print(i)
