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

n = II()
A = LMII()
q = II()
lr = [LMII() for _ in range(q)]

temp = 0
A1 = []
for i,x in enumerate(A):
    if i % 2 == 0 and i >= 2:
        temp += A[i] - A[i-1]
    A1.append(temp)

def get_sum_sleep(x):
    temp = bisect_left(A,x)
    if temp % 2 == 0:
        # print(A1[temp-1],x,A[temp-1])
        return A1[temp-1] + x - A[temp-1]
    else:
        return A1[temp-1]
# print(A1)
for l,r in lr:
    print(get_sum_sleep(r)-max(get_sum_sleep(l),0))

    







