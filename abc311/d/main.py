import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**9)
iinput = sys.stdin.readline
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

#n = int(input())

n,m = map(int,input().split())
for i in range(n):
    l.append(input())
touha = [[-1 for _ in range(m)] for _ in range(n)]    
co = 1

def up(x,y):
    global co
    if touha[x][y] == -1:
        co += 1
        touha[x][y] = 1
    if l[x-1][y] == "." :
            up(x-1,y)
    elif l[x-1][y] == "#":
        tnsk(x,y)

def down(x,y):
    global co
    if touha[x][y] == -1:
        co += 1
        touha[x][y] = 1
    if l[x+1][y] == "." :
        down(x+1,y)
    elif l[x+1][y] == "#":
        tnsk(x,y)

def left(x,y):
    global co
    if touha[x][y] == -1:
        co += 1
        touha[x][y] = 1
    if l[x][y-1] == "." :
        left(x,y-1)
    elif l[x][y-1] == "#":
        tnsk(x,y)

def right(x,y):
    global co
    if touha[x][y] == -1:
        co += 1
        touha[x][y] = 1
    if l[x][y+1] == "." :
        right(x,y+1)
    elif l[x][y+1] == "#":
        tnsk(x,y)
  
def tnsk(x,y):
    global co
    if l[x-1][y] =="."and touha[x-1][y] == -1:
        up(x-1,y)
    if l[x+1][y] =="."and touha[x+1][y] == -1:
        down(x+1,y)
    if l[x][y-1] =="."and touha[x][y-1] == -1:
        left(x,y-1)
    if l[x][y+1] =="."and touha[x][y+1] == -1:
        right(x,y+1)




touha[1][1] = 1
tnsk(1,1)
print(co)
