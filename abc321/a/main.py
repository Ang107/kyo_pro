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

#a,b = map(int,input().split())
    

if n < 10 :
    print("Yes")
    exit()
n = str(n)
prv = n[0]

for i in range(1,len(n)):
    if prv > n[i]:
        prv = n[i]
    else:
        print("No")
        exit()
print("Yes")


    


