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

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((0, -1), (0, 1), (-1, 0), (1, 0))
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
deq = deque()
dd = defaultdict()

II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
Ary2 = lambda w, h, element: [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x, y, h, w: 0 <= x < h and 0 <= y < w  # 範囲外参照


L, n1, n2 = MII()
vl1 = [None] * n1
vl2 = [None] * n2
temp = 0
for i in range(n1):
    v, l = MII()
    temp += l
    vl1[i] = (v, temp)
l1 = [i[1] for i in vl1]

temp = 0
for i in range(n2):
    v, l = MII()
    temp += l
    vl2[i] = (v, temp)
l2 = [i[1] for i in vl2]


l12 = sorted([0] + l1 + l2)

# print(l12)
ans = 0
for i, j in enumerate(l12):
    temp1 = bisect_left(l1, j)
    temp2 = bisect_left(l2, j)
    if j != 0 and vl1[temp1][0] == vl2[temp2][0]:
        ans += j - l12[i - 1]

print(ans)
