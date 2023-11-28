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
    L.append(["."]*(W+2))
    for _ in range(n):
        l = ["."]
        l.extend(list(input()))
        l.append(".")
        L.append(l)
    L.append(["."]*(W+2))    
    return L

#n = int(input())


def bfs():

    global ans

    for i1 in range(H+2):
        for j1 in range(W+2):
            if S[i1][j1] == "#" and stayed[i1][j1] == -1:
                deq.append((i1,j1))  
                while deq:
                    h,w = deq.popleft()
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if S[h+i][w+j] == "#" and stayed[h+i][w+j] == -1:
                                deq.append((h+i,w+j))
                                stayed[h+i][w+j] = 1
                ans += 1


H,W = map(int,input().split())
S = for_input(H)
    
stayed = array2(H+2,W+2,-1)
ans = 0

bfs()



print(ans)