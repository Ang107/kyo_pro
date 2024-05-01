# import sys
# import collections
# from collections import deque
# from copy import deepcopy
# from itertools import product
# sys.setrecursionlimit(10**7)
# deq = deque()
# l = []
# dic = {}
# dd = collections.defaultdict(int)

# def array2(i,j,element):
#     return [[element] * j for _ in range(i)]

# def for_input(n):
#     L = []
#     for _ in range(n):
#         L.append(tuple(map(int,input().split())))
#     return L

# #n = int(input())

# # n,m = map(int,input().split())

# # a = list(map(int,input().split()))

# # b = list(map(int,input().split()))

# # def mycode(n,m,a,b):
# #     x0 = set()
# #     x1 = set()
# #     ab = []
# #     for i in range(m):
# #         ab.append((min(a[i],b[i]),max(a[i],b[i])))
# #     ab.sort(key=lambda x:x[1])
# #     ab.sort(key=lambda x:x[0])
# #     # return(ab)

# #     for i in range(m):
# #         if ab[i][0] == ab[i][1]:
# #             return("No")
# #             exit()
            
# #         elif ab[i][0] in x0:
# #             if ab[i][1] in x0:
# #                 return("No")
# #                 exit()
# #             else:
# #                 x1.add(ab[i][1])

# #         else:
# #             if ab[i][0] in x1:
# #                 if ab[i][1] in x1:
# #                     return("No")
# #                     exit()
# #                 else:
# #                     x0.add(ab[i][1])

# #             else:
# #                 if ab[i][1] in x0:
# #                     x1.add(ab[i][0])
# #                 elif ab[i][1] in x1:
# #                     x0.add(ab[i][0])
# #                 else:
# #                     x0.add(ab[i][0])
# #                     x1.add(ab[i][1])
            
# #     return("Yes")



# import sys; R = sys.stdin.readline
# S = lambda: map(int,R().split())
# from collections import deque

# def anycode(n,m,a,b):
#     # n,m = S()
#     # a = [*S()]; b = [*S()]
#     e = [[] for _ in range(n+1)]
#     p = [0]*(n+1)
#     for i in range(m):
#         u,v = a[i],b[i]
#         e[u] += v,; e[v] += u,
#     for i in range(1,n+1):
#         if not p[i]:
#             p[i] = 1
#             q = deque([i])
#             while q:
#                 u = q.popleft()
#                 for v in e[u]:
#                     if not p[v]:
#                         p[v] = -p[u]
#                         q += v,
#                     elif p[v]==p[u]: return("No"); exit()
#     return("Yes")
    
# import random

# from collections import deque
# def mycode2(n,m,a,b):
#     x0 = set()
#     x1 = set()
#     ab = []

#     for i in range(m):
#         ab.append((min(a[i],b[i]),max(a[i],b[i])))
#     ab.sort(key=lambda x:x[1])
#     ab.sort(key=lambda x:x[0])
#     # return(ab)
#     ab = deque(ab)

#     p,q = ab.popleft()
#     #一つ目を追加
#     if p == q:
#         return("No")
#     else:
#         x0.add(p)
#         x1.add(q)

#     #abが空になるまで
#     while ab:
#         #bf:この時点でのabの数
#         bf = len(ab)
#         #p,q共に存在しない場合は末尾に戻しながら、一周
#         for _ in range(bf):
#             p,q = ab.popleft()
            
#             if p == q:
#                 return("No")
                
#             elif p in x0:
#                 if q in x0:
#                     return("No")
#                 else:
#                     x1.add(q)

#             elif p in x1:
#                 if q in x1:
#                     return("No")
#                 else:
#                     x0.add(q)

#             else:
#                 if q in x0:
#                     x1.add(p)
#                 elif q in x1:
#                     x0.add(p)
#                 else:
#                     #p,q共に存在しない場合
#                     ab.append((p,q))
                    
#         af = len(ab)
#         #一周させて変化なし（全ての組がp,q存在せず）
#         if bf == af:
#             #x0,x1をリセット
#             x0,x1 = set(),set()

#             #一つ目を追加
#             p,q = ab.popleft()
#             if p == q:
#                 return("No")
#             else:
#                 x0.add(p)
#                 x1.add(q)

#     return("Yes")

        
# n,m = map(int,input().split())

# a = list(map(int,input().split()))

# b = list(map(int,input().split()))

# print(mycode2(n,m,a,b))


# while True:
#     n,m = 10**5,10**5
#     a,b = [],[]
#     for i in range(10**5):
#         a.append(random.randint(1,10**3))
#         b.append(random.randint(10**3,10**5))
#     # if mycode2(n,m,a,b) != anycode(n,m,a,b):
#     print(a,b)
#     print(mycode2(n,m,a,b))
#     # print(anycode(n,m,a,b))

from collections import deque
from collections import defaultdict
def mycode2(n,m,a,b):
    x0 = set()
    x1 = set()
    ab = []
    dd = defaultdict(set)
    for i in range(m):
        ab.append((a[i],b[i]))
        dd[a[i]].add(b[i])
        dd[b[i]].add(a[i])

    ab.sort(reverse=True, key = lambda x:len(dd[x[0]])+len(dd[x[1]]))

    ab = deque(ab)
    #一つ目を追加
    p,q = ab.popleft()
    if p == q:
        return("No")
    else:
        x0.add(p)
        x1.add(q)

    #abが空になるまで
    while ab:
        #bf:この時点でのabの数
        bf = len(ab)
        #p,q共に存在しない場合は末尾に戻しながら、一周
        for _ in range(bf):
            p,q = ab.popleft()
            
            if p == q:
                return("No")
                
            elif p in x0:
                if q in x0:
                    return("No")
                else:
                    x1.add(q)

            elif p in x1:
                if q in x1:
                    return("No")
                else:
                    x0.add(q)

            else:
                if q in x0:
                    x1.add(p)
                elif q in x1:
                    x0.add(p)
                else:
                    #p,q共に存在しない場合
                    if len(dd[p]) == 1 and len(dd[q]) == 1:
                        pass
                    else:
                        ab.append((p,q))
                    
        af = len(ab)
        #一周させて変化なし（全ての組がp,q存在せず）
        if bf == af:
            #x0,x1をリセット
            x0,x1 = set(),set()

            #一つ目を追加
            p,q = ab.popleft()
            if p == q:
                return("No")
            else:
                x0.add(p)
                x1.add(q)

    return("Yes")

        
n,m = map(int,input().split())

a = list(map(int,input().split()))

b = list(map(int,input().split()))

print(mycode2(n,m,a,b))
