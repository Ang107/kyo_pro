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


n, d = MII()
a = LMII()
# dp = [list() for _ in range(n)]
# dp[0] = a[0]
# dp_num = [-1] * n
# dp_num[0] = 1

# s = SortedSet([a[0]])
# d = defaultdict(int)
# d[a[0]] += 1
# for i in range(1,n):
#     dp[i] = dp[i-1]

s = set([a[0]])
dd = defaultdict(int)
dd[a[0]] = 1
for idx in range(1, n):
    i = a[idx]
    dd[i] = max(dd[i], 1)
    tmp = set()
    tmp.add(i)
    for j in s:
        # print(j, i, j in range(i - d, i + d + 1))
        if j in range(i - d, i + d + 1):
            if dd[i] < dd[j] + 1:
                dd[i] = max(dd[i], dd[j] + 1)
                tmp.add(i)

        tmp.add(j)
    s = tmp
    # print(s)
print(max(dd.values()))
