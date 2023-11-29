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
C = [input() for _ in range(h)]

ans = [0] * min(h,w)
def is_Center(x,y):
    if C[x-1][y-1] == "#" and C[x-1][y+1] == "#" and C[x+1][y-1] == "#" and C[x+1][y+1] == "#" and C[x][y] == "#":
        return True
    else:
        return False

def get_size(x,y):
    temp = 0
    while 0 <= x+temp+1 < h and 0 <= y+temp+1 < w:
        if C[x+temp+1][y+temp+1] == "#":
            temp += 1
        else:
            break
    return temp

for x in range(1,h-1):
    for y in range(1,w-1):
        if is_Center(x,y):
            ans[get_size(x,y)-1] += 1

print(*ans)
