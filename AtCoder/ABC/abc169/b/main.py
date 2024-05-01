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

#n = int(input())

#a,b = map(int,input().split())
    

    
    

n = input()
a = list(map(int,input().split()))


ans = 1
maxnum = 10 ** 18

if 0 in a:
  print(0)
  exit()
  
for i in a:
  ans *= i
  if ans > maxnum:
    print("-1")
    exit()

print(ans)
