import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
sys.setrecursionlimit(10**7)

deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

#n = int(input())

n,k,p = map(int,input().split())
    
for i in range(n):
    l.append(list(map(int,input().split)))


for i in l:
    for p in range(1,k+1):
        dd[p] += i[p]
    
if min(dd.values()) < p:
    print(-1)
    exit()
else:
    pass

amari = []
for i in dd.values():
    amari.append(i - p)

for i in range(n):
    l[i].append(sum(l[i][1:])/l[i][0])

l_s = sorted(l,reverse=True,key=lambda x: x[-1])



    
    


    
    


