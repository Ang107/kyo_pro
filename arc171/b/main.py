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
from sortedcontainers import SortedSet, SortedList, SortedDict

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


n = II()
a = LMII()
ans = [set() for _ in range(n)]
# ans min,maxをもつ
ed = {}
for i, j in enumerate(a):
    # idx = i + 1
    if i + 1 < j:
        ed[i + 1] = j
    if i + 1 > j:
        print(0)
        exit()
    ans[i].add(1)
    ans[i].add(j)

dis = sorted(ed.items(), key=lambda i: abs(i[0] - i[1]))
print(dis)
num = n
ans = 0
rang = SortedSet(range(1, n + 1))
for i, j in dis:
    tmp = rang.bisect_left(j) - rang.bisect_left(i)
    print(tmp)
    ans += pow(2, tmp - 1, mod)
    rang.remove(i + 1)
    num -= 1
    # print(ans)
print(ans)

# def dfs(v):
#     deq = deque()
#     deq.append(v)
#     while deq:
#         v = deq.pop()
#         if v < a[v]
# print(ans)
