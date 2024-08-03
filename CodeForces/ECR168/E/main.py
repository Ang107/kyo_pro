import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import string
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

alph_s = tuple(string.ascii_lowercase)
alph_l = tuple(string.ascii_uppercase)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

from bisect import bisect_left, insort_left, bisect_right, insort_right


# 以下
def le(l, x):
    idx = bisect_left(l, x)
    if 0 <= idx < len(l) and l[idx] == x:
        return x
    elif 0 <= idx - 1 < len(l):
        return l[idx - 1]
    else:
        return None


# 以上
def ge(l, x):
    idx = bisect_right(l, x)
    if 0 <= idx - 1 < len(l) and l[idx - 1] == x:
        return x
    elif 0 <= idx < len(l):
        return l[idx]
    else:
        return None


# より小さい
def lt(l, x):
    idx = bisect_left(l, x)
    if 0 <= idx - 1 < len(l):
        return l[idx - 1]
    else:
        return None


# より大きい
def gt(l, x):
    idx = bisect_right(l, x)
    if 0 <= idx < len(l):
        return l[idx]
    else:
        return None


n, q = MII()
a = LMII()
fight = {}
k_list = []
for k in range(1, n + 450, 450):
    tmp = []
    cnt = 0
    for i in a:
        if 1 + cnt // k > i:
            tmp.append(False)
            pass
        else:
            cnt += 1
            tmp.append(True)
    fight[k] = tmp
    k_list.append(tmp)

print(fight)
ans = []
def f(k):
    
    
for _ in range(q):
    i, x = MII()
    i -= 1
    l, r = le(k_list, x), ge(k_list, x)
    if not l:
        assert 1 == 0
    else:
        if r:
            if fight[l][i] == True:
                ans.append("YES")
            else:
                if fight[r][i] == True:
                    for 
                else:
                    ans.append("NO")

        else:
            if
            
            
        
        
