from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False


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


# 各入力に対する処理
def main(a):
    a = [a[0], a[3], a[4], a[1], a[2]]
    h = [10, 13, 16, 9, 6]
    # アイス・今川・大判をi個，キャンディをj個入れるときのせんべいを入れられる個数
    memo = [[[-1] * 100 for _ in range(100)] for _ in range(3)]
    for i in range(3):
        for j in range(100):
            for k in range(100):
                if h[i] * j + 9 * k <= 80:
                    memo[i][j][k] = (80 - h[i] * j + 9 * k) // 6
    # 運んだキャンディの数がiせんべいの数がjのときの，運搬数の最小値
    dp = [[[inf] * (a[4] + 1) for _ in range(a[3] + 1)] for _ in range(a[0] + 1)]
    dp[0][0][0] = 0
    for i in range(a[0] + 1):
        for j in range(a[3] + 1):
            for k in range(a[4] + 1):
                for p in range(a[0] - i + 1):
                    if 10 * p > 80:
                        break
                    for q in range(a[3] - j + 1):
                        if 10 * p + 9 * q > 80:
                            break
                        dp[i + p][j + q][min(k + memo[0][p][q], a[4])] = min(
                            dp[i + p][j + q][min(k + memo[0][p][q], a[4])],
                            dp[i][j][k] + 1,
                        )
    ndp = [[[inf] * (a[4] + 1) for _ in range(a[3] + 1)] for _ in range(a[1] + 1)]
    # print(dp)
    for i in range(a[3] + 1):
        for j in range(a[4] + 1):
            ndp[0][i][j] = dp[a[0]][i][j]
    dp = ndp

    for i in range(a[1] + 1):
        for j in range(a[3] + 1):
            for k in range(a[4] + 1):
                for p in range(a[1] - i + 1):
                    if 13 * p > 80:
                        break
                    for q in range(a[3] - j + 1):
                        if 13 * p + 9 * q > 80:
                            break
                        dp[i + p][j + q][min(k + memo[1][p][q], a[4])] = min(
                            dp[i + p][j + q][min(k + memo[1][p][q], a[4])],
                            dp[i][j][k] + 1,
                        )
    ndp = [[[inf] * (a[4] + 1) for _ in range(a[3] + 1)] for _ in range(a[2] + 1)]
    for i in range(a[3] + 1):
        for j in range(a[4] + 1):
            ndp[0][i][j] = dp[a[1]][i][j]
    dp = ndp
    for i in range(a[2] + 1):
        for j in range(a[3] + 1):
            for k in range(a[4] + 1):
                for p in range(a[2] - i + 1):
                    if 16 * p > 80:
                        break
                    for q in range(a[3] - j + 1):
                        if 16 * p + 9 * q > 80:
                            break
                        dp[i + p][j + q][min(k + memo[2][p][q], a[4])] = min(
                            dp[i + p][j + q][min(k + memo[2][p][q], a[4])],
                            dp[i][j][k] + 1,
                        )
    ans = inf
    ans = min(ans, dp[a[2]][a[3]][a[4]])
    return ans


"""
上限が80
アイスと今川焼，大判焼きの同時はだめ
今川と大判も同時はダメ
"""

if __name__ == "__main__":
    # 入力をここに追加
    Input = [[4, 7, 1, 2, 6], [11, 7, 13, 1, 13], [58, 54, 72, 77, 81]]

    Output = []
    for i in Input:
        Output.append(main(i))
    print(f"{Output[0]},{Output[1]},{Output[2]}")
