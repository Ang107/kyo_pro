import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
iinput = sys.stdin.readline
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(list)

#n = int(input())

n,m = map(int,input().split())
for i in range(m):
    l.append(tuple(map(int,input().split())))





numbers = set(range(n))


for i in l:
    if i[1]-1 in numbers:

        numbers.remove(i[1]-1)

if len(numbers) == 1:
    numbers = list(numbers)
    print(numbers[0] + 1)
else:
    print(-1)





    

    
    


