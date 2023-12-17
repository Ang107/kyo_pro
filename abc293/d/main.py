import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc
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

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照
    
    
n,m = MII()
abcd = [input().split() for _ in range(m)]
dic = {"R":0,"B":1}
l = [[] for _ in range(n)]
for a,b,c,d in abcd:
    a,c = int(a),int(c)
    l[a-1].append(c-1)
    l[c-1].append(a-1) 


temp = -1

@bootstrap
def dfs(p):
    # print(p)
    global temp
    visited.add(p)
    temp = len(l[p])
    for i in l[p]:
        if i not in visited:
            dfs(i)

    # global ans1,ans2
    # print(ans1,ans2)
    # print(l,visited)
    
    # visited.add(p)
    # if fr in l[p] :
    #     ans1 += 1
    #     return
    # if l[p][0] == None and l[p][1] == None:
    #     ans2 += 1
    # for i in range(2):
    #     if l[p][i]:
    #         temp = l[p][i]
    #         l[p][i] = None
    #         if l[temp][0] == p:
    #             l[temp][0] = None
    #         elif l[temp][1] == p:
    #             l[temp][1] = None
    #         dfs(temp,p) 





ans1 = 0
ans2 = 0
visited = set()
for i in range(n):
    # print(visited)
    if i not in visited:
        temp = -1
        dfs(i)
        if temp == 2:
            ans1 += 1
        else:
            ans2 += 1
        # print(i,ans1,ans2)


print(ans1,ans2)


