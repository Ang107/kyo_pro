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

a = list(map(int,input().split()))
for i in range(n):
    dic[i] = a[i]

s =set()

ansl = []
fl = 0
def next(x):
    global fl
    if not x in s:
        
        s.add(x)
        next(dic[x - 1])  
    else:
        lists = list(s)
        for i in range(len(s)):
            if lists[i] == x or fl == 1:
                ansl.append(lists[i])
                fl = 1

next(a[0])
print(len(ansl))
for i in ansl:
    print(i,end=" ")
      
    
    


