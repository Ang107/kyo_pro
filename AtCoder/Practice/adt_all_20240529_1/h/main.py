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

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
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

n,q = MII()
ed = [set() for _ in range(n)]
ans = n
for _ in range(q):
    tmp = LMII()
    if tmp[0] == 1:
        u,v = tmp[1:]
        u -= 1
        v -= 1
        if len(ed[u]) == 0:
            ans -= 1
        if len(ed[v]) == 0:
            ans -= 1
        ed[u].add(v)
        ed[v].add(u)
    else:
        v = tmp[1]
        v -= 1
        if len(ed[v]) != 0:
            ans += 1
        for i in ed[v]:
            ed[i].remove(v)
            if len(ed[i]) == 0:
                ans += 1
        ed[v] = set()
    # print(ed)
    pritn(ans)
        