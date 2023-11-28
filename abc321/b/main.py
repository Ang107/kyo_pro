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

n,x = map(int,input().split())
    
a = tuple(map(int,input().split()))
    

for i in range(101):
    ai = list(a)
    ai.append(i)
    ai.sort()
    if sum(ai[1:-1]) >= x:
        print(i)
        exit()
print("-1")

