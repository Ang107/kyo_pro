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

a= list(map(int,input().split()))
sum = 0
for i in a:
    sum += i
avemai = sum//n
avepl = avemai + 1

mai = 0
pl = 0
for i in a:
    if i <= avemai:
        mai += avemai - i

    else:
        pl += i - avepl

print(max(mai,pl))


    

    
    


