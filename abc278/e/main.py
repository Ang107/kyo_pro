import sys
from collections import deque, defaultdict
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
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
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
mod = 998244353
def input(): return sys.stdin.readline().rstrip()
def Pr(*x): return print(*x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill]*l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]

H,W,N,h,w = MII()
s = set()
A = [LMII() for _ in range(H)]
dd =defaultdict(int)    #個数
for i in range(H):
    for j in range(W):
        s.add(A[i][j])
        dd[A[i][j]] += 1
        
ans = [[0]*(W-w+1) for _ in range(H-h+1)]    
for i in range(0,H-h+1):
    for x in range(h):
        for y in range(w):
            tmp = A[i+x][y]
            dd[tmp] -= 1
            if dd[tmp] == 0:
                s.discard(tmp)
    for j in range(0,W-w+1):
        ans[i][j] = len(s)
        for x in range(i,i+h):
            tmp = A[x][j]
            dd[tmp] += 1
            if dd[tmp] == 1:
                s.add(tmp)
            if j+w == W:
                continue
            tmp = A[x][j+w]
            dd[tmp] -= 1
            if dd[tmp] == 0:
                s.discard(tmp)
    s = set()
    dd =defaultdict(int) 

    for p in range(H):
        for q in range(W):
            s.add(A[p][q])
            dd[A[p][q]] += 1


for i in ans:
    print(*i)