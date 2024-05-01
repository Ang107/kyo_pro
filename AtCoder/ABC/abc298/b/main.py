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
    
n = II()
A = [LMII() for _ in range(n)]
B = [LMII() for _ in range(n)]

#90度右回転させたリストを返す
def list_rotate_R90(l):
    return list(zip(*reversed(l)))

A1 = list_rotate_R90(A)
A2 = list_rotate_R90(A1)
A3 = list_rotate_R90(A2)

def judge(l1,l2):
    for i in range(n):
        for j in range(n):
            if l1[i][j] == 1:
                if l2[i][j]:
                    pass
                else:
                    return False
    return True

if judge(A,B) or judge(A1,B) or judge(A2,B) or judge(A3,B):
    print("Yes")
else:
    print("No")
    
# for i in range(n):
#     for j in range(n):
#         A1[i][j] = A[n-1-j][i] 
    
# for i in range(n):
#     for j in range(n):
#         A2[i][j] = A1[n-1-j][i] 

# for i in range(n):
#     for j in range(n):
#         A3[i][j] = A2[n-1-j][i]    



# # flag1 = True
# # flag2 = True
# # flag3 = True
# # flag4 = True
# # for i in range(n):
# #     for j in range(n):
# #         k = 1
# #         for p,q in ((i,j),(n+1-j,i),(n+1-i,n+1-j),(n+1-n-1+j,n+1-i)):
# #             if A[p][q] == 1 :
# #                 if B[i][j] == 1:
# #                     pass
# #                 else:
# #                     if k == 1:
# #                         flag1 = False
# #                     elif k == 2:
# #                         flag2 = False
# #                     elif k == 3:
# #                         flag3 = False
# #                     elif k == 4:
#                         # flag4 = False

# # if flag1 or flag2 or flag3 or flag4:
# #     print("Yes")
# # else:
# #     print("No")







