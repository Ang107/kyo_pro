import sys
from bisect import bisect_left, bisect_right

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


n, m = MII()

a = LMII()
b = LMII()
c = LMII()
ans = 0
# 作れるやつの中でコスパが最も良いものを選びたい。

ab = [(i, j, i - j) for i, j in zip(a, b)]

ab.sort(key=lambda x: x[0])
ab_new = []
tmp = inf
for i, j, k in ab:
    if tmp > k:
        tmp = k
        ab_new.append((i, j, k))

ab = ab_new

score = [(i[2], idx) for idx, i in enumerate(ab)]
a = [i[0] for i in ab]
min_ = []

for i in score:
    if not min_:
        min_.append(i)
    else:
        min_.append(min(min_[-1], i))

for i in c:
    amari = i
    while amari > 0:
        idx = bisect_right(a, amari)
        if idx == 0:
            break
        rslt = min_[idx - 1]
        tmp = (amari - a[rslt[1]]) // rslt[0] + 1
        ans += tmp * 2
        amari -= tmp * rslt[0]

print(ans)
