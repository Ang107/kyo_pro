import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
from pprint import pprint
from heapq import heapify,heappop,heappush
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
dd = defaultdict()
mod = 998244353

Pr = lambda x : print(x)
PY = lambda : print("Yes")
PN = lambda : print("No")
I = lambda : input()
II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照

a,m,l,r = MII()

temp = r - l
if l <= a <= r:
    st = a
elif a < l:
    st = a + m*math.ceil((l-a) // m)
elif r < a:
    st = a - m*math.ceil((a-r) // m)

ans = ((a-l)//m + (r-a)//m +1)
print(ans)
# if a < l:
#     flagl = False
#     while a <= r:
#         if not flagl and l <= a:
#             flagl = True
#             count = 0
#         if flagl :
#             count += 1
#         a += m
# elif l <= a <= r:
#     count = 0
#     al,ar = a,a
#     while l <= al:
#         count += 1
#         al -= m
#     while ar <= r:
#         count += 1
#         ar += m
#     count -= 1
# elif r < a:
#     flagr = False
#     while l <= a:
#         if not flagr and a <= r:
#             flagr = True
#             count = 0
#         if flagr :
#             count += 1
#         a -= m 

# print(count)









