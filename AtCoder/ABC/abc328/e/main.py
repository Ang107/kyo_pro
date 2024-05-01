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


n, m, k = MII()
ed = []
for i in range(m):
    u, v, w = MII()
    ed.append([u, v, w])


def isTree(x, pas):
    deq = deque([[x, -1]])

    while deq:
        node, pre = deq.pop()
        visited.add(node)
        for u, v, w in pas:
            if u == node:
                if v in visited and v != pre:
                    return False
                elif v not in visited:
                    deq.append([v, node])
            elif v == node:
                if u in visited and u != pre:
                    return False
                elif u not in visited:
                    deq.append([u, node])
    return True


# visited = set()
# for i in range(1, n + 1):
#     if i not in visited:
#         print(isTree(i, [[2, 3, 86], [2, 4, 94], [2, 5, 95], [3, 4, 81]]))

ans = inf
for i in combinations(ed, n - 1):
    visited = set()
    flag = True
    for j in range(1, n + 1):
        if j not in visited:
            if isTree(j, i):
                pass
            else:
                flag = False
                continue
    if flag:
        # print(sum([l[2] for l in i]) % k, i)
        ans = min(ans, sum([l[2] for l in i]) % k)


print(ans)
