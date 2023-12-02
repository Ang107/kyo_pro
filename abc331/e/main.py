import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((0, -1), (0, 1), (-1, 0), (1, 0))
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict(set)

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照
    
    
n,m,l = MII()
a = LMII()
b = LMII()


for i in range(l):
    c,d = MII()
    dd[c-1].add(d-1) 




sorted_b = SortedList(b)

ans = 0
# print(dd)
# for k,v in dd.items():
#     for i in v:
#         sorted_b.discard(b[i])
#     ans = max(ans,a[k] + sorted_b[-1])
#     for i in v:
#         sorted_b.add(b[i])

sorted_b.add(0)

for i in range(n):
    # print(i,dd[i],a[i])
    for j in dd[i]:
        sorted_b.discard(b[j])
        # print(sorted_b)
    ans = max(ans,a[i] + sorted_b[-1])
    for j in dd[i]:
        sorted_b.add(b[j])
        # print(sorted_b)

print(ans)

    





