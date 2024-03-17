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
    A = []
    ans = 0
    for i in range(1, 20, 2):
        A.append((n[i - 1], n[i]))
    visited = set(A)

    for i in list(permutations(range(10))):
        # i = (0, 5, 6, 7, 1, 2, 8, 9, 4, 3)
        # if i == (0, 5, 6, 7, 1, 2, 8, 9, 4, 3):
        #     print("ac")
        # exit()

        if i[0] != 0:
            continue
        visited_n = visited.copy()
        dis_sum = 0
        big_flag = False
        for j in range(1, 10):
            (x1, y1), (x2, y2) = A[i[j]], A[i[j - 1]]
            dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            if dis == int(dis):
                x_dis = abs(x1 - x2)
                y_dis = abs(y1 - y2)
                gcd = math.gcd(x_dis, y_dis)
                x_dis /= gcd
                y_dis /= gcd
                flag = True
                if x1 > x2:
                    x_dis *= -1
                if y1 > y2:
                    y_dis *= -1
                # print(x1, y1, x2, y2, x_dis, y_dis)

                while True:
                    x1 += x_dis
                    y1 += y_dis
                    if x1 == x2 and y1 == y2:
                        break
                    if (x1, y1) in visited:
                        flag = False
                        break
                    visited_n.add((x1, y1))
                if flag:
                    # print(dis_sum)
                    dis_sum += dis
                    # print(j)
                    if j == 9:
                        big_flag = True
                else:
                    break
            else:
                break
        if big_flag:
            # print([alph_s[j] for j in i])
            ans = max(ans, dis_sum)

    return int(ans)


if __name__ == "__main__":
    # 入力をここに追加
    Input = [
        [4, 3, 0, 6, 8, 6, 1, 5, 0, 0, 4, 1, 8, 0, 8, 2, 5, 2, 5, 6],
        [0, 0, 30, 0, 60, 0, 90, 0, 96, 0, 0, 40, 30, 40, 60, 40, 90, 40, 96, 40],
        [100, 20, 65, 18, 1, 0, 86, 90, 0, 90, 92, 60, 86, 23, 80, 51, 50, 100, 2, 10],
    ]

    Output = []
    for i in Input:
        Output.append(main(i))
        # print(main(i))
    print(f"{Output[0]},{Output[1]},{Output[2]}")
