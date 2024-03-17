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


# 各入力に対する処理
def main(n):
    # i個目まで合計j円で飲み物の質量の合計,おやつの値段の時の質量の最大値

    n = [(j, k, l) for i, j, k, l in n if j != "omotya"]
    # print(n)
    # dp = [
    #     [[[0] * 501 for _ in range(701)] for _ in range(2001)] for _ in range(len(n) + 1)
    # ]
    # for i in range(1,len(n)+1):
    #     for j in
    s = set()
    s.add((0, 0, 0, 0))
    for i, j, k in n:
        tmp = set()
        for o, p, q, r in s:
            tmp.add((o, p, q, r))
            p_n, q_n, r_n = p, q, r
            if i == "oyatu":
                r_n = r + j
            elif i == "nomimono":
                q_n = q + k
            o_n = o + k
            p_n = p + j
            if p_n <= 2000 and r_n <= 500:
                tmp.add((o_n, p_n, q_n, r_n))
        s = tmp

    # print(s)
    return max([o for o, p, q, r in s if q >= 700])


if __name__ == "__main__":
    # 入力をここに追加
    Input = [
        [
            ["cake", "oyatu", 322, 765],
            ["chienowa", "omotya", 252, 670],
            ["jigsaw puzzle", "omotya", 410, 974],
            ["onigiri", "bento", 250, 870],
            ["salad", "bento", 314, 481],
            ["suika", "oyatu", 321, 764],
            ["chocolate", "oyatu", 59, 86],
            ["ham", "bento", 54, 10],
            ["ginger ale", "nomimono", 185, 196],
            ["mizu", "nomimono", 229, 196],
            ["umebosi", "bento", 347, 873],
            ["orange juice", "nomimono", 477, 271],
            ["crisps", "oyatu", 38, 452],
            ["banana", "oyatu", 49, 943],
            ["syakeben", "bento", 472, 886],
            ["ball", "omotya", 321, 927],
            ["apple juice", "nomimono", 408, 302],
            ["sandwich", "bento", 9, 48],
            ["cookie", "oyatu", 33, 783],
            ["sports drink", "nomimono", 230, 197],
            ["tamagoyaki", "bento", 22, 696],
            ["chikuwa", "bento", 286, 90],
            ["otya", "nomimono", 117, 503],
            ["sausage", "bento", 306, 597],
            ["senbei", "oyatu", 346, 648],
        ],
        [
            ["syakeben", "bento", 110, 200],
            ["chikuwa", "bento", 200, 200],
            ["orange juice", "nomimono", 663, 1987],
            ["onigiri", "bento", 110, 200],
            ["apple juice", "nomimono", 505, 2000],
            ["kendama", "omotya", 1, 2000],
            ["grape juice", "nomimono", 312, 1999],
            ["sandwich", "bento", 110, 200],
            ["coffee", "nomimono", 2000, 2000],
            ["ukiwa", "omotya", 2000, 1],
            ["senbei", "oyatu", 5, 40],
            ["cake", "oyatu", 100, 100],
            ["noriben", "bento", 300, 600],
            ["crisps", "oyatu", 2000, 2000],
            ["chienowa", "omotya", 1, 1],
        ],
        [
            ["apple tea", "nomimono", 324, 118],
            ["apple", "oyatu", 33, 35],
            ["gum", "oyatu", 97, 828],
            ["dango", "oyatu", 55, 698],
            ["coffee", "nomimono", 210, 115],
            ["grape", "oyatu", 140, 401],
            ["crisps", "oyatu", 32, 794],
            ["cookie", "oyatu", 24, 522],
            ["salad", "bento", 15, 143],
            ["sports drink", "nomimono", 125, 75],
            ["pine juice", "nomimono", 308, 103],
            ["umebosi", "bento", 19, 206],
            ["cake", "oyatu", 42, 971],
            ["cherry juice", "nomimono", 398, 145],
            ["senbei", "oyatu", 79, 996],
            ["onigiri", "bento", 105, 84],
            ["cocoa", "nomimono", 204, 60],
            ["gummy", "oyatu", 111, 320],
            ["banana", "oyatu", 41, 837],
            ["tamagoyaki", "bento", 45, 45],
            ["melon juice", "nomimono", 505, 105],
            ["sandwich", "bento", 73, 80],
            ["grape juice", "nomimono", 126, 47],
            ["tomato", "bento", 65, 40],
            ["suika", "oyatu", 29, 955],
            ["sausage", "bento", 61, 203],
            ["banana juice", "nomimono", 363, 125],
            ["tansansui", "nomimono", 181, 60],
            ["cherry", "oyatu", 241, 105],
            ["ham", "bento", 39, 555],
            ["syakeben", "bento", 10, 301],
            ["orange juice", "nomimono", 129, 114],
            ["peach juice", "nomimono", 364, 129],
            ["rice", "bento", 376, 245],
            ["yakisoba", "bento", 42, 57],
            ["otya", "nomimono", 104, 68],
            ["noriben", "bento", 86, 228],
            ["bread", "bento", 190, 62],
            ["milk", "nomimono", 180, 102],
            ["water", "nomimono", 109, 30],
            ["pudding", "oyatu", 68, 807],
            ["potate", "bento", 96, 65],
            ["chocolate", "oyatu", 40, 550],
            ["ball", "omotya", 1, 2000],
            ["apple juice", "nomimono", 74, 116],
            ["fish", "bento", 302, 145],
            ["chikuwa", "bento", 27, 307],
            ["ginger ale", "nomimono", 101, 42],
        ],
    ]

    Output = []
    for i in Input:
        Output.append(main(i))
    print(f"{Output[0]},{Output[1]},{Output[2]}")
