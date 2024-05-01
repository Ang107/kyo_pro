#  if you win, you live. you cannot win unless you fight.
import sys
from sys import stdin, setrecursionlimit
# fd=open("cses.txt")
# sys.stdin=fd
input = stdin.readline
import heapq
rd = lambda: map(lambda s: int(s), input().strip().split())
rdone = lambda: map(lambda s: int(s) - 1, input().strip().split())
ri = lambda: int(input())
rs = lambda: input().strip()
from collections import defaultdict as unsafedict, deque, Counter as unsafecounter
from bisect import bisect_left as bl, bisect_right as br
from random import randint
from math import gcd, floor, log2, factorial, radians, sin, cos, ceil,sqrt

n,m,k=rd()
g=unsafedict(list)
for i in range(m):
    x,y,w=rdone()
    g[x].append((y,w))
    g[y].append((x,w))
ts=list(rd())
s=[0]*n
for i in ts:
    s[i-1]=1
q=deque([(0,0)])
dis=[[float("inf")]*2 for i in range(n)]
dis[0]=[0,float("inf")]
# print(dis)
while q:
    t,w=q.popleft()
    for i,p in g[t]:
        if w%2==p%2:
            # print(p,i,w,t,dis[p%2],dis[w%2])
            if dis[i][p%2]>dis[t][w%2]+1:
                dis[i][p%2]=dis[t][w%2]+1
                q.append((i,p%2))
        else:
            if s[t]:
                # print(t,i)
                if dis[i][p%2]>dis[t][w]+1:
                    dis[i][p%2]=dis[t][w]+1
                    q.append((i,p%2))

ans=min(dis[-1])
if ans==float("inf"):
    print(-1)
else:
    print(ans)
