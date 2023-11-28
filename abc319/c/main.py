import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
import itertools
sys.setrecursionlimit(10**7)

deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

#n = int(input())

#a,b = map(int,input().split())
    
for i in range(3):
    a= tuple(map(int,input().split()))
    l.append(a)

p = itertools.permutations(range(9),9)
for i in p:
    print(i)
# p = product(range(0,9),repeat=3)
# count = 0
# for i in p:
#     if i[0] != i[1] and i[1] != i[2] and i[0] != i[2]:
#         if max(i) - min(i) == 2 or (i[0] + 1) % 3 == (i[1] + 1) % 3 == (i[2] + 1) % 3 or [0,4,8] == sorted(i) or [2,4,6] == sorted(i):
#             if l[i[0]] == l[i[1]] and l[i[0]] != l[i[2]]:
#                 count += 1
#                 print(l[i[0]],l[i[1]],l[i[2]])
        
# print(count/48)
# for i1 in range(0,9):
#     for i2 in range(0,8):
#         for i3 in range(0,7):
#             for i4 in range(0,6):
#                 for i5 in range(0,5):
#                     for i6 in range(0,4):
#                         for i7 in range(0,3):
#                             for i8 in range(0,2):
#                                 for i9 in range(0,1):
#                                     if i1 != i2 != i3 != i4 != i5 != i6 != i7 != i8 != i9:
                                        
                                        

# count = 0
# for x in range(3):

#     if len(set(l[x][0],l[x][1],l[x][2])) < 3:
#         count += 1

#     if len(set(l[x])) < 3:
#         count += 1

# if len(set(l[0][0],l[1][1],l[2][2])) < 3:
#     count += 1

# if 
    



# l1 = range(1,10,1)   
# l2 = range(1,9,1) 
# l1 = range(1,8,1) 
# for i in range(9*9*)

#     for x in range(3):
#         for y in range(3):

#     for x in range(3):
#         for y in range(3):

#     for x in range(3):
#         for y in range(3):