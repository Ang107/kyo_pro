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

import sys

test = False

t = II()

for _ in range(t):
    if test:
        target = II()

    def meguru(ng, ok):
        while abs(ok - ng) > 1:
            if abs(ok - ng) <= 3:
                l = ng + 1
                r = ng + 2
                print("?", l, r)
                sys.stdout.flush()
                if test:
                    nl, nr = l, r
                    if l >= target:
                        nl += 1
                    if r >= target:
                        nr += 1

                    s = nl * nr
                else:
                    s = II()

                if s == (l + 1) * (r + 1):
                    return l
                elif s == l * r:
                    return r + 1
                else:
                    return r

            else:
                tmp = abs(ok - ng) // 3
                l = ng + tmp
                r = ng + tmp * 2
                print("?", l, r)
                sys.stdout.flush()
                if test:
                    nl, nr = l, r
                    if l >= target:
                        nl += 1
                    if r >= target:
                        nr += 1

                    s = nl * nr
                else:
                    s = II()
                if s == (l + 1) * (r + 1):
                    ok = l
                elif s == l * r:
                    ng = r
                else:
                    ng = l
                    ok = r

        return ok

    ans = meguru(1, 999)
    print("!", ans)
    sys.stdout.flush()
