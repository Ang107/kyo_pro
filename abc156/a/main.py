import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
iinput = sys.stdin.readline
deq = deque()
dic = {}
dd = collections.defaultdict(int)

def Iin(x) :
    x = int(iinput())

def LIin(x):
    for i in range(x):
        deq.append(tuple(map(int,iinput().split())))

def L2(x,y,z):
    lis2 = [[z] * y for _ in range(x)]

n,r = map(int,input().split())
if n <= 10:
    r = r + 100*(10-n)
print(r)

