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
import string

# 小文字アルファベットのリスト
alph_s = list(string.ascii_lowercase)
# 大文字アルファベットのリスト
alph_l = list(string.ascii_uppercase)

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


# n以下の素数のリストを取得
def get_Sosuu(n):
    A = list(range(2, n + 1))
    p = list()
    while A[0] ** 2 <= n:
        tmp = A[0]
        p.append(tmp)
        A = [e for e in A if e % tmp != 0]
    return p + A


# 各入力に対する処理
def main(n):
    sosuu = get_Sosuu(n)
    ans = 0
    for i in sosuu:
        for j in sosuu:
            if i + j == n:
                ans = max(ans, i * j)
    return ans


if __name__ == "__main__":
    # 入力をここに追加
    Input = [9876, 1358, 4922]

    Output = []
    for i in Input:
        Output.append(main(i))
    print(*Output)
