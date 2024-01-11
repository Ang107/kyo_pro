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

def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill]*l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]

def MII(): return map(int, input().split())
n,q = MII()

a = []
for i in range(n,0,-1):
    a.append((i,0))
    
around4 = ((0,1), (0, -1), (-1, 0), (1, 0))
UDLR = {"U":0,"D":1,"L":2,"R":3}
x,y = 1,0
for i in range(q):
    u,v = input().split()
    if u == "1":
        v = UDLR[v]
        a.append((x+around4[v][0],y+around4[v][1]))
        x += around4[v][0]
        y += around4[v][1]
    if u  == "2":
        print(*a[int(v)*-1])

            
        
    
    