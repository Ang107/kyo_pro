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
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x): return print(x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


def bfs(u):
    visited = defaultdict(int)
    r = defaultdict(int)
    visited[u] = 0
    r[u] = a[u-1]
    deq = deque([u])
    while deq:
        x = deq.popleft()
        for i in can_go[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                r[i] = max(r[i],r[x] + a[i-1])
                deq.append(i)
            elif visited[i] == visited[x] + 1:
                r[i] = max(r[i],r[x] + a[i-1])
    return visited,r


            
    
n = II()
a = LMII()
can_go = defaultdict(list)

for i in range(n):
    s = input()
    for j in range(n):
        if s[j] == "Y":
            can_go[i+1].append(j+1)

q = II()
visited_list = {}
r_list = {}
for i in range(1,n+1):
    visited_list[i],r_list[i] = bfs(i)
    
for i in range(q):
    u,v = MII()
    visited,r = visited_list[u][v],r_list[u][v]
    # visited,r = bfs(u,v)
    # get_max_r(u,v,dis_p)
    if visited == 0:
        print("Impossible")
    else:
        print(visited,r)
        

    