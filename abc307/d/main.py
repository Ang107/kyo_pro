import sys
from  collections import deque,defaultdict
from itertools import product
from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
deq = deque()
dic = {}
dd = defaultdict()

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]

n = input()
s = input()

# count = 0
# for i in s:
#     if i =="(":
#         count += 1
#     elif i == ")":
#         count = max(0,count-1)
# l = 0
# r = 0
# while r < n:
#     if s[l] == 0:
#         print(s[l],end="")
#         l += 1
    

kakko = 0
for i in s:
    # print(i,temp)
    # print(deq)
    if i =="(":
        kakko += 1
        deq.append("(")
    elif i == ")":
        if kakko > 0:
            while deq.pop() != "(":
                pass
        else:
            deq.append(")")
        kakko = max(0,kakko-1)

    else:
        deq.append(i)



for i in deq:
    print(i,end="")
print()


