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

h,w = MII()
S = [input() for _ in range(h)]     
snuke = "snuke"   

def bfs():
    visited = set()
    around4 = ((-1,0),(1,0),(0,-1),(0,1))
    deq = deque()
    visited.add((0,0))
    deq.append((0,0,0))
    while deq:
        # print(deq)
        x,y,n = deq.popleft()
        for i,j in around4:
            if 0 <= x+i < h and 0 <= y+j < w:
                if S[x+i][y+j] == snuke[(n+1) % 5] and (x+i,y+j) not in visited:
                    visited.add((x+i,y+j))
                    deq.append((x+i,y+j,n+1))
                    if x+i == h-1 and y+j == w-1:
                        print("Yes")
                        exit()

bfs()
print("No")
            


