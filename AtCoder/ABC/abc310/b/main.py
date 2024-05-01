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
        deq.append(tuple(map(int,iinput().split())))

def L2(x,y,z):
    lis2 = [[z] * y for _ in range(x)]

n,m = map(int,input().split())
l = []
for i in range(n):
    l.append(tuple(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if l[i][0] > l[j][0] :
            if l[i][1] <= l[j][1]  :
                co = 0
                for a in l[i][2:]:
                    if  a in set(l[j][2:]):
                        co += 1
                if co == l[i][1]:
                    print("Yes")
                    #print(i,j)
                    exit()

        elif l[i][0] == l[j][0] :
            if l[i][1] < l[j][1]  :
                co = 0
                for a in set(l[i][2:]):
                    
                    if  a in set(l[j][2:]):
                        co += 1
                if co == l[i][1]:
                    #print(i,j)
                    print("Yes")
                    exit()

print("No")
 


