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

#a,b = map(int,input().split())
syouriList = {}
for i in range(n):
    k = input()
    syouri = 0
    for j in k:
        if j == "o":
            syouri += 1
    syouriList[i+1] = syouri

sortlist = sorted(syouriList.items(),key=lambda x:x[1],reverse=True)

for i in sortlist:
    print(i[0],end=" ")

    
    


