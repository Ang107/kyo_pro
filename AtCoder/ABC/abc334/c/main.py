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


n,k = MII()
a = set(LMII())
s = []
for i in range(1,n+1):
    s.append(i)
    if i not in a:
        s.append(i)
len_s = len(s)
ans = 0
if len(s) % 2 == 0:
    for i in range(0,len_s,2):
        ans += s[i+1] - s[i]

else:
    g_r = [0]
    k_r = [0]
    temp = 0
    for i in range(0,len_s-1,2):
        temp += s[i+1] - s[i]
        g_r.append(temp)
    temp = 0
    for i in range(1,len_s,2):
        temp += s[i+1] - s[i]
        k_r.append(temp)
    ans = inf
    for i in range(len_s):
        if i % 2 == 0:
            ans = min(g_r[i // 2] + k_r[-1] - k_r[i // 2],ans)

print(ans)
        




    