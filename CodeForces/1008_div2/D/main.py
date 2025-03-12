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

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
# setrecursionlimit(10**7)
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


t = II()
aans = []


for _ in range(t):

    def f(m):
        a = m
        b = add_num - m
        for i, j, k, l in quers[idx + 1 :]:
            if i == "+":
                a += int(j)
            else:
                a += a * (int(j) - 1)

            if k == "+":
                b += int(l)
            else:
                b += b * (int(l) - 1)
        return a + b

    def sanbutansaku_max(l, r):
        # 整数に対する三分探索
        # [l,r]: 定義域
        while r - l > 2:
            m1 = (l * 2 + r) // 3
            m2 = (l + r * 2) // 3
            if f(m1) < f(m2):
                l = m1
            else:
                r = m2
        return l, r

    pass
    n = II()
    ans = 1
    quers = []

    for _ in range(n):
        quers.append(input().split())
    memo = []
    for i in range(1, n):
        now = i
        memo.append(sanbutansaku_max(0, 10**18))
    # add = [[1, 0], [1, 0]]
    # for i, j, k, l in quers[::-1]:
    #     tmp = add[-1][:]
    #     if i == "+":
    #         tmp[0][0] += int(j) * tmp[0][1]
    #     else:
    #         tmp[0][1] *= int(j)

    #     if k == "+":
    #         tmp[1][0] += int(l) * tmp[0][1]
    #     else:
    #         tmp[1][1] *= int(l)
    #     add.append(tmp)
    # add = add[::-1]

    ans = [1, 1]
    for idx, (i, j, k, l) in enumerate(quers):
        add_num = 0
        if i == "+":
            add_num += int(j)
        else:
            add_num += ans[0] * (int(j) - 1)
        if k == "+":
            add_num += int(l)
        else:
            add_num += ans[1] * (int(l) - 1)
        l, r = memo[idx]
        if add_num < l:
            best = [ans[0] + add_num, ans[1]]
        else:
            for i in range(l, r + 1):
                res = f(i)
                if res > max_:
                    max_ = res
                    best = [ans[0] + i, ans[1] + (add_num - i)]

        # now = idx
        # l, r = sanbutansaku_max(0, add_num)
        # max_ = -1
        # best = -1
        # # for i in range(max(0, l - 5), min(add_num + 1, r + 5)):
        # for i in range(add_num + 1):
        #     res = f(i)
        #     if res > max_:
        #         max_ = res
        #         best = [ans[0] + i, ans[1] + (add_num - i)]

        ans = best
    aans.append(best[0] + best[1])


for i in aans:
    print(i)
