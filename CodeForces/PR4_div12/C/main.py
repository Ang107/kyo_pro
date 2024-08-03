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
    a.sort()
    a_n = [a[0]]
    for i in a:
        if a_n[-1] == i:
            continue
        else:
            a_n.append(i)
    a = a_n

    tmp = [i for i in a if i % 2 == 0]

    if len(tmp) == 0 or len(tmp) == len(a):
        pass
    else:
        ans.append(-1)
        continue

    rslt = []
    for i in range(39):
        # print(a)
        a_n = []
        if len(a) == 1:
            break
        tmp = (a[0] + a[-1]) // 2
        rslt.append(tmp)
        for j in range(len(a) - 1):
            a_n.append(abs(a[j] - tmp))
        a = a_n
        a.sort()
        a_n = [a[0]]
        for i in a:
            if a_n[-1] == i:
                continue
            else:
                a_n.append(i)
        a = a_n

    if len(a) == 1:
        if a[0] != 0:
            rslt.append(a[0])
        ans.append(len(rslt))
        ans.append(" ".join(map(str, rslt)))
    else:
        ans.append(-1)

    pass
for i in ans:
    print(i)
