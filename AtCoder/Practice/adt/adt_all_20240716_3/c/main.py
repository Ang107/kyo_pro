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

x, y, z = MII()
x += 1000
y += 1000
z += 1000

visited = [[inf, inf] for _ in range(2001)]
visited[1000] = [0, inf]
deq = deque()
# 場所、ハンマーの所持
deq.append((1000, 0))

while deq:
    p, h = deq.popleft()
    for i in [1, -1]:
        if p + i in range(2001):
            if p + i == y:
                if visited[p + i][1] > visited[p][1] + 1:
                    visited[p + i][1] = visited[p][1] + 1
                    deq.append((p + i, 1))
            elif p + i == z:
                if visited[p + i][0] > visited[p][0] + 1:
                    visited[p + i][0] = visited[p][0] + 1
                    deq.append((p + i, 0))
                if visited[p + i][1] > visited[p][0] + 1:
                    visited[p + i][1] = visited[p][0] + 1
                    deq.append((p + i, 1))

            else:
                if visited[p + i][0] > visited[p][0] + 1:
                    visited[p + i][0] = visited[p][0] + 1
                    deq.append((p + i, 0))
                if visited[p + i][1] > visited[p][1] + 1:
                    visited[p + i][1] = visited[p][1] + 1
                    deq.append((p + i, 1))

if min(visited[x]) == inf:
    print(-1)
else:
    print(min(visited[x]))
