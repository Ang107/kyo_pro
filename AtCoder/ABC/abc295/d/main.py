import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
import copy
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
dd = defaultdict(int)

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照

s = list(map(int,list(input())))
l =[[0] * 10 ]
d = defaultdict(int)
for i in range()
# print(s)
# print(l)
# for i,j in enumerate(s):
#     temp = l[i][:]
#     l.append(temp)
#     l[i+1][j] = (l[i+1][j]+1) % 2
#     # print(l)


# for i in l:
#     dd[tuple(i)] += 1
# ans = 0
# for i in dd.values():
#     if i >= 2:
#         ans += (i*(i-1))//2
# # print(l)
# # print(dd)
# print(ans)





