import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n, q = MII()

ans = n
ed = [set() for _ in range(n)]
for _ in range(q):
    tmp = LMII()
    if tmp[0] == 1:
        u, v = tmp[1:]
        u -= 1
        v -= 1
        if len(ed[u]) == 0:
            ans -= 1
        if len(ed[v]) == 0:
            ans -= 1

        ed[u].add(v)
        ed[v].add(u)
    else:
        v = tmp[1] - 1
        if len(ed[v]) > 0:
            ans += 1

        for i in ed[v]:
            ed[i].remove(v)
            if len(ed[i]) == 0:
                ans += 1
        ed[v] = set()

    print(ans)
