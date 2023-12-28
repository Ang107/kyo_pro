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

h,w = MII()
s = [input() for _ in range(h)]

visited = set()
dd = defaultdict(set)
def dfs(x,y,g):
    deq = deque([(x,y)])
    visited.add((x,y))
    dd[(x,y)] = g
    while deq:
        x,y = deq.pop()
        for i,j in around4:
            if is_not_Index_Er(x+i,y+j,h,w):
                if s[x+i][y+j] == "#" and (x+i,y+j) not in visited:
                    visited.add((x+i,y+j))
                    dd[(x+i,y+j)] = g
                    deq.append((x+i,y+j))
temp = 0

for i in range(h):
    for j in range(w):

        if s[i][j] =="#" and (i,j) not in visited:
            temp += 1
            dfs(i,j,temp)

ans = 0
ren = temp

num = 0
for i in range(h):
    for j in range(w):
        if s[i][j] ==".":
            num += 1
            l = set()
            for x,y in around4:
                if is_not_Index_Er(x+i,y+j,h,w):
                    if s[x+i][y+j] == "#":
                        l.add(dd[(x+i,y+j)])
            if l:
                ans += (ren - len(l) + 1) 
            else:
                ans += ren + 1

denominator = pow(num, -1, mod)
print(ans * denominator % mod)
            
