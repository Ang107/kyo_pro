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


h1, w1 = MII()
A = [LMII() for _ in range(h1)]
h2, w2 = MII()
B = [LMII() for _ in range(h2)]

for i in product(range(2), repeat=h1):
    i = [p for p, q in enumerate(i) if q == 1]
    for j in product(range(2), repeat=w1):
        # print(i, j)

        j = [p for p, q in enumerate(j) if q == 1]
        # print(i, j)
        if len(i) == h2 and len(j) == w2:
            flag = True
            for p, q in enumerate(i):
                for r, s in enumerate(j):
                    if A[q][s] == B[p][r]:
                        pass
                    else:
                        flag = False
                        break
            if flag:
                PY()
                exit()
        else:
            continue
        # tmp = [[] for _ in range(h1)]
        # print(list(i), list(j))
        # for p in range(h1):
        #     for q in range(w1):
        #         if i[p] == 1 and j[q] == 1:
        #             tmp[p].append(A[p][q])
        # tmp = [i for i in tmp if len(i) > 0]
        # pprint(tmp)
        # if tmp == B:
        #     PY()
        #     exit()

PN()
