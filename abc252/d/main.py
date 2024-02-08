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


n = II()
a = LMII()
a.sort()
dd = defaultdict(int)
for i in a:
    dd[i] += 1
# print(dd)
ans = n * (n - 1) * (n - 2) // 6
for i, j in dd.items():
    tmp = 0
    tmp += j * (j - 1) * (n - j) // 2
    tmp += j * (j - 1) * (j - 2) // 6
    ans -= tmp
print(ans)

# l = []
# for i in range(1, a[-1] + 1):
#     if i == 1:
#         l.append(0)
#     else:
#         l.append(l[-1] + dd[i - 1])


# r = []
# for i in range(a[-1], 0, -1):
#     if i == a[-1]:
#         r.append(0)
#     else:
#         r.append(r[-1] + dd[i + 1])

# r = r[::-1]

# ans = 0
# for i in a:
#     ans += l[i - 1] * r[i - 1]

# print(ans)
