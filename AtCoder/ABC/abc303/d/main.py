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

x,y,z = MII()
s = input()

dp = Ary2(2,len(s)+1,0)

dp[0][0] = 0
dp[0][1] = z
for i in range(len(s)):
    for j in range(2):
        #デフォルト小文字
        if j == 0:
            if s[i] == "a":
                dp[i+1][j] = min(dp[i][0]+x,dp[i][1]+z+x)
            else:
                dp[i+1][j] = min(dp[i][0]+y,dp[i][1]+z+y)
        #デフォルト大文字
        else:
            if s[i] == "a":
                dp[i+1][j] = min(dp[i][0]+z+y,dp[i][1]+y)
            else:
                dp[i+1][j] = min(dp[i][0]+z+x,dp[i][1]+x)

print(min(dp[-1]))

