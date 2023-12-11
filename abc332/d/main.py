import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((0, -1), (0, 1), (-1, 0), (1, 0))
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()
# import numpy as np

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照

#文字の差分を取得(文字列長が異なる場合False)
def get_str_difference(s1: str,s2: str) -> int :
    if len(s1) != len(s2):
        return False
    else:
        temp = 0
        for i,j in zip(s1,s2):
            if i != j:
                temp += 1
        return temp

    
h,w = MII()
A = [LMII() for _ in range(h)]
B = [LMII() for _ in range(h)]
A_R = list(zip(*A))
B_R = list(zip(*B))

A_R = list(map(list,A_R))
B_R = list(map(list,B_R))
A1 = set()
B1 = set()
for i in range(h):
    A1.add(tuple(sorted(A[i])))
    B1.add(tuple(sorted(B[i])))

for i in range(w):
    A1.add(tuple(sorted(A_R[i])))
    B1.add(tuple(sorted(B_R[i])))

count_yoko = 0
count_tate = 0
# print(B_R)
if A1 == B1:
    for i in A:
        count2 = inf
        for j in B:
            count1 = 0
            if sorted(i) == sorted(j):
                for k in range(len(i)-1,0,-1):
                    if i[k] != j[k]:
                        for p,q in enumerate(j):
                            if q == i[k]:
                                temp = p
                        for p in range(temp,k):
                            j[p],j[p+1] = j[p+1],j[p]
                            count1 += 1
        count2 = min(count2,count1)
    count_yoko = max(count_yoko,count2)
        
    for i in A_R:
        count2 = inf
        for j in B_R:
            count1 = 0
            if sorted(i) == sorted(j):
                for k in range(len(i)-1,0,-1):
                    if i[k] != j[k]:
                        for p,q in enumerate(j):
                            if q == i[k]:
                                temp = p
                        for p in range(temp,k):
                            j[p],j[p+1] = j[p+1],j[p]
                            count1 += 1
        count2 = min(count2,count1)
    count_tate = max(count_tate,count2)
        
    print(count_yoko+count_tate)
        



else:
    print(-1)







        


