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
s = input()
#a,b = map(int,input().split())
abc = "ABC"
k = 0    
for i in range(n):
    if s[i] == abc[k]:
        k += 1
    else:
        if s[i] == "A":
            k = 1
        else:
            k = 0
    
    if k == 3:
        print(i-1)
        exit()

print(-1)
    
    


