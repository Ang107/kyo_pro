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
s = input()

gensyou = True 
dfsco = 0
for i in range(n-2):
    if int(s[i]) >= int(s[i+1]):
        pass
    else:
        gensyou = False
        break

def dfs(x):
    global dfsco
    dfsco += 1
    kara = ""
    
    for i in range(0,len(x)-1,1):
        for _ in range(int(x[i+1])):
            kara += x[i]
    if len(kara) == 1:
        print(dfsco % 998244353 )
        exit()
    else:

        dfs(kara)

if gensyou:
    print(-1)
else:

    dfs(s)
    



    


