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
s = input()
temp = [None] * 2
lr = []
if "-" not in s:
    print(-1)
    exit()

for i,x in enumerate(s):
    if x == "o":
        if temp[0] != None:
            temp[1] = i
        else:
            temp[0] = i
            temp[1] = i
    else:
        if temp[0] != None:
            lr.append(temp)
        temp = [None] * 2
if temp[0] != None:
    lr.append(temp)
# print(lr)
ans = -1
for l,r in lr:
    ans = max(r - l + 1,ans)

print(ans)



    


