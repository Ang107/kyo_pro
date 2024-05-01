import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
iinput = sys.stdin.readline
deq = deque()
dic = {}
dd = collections.defaultdict(int)

def LIin(x):
    for i in range(x):
        deq.append(int,iinput())

def L2(x,y,z):
    lis2 = [[z] * y for _ in range(x)]
l = []
n = int(input())
for i in range(n):
    l.append(input())

lis2 = [[-1] * n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if 1 <= x < n-1 and 1 <= y < n-1 :
            lis2[x][y] = l[x][y]
        else:
            if ( x < n-1 and y == 0):
                lis2[y][x+1] = l[y][x]
            elif x == 0 :
                lis2[y-1][x] = l[y][x]
            elif  y == n-1:
                lis2[y][x-1] = l[y][x]
            elif x == n-1 :
                lis2[y+1][x] = l[y][x]
#print(l)
#print (lis2)
for i in lis2:
    print()
    for p in i:
        print(p,end='')


