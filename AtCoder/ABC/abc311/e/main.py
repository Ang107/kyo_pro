import sys

from itertools import (
    accumulate,
)


# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
# sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

h, w, n = MII()
imos = [[0] * w for _ in range(h)]
ana_ = [[False] * w for _ in range(h)]
for i in range(n):
    a, b = MII()
    ana_[a - 1][b - 1] = True
    imos[a - 1][b - 1] = 1

dp = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if ana_[i][j]:
            continue
        dp[i][j] = 1
        if i - 1 >= 0 and j - 1 >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

# for i in dp:
#     print(i)
ans = sum([sum(i) for i in dp])
print(ans)

# imos = [list(accumulate(i)) for i in imos]
# for i in range(h - 1):
#     for j in range(w):
#         imos[i + 1][j] += imos[i][j]


# def ana(x, y, s):
#     if x + s >= h or y + s >= w:
#         return False
#     tmp = imos[x + s][y + s]
#     if x > 0:
#         tmp -= imos[x - 1][y + s]
#     if y > 0:
#         tmp -= imos[x + s][y - 1]
#     if x > 0 and y > 0:
#         tmp += imos[x - 1][y - 1]

#     return tmp == 0


# def isOK(i, j, mid):
#     return ana(i, j, mid)


# def meguru(i, j, ng, ok):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if isOK(i, j, mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok


# ans = 0
# # 正方形のサイズ

# for i in range(h):
#     for j in range(w):
#         if ana_[i][j]:
#             continue
#         s = meguru(i, j, min(h - i, w - j) + 1, 0) + 1
#         ans += s

# print(ans)
