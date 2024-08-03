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
    p = LMII()
    p = [i - 1 for i in p]
    c = [[] for _ in range(n)]
    for i, j in enumerate(p):
        c[j].append(i + 1)

    depth = [[-1, i] for i in range(n)]
    depth[0][0] = 0
    deq = [0]
    while deq:
        now = deq.pop()
        for nxt in c[now]:
            depth[nxt][0] = depth[now][0] + 1
            deq.append(nxt)
    depth.sort(reverse=True, key=lambda x: x[0])

    for d, now in depth:
        # print(a)
        if d == 0:
            min_a = inf
            for nxt in c[now]:
                min_a = min(min_a, a[nxt])
            a[now] += min_a
        else:
            if not c[now]:
                continue
            min_a = inf
            for nxt in c[now]:
                min_a = min(min_a, a[nxt])
            if a[now] < min_a:
                a[now] = (a[now] + min_a) // 2
            else:
                a[now] = min_a
    ans.append(a[0])

    pass
for i in ans:
    print(i)
