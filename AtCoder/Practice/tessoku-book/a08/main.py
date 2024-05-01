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
def acc_2d(x):
    h,w = len(x),len(x[0])
    ans = [[0] * w for _ in range(h)]
    for i,j in enumerate(x):
        ans[i] = list(accumulate(j))
    for i in range(1,h):
        for j in range(w):
            ans[i][j] = ans[i-1][j] + ans[i][j]
    return ans

h,w = MII()
X = [LMII() for _ in range(h)]
q = II()
acc_x = acc_2d(X)
# pprint(acc_x)
for i in range(q):
    a,b,c,d = MII()
    ans = acc_x[c-1][d-1]
    if a >= 2:
        ans -= acc_x[a-2][d-1] 
    
    if b >= 2:
        ans -= acc_x[c-1][b-2]
    
    if a >= 2 and b >= 2:
        ans += acc_x[a-2][b-2]
        
    print(ans)
