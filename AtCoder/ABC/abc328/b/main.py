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

def array2(i,j,element):
    return [[element] * j for _ in range(i)]

def for_input(n):
    L = []
    for _ in range(n):
        L.append(tuple(map(int,input().split())))
    return L

n = int(input())
d = list(map(int,input().split()))
#a,b = map(int,input().split())
ans = 0
for m in range(1,n+1):
    # print("m:",m)
    for day in range(1,d[m-1]+1):
        if len(set(str(m))) == 1:
            if str(m) == str(day) or str(m)+str(m) == str(day) or str(m) == str(day)+str(day) or str(m)+str(m) == str(day)+str(day) :
                # print(m,day)
                ans+= 1
print(ans)


    
    


