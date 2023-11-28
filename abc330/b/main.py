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

#n = int(input())

n,l,r = map(int,input().split())
a = list(map(int,input().split()))
li = []
for i in a:
    if i <= l:
        li.append(l)
    elif i >= r:
        li.append(r)
    else:
        li.append(i)
print(*li)


