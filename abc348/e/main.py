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
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

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
X = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = MII()
    u -= 1
    v -= 1
    X[u].append(v)
    X[v].append(u)

c = LMII()
P = [-1] * n
Q = deque([0])
R = []
while Q:
    i = deque.popleft(Q)
    R.append(i)
    for a in X[i]:
        if a != P[i]:
            P[a] = i
            X[a].remove(i)
            deque.append(Q, a)

##### Settings
unit = 1
merge = lambda a, b: a + b
adj_bu = lambda a, i: a + 1
adj_td = lambda a, i, p: a + 1
adj_fin = lambda a, i: a
#####

ME = [unit] * n
XX = [0] * n
TD = [unit] * n
for i in R[1:][::-1]:
    XX[i] = adj_bu(ME[i], i)
    p = P[i]
    ME[p] = merge(ME[p], XX[i])
XX[R[0]] = adj_fin(ME[R[0]], R[0])

# print("ME =", ME) # Merge before adj
# print("XX =", XX) # Bottom-up after adj

for i in R:
    ac = TD[i]
    for j in X[i]:
        TD[j] = ac
        ac = merge(ac, XX[j])
    ac = unit
    for j in X[i][::-1]:
        TD[j] = adj_td(merge(TD[j], ac), j, i)
        ac = merge(ac, XX[j])
        XX[j] = adj_fin(merge(ME[j], TD[j]), j)

# print("TD =", TD) # Top-down after adj
# print("XX =", XX) # Final Result

print(*XX, sep="\n")
