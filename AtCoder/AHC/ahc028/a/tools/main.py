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
def Pr(*x): return print(*x)
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

def Input():
    global n,m,si,sj,A,T,T_backup,T_list
    n,m = MII()
    si,sj = MII()
    A = [list(input()) for _ in range(n)]
    T = set([input() for _ in range(m)])
    T_backup = T.copy()
    T_list = list(T)

    
def change_t():
    ans_list = []
    for i in range(20):
        start_string = ""
        global Sep
        T = T_backup.copy()
        start_string = random.choice(T_list)
        T.remove(start_string)
        string = deque()
        string.extend(start_string)   


        while T:
            d_l,d_r = {},{}
            l,r = [],[]
            for i in range(5):
                l.append(string[i])
                r.append(string[-5+i])
            l,r = "".join(l),"".join(r)
            # print(string,l,r)
            for i in T:
                d_r[i] = get_sameNum(i,l)
                d_l[i] = get_sameNum(r,i)
            max_l, max_r = max(d_l.items(),key = lambda x:x[1]),max(d_r.items(),key = lambda x:x[1])
            # print(max_l, max_r)
            if max_l[1] >= max_r[1]:
                max_str,max_num = max_l
                string.extend(max_str[max_num:])
                T.remove(max_str)
            else:
                max_str,max_num = max_r
                string.extendleft(max_str[5-max_num-1::-1])
                T.remove(max_str)
        ans_list.append(list(string))
    # string.appendleft(A[si][sj])
    # ans = list(string)

    # print(len(Sep))
    return ans_list
        
            
def get_sameNum(s1,s2):
    tmp = 0
    for i in range(4):
        flag = True
        for j in range(i+1):
            if s1[-i+j-1] == s2[j]:
                pass
            else:
                flag = False
                break
        if flag:
            tmp = i+1
    return tmp
                
    
        
def calc_min_dis():   
    #key->[(x,y)]->[a,b,...]->[x,y]
    global dis
    dis = defaultdict(lambda :defaultdict(list))
    for i in range(15):
        for j in range(15):
            for p in range(15):
                for q in range(15):

                    dis[(i,j)][A[p][q]].append((p,q,abs(i-p) + abs(j-q)))

def get_cost(string):
    x,y = si,sj
    # print(string)
    route = [dict() for _ in range(len(string)+1)]
    route[0][(x,y)] = (0,None,None)
    for idx,s in enumerate(string):
        from_list = route[idx]
        for (x,y),(num,frm_x,frm_y) in from_list.items():
            for p,q,cost in dis[(x,y)][s]:
                if (p,q) in route[idx+1]:
                    if num + cost < route[idx+1][(p,q)][0]:
                        route[idx+1][(p,q)] = (num+cost,x,y)
                else:
                    route[idx+1][(p,q)] = (num+cost,x,y)
    ans = deque()
    sumcost = min(route[-1].items(),key=lambda x:x[1][0])[1][0]
    ans.appendleft(min(route[-1].items(),key=lambda x:x[1][0])[0])
    x,y = ans[0]
    for i in route[-1:1:-1]:
        x,y = i[(x,y)][1:]
        ans.appendleft((x,y))
    return ans,sumcost
        
    
    
    # pprint(route)
    # print(ans)
                
            
        
    
    
    
                    
def get_next(char,x,y):
    return dis[(x,y)][char]
       


def solve(string,l,mid,r):
    x,y = si,sj
    
    cost = 0
    ans = []
    if l == -1:
        for i in range(0,len(string)):
            pr_x,pr_y = x,y
            x,y = get_next(string[i],x,y)
            cost += abs(x-pr_x) + abs(y-pr_y)
            ans.append((x,y))
    else:
        for i in range(0,l):
            pr_x,pr_y = x,y
            x,y = get_next(string[i],x,y)
            cost += abs(x-pr_x) + abs(y-pr_y)
            ans.append((x,y))
        for i in range(mid,r):
            pr_x,pr_y = x,y
            x,y = get_next(string[i],x,y)
            cost += abs(x-pr_x) + abs(y-pr_y)
            ans.append((x,y))
        for i in range(l,mid):
            pr_x,pr_y = x,y
            x,y = get_next(string[i],x,y)
            cost += abs(x-pr_x) + abs(y-pr_y)
            ans.append((x,y))
        for i in range(r,len(string)):
            pr_x,pr_y = x,y
            x,y = get_next(string[i],x,y)
            cost += abs(x-pr_x) + abs(y-pr_y)
            ans.append((x,y))
        
    return ans,cost

import random

def yamanobori(strings):
    cost = 1000000
    for string in strings:
        n_ans,n_cost = get_cost(string)
        if cost > n_cost:
            cost = n_cost
            ans = n_ans
    return ans
        

    # while time.perf_counter() - time_sta < 1.7:
    #     count += 1
    #     m = random.choice(range(1,len(Sep)-1))
    #     l,m,r = Sep[m-1],Sep[m],Sep[m+1]
    #     n_ans,n_cost = get_cost(string[:l]+string[m:r]+string[l:m]+string[r:])
    #     if cost > n_cost:
    #         cost = n_cost
    #         moregood += 1
    #         ans = n_ans
        
    # print(count,moregood)
    # for i,j in ans:
    #     print(i,j)
    # ans,cost = solve(string,-1,-1,-1)
    # while time.perf_counter() - time_sta < 1.7:
    #     l,r = random.choice(range(1,10)),random.choice(range(1,10))
 
    #     mid = random.choice(range(l,len(Sep)-r))
        

    #     n_ans,n_cost = solve(string,Sep[mid-l],Sep[mid],Sep[mid+r])

    #     if cost > n_cost:
    #         cost = n_cost
    #         ans = n_ans
    # for i,j in ans:
    #     print(i,j)
        
    
    
      
                
    

import time 
def main():
    global time_sta
    
    Input()
    time_sta = time.perf_counter()
    calc_min_dis()
    strings = change_t()

    yamanobori(strings)
    
    
    
    
if __name__ == '__main__':
    main()
