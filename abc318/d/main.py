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

for i in range(n-1):
    d = list(map(int,input().split()))
    for p in range(len(d)):
        dic[(i,p+i+1)] = d[p] 

dic_sort = sorted(dic.items(),key=lambda x:x[1],reverse=True)   

ans_list = []

ilist = set()
# print(dic_sort)
for  key,item in dic_sort:
    if not key[0] in ilist and not key[1] in ilist:
        ans_list.append(item)
        ilist.add(key[0])
        ilist.add(key[1])
    if len(ans_list) == n // 2:
        print(sum(ans_list))
        # print(ilist)
        # print(ans_list)
        exit()

    


