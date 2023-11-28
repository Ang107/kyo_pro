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

s = input()
s_len = len(s)

def is_kaibun(x):
    x_len = len(x)
    x_half_L = x[:x_len//2] 
    x_half_R = x[-1:-(x_len//2+1):-1]
    if x_half_L == x_half_R:
        return x_len
    else:
        return 1
ans = 1

for l in range(s_len):
    for r in range(s_len):
        ans = max(ans,is_kaibun(s[l:r+1]))

print(ans)

