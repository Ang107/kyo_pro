import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
sys.setrecursionlimit(10**7)
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(list)

def array2(i,j,element):
    return [[element] * j for _ in range(i)]




#n = int(input())

n,m = map(int,input().split())
a = list(map(int,input().split()))

pointdic = {}    
s = []

for i in range(n):
    score = i+1
    k = input()
    s.append(k)
    for j in range(m):
        if k[j] == "o":
            score+= a[j]
        else:
            dd[i].append(a[j])
    pointdic[i] = score

pointmax = max(pointdic.values())
for i in range(n):
    if pointdic[i] >= pointmax:
        print(0)
    else:
        needpoint = pointmax - pointdic[i]
        sortdd = sorted(dd[i],reverse=True)
        k = 0
        for i in sortdd:
            needpoint -= i
            k += 1
            if needpoint < 0:
                print(k)
                break



    
    


