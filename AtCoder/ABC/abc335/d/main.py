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

def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill]*l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]

around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
def II(): return int(input())
n = II()

ans = [["T"]*n for _ in range(n)]

def guru(x,y,vec):
    num = ans[x][y]
    while is_not_Index_Er(x+around4[vec][0],y+around4[vec][1],n,n) and ans[x+around4[vec][0]][y+around4[vec][1]] == "T":
        ans[x+around4[vec][0]][y+around4[vec][1]] = num+1
        num += 1
        x,y = x+around4[vec][0],y+around4[vec][1]
    return x,y

ans[0][0] = 1 
x,y = 0,0
for i in range(n//2):
    x,y = guru(x,y,3)
    x,y = guru(x,y,1)
    x,y = guru(x,y,2)
    x,y = guru(x,y,0)

for i in ans:
    print(*i)
    
    
        
        
        
    