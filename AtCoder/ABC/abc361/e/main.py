# import pypyjit

# pypyjit.set_param("max_unroll_recursion=-1")
import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)x
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
n = II()
cab = []
sum_c = 0
for _ in range(n - 1):
    a, b, c = MII()
    a -= 1
    b -= 1
    sum_c += c
    cab.append((c, a, b))
if n == 2:
    print(cab[0][0])
    exit()

ed = [[] for _ in range(n)]
for c, a, b in cab:
    ed[a].append((c, b))
    ed[b].append((c, a))


def f(x):
    deq = deque()
    deq.append(x)
    visited = [-1] * n
    visited[x] = 0
    while deq:
        x = deq.pop()
        for c, nxt in ed[x]:
            if visited[nxt] == -1:
                visited[nxt] = visited[x] + c
                deq.append(nxt)
    return max(visited), visited.index(max(visited))


rslt = f(0)
ans = f(rslt[1])
print(sum_c * 2 - ans[0])
