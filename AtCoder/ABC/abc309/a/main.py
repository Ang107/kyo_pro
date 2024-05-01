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

a,b = map(int,input().split())
if abs(a-b) == 1  and not (a==3 and b==4 ) and not(a==6 and b==7 ):
    print("Yes")
else:
    print("No")