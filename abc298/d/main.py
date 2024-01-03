
import fileinput
import sys
from collections import deque, defaultdict
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
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
# sys.set_int_max_str_digits(0)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()
mod = 998244353


def Pr(x): return print(x)
def PY(): return print("Yes")
def PN(): return print("No")
def I(): return input()
def II(): return int(input())


def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))


def is_not_Index_Er(x, y, h, w): return 0 <= x < h and 0 <= y < w  # 範囲外参照


Q = int(input())
q = [input().split() for _ in range(Q)]
# print(q)
MOD = mod
num = 1
keta = 1
ans_list = []
temp = 1
ruizyou_10 = []
# for i in range(10**5):
#     ruizyou_10.append(temp)
#     temp = temp * 10
deq = deque([1])
for i in q:
    # print(deq)
    if i[0] == "1":
        num = (num*10 + int(i[1])) % mod
        deq.append(int(i[1]))

    elif i[0] == "2":
        num = num - pow(10, (len(deq)-1), mod) * deq[0]
        deq.popleft()
    elif i[0] == "3":
        print(num % mod)
    # print(num)
    # deq = deque(list(str(ans)))
    # print(deq)
    # print(ans)

# for i in ans_list:
#     print(i)

# temp = 1

# for i in q:
#     if i[0] == 1:
#         temp = (temp * 10 + i[1])
#     elif i[0] == 2:
#         keta = len(str(temp)) - 1
#         temp = temp % 10**keta
#     elif i[0] == 3:
#         print(temp % mod)
