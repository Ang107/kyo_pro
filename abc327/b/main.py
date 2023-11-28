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

b = int(input())
ans = 1
while True:
    ans2 = ans ** ans
    if ans2 == b:
        print(ans)
        exit()
    elif ans2 > b:
        print(-1)
        exit()
    ans += 1




#a,b = map(int,input().split())

    

    
    


