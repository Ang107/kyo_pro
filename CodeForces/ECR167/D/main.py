import sys
from bisect import bisect_left, bisect_right

import string

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


n, m = MII()

a = LMII()
b = LMII()
c = LMII()
ans = 0

# 残りのブロックがiの時に、経験値を2得ることのできる最小の支払い数
prf = [inf] * (10**6 + 10)
for i, j in zip(a, b):
    prf[i] = min(prf[i], i - j)
# 累積minを取る
for i in range(1, 10**6 + 1):
    prf[i] = min(prf[i - 1], prf[i])

# 残りブロック数がiの時に、そこから得られる経験値の最大値
dp = [0] * (10**6 + 10)
for i in range(10**6 + 1):
    if i - prf[i] >= 0:
        dp[i] = dp[i - prf[i]] + 2


for i in c:
    if i <= 10**6:
        ans += dp[i]
    else:
        tmp = (i - 10**6) // prf[10**6] + 1
        ans += 2 * tmp
        i -= prf[10**6] * tmp
        ans += dp[i]
print(ans)

# 作れるやつの中でコスパが最も良いものを選びたい。

# ab = [(i, i - j) for i, j in zip(a, b)]

# ab.sort(key=lambda x: x[0])
# ab_new = []
# tmp = inf
# for i, k in ab:
#     if tmp > k:
#         tmp = k
#         ab_new.append((i, k))

# ab = ab_new


# score = [(i[1], idx) for idx, i in enumerate(ab)]
# a = [i[0] for i in ab]
# min_ = []

# for i in score:
#     if not min_:
#         min_.append(i)
#     else:
#         min_.append(min(min_[-1], i))


# dp = [0] * (10**6 + 1)
# idx = -1
# for i in range(10**6 + 1):
#     while True:
#         if idx + 1 < len(a) and a[idx + 1] <= i:
#             idx += 1
#         else:
#             break
#     if idx == -1:
#         continue
#     rslt = min_[idx]
#     dp[i] = dp[i - rslt[0]] + 2

# for i in c:
#     amari = i
#     if amari <= 10**6:
#         ans += dp[amari]
#     else:
#         rslt = min_[-1]
#         tmp = (amari - a[rslt[1]]) // rslt[0] + 1
#         ans += tmp * 2
#         amari -= tmp * rslt[0]
#         ans += dp[amari]

# print(ans)
