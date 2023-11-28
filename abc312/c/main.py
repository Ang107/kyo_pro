import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
iinput = sys.stdin.readline
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

#n = int(input())

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

    
a = sorted(a)
b = sorted(b)






k = 0
if max(b) < min(a)  :
     print(max(b)+1)
else:    
    for i in range(len(a)):


        for p in b:
            if p >= a[i]:
                k += 1
        if i+1 >= k:
            print(a[i])
            exit()
    print(max(b)+1)

    

    
    


