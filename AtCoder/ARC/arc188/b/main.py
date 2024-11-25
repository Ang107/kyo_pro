from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase


DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
import math


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def f(n, k):
    if n % 4 == 0:
        return "No"
    if n == 6:
        if k == 3:
            return "No"
        else:
            return "Yes"
    tmp = factorization(n)
    ans = "Yes"
    for index, (i, j) in enumerate(tmp):
        if i == 2:
            continue
        if i == 3:
            if j >= 2:
                if k % 9 == 0:
                    ans = "No"
        else:
            if k % i == 0:
                ans = "No"
    return ans


# t = II()
# ansl = []
# for _ in range(t):
#     n, k = MII()
#     if n == 6:
#         if k == 3:
#             ansl.append("No")
#         else:
#             ansl.append("Yes")
#         continue

#     if n % 4 == 0:
#         ansl.append("No")
#         continue
#     tmp = factorization(n)
#     ans = "Yes"
#     for index, (i, j) in enumerate(tmp):
#         if i == 2:
#             continue
#         if i == 3 and j >= 2:
#             if k % 9 == 0:
#                 ans = "No"
#         else:
#             if k % i == 0:
#                 ans = "No"
#     ansl.append(ans)
# for i in ansl:
#     print(i)


# n = II()
for n in range(2, 30):
    for k in range(1, n):
        b = [0] * n
        prev = -1
        ans = "Yes"
        for i in range(n):
            if i == 0:
                prev = 0
                b[0] = 1
            else:
                if i % 2 == 0:
                    if prev == 0:
                        assert n % 2 == 0
                        tmp = n // 2
                    elif prev == n / 2:
                        tmp = 0
                    elif prev >= n / 2:
                        tmp = n - prev
                    else:
                        tmp = n - prev
                    prev = tmp
                    if b[tmp] == 1:
                        ans = "No"
                        break
                    b[tmp] = 1
                else:
                    if prev == k:
                        tmp = (k + n // 2) % n
                    elif prev == (k + n // 2) % n:
                        tmp = k
                    elif k <= prev < n or 0 <= prev < (k + prev) % n:
                        tmp = (prev - k) % n
                        tmp = (k - tmp) % n
                    else:
                        tmp = (k - prev) % n
                        tmp = (k + tmp) % n

                    if b[tmp] == 1:
                        ans = "No"
                        break
                    prev = tmp
                    b[tmp] = 1
        # print(n, prev)

        print(n, k, ans)
        assert f(n, k) == ans, (n, k, f(n, k), ans)


# if res != ans:
#     print(n, k, res, ans)
#     exit()
#     # print(n, k, ans)
