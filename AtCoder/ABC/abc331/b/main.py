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
    
n,s,m,l = MII()

# ans = inf

# for i in range(18):
#     for j in range(18):
#         for k in range(18):
#             if 6 * i + 8 * j + 12 * k >= n:
#                 ans = min(ans,s*i+m*j+l*k)

# print(ans)

# dp = [inf] * (n+1)
# dp[0] = 0

# for i in range(1,n+1):
#     if i <= 6:
#         dp[i] = min(s,m,l)
#     else:
#         dp[i] = min(dp[i-6]+min(s,m,l),dp[max(i-8,0)]+min(m,l),dp[max(i-12,0)]+l)

# print(dp[-1])

cospa = s/6,m/8,l/12
sml_num = [6,8,12]
sml_price = [s,m,l]
cospa_max = max(s/6,m/8,l/12)
temp = cospa.index(cospa_max)
ans = 0
while n > 100:
    n -= sml_num[temp]
    ans += sml_price[temp]

temp = inf
for i in range(5):
    for j in range(4):
        for k in range(3):
            if 6*i + 8*j + 12*k >= n:
                temp = min(temp,s*i + m*j + l*k)

print(ans+temp)








