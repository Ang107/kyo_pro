import sys
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import deque
from copy import deepcopy
from itertools import product
sys.setrecursionlimit(10**7)
deq = deque()
l = []
dic = {}


def array2(i,j,element):
    return [[element] * j for _ in range(i)]

def for_input(n):
    L = []
    for _ in range(n):
        L.append(tuple(map(int,input().split())))
    return L

#n = int(input())
dd = defaultdict(int)
n,q = map(int,input().split())
A = list(map(int,input().split()))

ix = [list(map(int,input().split())) for _ in range(q)]

for i in A:
    dd[i] += 1
ss = SortedSet()
for i in range(2*10**5+1):
    if dd[i] == 0:
        ss.add(i)
# print(ss)
for i,x in ix:
    temp = A[i-1]
    A[i-1] = x
    dd[temp] -= 1
    dd[x] += 1
    if dd[temp] == 0:
        ss.add(temp)
    if dd[x] == 1:
        ss.discard(x)
    print(ss[0])

    
    

    
    


