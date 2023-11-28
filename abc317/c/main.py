import sys
import collections
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)
import itertools

deq = deque()
l = []
dic = {}

dd = collections.defaultdict(int)

n, m = map(int, input().split())
All = list(itertools.permutations(range(0,n)))
mp = [[0] * n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    mp[a-1][b-1] = c
    mp[b-1][a-1] = c


ans = 0
# print(All)
for i in All:
    # print(i)
    temp = 0
    for j in range(n-1):
        if mp[i[j]][i[j+1]] != 0:
            temp += mp[i[j]][i[j+1]]
        else:
            break
    ans = max(ans,temp)

print(ans)







# cost = 1


# def dfs(x, ikeru, itta, dis):
#     global cost
#     if dis > cost:
#         cost = dis
        
    
#     for i in ikeru:
#         if i not in itta:
#             itta_new = itta.copy()
#             itta_new.append(x)
#             dfs(i, dd[i],itta_new, dis + dic[(x, i)])


# for i in range(1, n + 1):
#     if len(dd[i]) > 0:
#         dfs(i, dd[i], [i], 0)
# print(cost)
