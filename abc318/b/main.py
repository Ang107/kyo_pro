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

n = int(input())

#a,b = map(int,input().split())
    
for i in range(n):
    k = tuple(map(int,input().split()))
    l.append(k)
    
s = set()    
for i in l:
    for x in range(i[0],i[1]):
        for y in range(i[2],i[3]):
            s.add((x,y))

print(len(s))





