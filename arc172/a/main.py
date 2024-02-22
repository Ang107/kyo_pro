import sys

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


sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)


def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict

II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
PY = lambda: print("Yes")
PN = lambda: print("No")
h, w, n = MII()
a = LMII()
a.sort(reverse=True)
dd = defaultdict(int)
# 面積が足りるか
S = 0
for i in a:
    S += (2**i) ** 2
    dd[i] += 1
if S > h * w:
    PN()
    exit()


# def solve(h, w, size):
#     return (h // size) * (w // size)
# dd[26] = 0

d = {}

d[26] = 0
for i in range(25, -1, -1):
    size = 2**i
    # print(i, 2**i, solve(h, w, 2**i))
    tmp = 0
    for k, v in d.items():
        tmp += v * 4 ** (math.log(k, 2) - i)
    d[size] = (h // size) * (w // size) - tmp

# # print(dd, d)
# for i in range(25, -1, -1):
#     # print(dd[i], d[i], dd[i + 1])
#     d[i] += d[i + 1] * 4
#     d[i] -= dd[i]
#     # print(dd[i])
#     if d[i] < 0:
#         PN()
#         exit()
# PY()


# 長方形を、より大きな正方形の組に分解
def henkan(h, w):
    tmp = defaultdict(int)
    if h == 0 or w == 0:
        return tmp
    if h == w:
        tmp[h] += 1
        return tmp
    while True:
        if h == 0 or w == 0:
            break
        elif h > w:
            num = h // w
            amari = h % w
            tmp[w] += num
            h = amari
        elif h < w:
            num = w // h
            amari = w % h
            tmp[h] += num
            w = amari
    return tmp


# key : 正方形の辺の長さ, valuse :個数
dd = d
# 正方形の辺の長さ
size = SortedSet()

# 初期化
for i, j in d.items():
    if j > 0:
        size.add(i)

for i in a:
    print(size, dd)
    I = 2**i

    # 使う正方形より大きく、存在する正方形の中で最も小さいものを選ぶ
    idx = size.bisect_left(I)
    # 使う正方形以上の大きさの正方形が存在しないなら
    if idx == len(size):
        PN()
        exit()

    # 使用する正方形の一片の長さ
    tmp = size[idx]

    # 使用分の削除
    if dd[tmp] == 1:
        size.remove(tmp)
    dd[tmp] -= 1

    # 使って余った部分の追加
    dd_n = henkan(tmp - I, tmp)
    for p, q in dd_n.items():
        if dd[p] == 0:
            size.add(p)
        dd[p] += q

    dd_n = henkan(tmp - I, I)
    for p, q in dd_n.items():
        if dd[p] == 0:
            size.add(p)
        dd[p] += q

PY()
