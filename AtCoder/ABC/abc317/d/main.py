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


Pr = lambda x : print(x)
PY = lambda : print("Yes")
PN = lambda : print("No")
I = lambda : input()
II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照


n = II()
l = []
l1 = []
giseki = 0
for i in range(n):
    x,y,z = MII()
    l.append((x,y,z))
    if x < y:
        temp = (x+y)//2 
        temp =  y - temp
        l1.append((temp,z))
    else:
        giseki += z


need = max(0,sum([z for x,y,z in l]) // 2 + 1 - giseki)

dp = [[inf] * (need+1) for _ in  range(len(l1)+1)]

# print(need,l1)
for i in dp:
    i[0] = 0

# print(dp)
for i in range(len(l1)):
    for j in range(1,need+1):
        dp[i+1][j] = min(dp[i][j],dp[i][max(0,j-l1[i][1])]+l1[i][0])

# print(dp)
print(dp[-1][-1])


    
    


