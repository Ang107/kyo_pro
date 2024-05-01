import sys
from collections import deque, defaultdict
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
mod = 998244353
def input(): return sys.stdin.readline().rstrip()
def Pr(*x): return print(*x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill]*l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


                    
n,m,k = MII()
a = []
edge = defaultdict(list)
for i in range(m):
    u,v,a = MII()
    edge[(u,a)].append((v,a))
    edge[(v,a)].append((u,a))
s = set(LMII())
for i in s:
    edge[(i,0)].append((i,1))      
    edge[(i,1)].append((i,0))      


def bfs():
    deq = deque()
    visited = [[inf]*2 for _ in range(n)]
    #頂点、スイッチの状態
    deq.append((1,1))
    visited[0][1] = 0
    # print(visited)
    while deq:
        v,sw = deq.popleft()
        # print(deq)
        # print(visited)
        for n_v,n_sw in edge[(v,sw)]:
            if v != n_v and visited[n_v-1][n_sw] > visited[v-1][sw] + 1:
                visited[n_v-1][n_sw] = visited[v-1][sw] + 1
                deq.append((n_v,n_sw))
            elif v == n_v and visited[n_v-1][n_sw] > visited[v-1][sw]:
                visited[n_v-1][n_sw] = visited[v-1][sw] 
                deq.appendleft((n_v,n_sw))

    return visited

visited = bfs()
ans = []
# pprint(visited)
if visited[-1][0] != inf:
    ans.append(visited[-1][0] )
if visited[-1][1] != inf:
    ans.append(visited[-1][1] )
    
if ans:
    print(min(ans))
else:
    print(-1)

                     
        

     