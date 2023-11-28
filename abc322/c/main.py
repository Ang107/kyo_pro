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

n,m = map(int,input().split())
    
a = list(map(int,input().split()))
sa_l = []
if not a[0]-1 == 0:
    sa_l.append(a[0]-1)

for i in range(1,m):
    sa_l.append(a[i] - a[i-1] - 1)

k = 0
i = 0
a = set(a)
while True:
    if i+1 in a:
        i += 1
        print(0)
    else:
        for p in range(sa_l[k],0,-1):
            print(p)
            i += 1
        k += 1
    if i == n:
        break

    
    


