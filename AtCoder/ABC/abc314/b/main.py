import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
iinput = sys.stdin.readline
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

n = int(input())

for i in range(n):
    c = int(input())
    a = set(map(int,input().split()))
    l.append(a)
x = int(input())

#a,b = map(int,input().split())

k = 1
minn = 40

for values in l:
    if x in values:
        if len(values) < minn:
            deq.clear()
            deq.append(k)
            minn = len(values)
        elif len(values) == minn:
            deq.append(k)

    k += 1


print(len(deq))
print(*deq)

    

    
    


