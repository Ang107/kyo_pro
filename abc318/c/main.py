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

n,d,p= map(int,input().split())
f = list(map(int,input().split()))

f.sort(reverse=True)

max_pas = n // d + 1
tinum = max_pas
l1 = []

f.extend([0]*(d+1))

for i in range(0,n+d+10,d):
    l1.append(sum(f[i:i+d]))

for i in range(len(l1)):

    if p > l1[i]:
        tinum = i 
        break


if tinum == max_pas:
    print(tinum * p)
else:
    ans = tinum * p + sum(l1[tinum:])
    print(ans)


    
    
    


