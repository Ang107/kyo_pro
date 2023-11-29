import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((0, -1), (0, 1), (-1, 0), (1, 0))
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照
    
n,m = map(int,input().split())
S = [input() for _ in range(n)]
from itertools import permutations
all = permutations(range(n))
def judge(x):
    for i in range(len(x)-1):
        temp = 0
        #前後の差分計算
        for p,q in zip(S[x[i]],S[x[i+1]]):
            if p == q:
                pass
            else:
                temp += 1
        #差分が1
        if temp == 1:
            pass
        else:
            return False
    return True


for i in all:
    if judge(i):
        print("Yes")
        exit()
    # # print(i)
    # flag = True
    # for j in range(n-1):
    #     # print(j)
    #     temp = 0
    #     for k in range(m):
    #         print(S[i[j]],S[i[j+1]])
    #         if S[i[j]][k] == S[i[j+1]][k]:
    #             pass
    #         else:
    #             temp += 1
    #     if temp == 1:
    #         pass
    #     else:
    #         break
    # if temp == 1:
    #     print("Yes")
    #     exit()
print("No")


