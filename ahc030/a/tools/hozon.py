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


def FirstInput():
    global N, M, E, D, sum_D, wariai, D_size
    N, M, E = input().split()
    N, M = int(N), int(M)
    E = float(E)
    D = []
    D_size = []
    sum_D = 0
    for i in range(M):
        tmp = LMII()
        sum_D += tmp[0]
        zahyou = []
        for i in range(2, len(tmp), 2):
            zahyou.append((tmp[i - 1], tmp[i]))
        D.append(zahyou)

    # D.sort(key=lambda x: len(x), reverse=True)

    for d in D:
        x, y = 0, 0
        for i, j in d:
            x = max(x, i)
            y = max(y, j)
        D_size.append((x, y))

    wariai = sum_D / N**2


def Output_Input(l: list):
    tmp = []
    for i, j in l:
        tmp.append(i)
        tmp.append(j)
    print("q", len(l), *tmp, flush=True)
    n = II()
    return n


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def Exit():
    ans = []
    for i in range(N):
        for j in range(N):
            if B[i][j] >= 1:
                ans.append((i, j))
    print("#", Last_Output(ans))
    exit()


# 答えの出力
def Last_Output(l):
    tmp = []
    for i, j in l:
        tmp.append(i)
        tmp.append(j)
    print("a", len(l), *tmp, flush=True)
    n = II()
    if n == 0:
        return False
    else:
        return True


def get_Weight():
    global Weight, Bunkatu, Idx
    num = N / 3
    Idx = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    Bunkatu = [[[] for i in range(3)] for j in range(3)]
    for i in range(N):
        for j in range(N):
            x = int(i // num)
            y = int(j // num)
            Bunkatu[x][y].append((i, j))
    Weight = [0] * 9
    for i in range(3):
        for j in range(3):
            Weight[i * 3 + j] = Output_Input(Bunkatu[i][j])

    avg = sum(Weight) / 9
    Weight = [i**1.5 + avg // 2 for i in Weight]

    print("#", Weight)


def solve():
    global B, possib_xy
    B = [[-100] * N for _ in range(N)]
    possib_xy = set()

    for i in range(N):
        for j in range(N):
            possib_xy.add((i, j))
    plus = []
    next = []
    Tarn = 2
    visited = 0
    while True:
        for i in B:
            print("#", *i)
        print("# next", len(next))
        if visited == N**2 or (Tarn != 2 and len(next) == 0):
            Exit()
        # クエリを送信、Bの更新
        if Tarn <= 50:
            num = 2
        elif Tarn <= 100:
            num = 3
        elif Tarn <= 150:
            num = 5
        elif Tarn < 200:
            num = 10
        else:
            num = 15

        for i in range(num):
            while True:
                tmp = random.choice(range(int(Tarn**1.25)))
                if tmp < 7:
                    # p, q = random.choices(Idx, weights=Weight)[0]
                    # x, y = random.choice(Bunkatu[p][q])

                    x, y = random.choice(range(N)), random.choice(range(N))
                    # print(f"#c {x} {y} blue")
                else:
                    if next:
                        x, y = next.pop()
                    else:
                        break
                    # print(f"#c {x} {y} green")

                if B[x][y] == -100:
                    possib_xy.discard((x, y))
                    Tarn += 1
                    visited += 1
                    B[x][y] = Output_Input([(x, y)])
                    for j in range(B[x][y]):
                        plus.append((x, y))

                    break

        # 答えの候補の取得
        ans_list, next = calc_next_and_ans()
        print("# ans", len(ans_list), len(next))

        # 絞り込めたなら
        if 1 <= len(ans_list) <= 10:
            for i in ans_list:
                tmp = set()
                for idx, j in enumerate(D):
                    sx, sy = i[idx]
                    for x, y in j:
                        tmp.add((x + sx, y + sy))
                Tarn += 1
                if Last_Output(tmp):
                    exit()
        # # 絞り込めなかった場合
        # else:
        #     # 次に送るクエリの候補を計算
        #     if ans_list:
        #         next = calc_next_from_ans(ans_list)
        #     else:
        #         next = calc_next_and_ans()


def calc_next_from_ans(ans_list):
    next = [[0] * N for _ in range(N)]
    for ans in ans_list:
        for idx, (x, y) in enumerate(ans):
            for i, j in D[idx]:
                next[x + i][y + j] += 1
    tmp = []
    for i in range(N):
        for j in range(N):
            if next[i][j] and B[i][j] == -100:
                tmp.append((next[i][j], i, j))

    tmp.sort(key=lambda x: abs(x[0] - len(ans_list) / 2), reverse=True)
    # print("# next_full_from_ans", tmp)

    return [(j, k) for i, j, k in tmp]


# 送るクエリ計算
# def calc_next():
#     # Dをグループに分けて、各グループで計算する

#     next = [[0] * N for _ in range(N)]
#     for idx, d in enumerate(D):
#         for i in range(N - D_size[idx][0]):
#             for j in range(N - D_size[idx][1]):
#                 tmp = []
#                 flag = 0
#                 for x, y in d:
#                     if i + x in range(N) and j + y in range(N):
#                         if B[i + x][j + y] == -100:
#                             tmp.append((i + x, j + y))
#                         elif B[i + x][j + y] >= 1:
#                             flag += 1
#                         else:
#                             flag = -1
#                             break
#                     else:
#                         flag = -1
#                         break
#                 # print("#", flag, i, j)
#                 if flag >= 0:
#                     for p, q in tmp:
#                         next[p][q] += 1
#     tmp = []
#     for i in next:
#         print("#", *i)
#     for i in range(N):
#         for j in range(N):
#             if next[i][j]:
#                 tmp.append((next[i][j], i, j))
#             elif next[i][j] == 0 and B[i][j] == -100:
#                 possib_xy.discard((i, j))
#                 B[i][j] = 0

#     tmp.sort(key=lambda x: x[0])

#     # 石油が存在する可能性が高い地点を優先して選択(?)
#     # もっと優先して送るべきクエリを選択するアルゴリズムがあるかも
#     if len(tmp) > 50:
#         tmp = tmp[int(len(tmp) * 0.7) :]
#     random.shuffle(tmp)
#     # print("# next_full", tmp)
#     return [(j, k) for i, j, k in tmp]


def calc_next_and_ans():
    ans_2 = []
    ans_list = []
    for i in range(0, M, 2):
        l, r = i, i + 1
        if r < M:
            ans_2.append(get_Ans_part(B, l, r))
        else:
            ans_2.append(get_Ans_part(B, l, l))

    for i in ans_2:
        print("#", len(i), i[:10])
    tmp = 1

    ans_list = get_Ans_part(B, 0, M - 1)

    next = [[0] * N for _ in range(N)]
    for i, j in enumerate(ans_2):
        for k in j:
            for l in range(len(k)):
                p, q = k[l]
                for x, y in D[i * 2 + l]:
                    next[p + x][q + y] += 1
    tmp = []
    # for i in next:
    #     print("#", *i)
    for i in range(N):
        for j in range(N):
            if next[i][j]:
                tmp.append((next[i][j], i, j))
            elif next[i][j] == 0 and B[i][j] == -100:
                print(f"#c {i} {j} red")
                possib_xy.discard((i, j))
                B[i][j] = 0

        tmp.sort(key=lambda x: x[0])

        # 石油が存在する可能性が高い地点を優先して選択(?)
        # もっと優先して送るべきクエリを選択するアルゴリズムがあるかも
        if len(tmp) > 50:
            tmp = tmp[int(len(tmp) * 0.7) :]
        random.shuffle(tmp)
        # print("# next_full", tmp)

    return ans_list, [(j, k) for i, j, k in tmp]


# 答えの案の出力
# 候補数が多すぎる場合打ち切っているが、上手いこと計算すれば、打ち切らずに済場合がある？


def get_Ans_part(B, l, r):
    deq = deque()
    B_n = [k[:] for k in B]
    deq.append((l, B_n, []))
    ans = []
    while deq:
        idx, B, prv = deq.popleft()
        shape = D[idx]
        for i in range(N - D_size[idx][0]):
            for j in range(N - D_size[idx][1]):
                flag = True
                for x, y in shape:
                    if (
                        i + x in range(N)
                        and j + y in range(N)
                        and (B[i + x][j + y] <= -100 or B[i + x][j + y] >= 1)
                    ):
                        pass
                    else:
                        flag = False
                        break

                if flag:
                    prv_n = prv[:]
                    prv_n.append((i, j))
                    B_n = [k[:] for k in B]
                    if idx == r:
                        for x, y in shape:
                            B_n[i + x][j + y] -= 1
                        if max([max(k) for k in B_n]) <= M - idx - 1 + M - (r - l) - 1:
                            ans.append(prv_n)
                    else:
                        for x, y in shape:
                            B_n[i + x][j + y] -= 1
                        if max([max(k) for k in B_n]) <= M - idx - 1 + M - (r - l) - 1:
                            deq.append((idx + 1, B_n, prv_n))
                        if len(deq) >= 1000:
                            return []
    return ans


import random


def main():
    FirstInput()
    # get_Weight()
    solve()


if __name__ == "__main__":
    main()
