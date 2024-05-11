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


n, m = MII()
deq_list = []
for _ in range(m):
    k = II()
    a = LMII()
    deq_list.append(deque(a))
s_ball = set()
s_ball_to_idx = {}
can_use = []
for idx, i in enumerate(deq_list):
    can_use.append((idx, i.popleft()))

while can_use:
    idx, v = can_use.pop()
    if v in s_ball:
        s_ball.discard(v)
        idx_ = s_ball_to_idx[v]
        if deq_list[idx_]:
            can_use.append((idx_, deq_list[idx_].popleft()))
        if deq_list[idx]:
            can_use.append((idx, deq_list[idx].popleft()))
    else:
        s_ball.add(v)
        s_ball_to_idx[v] = idx


if all(len(i) == 0 for i in deq_list):
    PY()
else:
    PN()


# s_ball = set()
# ball_idx = {}
# s_idx = set()

# for i in range(m):
#     idx = i
#     while True:
#         print(idx)
#         print(deq_list)
#         print(s_ball)
#         b = deq_list[idx].popleft()
#         if b in s_ball:
#             s_ball.discard(b)
#             s_idx.discard(ball_idx[b])
#             if deq_list[ball_idx[b]]:
#                 idx = ball_idx[b]
#                 continue
#             else:
#                 break
#         else:
#             s_ball.add(b)
#             s_idx.add(idx)
#             ball_idx[b] = idx
#             break

# if all([len(i) == 0 for i in deq_list]):
#     PY()
# else:
#     PN()
