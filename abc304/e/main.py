import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
from pprint import pprint
import heapq
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
dd = defaultdict(list)
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
for i in range(m):
    u,v = MII()
    dd[u].append(v)
    dd[v].append(u)

from sys import stdin
k = II()
xy = [list(map(int, stdin.readline().split())) for _ in range(k)]
q = II()
pq = [list(map(int, stdin.readline().split())) for _ in range(q)]

visited = {}
def dfs(x,num):
    global visited
    deq = deque([x])
    visited[x] = num
    while deq:
        x = deq.pop()
        for i in dd[x]:
            if i not in visited:
                visited[i] = num
                deq.append(i)
temp = 0
for i in range(1,n+1):
    if i not in visited:
        temp += 1
        dfs(i,temp)

not_touch = set()
for i,j in xy:
    not_touch.add((visited[i],visited[j]))
    not_touch.add((visited[j],visited[i]))

for i,j in pq:
    if (visited[i],visited[j]) in not_touch:
        PN()
    else:
        PY()





