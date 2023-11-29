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
    
    
snuke ="snuke"
h,w = map(int,input().split())
S = [input() for _ in range(h)]
around4 = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),)
def is_snuke(x,y):
    for i,j in around4:
        for p in range(1,5):
            if 0 <= x+p*i < h and 0 <= y+p*j < w:
                if S[x+p*i][y+p*j] == snuke[p]:
                    if p == 4:
                        for v in range(5):
                            print(x+v*i+1,y+v*j+1)
                        exit()
                else:
                    break
            else:
                break
    return False
        


for x in range(h):
    for y in range(w):
        if S[x][y] == "s":
            is_snuke(x,y)
                

