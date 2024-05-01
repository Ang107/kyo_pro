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


# n = II()
# q = LMII()
# a = LMII()
# b = LMII()

# iまでで材料がjの時の食事の合計の最大値
# dp = [[-inf] * (10**6 + 1) for i in range(n + 1)]
# dp[0][0] = 0
# for i in range(1,n+1):
#     for j in range(q[i]):
#         dp[i][j] =


def main():
    def solve(num):
        mid = num
        A = [0] * n
        B = [0] * n
        for i in range(n):
            A[i] = a[i] * mid
        idx = 0
        for i, j in zip(A, q):
            B[idx] = j - i
            idx += 1
        tmp = []
        for i, j in enumerate(B):
            if b[i] != 0:
                tmp.append(j // b[i])
        tmp = min(tmp)
        return mid + tmp

    tmp = []
    for i, j in enumerate(q):
        if a[i] != 0:
            tmp.append(j // a[i])

    r = min(tmp)
    ans = 0
    for i in range(r + 1):
        ans = max(ans, solve(i))
    return ans


def main2():
    def solve(num):
        mid = num
        A = [0] * n
        B = [0] * n
        for i in range(n):
            A[i] = a[i] * mid
        idx = 0
        for i, j in zip(A, q):
            B[idx] = j - i
            idx += 1
        tmp = []
        for i, j in enumerate(B):
            if b[i] != 0:
                tmp.append(j // b[i])
        tmp = min(tmp)
        return mid + tmp

    tmp = []
    for i, j in enumerate(q):
        if a[i] != 0:
            tmp.append(j // a[i])

    r = min(tmp)
    zyougen = r
    l = 0

    M = 0
    while True:
        mid = (r + l) // 2
        L, M, R = (
            solve(mid - 1),
            solve(mid),
            solve(mid + 1),
        )
        print(l, mid, r)

        if mid - 1 == -1:
            L = -inf
        if mid == zyougen:
            R = -inf
        print(L, M, R)

        if L < M or M < R:
            l = mid
        elif L > M or M > R:
            r = mid
        else:
            M = max(L, M, R)
            break

        M = max(L, M, R)

    return M


import random

while True:
    n = 5
    q = random.sample(range(300, 1000), n)
    a = random.sample(range(100), n)
    b = random.sample(range(100), n)
    print(main(), main2())
    if main() != main2():
        print(q, a, b)
        print(main(), main2())
        break

# zyougen = r
# l = 0

# M = 0
# ans = 0
# while r - l > 1:
#     mid = (r + l) // 2
#     L, M, R = (
#         solve(max(0, mid - 1)),
#         solve(mid),
#         solve(min(mid + 1, zyougen)),
#     )
#     if 0 in (L, M, R):
#         r = mid
#         continue
#     if L < M <= R:
#         l = mid
#     elif L >= M > R:
#         r = mid
#     elif l <= M >= R:
#         M = max(ans, L, M, R)
#         break
#     ans = max(ans, L, M, R)
#     # print(L, M, R)
#     # print(l, mid, r)

# print(M)
