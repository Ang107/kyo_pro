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
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
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


n = II()
a = LMII()
b = LMII()
c = LMII()


l_10 = []
l_01 = []
l_11 = []
for idx, (i, j) in enumerate(zip(a, b)):

    if i == j == 1:
        l_11.append(c[idx])
        # l_01.append((c[idx], idx))
        # l_10.append((c[idx], idx))

    if i == 0 and j == 1:
        l_01.append(c[idx])
    elif i == 1 and j == 0:
        l_10.append(c[idx])
ans = 0
tmp = 0
for i, j in zip(a, c):
    tmp += i * j
sss = tmp
l_01.sort()
l_10.sort(reverse=True)
l_11.sort(reverse=True)
l_11_rev = l_11[::-1]
for i in l_10:
    tmp -= i
    ans += tmp
tttmp = tmp
ttmp = tmp
cost_10 = []
more = []
# ss = SortedMultiset([i for i, _ in l_01])
# for _, i in l_01:
#     ss.add(c[i])
for i in l_11:
    ttmp -= i
    # more.append(c[i] * (len(ss) - ss.index_right(c[i])))
    cost_10.append(ttmp)
pref_cost_10 = list(accumulate(cost_10))
for i in l_01:
    tmp += i
    ans += tmp
aans = ans
pref = 0
pref2 = 0
prefs = [0]
ll_01 = [0]
for i in l_01:
    prefs.append(prefs[-1] + i)
    ll_01.append(i)

# prev = len(ss)
# print(cost_10)
# print(ll_01)
# print(prefs)
# print(l_11)
s = tttmp
plus_cost = 0
pref_l10 = list(accumulate(l_10))
idx = 0
p = []
m = []
q = sss
for i in l_11:
    while idx < len(l_10):
        if i < l_10[idx]:
            sss -= l_10[idx]
            idx += 1
        else:
            break
    sss -= i
    p.append(sss)
    m.append(i * (len(l_10) - idx))
pref = 0
pref2 = 0
# sss = list(ss)
sss = sorted(l_01)
for idx, i in enumerate(l_11):
    # 1->0のコスト
    # plus_cost += cost_10[idx]
    plus_cost += p[idx]
    pref += i
    s -= i
    pref2 += m[idx]
    minus_cost = pref * len(l_01) + pref2
    r = bisect_right(sss, i)
    plus_cost += i * (len(sss) - r)
    plus_cost += s + prefs[r] + i
    # print(minus_cost, plus_cost)
    aans = min(aans, ans + plus_cost - minus_cost)


print(aans)
