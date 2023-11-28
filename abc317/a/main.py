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

n,h,x = map(int,input().split())
p = list(map(int,input().split()))

for i in range(n):
    if h + p[i] >= x:
        print(i + 1)
        exit()
    

    
    


