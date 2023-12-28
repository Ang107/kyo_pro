# import sys
# import collections
# from collections import deque
# from copy import deepcopy
# from itertools import product
# sys.setrecursionlimit(10**7)
# deq = deque()
# l = []
# dic = {}
# dd = collections.defaultdict(int)

# def array2(i,j,element):
#     return [[element] * j for _ in range(i)]

# def sinnsuu(s,c):
#     l = []
#     binc = bin(c)
#     for i in range(-1,-len(str(binc))-1,-1):
#         if i == "1":
#             l.append(dic[s*(-i)])
#     return(l)
    
# def for_input(n):
#     dd = collections.defaultdict(int)
#     for _ in range(n):
#         s,c = map(int,input().split())
        
#         for i in range(sinnsuu(s,c)):
#             dd[i] += 1

#     return 

# n = int(input())

# sc = for_input(n)
# #a,b = map(int,input().split())
# sl_sum = sum(sc.values())

# sc = dict(sorted(sc.items(), key=lambda x: x[0]))
# def gattai(s,c):
#     if c % 2 == 0:
#         return(s*2,c//2,0)
#     else:
#         return(s*2,c//2,1)
# tuika = {}
# while True:
#     prev = sl_sum
#     for s,c in sc.items():
#         if c > 1:
#             saizu,hetta,nokotta = gattai(s,c)
#             sl_sum -= hetta
#             if saizu in sc.keys():
#                 sc[saizu] += hetta
#             else:
#                 tuika[saizu] = hetta
#             sc[s] = nokotta
#     new = sl_sum
#     if new == prev:
#         print(sl_sum)
#         exit()
#     for s,c in tuika.items():
#         sc[s] = c
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
n = II()
for i in range(n):
    s,c = MII()
    dd[s] += c

dd_sorted = dict(sorted(dd.items(),key = lambda x:x[0]))
heap = list(dd_sorted.keys())
heapq.heapify(heap)

ans = 0
while heap:
    min = heapq.heappop(heap)
    # print(min,dd[min] % 2)
    ans += dd[min] % 2
    if min*2 not in dd and dd[min] // 2 >= 1:
        heapq.heappush(heap,min*2,)
    
    dd[min*2] += dd[min] // 2

print(ans)



    
    


