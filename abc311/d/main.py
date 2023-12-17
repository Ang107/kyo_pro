import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
from pprint import pprint
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))
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


n,m = MII()
s = [list(input()) for _ in range(n)]
visited = [[[-1,-1,-1,-1]  for _ in range(m)] for _ in range(n) ]

ans = set()
ans1 = [i[:] for i in s]

def dfs(x,y,v):
    # print(x,y)
    temp = -1
    ans.add((x,y))
    ans1[x][y] = "x"
    if v == -1:
        for i,j in around4:
            temp += 1
            # print(s[x+i][y+j],visited[x][y][temp])
            if s[x+i][y+j] == "." and visited[x][y][temp] == -1:

                visited[x][y][temp] = 1
                dfs(x+i,y+j,temp)
    else:
        if s[x+around4[v][0]][y+around4[v][1]] == ".":
            dfs(x+around4[v][0],y+around4[v][1],v)
        else:
            dfs(x,y,-1)
    
dfs(1,1,-1)

from pprint import pprint
# pprint(ans1)
print(len(ans))
