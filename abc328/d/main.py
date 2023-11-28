import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
sys.setrecursionlimit(10**7)
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

def array2(i,j,element):
    return [[element] * j for _ in range(i)]

def for_input(n):
    L = []
    for _ in range(n):
        L.append(tuple(map(int,input().split())))
    return L

#n = int(input())

#a,b = map(int,input().split())
    
d = deque(input())
s = {"A","B","C"}
count = 0
count1 = 0
ans =deque()
ans.append("")
temp =""
while d:

    if count == 0:
        if ans[-1] == "A":
            count = 1
            temp = ans.pop()
        elif ans[-1] =="AB":
            count = 2
            temp = ans.pop()

    temp = temp + d.popleft()

    if count == 0:
        if temp != "A":
            ans.append(temp)
            temp=""
            count = 0
        else:
            count += 1
    elif count == 1:
        if temp[1] == "A":
            ans.append("A")
            temp="A"
            count = 1
        elif temp[1] == "B":
            count += 1
        else:
            ans.append(temp)
            temp = ""
            count = 0

            
    elif count == 2:
        if temp[2] == "A":
            ans.append("AB")
            temp="A"
            count = 1
        elif temp[2] == "B":
            ans.append("ABB")
            temp=""
            count = 0
        else:
            temp=""
            count = 0
ans.append(temp)
ans = ''.join(ans)
print(ans)
    


