import sys

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)

around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 2**61 - 1
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n = int(input())
s = input().split()
from collections import defaultdict

dd = defaultdict(int)
ans = 0
mod = 2**61 - 1
b = 31
for i in s:
    hash = 0
    for j in i:
        hash = (hash + (ord(j) - ord("a") + 1)) % mod
        ans += dd[hash]
        # print(i, hash)
        dd[hash] += 1
        hash *= b
        hash %= mod
pritn(ans)


# class Node:
#     def __init__(self):
#         self.cnt = 0
#         self.child = [None] * 26


# class TrieTree:
#     def __init__(self):
#         self.root = Node()

#     def add(self, s: str):
#         node = self.root
#         for i in s:
#             v = ord(i) - ord("a")
#             if node.child[v] == None:
#                 node.child[v] = Node()
#             node = node.child[v]
#             node.cnt += 1

#     def get_sum(self, s: str) -> int:
#         result = 0
#         node = self.root
#         for i in s:
#             v = ord(i) - ord("a")
#             if node.child[v] == None:
#                 return result
#             node = node.child[v]
#             result += node.cnt
#         return result


# tt = TrieTree()
# for i in s:
#     ans += tt.get_sum(i)
#     tt.add(i)
#     # print(ans)


# print(ans)


# s.sort()
# ans = 0

# for index, i in enumerate(s):
#     tmp = i[:]
#     ok = index
#     ng = n
#     for j in range(len(i)):

#         def isOK(mid):
#             return j < len(s[mid]) and i[j] == s[mid][j]

#         def meguru(ng, ok):
#             while abs(ok - ng) > 1:
#                 mid = (ok + ng) // 2
#                 if isOK(mid):
#                     ok = mid
#                 else:
#                     ng = mid
#             return ok

#         tmp = meguru(ng, ok)
#         ans += tmp - index
#         ng = tmp + 1

# print(ans)
