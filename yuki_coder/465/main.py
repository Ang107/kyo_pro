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
    global N, A, B, St, A_list, B_list
    St = 5 * 10**17
    N = II()
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = MII()
    A_list = A[:]
    B_list = B[:]

    A = tuple(A)
    B = tuple(B)


def solve():
    ans = beam()

    A_n, B_n = get_A_B(ans)
    tmp, _ = get_ans(A_n, B_n, ans)
    ans = [(i + 1, j + 1) for i, j in ans]
    # print(len(ans))
    for i in tmp:
        ans.append(i)

    # A_n = A_list[:]
    # B_n = B_list[:]

    # for i, j in ans:
    #     A_n[i - 1], A_n[j - 1] = (A_n[i - 1] + A_n[j - 1]) // 2, (
    #         A_n[i - 1] + A_n[j - 1]
    #     ) // 2
    #     B_n[i - 1], B_n[j - 1] = (B_n[i - 1] + B_n[j - 1]) // 2, (
    #         B_n[i - 1] + B_n[j - 1]
    #     ) // 2
    #     print(max(abs(St - A_n[0]) // 1000000, abs(St - B_n[0]) // 1000000))

    return ans


def get_A_B(ans):
    A_n = A_list[:]
    B_n = B_list[:]
    # print(ans)
    for i, j in ans:
        A_n[i], A_n[j] = A_n[i] // 2 + A_n[j] // 2, A_n[i] // 2 + A_n[j] // 2
        B_n[i], B_n[j] = B_n[i] // 2 + B_n[j] // 2, B_n[i] // 2 + B_n[j] // 2
    return A_n, B_n


def get_ans(A, B, ans_prv):
    ans_list = []
    A_n = A[:]
    B_n = B[:]
    for _ in range(50 - len(ans_prv)):
        score = max(abs(St - A_n[0]), abs(St - B_n[0]))
        tmp = score
        ans = None
        for j in range(1, 45):
            a, b = A_n[0] // 2 + A_n[j] // 2, B_n[0] // 2 + B_n[j] // 2
            if max(abs(St - a), abs(St - b)) < tmp:
                tmp = max(abs(St - a), abs(St - b))
                ans = j
        if ans:
            ans_list.append([1, ans + 1])
            A_n[0], A_n[ans] = A_n[0] // 2 + A_n[ans] // 2, A_n[0] // 2 + A_n[ans] // 2
            B_n[0], B_n[ans] = B_n[0] // 2 + B_n[ans] // 2, B_n[0] // 2 + B_n[ans] // 2
        else:
            break
    return ans_list, max(abs(St - a), abs(St - b))


def beam():
    depth = 11
    width = 3
    heap = []
    heap.append((max(abs(St - A[0]), abs(St - B[0])), []))

    heap = sorted(heap, key=lambda x: x[0])[:width]
    ans = []
    for _ in range(depth):
        new_heap = []
        while heap:
            score, ans = heap.pop()
            A_n, B_n = get_A_B(ans)
            for i in range(0, 45):
                for j in range(i + 1, 45):
                    if A_n[i] == A_n[j] and B_n[i] == B_n[j]:
                        continue
                    ans_n = ans[:]
                    ans_n.append((i, j))
                    A_nn, B_nn = A_n[:], B_n[:]
                    A_nn[i], A_nn[j] = (
                        A_nn[i] // 2 + A_nn[j] // 2,
                        A_nn[i] // 2 + A_nn[j] // 2,
                    )
                    B_nn[i], B_nn[j] = (
                        B_nn[i] // 2 + B_nn[j] // 2,
                        B_nn[i] // 2 + B_nn[j] // 2,
                    )

                    _, tmp = get_ans(A_nn, B_nn, ans_n)

                    if tmp < score:
                        new_heap.append((tmp, ans_n))
        if len(new_heap) == 0:
            break

        heap = sorted(new_heap, key=lambda x: x[0])[:width]
        # print(heap)
        _, ans = heap[0]

    return ans


# 出力
def Output(ans):
    print(len(ans))
    for i in ans:
        print(*i)


def main():
    Input()
    Output(solve())
    # Output([])


if __name__ == "__main__":
    main()
