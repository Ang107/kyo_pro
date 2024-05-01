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


n, t = input().split()
n = int(n)
l, r = (
    [0] * (5 * 10**5 + 10),
    [0] * (5 * 10**5 + 10),
)
s = [input() for _ in range(n)]
l_num, r_num = [0] * (5 * 10**5 + 10), [0] * (5 * 10**5 + 10)
for idx, i in enumerate(s):
    tmp = 0
    for j in i:
        if tmp >= len(t):
            break
        if j == t[tmp]:
            tmp += 1
    l_num[idx] = tmp
    l[tmp] += 1
t = t[::-1]
for idx, i in enumerate(s):
    tmp = 0
    for j in i[::-1]:
        if tmp >= len(t):
            break
        if j == t[tmp]:
            tmp += 1
    r_num[idx] = tmp
    r[tmp] += 1
prf_l = list(accumulate(l))
prf_r = list(accumulate(r[::-1]))[::-1]

# print(l, r)
# print(l_num, r_num)
# print(prf_l, prf_r)
ans = 0
for i in range(n):
    tmp = prf_r[len(t) - l_num[i]]

    ans += tmp
print(ans)
