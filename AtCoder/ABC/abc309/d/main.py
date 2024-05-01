import sys
from  collections import deque,defaultdict
from itertools import product
from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
deq = deque()
dic = {}
dd = defaultdict()

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]

n1,n2,m = MII()
ab = [LMII() for _ in range(m)]

def get_link_dict(l):
    dd = defaultdict(set)
    for i,j, in l:
        dd[i].add(j)
        dd[j].add(i)
    return dd

dd1 = defaultdict(set)
dd2 = defaultdict(set)
visited1 = set()
visited2 = set()
for a,b in ab:
    if a <= n1:
        dd1[a].add(b)
        dd1[b].add(a)
    else:
        dd2[a].add(b)
        dd2[b].add(a)
ans1 = 0
def bfs1():
    visited = [-1] * n1
    deq = deque()
    deq.append((1,0))
    visited[0] = 0
    while deq:
        temp,dis = deq.popleft()
        # print(deq)
        # print(visited)
        for i in dd1[temp]:
            if visited[i-1] == -1:
                visited[i-1] = dis+1
                deq.append((i,dis+1))
    return visited

def bfs2():
    visited = [-1] * n2
    deq = deque()
    deq.append((n1+n2,0))
    visited[-1] = 0
    while deq:
        temp,dis = deq.popleft()
        # print(temp,dis)
        # print(visited)
        # print(deq)
        for i in dd2[temp]:
            if visited[i-n1-1] == -1:
                visited[i-n1-1] = dis+1
                deq.append((i,dis+1))
    return visited
# def dfs1(n,depth):
#     global ans1
#     for i in dd1[n]:
#         if i not in visited1 and (n1 not in dd1[i] or depth == 0):
#             visited1.add(i)
#             ans1 = max(ans1,depth+1)
#             dfs1(i,depth+1)
# ans2 = 0
# def dfs2(n,depth):
#     global ans2
#     for i in dd2[n]:
#         if i not in visited2 and (n1 not in dd1[i] or depth == 0):
#             visited2.add(i)
#             ans2 = max(ans2,depth+1)
#             dfs2(i,depth+1)

ans1 = max(bfs1())
ans2 = max(bfs2())

# print(ans1,ans2)
print(ans1+ans2+1)

        

