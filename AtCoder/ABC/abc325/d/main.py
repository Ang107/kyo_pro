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
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = II()
td = []
heap = []
for i in range(n):
    t, d = MII()
    d += t
    heappush(heap, (t, d))
t = 0
can_stamp = []
ans = 0
while heap or can_stamp:
    if not can_stamp:
        l, r = heappop(heap)
        heappush(can_stamp, r)
        t = max(t, l)

    while heap and heap[0][0] <= t:
        l, r = heappop(heap)
        heappush(can_stamp, r)

    while can_stamp and can_stamp[0] < t:
        heappop(can_stamp)

    if can_stamp and t <= can_stamp[0]:
        heappop(can_stamp)
        ans += 1
        t += 1

print(ans)
