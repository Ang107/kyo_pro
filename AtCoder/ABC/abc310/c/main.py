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
s = set()
s1 = set()
len1 = 0
for i in range(n):
    k = input()
    if not k in s and not k[::-1] in s:
        s.add(k)
    #s1.add(k[::-1])
    #if len(k) == 1:
        #len1 += 1
kaburi = 0
#for i in s:
    #if i in s1:
        #kaburi += 1
#ans = len(s) - kaburi/2 + len1/2
print(len(s))

