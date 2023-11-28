import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
iinput = sys.stdin.readline
deq = deque()
dic = {}
dd = collections.defaultdict(int)

def LIin(x):
    for i in range(x):
        deq.append(tuple(map(int,iinput().split())))

def L2(x,y,z):
    lis2 = [[z] * y for _ in range(x)]

n = int(input())
s = input()
lens = len(s)
co = 0

def nand(x,y):
    if x == 1 and y == 1:
        return 0
    else:
        return 1
    
for i in range(lens):
    for p in range(i,lens):
        if i == p:
            if s[i] == "0":
                prev = 0
            else:
                prev = 1
                co += 1
        elif i < p:
            prev = nand(prev,int(s[p]))
            if prev == 1:
                co += 1
print(co)

            



                




