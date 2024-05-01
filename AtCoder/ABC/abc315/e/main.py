import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
from pprint import pprint
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1)) #上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()
mod = 998244353

Pr = lambda x : print(x)
PY = lambda : print("Yes")
PN = lambda : print("No")
I = lambda : input()
II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照


n = II()
d = defaultdict(set)
d_rev = defaultdict(set)
d_num = {}
for i in range(n):
    c,*p = LMII()
    d_num[i+1] = c
    for j in range(c):
        d[i+1].add(p[j])
        d_rev[p[j]].add(i+1)
    


def bfs():
    deq = deque()
    deq.append(1)
    visited_set = set()
    visited_set.add(1)
    while deq:
        temp = deq.popleft()
        for i in d[temp]:
            if i not in visited_set:
                visited_set.add(i)
                deq.append(i)
    return visited_set

visited = bfs()
deq = deque([i for i in visited if d_num[i] == 0])
ans = []

# print(d,d_rev,d_num)

while deq:
    # print(visited,ans)
    x = deq.popleft()
    ans.append(x)
    for i in d_rev[x]:
        d_num[i] -= 1
        if d_num[i] == 0:
            if i in visited:
                deq.append(i)

print(*ans[:-1])
