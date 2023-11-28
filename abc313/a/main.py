import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
iinput = sys.stdin.readline
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

n = int(input())
p = list(map(int,input().split()))
#a,b = map(int,input().split())
if len(p) != 1:

    np =p[1:]    
    maxnp = max(np)

    if maxnp < p[0]:
        print(0)
    else:

        print(maxnp-p[0]+1)  
else:
    print(0)
    


