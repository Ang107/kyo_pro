import sys

from bisect import bisect_left, bisect_right

import string

# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

sys.setrecursionlimit(10**7)
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

n = int(input())
s = list(map(list, input().split()))

s.sort()
ans = 0

for index, i in enumerate(s):
    tmp = i[:]
    ok = index
    ng = n
    for j in range(len(i)):

        def isOK(mid):
            return j < len(s[mid]) and i[j] == s[mid][j]

        def meguru(ng, ok):
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if isOK(mid):
                    ok = mid
                else:
                    ng = mid
            return ok

        tmp = meguru(ng, ok)
        ans += tmp - index
        ng = tmp + 1

print(ans)
