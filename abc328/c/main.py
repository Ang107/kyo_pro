import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
sys.setrecursionlimit(10**7)
deq = deque()
lis = [0]
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

n,q = map(int,input().split())
s = input()
lr = for_input(q)
    
temp = 0
for i in range(1,n):
    if s[i-1] == s[i]:
        temp += 1
    lis.append(temp)


for l,r in lr:
    print(lis[r-1] - lis[l-1])





    


