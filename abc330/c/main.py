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

#a,b = map(int,input().split())
    
d =int(input())
limit = int(d ** (1/2))
ans = []

for i in range(limit,-1,-1):
    temp = int((d - i ** 2) ** (1/2))
    temp1 = abs(i ** 2 + temp ** 2 - d)
    temp2 = abs(i ** 2 + (temp+1) ** 2 - d)
    # print(i,temp,temp1,temp2)
    ans.append(int(min(temp1,temp2)))
    # temp_min = 10** 12
    # for j in range(0,int(limit//2)+1):
    #     temp = i ** 2 + j ** 2 - d
    #     # print(i,j,temp)
    #     temp_min = min(temp_min,abs(temp))
    #     if temp > 0:
    #         break
    # ans.append(temp_min)

print(min(ans))
        

    
    


21