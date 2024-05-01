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

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照
    
    
n,m,d = MII()
A = LMII()
B = LMII()
A.sort()
B.sort()
ans = -1
for i in A:
    temp = bisect_left(B,i)
    # print(i,B[temp])
    if 0 <= temp-1 < m:
        if i - B[temp-1] <= d:
            ans = max(ans,i+B[temp-1])
    if 0 <= temp < m:
        if B[temp] - i <= d:
            ans = max(ans,i+B[temp])

for i in B:
    temp = bisect_left(A,i)
    # print(i,B[temp])
    if 0 <= temp-1 < n:
        if i - A[temp-1] <= d:
            ans = max(ans,i+A[temp-1])
    if 0 <= temp < n:
        if A[temp] - i <= d:
            ans = max(ans,i+A[temp])


print(ans)

