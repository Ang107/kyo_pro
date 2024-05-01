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


n, s = MII()

Set = set([0])
d = [defaultdict(int) for _ in range(n + 1)]
# d[0][0] = [0]
for i in range(n):
    a, b = MII()
    tmp = set()
    for j in Set:
        tmp.add(a + j)
        tmp.add(b + j)
        d[i + 1][a + j] = d[i][j] * 10 + 1
        d[i + 1][b + j] = d[i][j] * 10 + 0
    Set = tmp
# print(d)
if s in Set:
    PY()
    tmp = ["T", "H"]
    ans = []
    TH = "0" * (n - len(str(d[n][s]))) + str(d[n][s])
    # print(TH)
    for i in TH:
        ans.append(tmp[int(i)])
    print("".join(ans))
else:
    PN()
