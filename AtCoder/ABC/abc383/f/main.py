from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n, x, K = MII()
is_last = [False] * n
puc = [tuple(LMII()) for _ in range(n)]

puc.sort(key=lambda x: x[2])
for index, (p, u, c) in enumerate(puc):
    if index == n - 1 or c != puc[index + 1][2]:
        is_last[index] = True

# i 番目の商品までで、合計金額がjで、今いるエリアの商品を買ったかどうかがkのときの満足度の最大値
dp = [[-(1 << 63)] * 2 for _ in range(x + 1)]
dp[0][0] = 0
next_dp = [[-(1 << 63)] * 2 for _ in range(x + 1)]
for i in range(n):
    for j in range(x + 1):
        for k in range(2):
            p, u, c = puc[i]
            if is_last[i]:
                # 買う
                if k == 1:
                    if j + p <= x:
                        if next_dp[j + p][0] < dp[j][k] + u:
                            next_dp[j + p][0] = dp[j][k] + u
                else:
                    if j + p <= x:
                        if next_dp[j + p][0] < dp[j][k] + u + K:
                            next_dp[j + p][0] = dp[j][k] + u + K

                # 買わない
                next_dp[j][0] = max(next_dp[j][0], dp[j][k])
                next_dp[j][1] = max(next_dp[j][1], dp[j][k])

            else:
                # 買う
                if k == 1:
                    if j + p <= x:
                        next_dp[j + p][1] = max(next_dp[j + p][1], dp[j][k] + u)
                else:
                    if j + p <= x:
                        next_dp[j + p][1] = max(next_dp[j + p][1], dp[j][k] + u + K)

                # 買わない
                next_dp[j][k] = max(next_dp[j][k], dp[j][k])
    dp, next_dp = next_dp, dp

ans = 0


for j in range(x + 1):
    for k in range(2):
        ans = max(ans, dp[j][k])
print(ans)
