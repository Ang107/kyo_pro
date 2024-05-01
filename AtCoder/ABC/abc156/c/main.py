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
l = list(map(int,input().split()))
co = 0
for i in l:
    co += i / n

co = int(co)

while True:
    to1,to2,to3 = 0,0,0

    for i in l:
        to1 += (i - (co - 1))**2
        to2 += (i - co)**2
        to3 += (i - (co + 1))**2
    if to1 < to2:
        co -= 1
    elif to3 < to2:
        co += 1
    else:
        print(to2)
        exit()
