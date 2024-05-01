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

#n = int(input())

n,d = map(int,input().split())
for i in range(n):
    l.append(input())
daylis = []
day = 0
for dx in range(d):
    con = 0
    for nx in range(n):
        if l[nx][dx] != "o" :
            if day != 0:
                daylis.append(day)
                day = 0

            continue
        else:
            con += 1
            if con == n:
                day += 1
daylis.append(day)
if len(daylis) != 0:
    print(max(daylis))
else:
    print(0)




    
    


