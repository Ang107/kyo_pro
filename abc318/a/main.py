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

n,m,p = map(int,input().split())


if n < m :
    print(0)
else:
 ans = 1
 ans += (n-m)//p
 print(ans)


    
    


