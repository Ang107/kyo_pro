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

DEBUG = True
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

import typing


def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


def _bsf(n: int) -> int:
    x = 0
    while n % 2 == 0:
        x += 1
        n //= 2

    return x


class LazySegTree:
    def __init__(
        self,
        op: typing.Callable[[typing.Any, typing.Any], typing.Any],
        e: typing.Any,
        mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
        composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
        id_: typing.Any,
        v: typing.Union[int, typing.List[typing.Any]],
    ) -> None:
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self._e
        smr = self._e
        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def apply(
        self,
        left: int,
        right: typing.Optional[int] = None,
        f: typing.Optional[typing.Any] = None,
    ) -> None:
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, g: typing.Any) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id


# 区間加算・区間最大値取得^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
op = lambda a, b: max((min(a), min(a)), (min(b), min(b)))
e = (-float("inf"), -float("inf"))
mapping = lambda f, x: (f[0] + x[0], f[1] + x[1])
composition = lambda f, g: (f[0] + g[0], f[1] + g[1])
id_ = (0, 0)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ans = 0


def solve(n, q, s, qs):
    global ans
    pref_1 = [0]
    pref_2 = [0]
    for i in s:
        if i == "1":
            pref_1.append(pref_1[-1] + 1)
        else:
            pref_1.append(pref_1[-1])
    for i in s[::-1]:
        if i == "2":
            pref_2.append(pref_2[-1] + 1)
        else:
            pref_2.append(pref_2[-1])
    pref_1.append(pref_1[-1])
    pref_2.append(pref_2[-1])
    pref_2 = pref_2[::-1]
    deb(pref_1)
    deb(pref_2)
    tmp = []
    indexs = []
    for i in range(n):
        if s[i] == "/":
            indexs.append(i)
            tmp.append((pref_1[i], pref_2[i + 2]))
    deb(tmp)
    # seg = LazySegTree(op, e, mapping, composition, id_, lst)
    ans_l = []

    # for i in range(len(tmp)):
    #     for j in range(i, len(tmp)):
    #         print(i, j, seg.prod(i, j + 1))
    # for i in range(len(tmp)):
    #     for j in range(i, len(tmp)):
    #         print(i, j, seg.prod(i, j + 1))

    for l, r in qs:
        l -= 1
        r -= 1
        ll = bisect_left(indexs, l)
        rr = bisect_right(indexs, r)
        # print(ll, rr)
        minus_l = pref_1[l]
        minus_r = pref_2[r + 2]
        ans = 0

        # print(minus_l, minus_r)
        def isOK(mid):
            global ans
            ans = max(ans, min(tmp[mid][0] - minus_l, tmp[mid][1] - minus_r) * 2 + 1)
            if tmp[mid][0] - minus_l < tmp[mid][1] - minus_r:
                return False
            else:
                return True
            pass

        def meguru(ng, ok):
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if isOK(mid):
                    ok = mid
                else:
                    ng = mid
            return ok

        if ll < rr:
            i = meguru(ll - 1, rr - 1)
            ans = max(ans, min(tmp[i][0] - minus_l, tmp[i][1] - minus_r) * 2 + 1)
        ans_l.append(ans)

    return ans_l


def native(n, q, s, qs):
    ans_l = []
    for l, r in qs:
        l -= 1
        r -= 1
        ans = 0
        for i in range(l, r + 1):
            if s[i] == "/":
                cnt = min(s[l:i].count("1"), s[i : r + 1].count("2")) * 2 + 1
                ans = max(ans, cnt)
        ans_l.append(ans)
    return ans_l


if 1:
    n, q = MII()
    s = input()
    qs = [LMII() for _ in range(q)]
    for i in solve(n, q, s, qs):
        print(i)
else:
    import random

    while 1:
        n = random.randrange(5, 20)
        q = n * (n + 1) // 2
        s = "".join([random.choice("12/") for _ in range(n)])
        qs = []
        for i in range(n):
            for j in range(i, n):
                qs.append((i + 1, j + 1))
        if solve(n, q, s, qs) != native(n, q, s, qs):
            print(n, q)
            print(s)
            res1 = solve(n, q, s, qs)
            res2 = native(n, q, s, qs)
            for i in range(n * (n + 1) // 2):
                if res1[i] != res2[i]:
                    print(qs[i], res1[i], res2[i])
            exit()
