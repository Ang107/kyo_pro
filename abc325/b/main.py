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
    global W
    W = {}
    L = []
    for i in range(n):
        w,x = map(int,input().split())
        L.append({x-4,x-3,x-2,x-1,x,x+1,x+2,x+3,x+4})
        W[i] = w
    return L

n = int(input())
wx = for_input(n)

#a,b = map(int,input().split())
    
ans = []
for i in range(0,24):
    a = 0
    for x in range(n):
        if i in wx[x] or i+24 in wx[x] or i-24 in wx[x]:
            a += W[x]
    ans.append(a)
print(max(ans))



