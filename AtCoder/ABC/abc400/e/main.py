from sys import stdin, stderr, setrecursionlimit
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

import time

start = time.perf_counter()
q = II()


def get_primes(n):
    if n <= 1:
        return 0
    # n以下のすべての数について素数かどうかを記録する配列
    is_prime = [True] * (n + 1)
    is_prime[0] = False  # 0は素数ではない
    is_prime[1] = False  # 1は素数ではない
    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            # iの倍数を素数ではないとマーク
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False

    return primes


primes = get_primes(10**6)
n = len(primes)
cand = []
for i in primes:
    for j in range(2, 64, 2):
        if i**j > 10**12:
            break
        cand.append(i**j)
cand.sort()
print(len(cand))
# print(time.perf_counter() - start)
# print(n)
# mx = 10**12
# cand = []
# for i in range(n):
#     x = primes[i]
#     for j in range(i + 1, n):
#         y = primes[j]
#         for p in range(2, 100, 2):
#             if x**p > mx:
#                 break
#             for q in range(2, 100, 2):
#                 # print(x, y, p, q)
#                 tmp = x**p * y**q
#                 if tmp > mx:
#                     break
#                 cand.append(tmp)

# cand.sort()
cnt = 0
for _ in range(q):
    a = II()
    # print(cand[bisect_left(cand, a)])
    ans = 0
    for i in primes:
        if i**4 > a:
            break
        for p in range(2, 64, 2):
            tmp = i**p
            if tmp * i**2 >= a:
                break
            idx2 = bisect_right(cand, a // tmp) - 1
            # for j in range(idx2, -1, -1):
            #     if cand[j] != i:
            #         cnt += abs(j - idx2)
            #         ans = max(ans, tmp * cand[j][0])
            #         break
            # for j in primes[idx + 1 :]:
            #     if tmp * j**2 > a:
            #         break
            #     for q in range(2, 64, 2):
            #         if tmp * j**q > a:
            #             break
            #         ans = max(ans, tmp * j**q)
    print(ans)
print(time.perf_counter() - start)
