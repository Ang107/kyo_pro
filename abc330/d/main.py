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
S = [list(input()) for _ in range(n)]

yoko_o = [0]*n 
tate_o = [0]*n 

for i in range(n):
    temp1 = 0
    temp2 = 0
    for j in range(n):
        if S[i][j] == "o":
            temp1 += 1
        if S[j][i] == "o":
            temp2 += 1
    yoko_o[i] = temp1
    tate_o[i] = temp2

# print(yoko_o)
# print(tate_o)
ans = 0
for i in range(n):
    for j in range(n):
        if S[i][j] == "o":
            # print(yoko_o[i],tate_o[j])
            ans += (yoko_o[i]-1) * (tate_o[j]-1)

print(ans)

        
#a,b = map(int,input().split())
    

    
    


