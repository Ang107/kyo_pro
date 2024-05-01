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

n,m = map(int,input().split())
l = list(map(int,input().split()))
ans_min = max(l) - 1
ans_max = 10 ** 18
fkt= 0

while ans_max - ans_min > 1:
    ans = (ans_min + ans_max)//2
    ansk = ans
    fkt = 0
    for i in l:
        if ansk - i >= 0:
            ansk -= (i + 1)
        else:
            ansk = ans
            ansk -= (i + 1)
            fkt += 1
    if fkt <= m - 1 :
        ans_max = ans
    else:
        ans_min = ans

print(ans_max)








    
    


