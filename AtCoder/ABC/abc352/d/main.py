import sys


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


class SegTree:
    def __init__(
        self,
        op: typing.Callable[[typing.Any, typing.Any], typing.Any],
        e: typing.Any,
        v: typing.Union[int, typing.List[typing.Any]],
    ) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

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

    def max_right(self, left: int, f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


n, k = MII()
p = LMII()
v = [-1] * n
for i, j in enumerate(p):
    v[j - 1] = i

from collections import deque

# print(v)


def swag(l, k, mode="min"):
    """
    lの中から連続してk個選ぶ時、左端が 0 ~ i-k の時それぞれの最大値、最小値を取得。
    n - k + 1個のリストを返す。
    """
    deq = deque()
    result = []
    if mode == "min":
        for i, a in enumerate(l):
            while deq and l[deq[-1]] >= a:
                deq.pop()
            deq.append(i)
            if deq[0] == i - k:
                deq.popleft()
            if i >= k - 1:
                result.append(l[deq[0]])
    elif mode == "max":
        for i, a in enumerate(l):
            while deq and l[deq[-1]] <= a:
                deq.pop()
            deq.append(i)
            if deq[0] == i - k:
                deq.popleft()
            if i >= k - 1:
                result.append(l[deq[0]])
    return result


ans = inf

max_ = swag(v, k, "max")
min_ = swag(v, k, "min")

for mn, mx in zip(min_, max_):
    ans = min(ans, mx - mn)
print(ans)
# # 区間加算・区間最大値取得^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# op = lambda a, b: max(a, b)
# e = -float("inf")
# mapping = lambda f, x: f + x
# composition = lambda f, g: f + g
# id_ = 0
# # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# st_max = SegTree(op, e, v)
# # 区間加算・区間最小値取得^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# op = lambda a, b: min(a, b)
# e = float("inf")
# mapping = lambda f, x: f + x
# composition = lambda f, g: f + g
# id_ = 0
# # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# st_min = SegTree(op, e, v)
# ans = inf
# for i in range(n - k + 1):
#     ans = min(ans, st_max.prod(i, i + k) - st_min.prod(i, i + k))
# print(ans)
