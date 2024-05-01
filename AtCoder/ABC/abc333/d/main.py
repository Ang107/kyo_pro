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
dd = defaultdict(set)

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
uv = [LMII() for _ in range(n-1)]

for u,v in uv:
    dd[u].add(v)
    dd[v].add(u)

temp = dd[1]

def bfs(x):
    visited = set()
    deq = deque()
    deq.append(x)
    visited.add(x)
    while deq:
        x = deq.popleft()

        for i in dd[x]:
            if i not in visited and i != 1:
                visited.add(i)
                deq.append(i)
    return len(visited)

l = []
for i in temp:
    l.append(bfs(i))

l.sort()

print(sum(l[:len(l)-1])+1)

# dd_sorted = dict(sorted(dd.items(),key = lambda x:len(x[1]) ))
# print(dd_sorted)

# for i,j in dd_sorted.items():
#     if i == 1
#     if len(j) == 1:
#         temp = j.pop
#         dd_sorted[temp].remove(i)
    