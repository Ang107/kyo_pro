from sys import stdin, setrecursionlimit
from itertools import accumulate
from bisect import bisect_left, bisect_right


DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


n, m, k = MII()
a = LMII()
sa = sorted(a)
pa = [0] + list(accumulate(sa))
sum_a = sum(a)
ans = [-2] * n
for i in range(n):

    def isOK(mid):
        # 票数が a[i] + mid を元々超えている人の人数
        p = n - bisect_right(sa, a[i] + mid)
        # 票数が a[i] + mid 以下の人数
        le = n - p

        def isOK2(mid2):
            # 含まれる
            assert le - mid2 - 1 >= 0
            if sa[le - mid2 - 1] < a[i]:
                return (
                    mid2 * (a[i] + mid + 1) - (pa[le] - pa[le - mid2 - 1] - a[i])
                    <= k - sum_a - mid
                )
            # 含まれない
            else:
                return (
                    mid2 * (a[i] + mid + 1) - (pa[le] - pa[le - mid2])
                    <= k - sum_a - mid
                )

        def meguru2(ng, ok):
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if isOK2(mid):
                    ok = mid
                else:
                    ng = mid
            return ok

        # 自由な票が、k - sum_a - mid のとき、票数が a[i] + mid より大きい人の人数の最大値
        p += meguru2(le, 0)
        return p < m

    def meguru(ng, ok):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if isOK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    res = meguru(-1, k - sum_a + 1)
    if res > k - sum_a:
        res = -1
    ans[i] = res
pritn(*ans)
