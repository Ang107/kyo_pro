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
    n = II()
    a = LMII()
    exp = [1]
    prv = -1
    rslt = 0
    for idx, i in enumerate(a):
        if idx == 0:
            continue
        if i == 1:
            if a[idx - 1] > i:
                rslt = -1
                break
            else:
                exp.append(1)
        else:
            # print(a[idx - 1], i, exp[idx - 1])
            # print(a[idx - 1], math.log(a[idx - 1], i), exp[idx - 1])
            tmp = math.ceil(math.log(a[idx - 1], i) * exp[idx - 1])
            if tmp <= 1:
                exp.append(1)
                continue
            exp.append(2 ** math.ceil(math.log(tmp, 2)))

            # pritn(i, tmp)
            rslt += int(math.log(tmp - 1, 2)) + 1
            # print(exp)
            # print(i, tmp, int(math.log(tmp - 1, 2)) + 1)
            # while prv > i:
            #     i *= i
            #     rslt += 1

    ans.append(rslt)

    pass
for i in ans:
    print(i)
