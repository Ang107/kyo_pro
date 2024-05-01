import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
#from sortedcontainers import SortedSet, SortedList, SortedDict
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
XY = [LMII() for _ in range(n)]

dp = Ary2(2,n+1,0)

dp[0][0] = 0
dp[0][1] = 0

for i in range(n):
    for j in range(2):
        #解毒
        if XY[i][0] == 0:
            #健康
            if j == 0:
                dp[i+1][j] = max(dp[i][0],dp[i][0]+XY[i][1],dp[i][1]+XY[i][1])
            #不調
            else:
                dp[i+1][j] = dp[i][1]
        #毒
        else:
            #健康
            if j == 0:
                dp[i+1][j] = dp[i][0]
            #不調
            else:
                dp[i+1][j] = max(dp[i][1],dp[i][0]+XY[i][1])

print(max(dp[-1]))
        
