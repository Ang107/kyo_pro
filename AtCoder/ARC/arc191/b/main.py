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


def solve(n, k):
    cnt = bin(n)[2:].count("0")
    # print(n, bin(n), cnt)
    if 2**cnt < k:
        return -1
    else:
        tmp = list(bin(k - 1)[2:])[::-1]
        ans = list(bin(n)[2:])
        # tmp = ["0"] * (len(ans) - len(tmp)) + tmp
        index = 0
        # print(ans.count(0))
        # print(len(tmp))
        for i in reversed(range(len(ans))):
            if ans[i] == "0" and index < len(tmp):
                ans[i] = tmp[index]
                index += 1
        return int("".join(ans), 2)


def native(n, k):
    cnt = 0
    for x in range(n, n + 1000):
        if x ^ n == x % n:
            cnt += 1
            if cnt == k:
                return x
    return -1


if 1:
    t = II()
    for _ in range(t):
        n, k = MII()
        print(solve(n, k))
else:
    import random

    while True:
        n = random.randrange(1, 1000)
        k = random.randrange(1, 2 * n)
        r1 = solve(n, k)
        r2 = native(n, k)
        print(r1, r2)
        if r1 != r2:
            print(n, k, r1, r2)
            exit()


# for n in range(1, 100):
#     print(f"n: {n}")
#     for x in range(100):
#         if x ^ n == x % n:
#             print(x)
#     print()
