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


# 入力
def Input():
    global N, A, B, St
    St = 5 * 10**17
    N = II()
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = MII()


def solve():
    ans = get_first_ans()
    return ans


def get_first_ans():
    ans_list = []
    for _ in range(50):
        score = abs(St - A[0]) + abs(St - B[0])
        tmp = score
        ans = None
        for j in range(1, 45):
            a, b = (A[0] + A[j]) // 2, (B[0] + B[j]) // 2
            if abs(St - a) + abs(St - b) < tmp:
                tmp = abs(St - a) + abs(St - b)
                ans = j
        if ans:
            ans_list.append([1, ans + 1])
            A[0], A[ans] = (A[0] + A[ans]) // 2, (A[0] + A[ans]) // 2
            B[0], B[ans] = (B[0] + B[ans]) // 2, (B[0] + B[ans]) // 2
        else:
            break
    return ans_list


# 出力
def Output(ans):
    print(len(ans))
    for i in ans:
        print(*i)


def main():
    Input()
    Output(solve())


if __name__ == "__main__":
    main()
