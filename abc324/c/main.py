import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
import string
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

n,t= input().split()
n = int(n)

t_l = []
for i in range(n):
    t_l.append(input())

def judge(t1,t2):
    if len(t1) == len(t2):
        diff = 0
        for i in range(len(t1)):
            if t1[i] != t2[i]:
                diff += 1
        return diff <= 1
      
    else:
        if len(t1) - len(t2) == 1 :
            t1,t2 = t2,t1
        elif  len(t1) - len(t2) == -1:   
            pass
        else:
            return False
        i,j,diff = 0,0,0
        # print(len(t1),len(t2))
        while True:
            # print(t1,t2)
            # print(i,j)
            if t1[i] == t2[j]:
                i += 1
                j += 1
            else:
                j += 1
                diff += 1
            if i == len(t1) or j == len(t2):
                return  diff <= 1
ans = []
for i in range(n):
    if judge(t_l[i],t):
        ans.append(i+1)
print(len(ans))
print(*ans)


            
                
            


# def fil1(sent,kouho):
#     if sent == kouho:
#         return True 
#     else:
#         return False
# def fil2(sent,kouho):

# ans ={t}
# t_len= len(t)
# abc = list(string.ascii_lowercase)
# for i in range(t_len+1):
#     L = t[:i]
#     R = t[i:]
#     R1 = t[i+1:]
#     ans.add(L + R1)
#     for alp in abc:
#         ans.add(L + alp + R)
#         ans.add(L + alp + R1)



# out = []
# for i in range(n):
#     if t_l[i] in ans:
#         out.append(i+1)

# print(len(out))
# print(*out)



    


    

    
    


