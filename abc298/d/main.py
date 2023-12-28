import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
from pprint import pprint
from heapq import heapify,heappop,heappush
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1)) #上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()
mod = 998244353

Pr = lambda x : print(x)
PY = lambda : print("Yes")
PN = lambda : print("No")
I = lambda : input()
II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照

import fileinput
q = []
for i,line in enumerate(fileinput.input()):
    # print(line)
    if i == 0:
      Q = line 
    else:
        q.append(line.split())

    
# Q = int(input())
# q = [input().split() for _ in range(Q)]
# print(q)

deq = deque(["1"])
ans_list = []
for i in q:
    # print(deq)
    if i[0] == "1":
        deq.append(i[1])
    elif i[0] == "2":
        deq.popleft()
    elif i[0] == "3":
        ans = int("".join(deq)) % mod
        ans_list.append(ans)
        # print(ans)

print(len(ans))
print(ans)

# temp = 1

# for i in q:
#     if i[0] == 1:
#         temp = (temp * 10 + i[1]) 
#     elif i[0] == 2:
#         keta = len(str(temp)) - 1
#         temp = temp % 10**keta
#     elif i[0] == 3:
#         print(temp % mod)
