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


n, h, w = MII()
ab = [LMII() for _ in range(n)]


def solve(use):
    b = [False] * (w * h)
    deq = deque([(0, b)])

    while deq:
        idx, b = deq.pop()
        fin = True
        for i in range(h):
            for j in range(w):
                if b[i * w + j]:
                    pass
                else:
                    fin = False
                    break
        if fin:
            return True
        if idx == len(use):
            continue

        p, q = use[idx]
        not_rotate = False
        rotate = False

        for i in range(h):
            for j in range(w):
                if not_rotate and rotate:
                    break
                if not not_rotate:
                    # not rotate
                    flag = True
                    for x in range(p):
                        for y in range(q):
                            if (
                                i + x in range(h)
                                and j + y in range(w)
                                and not b[(i + x) * w + j + y]
                            ):
                                pass
                            else:
                                flag = False
                                break
                    if flag:
                        b_n = b[:]
                        for x in range(p):
                            for y in range(q):
                                b_n[(i + x) * w + j + y] = True
                        deq.append((idx + 1, b_n))
                        not_rotate = True

                if not rotate:
                    # rotate
                    flag = True
                    for x in range(q):
                        for y in range(p):
                            if (
                                i + x in range(h)
                                and j + y in range(w)
                                and not b[(i + x) * w + j + y]
                            ):
                                pass
                            else:
                                flag = False
                                break
                    if flag:
                        b_n = b[:]
                        for x in range(q):
                            for y in range(p):
                                b_n[(i + x) * w + j + y] = True
                        deq.append((idx + 1, b_n))
                        rotate = True
            if not_rotate and rotate:
                break
    return False


for i in range(2**n):
    use = []
    for j in range(n):
        if i >> j & 1:
            use.append(ab[j])

        if sum([p * q for p, q in use]) == h * w:
            for per in permutations(use):
                if solve(per):
                    PY()
                    exit()
PN()
