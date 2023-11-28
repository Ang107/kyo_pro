import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
iinput = sys.stdin.readline
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(deque)

#n = int(input())

n,m = map(int,input().split())
s = input()
c = list(map(int,input().split()))
    
for i in range(len(c)):
    dd[c[i]].append(s[i])
for i in dd.values():
    k = i.pop()
    i.appendleft(k)


for i in range(n):
    print(dd[c[i]][0],end="")
    dd[c[i]].popleft()

    
    


