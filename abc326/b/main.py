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
    
while True:
    
    n_str = str(n)
    if int(n_str[0]) * int(n_str[1]) == int(n_str[2]):
        print(n_str[0],n_str[1],n_str[2],sep="")
        exit()
    n += 1

    
    


