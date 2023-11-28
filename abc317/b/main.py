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
a = set(map(int,input().split()))
#a,b = map(int,input().split())
a_max = max(a)
a_min = min(a)    
nlist = set(range(a_min,a_max+1,1))
print(*(nlist - a))
    
    


