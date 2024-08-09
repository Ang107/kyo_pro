import sys
from collections import deque, defaultdict
from itertools import (
    accumulate,  # 累積和
    product,  # bit全探索 product(range(2),repeat=n)
    permutations,  # permutations : 順列全探索
    combinations,  # 組み合わせ（重複無し）
    combinations_with_replacement,  # 組み合わせ（重複可）
)
import math
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
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

T = II()
ans = []

b = []
f = []
for i, j in enumerate(alph_s, start=1):
    cnt = 0
    for k in range(1, i + 1):
        if i % k == 0:
            cnt += 1
    if cnt <= 2:
        b.append(j)
    else:
        f.append(j)

# print(b)
# print(f)


def solve(s):
    back = "kcab"
    front = "front"
    b_list = []
    f_list = []
    rslt = 0
    for i in s:
        if i in back:
            b_list.append(i)
        elif i in front:
            f_list.append(i)
        else:
            rslt += 1
    b_list = b_list[::-1]
    cnt = defaultdict(int)
    for i in b_list:
        if i == "k":
            cnt[i] += 1
        elif i == "c":
            cnt[i] = min(cnt[i] + 1, cnt["k"])
        elif i == "a":
            cnt[i] = min(cnt[i] + 1, cnt["c"])
        elif i == "b":
            cnt[i] = min(cnt[i] + 1, cnt["a"])

    tmp = len(b_list)
    b_del_cnt = cnt["b"]
    tmp -= 3 * b_del_cnt
    if b_del_cnt > 0 and (cnt["a"] - cnt["b"]) > 0:
        tmp -= max(0, 3 * (cnt["a"] - cnt["b"]))

    if b_del_cnt and (cnt["c"] - cnt["a"]) > 0:
        mn = max(0, min((b_del_cnt - 2) + 1, (cnt["c"] - cnt["a"])))
        tmp -= 3 * mn
        b_del_cnt -= mn

    if b_del_cnt and (cnt["k"] - cnt["c"]) > 0:
        mn = max(0, min((b_del_cnt - 3) // 2 + 1, (cnt["k"] - cnt["c"])))
        tmp -= 3 * mn
        b_del_cnt -= mn * 2

    mn = max(0, (b_del_cnt - 4) // 3 + 1)
    tmp -= 3 * mn
    # print(tmp)
    rslt += tmp

    cnt = defaultdict(int)
    for i in f_list:
        if i == "f":
            cnt[i] += 1
        elif i == "r":
            cnt[i] = min(cnt[i] + 1, cnt["f"])
        elif i == "o":
            cnt[i] = min(cnt[i] + 1, cnt["r"])
        elif i == "n":
            cnt[i] = min(cnt[i] + 1, cnt["o"])
        elif i == "t":
            cnt[i] = min(cnt[i] + 1, cnt["n"])

    tmp = len(f_list)
    f_del_cnt = cnt["t"]
    tmp -= 4 * f_del_cnt
    if f_del_cnt > 0 and (cnt["n"] - cnt["t"]) > 0:
        tmp -= max(0, 4 * (cnt["n"] - cnt["t"]))

    if f_del_cnt and (cnt["o"] - cnt["n"]) > 0:
        mn = max(0, min((f_del_cnt - 2) + 1, (cnt["o"] - cnt["n"])))
        tmp -= 4 * mn
        f_del_cnt -= mn

    if f_del_cnt and (cnt["r"] - cnt["o"]) > 0:
        mn = max(0, min((f_del_cnt - 3) // 2 + 1, (cnt["r"] - cnt["o"])))
        tmp -= 4 * mn
        f_del_cnt -= mn * 2

    if f_del_cnt and (cnt["f"] - cnt["r"]) > 0:
        mn = max(0, min((f_del_cnt - 4) // 3 + 1, (cnt["f"] - cnt["r"])))
        tmp -= 4 * mn
        f_del_cnt -= mn * 3

    mn = max(0, (f_del_cnt - 5) // 4 + 1)
    tmp -= 4 * mn

    rslt += tmp
    # print(tmp)
    return rslt


def native(s):
    other = []
    b_list = []
    f_list = []
    back = "kcab"
    front = "front"
    for i in s:
        if i in back:
            b_list.append(i)
        elif i in front:
            f_list.append(i)
        else:
            other.append(i)
    rslt = len(other)
    free_cnt = 0
    b_list = b_list[::-1]

    def get_del_list(s, t):
        del_list = []
        idx = 0
        for i, j in enumerate(s):
            if j == t[idx]:
                idx += 1
                del_list.append(i)
                if idx == len(t):
                    break
        return del_list

    while True:
        del_list = get_del_list(b_list, back)
        if len(del_list) < 4:
            break
        nb = []
        for i in range(len(b_list)):
            if i not in del_list:
                nb.append(b_list[i])
        b_list = nb
        free_cnt += 1
    while True:
        del_list = get_del_list(b_list, back)
        if len(del_list) == 4:
            nb = []
            for i in range(len(b_list)):
                if i not in del_list:
                    nb.append(b_list[i])
            b_list = nb
            free_cnt += 1
        elif len(del_list) == 3:
            if free_cnt >= 1:
                b_list.append("b")
                free_cnt -= 1
            else:
                break

        elif len(del_list) == 2:
            if free_cnt >= 2:
                b_list.append("a")
                b_list.append("b")
                free_cnt -= 2
            else:
                break

        elif len(del_list) == 1:
            if free_cnt >= 3:
                b_list.append("c")
                b_list.append("a")
                b_list.append("b")
                free_cnt -= 3
            else:
                break

        elif len(del_list) == 0:
            if free_cnt >= 4:
                b_list.append("k")
                b_list.append("c")
                b_list.append("a")
                b_list.append("b")
                free_cnt -= 4
            else:
                break
    rslt += len(b_list) + free_cnt

    free_cnt = 0
    while True:
        del_list = get_del_list(f_list, front)
        if len(del_list) < 5:
            break
        nf = []
        for i in range(len(f_list)):
            if i not in del_list:
                nf.append(f_list[i])
        f_list = nf
        free_cnt += 1
    while True:
        del_list = get_del_list(f_list, front)

        if len(del_list) == 5:
            nf = []
            for i in range(len(f_list)):
                if i not in del_list:
                    nf.append(f_list[i])
            f_list = nf
            free_cnt += 1
        elif len(del_list) == 4:
            if free_cnt >= 1:
                f_list.append("t")
                free_cnt -= 1
            else:
                break

        elif len(del_list) == 3:
            if free_cnt >= 2:
                f_list.append("n")
                f_list.append("t")
                free_cnt -= 2
            else:
                break

        elif len(del_list) == 2:
            if free_cnt >= 3:
                f_list.append("o")
                f_list.append("n")
                f_list.append("t")
                free_cnt -= 3
            else:
                break

        elif len(del_list) == 1:
            if free_cnt >= 4:
                f_list.append("r")
                f_list.append("o")
                f_list.append("n")
                f_list.append("t")
                free_cnt -= 4
            else:
                break

        elif len(del_list) == 0:
            if free_cnt >= 5:
                f_list.append("f")
                f_list.append("r")
                f_list.append("o")
                f_list.append("n")
                f_list.append("t")
                free_cnt -= 5
            else:
                break
    rslt += len(f_list) + free_cnt
    return rslt


for i in range(T):
    if 1:
        n = II()
        s = input()
        ans.append(solve(s))
    else:
        import random

        s = [random.choice("backfront") for _ in range(50)]
        r1, r2 = solve(s), native(s)
        print(r1, r2)
        if r1 != r2:
            print(s)
            exit()


for i in ans:
    print(i)
