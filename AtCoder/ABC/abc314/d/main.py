import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
iinput = sys.stdin.readline
deq = deque()
l = []
dic = {}
ldic = {}
dd = collections.defaultdict(int)

n = int(input())
s = input()
q = int(input())
k = -1
sl = list(s)
se = set()

last23 = n+1
OR23 = -1
count = 0

for i in range(q):
    t = input().split()

    if t[0] == "1":
        num = int(t[1]) -1
        dic[num] = t[2]
        ldic[num] = t[2]
    elif t[0] == "2":
        last23 = count
        OR23 = 2
        ldic.clear()
    else:
        last23 = count
        OR23 = 3
        ldic.clear()
    count += 1

for key in dic.keys():
    sl[key] = dic[key]

if OR23 == 2:
    for i in range(n):
        sl[i] = sl[i].lower()
elif OR23 == 3:
    for i in range(n):
        sl[i] = sl[i].upper()

for key in ldic.keys():
    sl[key] = ldic[key]

for i in range(n):
    print(sl[i],end="")


    
    


