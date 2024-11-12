from sys import stdin, setrecursionlimit
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
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


def solve(n, m, x, a):
    if sum(a) != n:
        return -1
        exit()
    x = [i - 1 for i in x]

    xa = [[i, j - 1] for i, j in zip(x, a)] + [[n, 0]]
    xa.sort()
    # print(xa)
    if xa[0][0] > 0:
        return -1
    ans = 0
    st = deque()
    for i in range(m):
        st.append(xa[i])
        l = xa[i + 1][0] - xa[i][0] - 1
        # print(l)
        now = xa[i][0] + 1
        while st and l > 0:
            tmp = st[0]
            num = min(tmp[1], l)
            ans += (now - tmp[0] + now - tmp[0] + num - 1) * num // 2
            st[0][1] -= num
            l -= num
            now += num
            if st[0][1] == 0:
                st.popleft()
            # print(st)
            # print("ans", ans)
        if l > 0:
            return -1
            exit()
    return ans


def native(n, m, x, a):
    x = [i - 1 for i in x]
    tmp = [0] * n
    for i, j in zip(x, a):
        tmp[i] = j
    if sum(tmp) != n:
        return -1
        exit()
    deq = deque()
    ans = 0
    for i in range(n):
        if tmp[i] > 1:
            for _ in range(tmp[i] - 1):
                deq.append(i)
        elif tmp[i] == 1:
            pass
        else:
            if not deq:
                return -1
                exit()
            ans += i - deq.popleft()
    return ans


if 1:
    n, m = MII()
    x = LMII()
    a = LMII()
    print(solve(n, m, x, a))
else:
    import random

    while 1:
        n = random.randrange(5, 20)
        a = []
        tmp = n
        while tmp > 0:
            a.append(random.randrange(1, tmp + 1))
            tmp -= a[-1]
        x = list(range(1, n + 1))
        random.shuffle(x)
        x = x[: len(a)]

        m = len(a)
        r1 = native(n, m, x, a)
        r2 = solve(n, m, x, a)
        if r1 != r2:
            print(n, m, x, a)
            print(r1, r2)
            exit()
