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
  
A = for_input(9)
A_rev = list(zip(*A)) 

flag = True
for i in A:
    if len(set(i)) != 9:
        flag = False
        print("No")
        exit()
for i in A_rev:
    if len(set(i)) != 9:
        flag = False
        print("No")
        exit()

l = [set(),set(),set(),set(),set(),set(),set(),set(),set(),]  

for i in range(9):
    for j in range(9):

        if 0 <= i <= 2:
            if 0 <= j <= 2:

                l[0].add(A[i][j])
            elif 3 <= j <= 5:
                l[1].add(A[i][j])
            else:
                l[2].add(A[i][j])
        
        elif 3 <= i <= 5:
            if 0 <= j <= 2:
                l[3].add(A[i][j])
            elif 3 <= j <= 5:
                l[4].add(A[i][j])
            else:
                l[5].add(A[i][j])
        
        else:
            if 0 <= j <= 2:
                l[6].add(A[i][j])
            elif 3 <= j <= 5:
                l[7].add(A[i][j])
            else:
                l[8].add(A[i][j])


for i in l:
    if len(i) != 9:
        flag = False
        print("No")
        exit()

print("Yes")







    
    


