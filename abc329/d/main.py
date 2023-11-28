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
dd_set = collections.defaultdict(set)

def array2(i,j,element):
    return [[element] * j for _ in range(i)]

def for_input(n):
    L = []
    for _ in range(n):
        L.append(tuple(map(int,input().split())))
    return L

#n = int(input())

n,m = map(int,input().split())
a = list(map(int,input().split()))
l = [0] * n
max_num = 0
min_num = 10 ** 6
d = {}
for i in a:
    dd[i] += 1
    if dd[i] not in dd_set.keys():
        dd_set[dd[i]].add(i)
        max_num = dd[i]
        d[dd[i]] = i
        print(i)
    else:
        dd_set[dd[i]].add(i)
        max_num = max(max_num,dd[i])
        d[dd[i]] = min(d[dd[i]],i)
        print(d[max_num])

    



    


    


