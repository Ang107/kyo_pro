import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)
import math
from bisect import bisect_left, insort_left, bisect_right, insort_right
from pprint import pprint
from heapq import heapify, heappop, heappush

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
# input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


n = II()
num = math.ceil(math.log(n, 2))
print(num, flush=True)
ans = [[] for _ in range(num)]
for i in range(n):
    tmp = bin(i)[2:]
    tmp = "0" * (num - len(tmp)) + tmp
    for j, k in enumerate(tmp):
        if k == "1":
            ans[j].append(i + 1)

# print(ans)
for i, j in enumerate(ans):
    print(len(j), *j, flush=True)
s = input()
print(int(s, base=2) + 1, flush=True)
# if n == 2:
#     print(1, flush=True)
#     print(1, 1, flush=True)
#     s = input()
#     if s == "1":
#         print(1, flush=True)
#     else:
#         print(2, flush=True)

# elif n == 3:
#     print(2, flush=True)
#     print(1, 1, flush=True)
#     print(2, 2, flush=True)
#     s = input()
#     if s[0] == "1":
#         print(1, flush=True)
#     elif s[1] == "1":
#         print(2, flush=True)
#     else:
#         print(3, flush=True)
# else:
#     tmp = (n - 1) // 3
#     tmp *= 2
#     # tmp += (n - 1) % 3

#     print(tmp)
#     num = -1
#     d = defaultdict(list)
#     for i in range(1, tmp + 1):
#         if i % 2 == 1:
#             num += 2
#         else:
#             num += 1
#         print(i, num, num + 1, flush=True)
#         d[i].append(num)
#         d[i].append(num + 1)
#     for i in range(tmp + 1, tmp + (n - 1) % 3 + 1):
#         num += 1
#         print(i, num, flush=True)
#         d[i].append(num)

#     s = input()
#     bad = []

#     for i, j in enumerate(s):
#         if j == "1":
#             bad.extend(d[i + 1])
#     # print(bad)
#     if len(bad) == 0:
#         print(n, flush=True)
#     elif len(bad) == 1:
#         print(*bad, flush=True)
#     elif len(bad) == 2:
#         if bad[0] % 2 == 1:
#             print(bad[0], flush=True)
#         else:
#             print(bad[1], flush=True)
#     elif len(bad) == 3:
#         print(bad[-1], flush=True)
#     else:
#         print(sum(bad) // 4, flush=True)
