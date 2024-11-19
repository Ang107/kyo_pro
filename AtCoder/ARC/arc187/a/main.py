from sys import stdin, setrecursionlimit
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
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

DEBUG = True


def solve():
    ans = []
    for i in range(n):
        tmp = []
        for j in range(i, n):
            tmp.append(a[j] + k * (j - i))
        min_ = min(tmp)
        index = -1
        for j in range(len(tmp)):
            if tmp[j] == min_:
                index = i + j
        # deb(index)
        for j in reversed(range(i, index)):
            a[j], a[j + 1] = a[j + 1] + k, a[j]
            ans.append(j + 1)
    if a[0] > a[1] and a[0] - a[1] <= k:
        a[0], a[1] = a[1], a[0]
        a[0] += k
        ans.append(1)
    for i in range(1, n - 1):
        if a[i - 1] > a[i]:
            # if a[i] <= a[i + 1]:
            #     while a[i - 1] > a[i] or (i >= 2 and a[i - 2] > a[i - 1]):
            #         a[i] += k
            #         a[i + 1] += k
            #         ans.append(i + 1)
            #         ans.append(i + 1)
            #         if len(ans) > 500000:
            #             break
            # else:
            while a[i - 1] > a[i] or (i >= 2 and a[i - 2] > a[i - 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                a[i] += k
                ans.append(i + 1)
                if len(ans) > 500000:
                    break
            if a[i + 1] + k < a[i]:
                a[i], a[i + 1] = a[i + 1], a[i]
                a[i] += k
                ans.append(i + 1)
        # print(a)
    while a[-2] > a[-1] or (n >= 3 and a[-3] > a[-2]):
        a[-2], a[-1] = a[-1], a[-2]
        a[-2] += k
        ans.append(n - 1)
        if len(ans) > 500000:
            break
    return ans


if 1:
    n, k = MII()
    a = LMII()
    ans = solve()
    if sorted(a) == a and len(ans) <= 500000:
        PY()
        print(len(ans))
        print(*ans)
    else:
        PN()
else:
    import random

    while 1:
        n = random.randrange(5, 10)
        k = random.randrange(1, 51)
        a = [random.randrange(1, 51) for _ in range(n)]
        print(n, k)
        print(*a)
        solve()
        # print(solve())
        print(a)
        input()
