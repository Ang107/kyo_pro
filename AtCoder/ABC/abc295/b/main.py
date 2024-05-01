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
dd = defaultdict()

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照
    
    
r,c = MII()
b = [list(input()) for _ in range(r)]



ans = copy.deepcopy(b)

def dfs(x,y,d):
    ans[x][y] = "."
    if d != 0:
        for i,j in around4:
            if 0 <= x+i < r and 0 <= y+j < c:
                dfs(x+i,y+j,d-1)

for i in range(r):
    for j in range(c):
        if b[i][j] != "#" and b[i][j] != ".":
            dfs(i,j,int(b[i][j]))

for i in ans:
    print("".join(i))



