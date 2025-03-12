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
    b = [[] for _ in range(5)]
    pos = [-1] * 51
    for i in range(5):
        for j in range(5):
            pos[a[i * 5 + j]] = (i, j)
            b[i].append(a[i * 5 + j])
    # print(b)
    a = a[25:]
    # print(a)

    free = [0] * 50
    ss = []
    cnt = 0
    s = [[-1] * 5 for _ in range(5)]
    # print(pos)
    for index, i in enumerate(a):
        if pos[i] == -1:
            cnt += 1
            if cnt % 3 == 0:
                free[index] = 1
                cnt = 0
        else:
            p, q = pos[i]
            if s[p][q] != -1:
                cnt += 1
                if cnt % 3 == 0:
                    free[index] = 1
                    cnt = 0

            else:
                # print(index)
                s[p][q] = 1
                cnt = 0
        ss.append([j[:] for j in s])
    # for i in ss:
    #     print(i)
    # print(free)
    ans = 0
    for i in range(5):
        cnt = 0
        for j in range(50):
            cnt += free[j]
            # print(j, cnt, len([ss[j][i][k] for k in range(5) if ss[j][i][k] == 1]))
            if cnt + len([ss[j][i][k] for k in range(5) if ss[j][i][k] == 1]) == 5:
                tmp = 0

                for p in range(5):
                    for q in range(5):
                        if p != i and ss[j][p][q] == -1:
                            tmp += b[p][q]
                ans = max(ans, tmp)
                break
    for i in range(5):
        cnt = 0
        for j in range(50):
            cnt += free[j]
            if cnt + len([ss[j][k][i] for k in range(5) if ss[j][k][i] == 1]) == 5:
                tmp = 0
                for p in range(5):
                    for q in range(5):
                        if q != i and ss[j][p][q] == -1:
                            tmp += b[p][q]
                ans = max(ans, tmp)
                break

    cnt = 0
    for j in range(50):
        cnt += free[j]
        if cnt + len([ss[j][k][k] for k in range(5) if ss[j][k][k] == 1]) == 5:
            tmp = 0
            for p in range(5):
                for q in range(5):
                    if p != q and ss[j][p][q] == -1:
                        tmp += b[p][q]
            ans = max(ans, tmp)
            break

    cnt = 0
    for j in range(50):
        cnt += free[j]
        if cnt + len([ss[j][k][4 - k] for k in range(5) if ss[j][k][4 - k] == 1]) == 5:
            tmp = 0

            for p in range(5):
                for q in range(5):
                    if p + q != 4 and ss[j][p][q] == -1:
                        tmp += b[p][q]
            ans = max(ans, tmp)
            break
    return ans


if __name__ == "__main__":
    # 入力をここに追加
    Input = [
        [
            43,
            18,
            35,
            34,
            46,
            15,
            8,
            49,
            29,
            19,
            44,
            37,
            7,
            30,
            14,
            13,
            11,
            39,
            27,
            6,
            23,
            36,
            22,
            21,
            50,
            4,
            2,
            27,
            26,
            33,
            10,
            18,
            28,
            42,
            14,
            41,
            17,
            49,
            21,
            23,
            48,
            32,
            35,
            3,
            20,
            12,
            9,
            43,
            8,
            50,
            22,
            40,
            31,
            7,
            1,
            45,
            47,
            44,
            5,
            39,
            37,
            38,
            36,
            29,
            15,
            46,
            24,
            30,
            16,
            11,
            25,
            6,
            34,
            19,
            13,
        ],
        [
            8,
            43,
            9,
            29,
            6,
            13,
            47,
            5,
            40,
            27,
            48,
            50,
            10,
            11,
            35,
            44,
            1,
            12,
            3,
            16,
            42,
            33,
            21,
            24,
            2,
            49,
            43,
            27,
            31,
            5,
            20,
            28,
            19,
            32,
            4,
            15,
            48,
            1,
            7,
            29,
            22,
            14,
            10,
            13,
            25,
            35,
            3,
            21,
            12,
            2,
            36,
            40,
            39,
            46,
            44,
            18,
            9,
            8,
            23,
            30,
            16,
            34,
            26,
            45,
            37,
            41,
            17,
            50,
            6,
            38,
            24,
            42,
            11,
            33,
            47,
        ],
        [
            39,
            38,
            36,
            24,
            1,
            32,
            45,
            47,
            50,
            48,
            40,
            31,
            30,
            34,
            49,
            41,
            33,
            42,
            25,
            44,
            29,
            28,
            37,
            46,
            43,
            15,
            20,
            41,
            27,
            23,
            1,
            11,
            2,
            10,
            9,
            22,
            31,
            4,
            7,
            16,
            3,
            26,
            5,
            8,
            6,
            47,
            17,
            12,
            43,
            18,
            13,
            46,
            19,
            14,
            33,
            35,
            38,
            28,
            37,
            24,
            42,
            34,
            32,
            36,
            29,
            49,
            21,
            30,
            50,
            25,
            44,
            39,
            48,
            45,
            40,
        ],
    ]

    Output = []
    for i in Input:
        Output.append(main(i))
    print(f"{Output[0]},{Output[1]},{Output[2]}")
