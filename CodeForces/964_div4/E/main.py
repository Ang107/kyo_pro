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
tmp = []
from functools import cache


@cache
def f(x):
    if x == 0:
        return 0
    else:
        return 1 + f(x // 3)


acc = [0]
for i in range(1, 2 * 10**5 + 1):
    acc.append(acc[-1] + f(i))
# print(acc)
for _ in range(t):
    l, r = MII()
    rslt = 0
    rslt += f(l) * 2
    # print(acc[r], acc[l])
    rslt += acc[r] - acc[l]
    # for i in range(l + 1, r + 1):
    #     rslt += f(i)

    ans.append(rslt)

    pass
for i in ans:
    print(i)
