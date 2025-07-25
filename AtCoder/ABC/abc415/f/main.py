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

    def __str__(self) -> str:
        return f"LazySegTree: {[self.get(i) for i in range(self._n)]}"

    def __iter__(self) -> typing.Iterator[typing.Any]:
        return iter(self.get(i) for i in range(self._n))

    def __setitem__(self, p: int, x: typing.Any) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def __getitem__(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

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


n, q = MII()
s = input()


# 区間更新・区間最大値取得^^^^^^^^^^^^^^^^^^^^^^^^^
INF = 1 << 63
ID = (INF, -1, -1)


def op(x, y):
    if x[0] < y[0]:
        return y
    else:
        return x


e = (-INF, -1, -1)
mapping = lambda f, x: x if f == ID else f
composition = lambda f, g: g if f == ID else f
id_ = ID
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
v = []
a = [[s[0], 1]]
for i in s[1:]:
    if i == a[-1][0]:
        a[-1][1] += 1
    else:
        a.append([i, 1])
# print(a)
l = 0
for i, j in a:
    r = l + j - 1
    for _ in range(j):
        v.append((j, l, r))
    l = r + 1
# print(v)
s = list(s)
# print(v)
st = LazySegTree(op, e, mapping, composition, id_, v)
# print(st)

for _ in range(q):
    tmp = input().split()
    tmp[0] = int(tmp[0])
    if tmp[0] == 1:
        i = int(tmp[1]) - 1
        x = tmp[2]
        if s[i] == x:
            continue
        prev_same_cnt = 0
        if i - 1 >= 0 and s[i - 1] == s[i]:
            prev_same_cnt += 1
        if i + 1 < n and s[i + 1] == s[i]:
            prev_same_cnt += 1

        next_same_cnt = 0
        if i - 1 >= 0 and s[i - 1] == x:
            next_same_cnt += 1
        if i + 1 < n and s[i + 1] == x:
            next_same_cnt += 1

        if prev_same_cnt == 0:
            if next_same_cnt == 0:
                pass
            elif next_same_cnt == 1:
                if i - 1 >= 0 and s[i - 1] == x:
                    l = st.get(i - 1)
                    new = (l[0] + 1, l[1], l[2] + 1)
                    st.apply(new[1], new[2] + 1, new)
                else:
                    r = st.get(i + 1)
                    new = (r[0] + 1, r[1] - 1, r[2])
                    st.apply(new[1], new[2] + 1, new)
            elif next_same_cnt == 2:
                l = st.get(i - 1)
                r = st.get(i + 1)
                new = (l[0] + r[0] + 1, l[1], r[2])
                st.apply(new[1], new[2] + 1, new)
        elif prev_same_cnt == 1:
            if next_same_cnt == 0:
                if i - 1 >= 0 and s[i - 1] == s[i]:
                    l = st.get(i - 1)
                    new = (l[0] - 1, l[1], l[2] - 1)
                    st.apply(new[1], new[2] + 1, new)
                    st.set(i, (1, i, i))
                else:
                    r = st.get(i + 1)
                    new = (r[0] - 1, r[1] + 1, r[2])
                    st.apply(new[1], new[2] + 1, new)
                    st.set(i, (1, i, i))

            elif next_same_cnt == 1:
                if i - 1 >= 0 and s[i - 1] == s[i]:
                    l = st.get(i - 1)
                    r = st.get(i + 1)
                    # 左を減らす
                    new = (l[0] - 1, l[1], i - 1)
                    st.apply(new[1], new[2] + 1, new)
                    # 右を増やす
                    new = (r[0] + 1, r[1] - 1, r[2])
                    st.apply(new[1], new[2] + 1, new)
                else:
                    l = st.get(i - 1)
                    r = st.get(i + 1)
                    # 右を減らす
                    new = (r[0] - 1, r[1] + 1, r[2])
                    st.apply(new[1], new[2] + 1, new)
                    # 左を増やす
                    new = (l[0] + 1, l[1], l[2] + 1)
                    st.apply(new[1], new[2] + 1, new)

            elif next_same_cnt == 2:
                raise ValueError()
        elif prev_same_cnt == 2:
            if next_same_cnt == 0:
                l = st.get(i - 1)
                r = st.get(i + 1)
                # 左
                new = (i - l[1], l[1], l[2] - 1)
                st.apply(new[1], new[2] + 1, new)
                # 右
                new = (r[2] - i, r[1] + 1, r[2])
                st.apply(new[1], new[2] + 1, new)

                st.set(i, (1, i, i))
            elif next_same_cnt == 1:
                raise ValueError()
            elif next_same_cnt == 2:
                raise ValueError()

        s[i] = x
        # print(s)
        # print(st)

    else:
        l, r = int(tmp[1]) - 1, int(tmp[2]) - 1
        # print(st)
        ans = 1
        ll = st.get(l)
        ans = max(ans, min(ll[2], r) - l + 1)
        rr = st.get(r)
        ans = max(ans, r - max(rr[1], l) + 1)

        l = ll[2] + 1
        r = rr[1] - 1
        # print(ll, rr, l, r)
        if 0 <= l <= r <= n:
            ans = max(ans, st.prod(l, r + 1)[0])
        print(ans)
