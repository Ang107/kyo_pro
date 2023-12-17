import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((0, -1), (0, 1), (-1, 0), (1, 0))
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()


Pr = lambda x : print(x)
PY = lambda : print("Yes")
PN = lambda : print("No")
I = lambda : input()
II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照


n = II()
tx = [LMII() for _ in range(n)]
dd = defaultdict(SortedSet)
dd_mons = defaultdict(list)
for i,j in enumerate(tx):
    if j[0] == 1:
        dd[j[1]].add(i)
    elif j[0] == 2:
        dd_mons[j[1]].append(i)

ans = [0] * n

for i,j in dd_mons.items():
    for p in j:
        temp = bisect_left(dd[i],p) - 1
        # print(dd[i][temp])
        if temp == -1:
            print(-1)
            exit()
        else:
            ans[dd[i][temp]] = 1
            dd[i].remove(dd[i][temp])

p_max = 0 
p = 0
ans1 = []
for i,j in zip(ans,tx):
    if j[0] == 1:
        # print(i,j)
        ans1.append(i)
        if i == 1:
            p += 1
    else:
        p -= 1
    # print(p)
    p_max = max(p_max,p)
    

print(p_max)
print(*ans1)








