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
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x): return print(x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照
class Imos:
    def __init__(self,h,w):
        self.l = [[0]*w for _ in range(h)]
        self.h, self.w = h, w
        
    def add_section_from_1(self,a,b,c,d,diff):
        self.l[a-1][b-1] += diff
        if c < self.h:
            self.l[c][b-1] -= diff
        if d < self.w:
            self.l[a-1][d] -= diff
        if c < self.h and d < self.w:
            self.l[c][d] += diff   
    
    def add_section_from_0(self,a,b,c,d,diff):
        self.l[a][b] += diff
        if c < self.h:
            self.l[c+1][b] -= diff
        if d < self.w:
            self.l[a][d+1] -= diff
        if c < self.h and d < self.w:
            self.l[c+1][d+1] += diff    
    
    def get_all(self):
        return self.l       
        
class Prefix_sum_2d:
    def __init__(self,l):
        h,w = len(l),len(l[0])
        tmp = [[0] * w for _ in range(h)]
        for i,j in enumerate(l):
            tmp[i] = list(accumulate(j))
        for i in range(1,h):
            for j in range(w):
                tmp[i][j] = tmp[i-1][j] + tmp[i][j]
        self.prf_sum = tmp
        
    def get_all(self):
        return self.prf_sum
    
    #左上のx,y,右下のx,y = a,b,c,d
    def get_section_from_1(self,a,b,c,d):
        tmp = self.prf_sum[c-1][d-1]
        if a >= 2:
            tmp -= self.prf_sum[a-2][d-1] 
        if b >= 2:
            tmp -= self.prf_sum[c-1][b-2]
        if a >= 2 and b >= 2:
            tmp += self.prf_sum[a-2][b-2]
        return tmp
    
    def get_section_from_0(self,a,b,c,d):
        tmp = self.prf_sum[c][d]
        if a >= 1:
            tmp -= self.prf_sum[a-1][d] 
        if b >= 1:
            tmp -= self.prf_sum[c][b-1]
        if a >= 1 and b >= 1:
            tmp += self.prf_sum[a-1][b-1]
        return tmp

n = II()
imos = Imos(1501,1501)
for i in range(n):
    a,b,c,d = MII()
    imos.add_section_from_0(a,b,c-1,d-1,1)

prf = Prefix_sum_2d(imos.get_all())
tmp = prf.get_all()
ans = 0
for i in range(1501):
    for j in range(1501):
        if tmp[i][j] >= 1:
            ans += 1
# print(imos.get_all())
# print(tmp)
print(ans)
            