import sys
from  collections import deque,defaultdict
from itertools import product
from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
deq = deque()
dic = {}
dd = defaultdict()

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]

    
    


