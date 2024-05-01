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


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n, x, y = MII()
x, y = x - 1, y - 1
ed = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = MII()
    u, v = u - 1, v - 1
    ed[u].append(v)
    ed[v].append(u)

pre_list = [None] * n
ans = [y]


def bfs():
    deq = deque([x])
    visited = set()
    while deq:
        v = deq.popleft()
        for i in ed[v]:
            if i not in visited:
                visited.add(i)
                deq.append(i)
                pre_list[i] = v


bfs()
while True:
    ans.append(pre_list[ans[-1]])
    if ans[-1] == x:
        break
ans = ans[::-1]
ans = [i + 1 for i in ans]
print(*ans)
