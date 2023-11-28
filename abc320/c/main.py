import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
sys.setrecursionlimit(10**7)

deq = deque()
l = []
dic = {}
dd_s1 = collections.defaultdict(list)
dd_s2 = collections.defaultdict(list)
dd_s3 = collections.defaultdict(list)

m = int(input())
s1 = input()
s2 = input()
s3 = input()

k = 0
for i in s1:
    k += 1
    dd_s1[i].append(k)
k = m
for i in s1:
    k += 1
    dd_s1[i].append(k)

k = 0
for i in s2:
    k += 1
    dd_s2[i].append(k)
    k = m
for i in s2:
    k += 1
    dd_s2[i].append(k)

k = 0
for i in s3:
    k += 1
    dd_s3[i].append(k)
k = m
for i in s3:
    k += 1
    dd_s3[i].append(k)

ans =[]

def judge(a1,a2,a3):
    fl1 = False
    fl2 = False
    fl3 = False

    while True:
        


for i in range(10):
    if len(dd_s1[i]) > 0 and len(dd_s2[i]) > 0 and len(dd_s3[i]) > 0 :
        if dd_s1[i][0] != dd_s2[i][0] and dd_s1[i][0] != dd_s3[i][0] and dd_s2 != dd_s3[i][0]:
            ans.append(max((dd_s1[0],dd_s2[0],dd_s3[0])))
        else:



    
    


