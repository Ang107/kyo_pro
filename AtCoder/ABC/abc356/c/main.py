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

n, m, k = MII()
ar = []
for _ in range(m):
    tmp = input().split()
    r = tmp[-1]
    a = tmp[1:-1]
    a = [int(i) - 1 for i in a]
    a = set(a)
    ar.append((r, a))
ans = 0
for i in range(1 << n):
    cr_key = set()
    for j in range(n):
        if i >> j & 1:
            cr_key.add(j)
    flag = True
    for r, a in ar:
        if (len(cr_key & a) >= k and r == "o") or (len(cr_key & a) < k and r == "x"):
            pass
        else:
            flag = False
            break
    if flag:
        ans += 1

print(ans)
