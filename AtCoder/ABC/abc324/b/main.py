import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
import math

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

max_2 = math.log(n, 2)
max_3 = math.log(n,3)

for i in range(int(max_2+1)):
    for j in range(int(max_3+1)):
        ans = (2 ** i) * (3 ** j)

        if ans == n:
            print("Yes")
            exit()
        elif ans > n:
            break
print("No")

#a,b = map(int,input().split())
    

    
    


