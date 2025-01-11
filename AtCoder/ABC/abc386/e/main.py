# oj t -c "python3 main.py"
import sys, math

sys.setrecursionlimit(10**7)
from collections import defaultdict, deque
from itertools import combinations, permutations, accumulate, product
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush, heapify


# from more_itertools import distinct_permutations,distinct_combinations
# from sortedcontainers import SortedList,SortedSet
def input():
    return sys.stdin.readline().rstrip()


def ii():
    return int(input())


def ms():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


inf = pow(10, 18)
mod = 998244353
# /////////////////////////////////
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10**7)
N, K = ms()
A = li()

flag = False
if K > N - K:
    flag = True
    K = N - K

SUM = 0
for a in A:
    SUM ^= a

ans = 0


def dfs(i, LEN, tmp):
    global ans
    for j in range(i + 1, N):
        nex = tmp ^ A[j]
        if LEN + 1 == K:
            if flag == False:
                ans = max(ans, nex)
            else:
                ans = max(ans, SUM ^ nex)
        else:
            dfs(j, LEN + 1, nex)


dfs(-1, 0, 0)
print(ans)
