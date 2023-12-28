import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
from pprint import pprint
import heapq
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1)) #上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict(int)
mod = 998244353

Pr = lambda x : print(x)
PY = lambda : print("Yes")
PN = lambda : print("No")
I = lambda : input()
II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照

from sys import stdin
w,h = MII()
n = II()
pq = [list(map(int, stdin.readline().split())) for _ in range(n)]
A = II()
a = LMII()
B = II()
b = LMII()

# itigo = [[0]*(B+1) for _ in range(A+1)]
itigo = defaultdict(int)
a.sort();b.sort()

for p,q in pq:
    x = bisect_left(a,p)
    y = bisect_left(b,q)
    itigo[(x,y)] += 1

if len(itigo) == (A+1)*(B+1):  
    print(min(itigo.values()),max(itigo.values()))
else:
    print(0,max(itigo.values()))


    


