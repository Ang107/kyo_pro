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

k = int(input())

#a,b = map(int,input().split())
    
num = list(map(str,range(9,-1,-1)))

bit = list(product(range(2),repeat=10))
# print(bit)
ans = []
for i in bit:
    temp = ""
    for j in range(10):
        if i[j] == 1:
            temp += num[j]
    if temp:
        ans.append(int(temp))

ans.sort()
# print(ans)
print(ans[k])


# ans = 0
# n = 1

# def gensyou(x):
#     x = str(x)
#     prv = x[0]
#     for  i in range(1,len(x)):
#         if prv <= x[i]:
#             return False
#         else:
#             prv = x[i]
#     return True

# while True:
#     n += 1

#     if n < 10:
#         ans += 1
#         n += 1
#     elif gensyou(n):
#         ans += 1
#         n = (n // 10 + 1) * 10
    
#     if ans == k:
#         print(n)
#         exit()




# def seki(x,keta):
#     seki = 1/2
#     for i in range(x,x-keta+1,-1):
#         seki *= i
#     return seki

# def gensyou(x):
#     x = str(x)
#     prv = x[0]
#     for  i in range(1,len(x)):
#         if prv <= x[i]:
#             return False
#         else:
#             prv = x[i]
#     return True

# def inkuri(n):
#     global ans
#     while True:
#         n += 1
#         if gensyou(n):
#             ans += 1
        
#         if ans == k:
#             print(n)
#             exit()

# if k < 10:
#     print(k)
#     exit()
# ans = 9
# for keta in range(2,11):
#     for l in range(0,10):
#         kumi = seki(l,keta)

#         if ans + kumi < k:
#             ans += kumi
#         else:
#             inkuri(int(str(l) + "0"*(keta - 1)))



            


    



    


