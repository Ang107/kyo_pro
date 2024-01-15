import sys
from collections import deque, defaultdict
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush
# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
mod = 998244353
def input(): return sys.stdin.readline().rstrip()
def Pr(x): return print(x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill]*l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n = II()
l = []
# for i in range(1,19):
#     tmp = (10 ** i - 1) - 10 * 9 ** (i-1)
#     l.append(tmp)



def getnum(mid):

    
    
    
    idx_0 = str(mid).index("0")
    ans = 0
    for i,n in enumerate(str(mid)):
        #０の場合
        if n == "0":
            ans += int(str(mid)[idx_0:])
            break
        if i == 0:
            tmp = 0
            tmp += int(n) * 9 ** (len(str(mid)) - 1)
            for k in range(1,len(str(mid)) - 1):
                tmp += 9 ** k
            ans += int(n) * 10 ** (len(str(mid)) - 1) - tmp
        else:
            ans += int(n) * 10 ** (len(str(mid)) - 1 - i) - (int(n)-1) * 9 ** (len(str(mid)) - 1 - i)
             
    return ans
import random
l = 0
r = 10**18+10
while True:
    mid = (r+l)//2
    if "0" not in str(mid):
        mode = random.choice(range(2))
        if mode == 0:
            mid = mid // 10 * 10
        else:
            mid = mid // 10 * 10
            mid += 10            
    ans = getnum(mid)
    # print(l,mid,r,ans,n)
    if ans < n:
        l = mid
    elif n < ans:
        r = mid
    else:
        print(mid)
        break
# while True:
#     n = random.choice(range(1,1000000))
#     print("num",n)
#     l = 0
#     r = 10**18+10
#     while True:
#             mid = (r+l)//2
#             if "0" not in str(mid):
#                 mode = random.choice(range(2))
#                 if mode == 0:
#                     mid = mid // 10 * 10
#                 else:
#                     mid = mid // 10 * 10
#                     mid += 10            
#             ans = getnum(mid)
#             # print(l,mid,r,ans,n)
#             if ans < n:
#                 l = mid
#             elif n < ans:
#                 r = mid
#             else:
#                 print(mid)
#                 break
        
    


            
            
    

# def getnum1(mid):
#     num = 10
#     count = 0
#     while True:
#         if "0" in str(num):
#             count += 1
#         if num == mid:
#             return count
#         num += 1
    
# import random    
# for i in range(500):
#     num = random.choice(range(10,20000))
#     # num = II()
#     ans1 = getnum(num)
#     ans2 = getnum1(num)
#     # print(num,ans2)
#     print(ans1,ans2 )
#     if ans1 != ans2 :
#         break
# for i in [10
# ,
# 20
# ,
# 30
# ,
# 40
# ,
# 50
# ,
# 60
# ,
# 70
# ,
# 80
# ,
# 90
# ,
# 100
# ,
# 101
# ,
# 102
# ,]:
#     print(i)
#     tmp = 0
#     mid = i
#     if str(i).count("0") == 0:
#         i = i // 10 * 10
#         mid = i

#     limit = str(i).index("0")
#     print(limit)
#     for j in range(len(str(i)),len(str(i))-limit,-1):
#         top = mid // 10 ** (j-1)
#         mid -= top * 10 ** (j-1)
        
#         num = (top * 10 ** (j-1)) - top *  9 ** (j-1)
#         if j > 1:
#             num -= 9
#         print(top,num)
#         tmp += num
#     tmp += i % 10 ** (len(str(i)) - limit)
#     print(tmp)
    
    