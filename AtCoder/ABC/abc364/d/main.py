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


n, q = MII()
a = LMII()
bk = [LMII() for _ in range(q)]
a.sort()
for b, k in bk:

    def isOK(mid):
        # 距離がmid以内にある点の数
        tmp = 0
        tmp += bisect_right(a, b + mid) - bisect_left(a, b - mid)
        return tmp >= k

        return
        pass

    def meguru(ng, ok):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if isOK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru(-1, 10**9))

# print(a)
# for b, k in bk:

#     def isOK(mid, now):
#         # 右端との差
#         if now - (k - mid) < 0:
#             # print(-1)
#             return False
#         if now + mid - 1 >= n:
#             # print(1)
#             return True

#         r = a[now + mid - 1] - b
#         l = b - a[now - (k - mid)]
#         # print(l, r)
#         return l <= r
#         pass

#     def meguru(ng, ok, now):
#         while abs(ok - ng) > 1:
#             mid = (ok + ng) // 2
#             rslt = isOK(mid, now)
#             # print(now, mid, rslt)

#             if rslt:
#                 ok = mid
#             else:
#                 ng = mid
#         return ok

#     # 自分より左にある数
#     l = bisect_right(a, b)
#     if k == 1:
#         rslt = inf
#         if l - 1 in range(n):
#             rslt = min(rslt, abs(b - a[l - 1]))
#         if l in range(n):
#             rslt = min(rslt, abs(b - a[l]))

#         print(rslt)
#         continue
#     # 自分を含む右にある数
#     r = n - l
#     tmp = meguru(-1, min(r, k), l)
#     # print(l - 1, tmp, min(r, k))
#     rslt = 0

#     if tmp > 0:
#         # print(a[l - 1 + tmp])
#         rslt = max(rslt, abs(b - a[l + tmp]))
#     if n - tmp > 0:
#         # print(l - (k - tmp))
#         # print(a[l - (k - tmp)])
#         rslt = max(rslt, abs(b - a[l - (k - tmp) + 1]))

#     # p = a[l + tmp]
#     # q = a[l - 1 - (k - tmp + 1)]
#     # print(p, q)
#     print(rslt)
