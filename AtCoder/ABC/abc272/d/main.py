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

n,m = MII()
bord = [[-1]*n for _ in range(n)]
bord[0][0] = 0
x,y = 0,0
diff = set()
for i in range(m+10):
    a = i 
    b = (m - a**2) 
    if b < 0 :
        continue
    b = b ** 0.5
    if b == int(b):
        b = int(b)
        for j in [1,-1]:
            for k in [1,-1]:
                diff.add((j*a,k*b))

def bfs():
    deq = deque()
    deq.append((0,0))
    while deq:
        x,y = deq.popleft()
        for i,j in diff:
            if x+i in range(n) and y+j in range(n) and bord[x+i][y+j] == -1:
                deq.append((x+i,y+j))
                bord[x+i][y+j] = bord[x][y] + 1

bfs()
for i in bord:
    print(*i)
