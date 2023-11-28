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

x,y = map(int,input().split())

if x > y:
    if x - y <= 3:
        print("Yes")
    else:
        print("No")
else:
    if y - x <= 2:
        print("Yes")
    else:
        print("No")
    

    
    


