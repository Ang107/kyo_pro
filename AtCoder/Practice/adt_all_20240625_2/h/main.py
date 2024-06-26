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
import inspect


# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
def deb(*vars):
    try:
        frame = inspect.currentframe().f_back
        names = {id(value): name for name, value in frame.f_locals.items()}
        for var in vars:
            var_id = id(var)
            var_name = names.get(var_id, "<unknown>")
            sys.stderr.write(f"{var_name}: {var}\n")
    except Exception as e:
        sys.stderr.write(f"Error in deb function: {e}\n")


sys.setrecursionlimit(10**7)
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

n, d = MII()
w = LMII()
ans = inf

sum_w = sum(w)


def get_b(z):
    tmp = [sum(i) for i in z]
    avr = sum(tmp) / d
    rslt = 0
    for i in tmp:
        rslt += (i - avr) ** 2
    rslt /= d
    return rslt


def split_into_groups_with_empty_no_order(n, m):
    def helper(indices):
        groups = [[] for _ in range(m)]
        for i, group_index in enumerate(indices):
            groups[group_index].append(i)
        return groups

    results = []
    for indices in combinations_with_replacement(range(m), n):
        results.append(helper(indices))

    # 重複を排除して結果を返す
    unique_results = []
    seen = set()
    for result in results:
        sorted_result = tuple(sorted(map(tuple, result)))
        if sorted_result not in seen:
            seen.add(sorted_result)
            unique_results.append(result)

    return unique_results


c = split_into_groups_with_empty_no_order(n, d)
print(len(c))
pritn(c)
for i in c:
    # print(i)
    tmp = [[] for _ in range(d)]
    for j in range(d):
        for k in i[j]:
            tmp[j].append(w[k])
    # print(i)
    print(tmp)
    ans = min(ans, get_b(tmp))
print(ans)
