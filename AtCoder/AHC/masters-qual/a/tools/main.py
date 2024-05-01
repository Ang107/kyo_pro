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
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1), (0, 0))  # 上下左右
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


def calc_can_visit():
    global UDLR
    UDLR = [[] for _ in range(N**2)]

    for i in range(N):
        for j in range(N):
            UDLR[i * N + j].append(4)
            # 上
            if 0 <= i - 1 < N - 1 and 0 <= j < N:
                if h[i - 1][j] == "0":
                    UDLR[i * N + j].append(0)
            # 下
            if 0 <= i < N - 1 and 0 <= j < N:
                if h[i][j] == "0":
                    UDLR[i * N + j].append(1)

            # 左
            if 0 <= j - 1 < N - 1 and 0 <= i < N:
                if v[i][j - 1] == "0":
                    UDLR[i * N + j].append(2)
            # 右
            if 0 <= j < N - 1 and 0 <= i < N:
                if v[i][j] == "0":
                    UDLR[i * N + j].append(3)
    # print(UDLR)


def choice_calender():
    global calender
    calender = []
    tmp = []
    for i in range(N):
        for j in range(N):
            tmp.append(i * N + j)
    calender.append(tmp)

    tmp = []
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            tmp.append(i * N + j)
    calender.append(tmp)

    tmp = []
    for i in range(N):
        for j in range(N - 1, -1, -1):
            tmp.append(i * N + j)
    calender.append(tmp)

    tmp = []
    for i in range(N - 1, -1, -1):
        for j in range(N):
            tmp.append(i * N + j)
    calender.append(tmp)

    diff_num = N**2
    idx = 0
    for i, j in enumerate(calender):
        tmp = 0
        for k, l in zip(a, j):
            if k != l:
                tmp += 1
        if tmp < diff_num:
            diff_num = tmp
            idx = i

    calender = calender[idx]
    # print(calender)


def Input():
    global t, N, h, v, a
    t, N = MII()
    v = [input() for _ in range(N)]
    h = [input() for _ in range(N - 1)]
    # print(v, h)
    a = []
    for i in range(N):
        a.extend(LMII())


def Start():
    global TK_x, TK_y, AO_x, AO_y
    # Clear = [False] * (N**2)
    # for idx, (i, j) in enumerate(zip(calender, a)):
    #     if i != j:
    #         TK_x, TK_y = idx // N, idx % N
    #     else:
    #         Clear[idx] = True

    # for idx, i in enumerate(a):
    #     if i == calender[TK_x * N + TK_y]:
    #         AO_x, AO_y = idx // N, idx % N
    #         break
    TK_x, TK_y, AO_x, AO_y = (
        random.choice(range(N)),
        random.choice(range(N)),
        random.choice(range(N)),
        random.choice(range(N)),
    )
    print(TK_x, TK_y, AO_x, AO_y)


import random


def calc_bef():
    global before
    before = [0] * (N**2)
    for i in range(N**2):
        for p in UDLR[i]:
            before[i] += (
                a[i] - a[(i // N + around4[p][0]) * N + i % N + around4[p][1]]
            ) ** 2


def get_good(s):
    if s == 1:
        kaizen = [[0] * N**2 for _ in range(N**2)]
        for i in range(N**2):
            for j in range(i + 1, N**2):
                for p in UDLR[i]:
                    kaizen[i][j] += (
                        a[j] - a[(i // N + around4[p][0]) * N + i % N + around4[p][1]]
                    ) ** 2
                for p in UDLR[j]:
                    kaizen[i][j] += (
                        a[i] - a[(j // N + around4[p][0]) * N + j % N + around4[p][1]]
                    ) ** 2
                kaizen[i][j] = before[i] + before[j] - kaizen[i][j]
                x, y, p, q = i // N, i % N, j // N, j % N
                dis = min(
                    abs(TK_x - x) + abs(TK_y - y) + abs(AO_x - p) + abs(AO_y - q),
                    abs(TK_x - p) + abs(TK_y - q) + abs(AO_x - x) + abs(AO_y - y),
                )
                kaizen[i][j] /= dis**0.5 + 1
        # print(kaizen)
        tmp = -10000000
        for i in range(N**2):
            for j in range(i + 1, N**2):
                if kaizen[i][j] > tmp:
                    tmp = kaizen[i][j]
                    p, q = i, j
        a[p], a[q] = a[q], a[p]

        for i in UDLR[p]:
            before[(p // N + around4[i][0]) * N + p % N + around4[i][1]] = 0
            for j in UDLR[(p // N + around4[i][0]) * N + p % N + around4[i][1]]:
                before[p] += (
                    a[p] - a[(p // N + around4[i][0]) * N + p % N + around4[i][1]]
                )
        for i in UDLR[q]:
            before[(q // N + around4[i][0]) * N + q % N + around4[i][1]] = 0
            for j in UDLR[(q // N + around4[i][0]) * N + q % N + around4[i][1]]:
                before[q] += (
                    a[q] - a[(q // N + around4[i][0]) * N + q % N + around4[i][1]]
                )

        return p, q
    else:
        kaizen = [[0] * N**2 for _ in range(N**2)]
        for i in range(N**2):
            for j in range(i + 1, N**2):
                for p in UDLR[i]:
                    kaizen[i][j] += (
                        a[j] - a[(i // N + around4[p][0]) * N + i % N + around4[p][1]]
                    ) ** 2
                for p in UDLR[j]:
                    kaizen[i][j] += (
                        a[i] - a[(j // N + around4[p][0]) * N + j % N + around4[p][1]]
                    ) ** 2
                kaizen[i][j] = before[i] + before[j] - kaizen[i][j]
                x, y, p, q = i // N, i % N, j // N, j % N
                dis = 0
                kaizen[i][j] /= dis**0.5 + 1
        # print(kaizen)
        tmp = -10000000
        for i in range(N**2):
            for j in range(i + 1, N**2):
                if kaizen[i][j] > tmp:
                    tmp = kaizen[i][j]
                    p, q = i, j
        a[p], a[q] = a[q], a[p]

        for i in UDLR[p]:
            before[(p // N + around4[i][0]) * N + p % N + around4[i][1]] = 0
            for j in UDLR[(p // N + around4[i][0]) * N + p % N + around4[i][1]]:
                before[p] += (
                    a[p] - a[(p // N + around4[i][0]) * N + p % N + around4[i][1]]
                )
        for i in UDLR[q]:
            before[(q // N + around4[i][0]) * N + q % N + around4[i][1]] = 0
            for j in UDLR[(q // N + around4[i][0]) * N + q % N + around4[i][1]]:
                before[q] += (
                    a[q] - a[(q // N + around4[i][0]) * N + q % N + around4[i][1]]
                )

        return p, q


def solve():
    global TK_x, TK_y, AO_x, AO_y, visited, ans, zahyou
    # visited = [[False] * (N**2) for _ in range(N**2)]
    cnt = 0
    ans = []
    zahyou = []
    calc_bef()
    p, q = get_good(0)
    TK_x, TK_y = p // N, p % N
    AO_x, AO_y = q // N, q % N
    print(TK_x, TK_y, AO_x, AO_y)
    print(1, ".", ".")
    while True:
        p, q = get_good(1)
        # print(TK_x, TK_y, AO_x, AO_y, p, q)
        if abs(TK_x - p // N) + abs(TK_y - p % N) + abs(AO_x - q // N) + abs(
            AO_y - q % N
        ) < abs(TK_x - q // N) + abs(TK_y - q % N) + abs(AO_x - p // N) + abs(
            AO_y - p % N
        ):
            TKR = get_next_TK(TK_x, TK_y, p)
            AOR = get_next_AO(AO_x, AO_y, q)
            TK_x, TK_y = p // N, p % N
            AO_x, AO_y = q // N, q % N
        else:
            TKR = get_next_TK(TK_x, TK_y, q)
            AOR = get_next_AO(AO_x, AO_y, p)
            TK_x, TK_y = q // N, q % N
            AO_x, AO_y = p // N, p % N

        if cnt + max(len(TKR), len(AOR)) < 4 * N**2:
            cnt += max(len(TKR), len(AOR))
            Out(TKR, AOR)
        else:
            exit()

    # i, j = random.choice(UDLR[TK_x * N + TK_y]), random.choice(
    #     UDLR[AO_x * N + AO_y]
    # )
    # zahyou.append((TK_x * N + TK_y, AO_x * N + AO_y))
    # ans.append([0, i, j])
    # TK_x, TK_y = TK_x + around4[i][0], TK_y + around4[i][1]
    # AO_x, AO_y = AO_x + around4[j][0], AO_y + around4[j][1]
    # yamanobori()
    # for i in ans:
    #     Out(*i)
    # i, j, k = judge()
    # if i == 1:
    #     a[(AO_x) * N + (AO_y)], a[(TK_x) * N + (TK_y)] = (
    #         a[(TK_x) * N + (TK_y)],
    #         a[(AO_x) * N + (AO_y)],
    #     )
    # visited[TK_x * N + TK_y][AO_x * N + AO_y] = True
    # # print(i, j, k)
    # TK_x, TK_y = TK_x + around4[j][0], TK_y + around4[j][1]
    # AO_x, AO_y = AO_x + around4[k][0], AO_y + around4[k][1]

    # Out(i, j, k)
    # print(TK_x, TK_y, AO_x, AO_y)

    # TK, num = get_next_TK(TK_x, TK_y)
    # AO = get_next_AO(AO_x, AO_y, num)
    # for i in TK:
    #     TK_x += around4[i][0]
    #     TK_y += around4[i][1]

    # for i in AO:
    #     AO_x += around4[i][0]
    #     AO_y += around4[i][1]

    # a[TK_x * N + TK_y], a[AO_x * N + AO_y] = a[AO_x * N + AO_y], a[TK_x * N + TK_y]
    # if cnt + max(len(TK), len(AO)) < 4 * N**2:
    #     cnt += max(len(TK), len(AO))
    #     Out(TK, AO)
    # else:
    #     break


def yamanobori():
    change = SortedSet()
    score = 0
    for i in range(N):
        for j in range(N - 1):
            if v[i][j] == "0":
                score += (a[i * N + j] - a[i * N + j + 1]) ** 2
    for i in range(N - 1):
        for j in range(N):
            if h[i][j] == "0":
                score += (a[i * N + j] - a[(i + 1) * N + j]) ** 2

    while time.perf_counter() - start < 1.5:
        idx = random.choice(range(4 * N**2))
        change.add(idx)

        a[zahyou[idx][0]], a[zahyou[idx][1]] = a[zahyou[idx][1]], a[zahyou[idx][0]]
        tmp = 0
        for i in range(N):
            for j in range(N - 1):
                if v[i][j] == "0":
                    tmp += (a[i * N + j] - a[i * N + j + 1]) ** 2
        for i in range(N - 1):
            for j in range(N):
                if h[i][j] == "0":
                    tmp += (a[i * N + j] - a[(i + 1) * N + j]) ** 2
        # print(tmp)
        if score > tmp:
            score = tmp
            ans[idx][0] = 1
        else:
            a[zahyou[idx][0]], a[zahyou[idx][1]] = a[zahyou[idx][1]], a[zahyou[idx][0]]
            change.discard(idx)


def Out(TK, AO):
    # print(i, "UDLR."[j], "UDLR."[k])
    TK = ["UDLR"[i] for i in TK]
    AO = ["UDLR"[i] for i in AO]
    if len(TK) < len(AO):
        for _ in range(len(AO) - len(TK)):
            TK.append(".")
    elif len(TK) > len(AO):
        for _ in range(len(TK) - len(AO)):
            AO.append(".")
    for idx, (i, j) in enumerate(zip(TK, AO)):
        if idx != len(AO) - 1:
            print(0, i, j)
        else:
            print(1, i, j)
    # for i in range(N):
    #     print(a[i * N : (i + 1) * N])


# def judge():
#     ans = [[[-inf] * 5 for _ in range(5)] for _ in range(2)]

#     # スワップ無し
#     for tk in UDLR[TK_x * N + TK_y]:
#         for ao in UDLR[AO_x * N + AO_y]:
#             x, y, p, q = (
#                 TK_x + around4[tk][0],
#                 TK_y + around4[tk][1],
#                 AO_x + around4[ao][0],
#                 AO_y + around4[ao][1],
#             )
#             bef = []
#             aft = []
#             for i in UDLR[x * N + y]:
#                 i, j = around4[i]
#                 if x + i in range(N) and y + j in range(N):
#                     bef.append((a[(x + i) * N + (y + j)] - a[x * N + y]) ** 2)
#                     aft.append((a[(x + i) * N + (y + j)] - a[p * N + q]) ** 2)
#             for i in UDLR[p * N + q]:
#                 i, j = around4[i]
#                 if p + i in range(N) and q + j in range(N):
#                     bef.append((a[(p + i) * N + (q + j)] - a[p * N + q]) ** 2)
#                     aft.append((a[(p + i) * N + (q + j)] - a[x * N + y]) ** 2)

#             ans[0][tk][ao] = sum(bef) - sum(aft)

#     for tk in UDLR[TK_x * N + TK_y]:
#         x, y, p, q = (
#             TK_x + around4[tk][0],
#             TK_y + around4[tk][1],
#             AO_x,
#             AO_y,
#         )
#         bef = []
#         aft = []
#         for i in UDLR[x * N + y]:
#             i, j = around4[i]
#             if x + i in range(N) and y + j in range(N):
#                 bef.append((a[(x + i) * N + (y + j)] - a[x * N + y]) ** 2)
#                 aft.append((a[(x + i) * N + (y + j)] - a[p * N + q]) ** 2)
#         for i in UDLR[p * N + q]:
#             i, j = around4[i]
#             if p + i in range(N) and q + j in range(N):
#                 bef.append((a[(p + i) * N + (q + j)] - a[p * N + q]) ** 2)
#                 aft.append((a[(p + i) * N + (q + j)] - a[x * N + y]) ** 2)

#         ans[0][tk][4] = sum(bef) - sum(aft)

#     for ao in UDLR[AO_x * N + AO_y]:
#         x, y, p, q = (
#             TK_x,
#             TK_y,
#             AO_x + around4[ao][0],
#             AO_y + around4[ao][1],
#         )
#         bef = []
#         aft = []
#         for i in UDLR[x * N + y]:
#             i, j = around4[i]
#             if x + i in range(N) and y + j in range(N):
#                 bef.append((a[(x + i) * N + (y + j)] - a[x * N + y]) ** 2)
#                 aft.append((a[(x + i) * N + (y + j)] - a[p * N + q]) ** 2)
#         for i in UDLR[p * N + q]:
#             i, j = around4[i]
#             if p + i in range(N) and q + j in range(N):
#                 bef.append((a[(p + i) * N + (q + j)] - a[p * N + q]) ** 2)
#                 aft.append((a[(p + i) * N + (q + j)] - a[x * N + y]) ** 2)

#         ans[0][4][ao] = sum(bef) - sum(aft)

#     # スワップ有
#     bef = []
#     aft = []
#     for i in UDLR[AO_x * N + AO_y]:
#         i, j = around4[i]
#         if x + i in range(N) and y + j in range(N):
#             bef.append((a[(AO_x + i) * N + (AO_y + j)] - a[AO_x * N + AO_y]) ** 2)
#             aft.append((a[(AO_x + i) * N + (AO_y + j)] - a[TK_x * N + TK_y]) ** 2)
#     for i in UDLR[TK_x * N + TK_y]:
#         i, j = around4[i]
#         if p + i in range(N) and q + j in range(N):
#             bef.append((a[(TK_x + i) * N + (TK_y + j)] - a[TK_x * N + TK_y]) ** 2)
#             aft.append((a[(TK_x + i) * N + (TK_y + j)] - a[AO_x * N + AO_y]) ** 2)
#     num = sum(bef) - sum(aft)

#     a_n = a[:]
#     a_n[TK_x * N + TK_y], a_n[AO_x * N + AO_y] = (
#         a_n[AO_x * N + AO_y],
#         a_n[TK_x * N + TK_y],
#     )
#     for tk in UDLR[TK_x * N + TK_y]:
#         for ao in UDLR[AO_x * N + AO_y]:
#             x, y, p, q = (
#                 TK_x + around4[tk][0],
#                 TK_y + around4[tk][1],
#                 AO_x + around4[ao][0],
#                 AO_y + around4[ao][1],
#             )
#             bef = []
#             aft = []
#             for i in UDLR[x * N + y]:
#                 i, j = around4[i]
#                 if x + i in range(N) and y + j in range(N):
#                     bef.append((a_n[(x + i) * N + (y + j)] - a_n[x * N + y]) ** 2)
#                     aft.append((a_n[(x + i) * N + (y + j)] - a_n[p * N + q]) ** 2)
#             for i in UDLR[p * N + q]:
#                 i, j = around4[i]
#                 if p + i in range(N) and q + j in range(N):
#                     bef.append((a_n[(p + i) * N + (q + j)] - a_n[p * N + q]) ** 2)
#                     aft.append((a_n[(p + i) * N + (q + j)] - a_n[x * N + y]) ** 2)

#             ans[1][tk][ao] = sum(bef) - sum(aft) + num

#     for tk in UDLR[TK_x * N + TK_y]:
#         x, y, p, q = (
#             TK_x + around4[tk][0],
#             TK_y + around4[tk][1],
#             AO_x,
#             AO_y,
#         )
#         bef = []
#         aft = []
#         for i in UDLR[x * N + y]:
#             i, j = around4[i]
#             if x + i in range(N) and y + j in range(N):
#                 bef.append((a[(x + i) * N + (y + j)] - a[x * N + y]) ** 2)
#                 aft.append((a[(x + i) * N + (y + j)] - a[p * N + q]) ** 2)
#         for i in UDLR[p * N + q]:
#             i, j = around4[i]
#             if p + i in range(N) and q + j in range(N):
#                 bef.append((a[(p + i) * N + (q + j)] - a[p * N + q]) ** 2)
#                 aft.append((a[(p + i) * N + (q + j)] - a[x * N + y]) ** 2)

#     for ao in UDLR[AO_x * N + AO_y]:
#         x, y, p, q = (
#             TK_x,
#             TK_y,
#             AO_x + around4[ao][0],
#             AO_y + around4[ao][1],
#         )
#         bef = []
#         aft = []
#         for i in UDLR[x * N + y]:
#             i, j = around4[i]
#             if x + i in range(N) and y + j in range(N):
#                 bef.append((a_n[(x + i) * N + (y + j)] - a_n[x * N + y]) ** 2)
#                 aft.append((a_n[(x + i) * N + (y + j)] - a_n[p * N + q]) ** 2)
#         for i in UDLR[p * N + q]:
#             i, j = around4[i]
#             if p + i in range(N) and q + j in range(N):
#                 bef.append((a_n[(p + i) * N + (q + j)] - a_n[p * N + q]) ** 2)
#                 aft.append((a_n[(p + i) * N + (q + j)] - a_n[x * N + y]) ** 2)

#         ans[1][4][ao] = sum(bef) - sum(aft) + num

#     # print(num, ans)
#     tmp = -1000000
#     for i in range(1, 2):
#         for j in range(5):
#             for k in range(5):
#                 if (
#                     ans[i][j][k] > tmp
#                     and not visited[
#                         (TK_x + around4[j][0]) * N + (TK_y + around4[j][1])
#                     ][(AO_x + around4[k][0]) * N + (AO_y + around4[k][1])]
#                 ):
#                     ret = i, j, k

#     return ret


import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional

T = TypeVar("T")


class SortedSet(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [
            a[n * i // num_bucket : n * (i + 1) // num_bucket]
            for i in range(num_bucket)
        ]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]:
                break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x:
            return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]
        return True

    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a:
            del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x:
            return False
        self._pop(a, b, i)
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self.a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0:
                    return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a):
                    return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


def get_next_AO(x, y, target):
    visited = [-1] * (N**2)
    deq = deque([(x, y)])
    visited[x * N + y] = 0
    while deq:
        x, y = deq.popleft()
        for i in UDLR[x * N + y]:
            if visited[(x + around4[i][0]) * N + (y + around4[i][1])] == -1:
                deq.append((x + around4[i][0], y + around4[i][1]))
                visited[(x + around4[i][0]) * N + (y + around4[i][1])] = (
                    visited[x * N + y] + 1
                )

            if (x + around4[i][0]) * N + (y + around4[i][1]) == target:
                deq = []
                x, y = x + around4[i][0], y + around4[i][1]
                break
    ans = []
    flag = True

    while flag and visited[x * N + y] != 0:

        for i in UDLR[x * N + y]:
            if visited[(x + around4[i][0]) * N + (y + around4[i][1])] == 0:
                if i == 0:
                    tmp = 1
                elif i == 1:
                    tmp = 0
                elif i == 2:
                    tmp = 3
                elif i == 3:
                    tmp = 2
                ans.append(tmp)
                flag = False
                break
            if (
                visited[(x + around4[i][0]) * N + (y + around4[i][1])]
                == visited[x * N + y] - 1
            ):
                x, y = x + around4[i][0], y + around4[i][1]
                if i == 0:
                    tmp = 1
                elif i == 1:
                    tmp = 0
                elif i == 2:
                    tmp = 3
                elif i == 3:
                    tmp = 2
                ans.append(tmp)
    return ans[::-1]


def get_next_TK(x, y, target):
    visited = [-1] * (N**2)
    deq = deque([(x, y)])
    visited[x * N + y] = 0
    while deq:
        x, y = deq.popleft()
        for i in UDLR[x * N + y]:
            if visited[(x + around4[i][0]) * N + (y + around4[i][1])] == -1:
                visited[(x + around4[i][0]) * N + (y + around4[i][1])] = (
                    visited[x * N + y] + 1
                )
                deq.append((x + around4[i][0], y + around4[i][1]))
            if (x + around4[i][0]) * N + (y + around4[i][1]) == target:
                # num = calender[(x + around4[i][0]) * N + (y + around4[i][1])]
                x, y = x + around4[i][0], y + around4[i][1]
                deq = []
                break
    ans = []
    flag = True
    while flag and visited[x * N + y] != 0:

        for i in UDLR[x * N + y]:
            # print(
            #     visited[(x + around4[i][0]) * N + (y + around4[i][1])],
            #     visited[x * N + y],
            # )
            if visited[(x + around4[i][0]) * N + (y + around4[i][1])] == 0:
                if i == 0:
                    tmp = 1
                elif i == 1:
                    tmp = 0
                elif i == 2:
                    tmp = 3
                elif i == 3:
                    tmp = 2
                ans.append(tmp)
                flag = False
                break
            if (
                visited[(x + around4[i][0]) * N + (y + around4[i][1])]
                == visited[x * N + y] - 1
            ):
                x, y = x + around4[i][0], y + around4[i][1]
                if i == 0:
                    tmp = 1
                elif i == 1:
                    tmp = 0
                elif i == 2:
                    tmp = 3
                elif i == 3:
                    tmp = 2
                ans.append(tmp)

    return ans[::-1]


import time


def main():
    global start
    start = time.perf_counter()
    Input()
    calc_can_visit()
    # choice_calender()
    # Start()
    solve()


if __name__ == "__main__":
    main()
