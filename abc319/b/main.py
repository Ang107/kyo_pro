import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
sys.setrecursionlimit(10**7)

deq = deque()
jl = []
dic = {}
dd = collections.defaultdict(int)

n = int(input())
ans = ""
for i in range(1,10):
    if n % i == 0:
        jl.append(i)

for i in range(n+1):
    minlist = []
    for j in jl:
        if i % (n/j) == 0:
            minlist.append(j)
    if len(minlist) > 0:
        ans += str(min(minlist))
    else:
        ans += "-"
    
print(ans)

        

#a,b = map(int,input().split())
    

    
    


