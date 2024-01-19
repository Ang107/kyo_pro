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
input = lambda: sys.stdin.readline().rstrip()
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


n,k,p = MII()
CA = [LMII() for _ in range(n) ]
dp = [[inf]*(p+1)**k for _ in range(n+1)]
#個目まで、値
dp[0][0] = 0
# 10進数->n進数
def base_n(num_10, n):
    if num_10 == 0:
        return 0
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return int(str_n[::-1])

for i in range(1,n+1):
    for j in range((p+1)**k):
        #not use
        notuse = dp[i-1][j]
        #use
        use = inf
        st = 0
        cost = CA[i-1][0]
        a = CA[i-1][1:]
        tmp = str(base_n(j,p+1))
        st = [0]*(k-len(tmp))
        for l in tmp:
            st.append(int(l))
        num = 0
        for l,m in enumerate(a):
            st[l] = max(0,st[l]-a[l])
        for l,m in enumerate(st[::-1]):
            num += m * (p+1) ** l
        

        
        # if st <= j:
        use = dp[i-1][num]+cost
        # else:
        #     dp[i][st] = min(dp[i][st],cost)
        dp[i][j] = min(use,notuse)
        # print(a,tmp,st,num,)
ans = dp[n][-1]
if ans == inf:
    print(-1)
else:
    print(ans)
# for i in dp:
#     print([(j,k) for j,k in enumerate(i)])