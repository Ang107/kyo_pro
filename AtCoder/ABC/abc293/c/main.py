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
    
h,w = MII()
A = [LMII() for _ in range(h)]


deq=deque([(0,0,set())])
around2 = ((0,1),(1,0))
ans = 0
def bfs():
    global ans
    while deq:
        x,y,visited = deq.popleft()
        if x==h-1 and y==w-1:
            # print(visited | {A[x][y]})
            if len(visited | {A[x][y]})  == h + w - 1:
                ans += 1
        for i,j in around2:
            #範囲外参照の確認
            if 0<= x+i < h and 0<= y+j < w: 
                deq.append((x+i,y+j,visited | {A[x][y]}))
bfs()           
print(ans)