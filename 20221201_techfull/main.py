import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
#from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((0, -1), (0, 1), (-1, 0), (1, 0))
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict(list)

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda h,w,element : [[element] * w for _ in range(h)]   #二次元リスト作成
is_not_Index_Er = lambda x,y,l : 0 <= x < len(l) and 0 <= y < len(l[0])    #範囲外参照していないことの確認

# a,b,c = MII()
# if a + b == 10 or a + c == 10 or b + c == 10:
#     print("Yes")
# else:
#     print("No")


# n,k = MII()
# xy = [LMII() for _ in range(n)]


# l = list(permutations(range(n)))

# def get_dis(z1,z2):
#     return ((z1[0]-z2[0])**2 + (z1[1]-z2[1])**2) ** (1/2)
# ans = 0
# for i in l:

#     temp = 0
#     for j in range(k-1):
#         z1 = xy[i[j]]
#         z2 = xy[i[j+1]]
#         temp += get_dis(z1,z2)
#     ans = max(ans,temp)

# print(round(ans,2))
    



            

    


