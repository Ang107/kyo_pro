import sys
from collections import deque, defaultdict
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
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
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x): return print(x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


n, m = MII()
more_big = defaultdict(set)
more_small = defaultdict(set)


for i in range(m):
    x, y = MII()
    more_big[x].add(y)
    more_small[y].add(x)

# print(more_big, more_small)
for i in range(1, n+1):
    if i not in more_small:
        temp = i

deq = deque([temp])
ans = [None] * n
temp = 1

num = 0
while len(deq) == 1:
    num += 1
    x = deq.popleft()
    ans[x-1] = temp
    temp += 1
    for i in more_big[x]:
        more_small[i].discard(x)
        if not more_small[i]:
            deq.append(i)

if len(deq) == 0 and num == n:
    print("Yes")
    print(*ans)
else:
    print("No")
