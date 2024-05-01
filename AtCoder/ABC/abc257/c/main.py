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


n = II()
s = input()
w = LMII()

# SW = [(i, j) for i, j in zip(s, w)]
# SW.sort(key=lambda x: x[1])
# prf_l = [0]
# prf_r = [0]
# for i, j in SW:
#     if i == 1:
#         prf_l.append(prf_l[-1] + 1)
#     else:
#         prf_l.append(prf_l[-1])
# prf_l = prf_l[1:]
# for i, j in SW[::-1]:
#     if i == 0:
#         prf_r.append(prf_r[-1] + 1)
#     else:
#         prf_r.append(prf_r[-1])
# prf_r = prf_r[1::-1]


# ans = 10**18

# otona, kodomo = [], []
# for i, j in zip(w, s):
#     if j == "1":
#         otona.append(i)
#     else:
#         kodomo.append(i)

# kodomo.sort()
# otona.sort()

# w.sort()
# w_set = sorted(set(w))
# l = 0
# r = len(w_set) - 1

otona, kodomo = [], []
for i, j in zip(w, s):
    if j == "1":
        otona.append(i)
    else:
        kodomo.append(i)

kodomo.sort()
otona.sort()

w.sort()
w_set = sorted(set(w))
l = 0
r = len(w_set) - 1

tmp = []
for i in w_set:
    tmp.extend([i - 1, i, i + 1])
ans = inf
for i in tmp:
    ans = min(ans, len(kodomo) - bisect_left(kodomo, i) + bisect_left(otona, i))
print(n - ans)

# print(w_set, otona, kodomo)
# while r - l > 1:
#     mid = (r + l) // 2
#     if mid == 0:
#         L = inf
#     else:
#         L = w_set[mid - 1]
#     if mid == len(w_set) - 1:
#         R = inf
#     else:
#         L = w_set[mid + 1]

#     M = w_set[mid]
#     L_out = bisect_left(kodomo, L) + bisect_right(otona, L)
#     M_out = bisect_left(kodomo, M) + bisect_right(otona, M)
#     R_out = bisect_left(kodomo, R) + bisect_right(otona, R)
#     ans = min(ans, L_out, M_out, R_out)
#     if L_out < M_out or M_out < R_out:
#         r = mid
#     elif L_out > M_out or M_out > R_out:
#         l = mid
#     else:
#         break

# print(n - ans)

# def isOK(n):
#     global ans
#     # 大人を子供と間違える
#     tmpO_K = 0
#     tmpK_O = 0
#     for i, j in zip(s, w):
#         if j < n and i == "1":
#             tmpK_O += 1
#         if j >= n and i == "0":
#             tmpO_K += 1

#     # print(n, tmp)
#     ans = min(ans, tmpO_K + tmpK_O)
#     # print(ans)

#     if tmpK_O <= tmpO_K:
#         return True
#     else:
#         return False


# while abs(ok - ng) > 1:
#     mid = (ok + ng) // 2
#     if isOK(mid):
#         ok = mid
#     else:
#         ng = mid
# # print(ans)
# print(n - ans)
