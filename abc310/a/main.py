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

n,p,q =map(int,input().split())
d = list(map(int,input().split()))
mind = min(d)

if mind + q < p:
    print(mind + q )
else:
    print(p)