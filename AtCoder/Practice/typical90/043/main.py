# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict

around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
from sys import stdin

input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
from typing import Generic, Iterable, Iterator, List, TypeVar, Callable

T = TypeVar("T")


class SmartDeque(Generic[T]):
    """
    A double-ended queue supporting O(1) index access, insertion/removal at both ends, and reversal.
    Manages unused space (garbage) with a manual `clean` method for memory optimization.
    """

    def __init__(self, v: Iterable[T] = (), maxlen: int = 1 << 60):
        """
        Initialize the deque with an optional iterable and maximum length.
        Time complexity: O(n), where n is the size of the input iterable.
        """
        v = list(v)
        assert len(v) <= maxlen
        self._maxlen = maxlen
        self._size = len(v)
        self._l: List[T] = v[: self._size >> 1][::-1]
        self._r: List[T] = v[self._size >> 1 :]
        self._l_delled = 0
        self._r_delled = 0

    def __iter__(self) -> Iterator[T]:
        """
        Iterate over the elements of the deque.
        Time complexity: O(n).
        """
        for i in reversed(range(self._l_delled, len(self._l))):
            yield self._l[i]
        for i in range(self._r_delled, len(self._r)):
            yield self._r[i]

    def __reversed__(self) -> Iterator[T]:
        """
        Iterate over the deque in reverse order.
        Time complexity: O(n).
        """
        for i in reversed(range(self._r_delled, len(self._r))):
            yield self._r[i]
        for i in range(self._l_delled, len(self._l)):
            yield self._l[i]

    def __eq__(self, other) -> bool:
        """
        Check if this deque is equal to another iterable.
        Time complexity: O(n).
        """
        return list(self) == list(other)

    def __len__(self) -> int:
        """
        Return the number of elements in the deque.
        Time complexity: O(1).
        """
        return self._size

    def __str__(self) -> str:
        """
        Return a string representation of the deque.
        Time complexity: O(n).
        """
        return f"MyDeque: {list(self)}"

    def __contains__(self, x: T) -> bool:
        """
        Check if the deque contains the specified element.
        Time complexity: O(n).
        """
        return x in self._l[self._l_delled :] or x in self._r[self._r_delled :]

    def __getitem__(self, i) -> List[T] | T:
        """
        Access an element or a slice of the deque.
        Time complexity: O(1) for single access, O(k) for slicing.
        """
        if isinstance(i, slice):
            start, stop, step = i.indices(self._size)
            return [self[idx] for idx in range(start, stop, step)]
        else:
            assert 0 <= i < self._size or -self._size <= i < 0
            if i < 0:
                i += self._size
            if i < len(self._l) - self._l_delled:
                return self._l[~i]
            else:
                return self._r[self._r_delled + i - (len(self._l) - self._l_delled)]

    def __setitem__(self, i: int, x: T) -> None:
        """
        Set the value at the specified index.
        Time complexity: O(1).
        """
        assert 0 <= i <= self._size or -self._size <= i <= -1
        if i < 0:
            i += self._size
        if i < len(self._l) - self._l_delled:
            self._l[~i] = x
        else:
            self._r[self._r_delled + i - (len(self._l) - self._l_delled)] = x

    def __delitem__(self, i: int) -> None:
        """
        Delete the element at the specified index.
        Time complexity: O(n).
        """
        assert 0 <= i <= self._size or -self._size <= i <= -1
        self.pop(i)

    def __add__(self, other: Iterable[T]):
        """
        Concatenate this deque with another iterable and return a new deque.
        Time complexity: O(n + k), where n is the size of this deque,
        and k is the size of the other iterable.
        """
        new_deque = SmartDeque(list(self), maxlen=self._maxlen)
        new_deque.extend(other)
        return new_deque

    def __iadd__(self, other: Iterable[T]):
        """
        Add another iterable to this deque in-place.
        Time complexity: O(k), where k is the size of the other iterable.
        """
        self.extend(other)
        return self

    def __mul__(self, n: int):
        """
        Repeat the elements of the deque n times and return a new deque.
        Time complexity: O(n * m),
        where n is the size of this deque,and m is the repetition factor.
        """
        return SmartDeque(list(self) * n, maxlen=self._maxlen)

    def __imul__(self, n: int):
        """
        Repeat the elements of the deque n times in-place.
        Time complexity: O(n * m),
        where n is the size of this deque, and m is the repetition factor.
        """
        repeated = list(self) * n
        self.clear()
        self.extend(repeated)
        return self

    def reverse(self) -> None:
        """
        Reverse the order of the deque in O(1).
        """
        self._l, self._r = self._r, self._l
        self._l_delled, self._r_delled = self._r_delled, self._l_delled

    def count(self, x: T) -> int:
        """
        Count the occurrences of the specified element.
        Time complexity: O(n).
        """
        return self._l[self._l_delled :].count(x) + self._r[self._r_delled :].count(x)

    def copy(self):
        """
        Create a shallow copy of the deque.
        Time complexity: O(n).
        """
        return SmartDeque(list(self), maxlen=self._maxlen)

    def sort(self, *, key: Callable[[T], object] = None, reverse: bool = False) -> None:
        """
        Sort the deque in-place.
        Time complexity: O(n log n).
        """
        sorted_list = sorted(self, key=key, reverse=reverse)
        mid = self._size >> 1
        self._l = sorted_list[:mid][::-1]
        self._r = sorted_list[mid:]
        self._l_delled = 0
        self._r_delled = 0

    def index(self, x: T, start: int = 0, stop=None) -> int:
        """
        Find the first occurrence of the element in the range [start, stop).
        Time complexity: O(n).
        """
        if stop == None:
            stop = self._size
        if start < 0:
            start += self._size
        if stop < 0:
            stop += self._size
        start = max(0, start)
        stop = min(self._size, stop)

        for i in range(start, stop):
            if self[i] == x:
                return i
        raise ValueError(f"{x} is not in MyDeque")

    def clear(self) -> None:
        """
        Remove all elements from the deque.
        Time complexity: O(1).
        """
        self._l.clear()
        self._r.clear()
        self._l_delled = 0
        self._r_delled = 0
        self._size = 0

    def append(self, x: T) -> None:
        """
        Add an element to the right end of the deque.
        Time complexity: O(1).
        """
        self._size += 1
        self._r.append(x)
        if self._size > self._maxlen:
            self.popleft()

    def appendleft(self, x: T) -> None:
        """
        Add an element to the left end of the deque.
        Time complexity: O(1).
        """
        self._size += 1
        self._l.append(x)
        if self._size > self._maxlen:
            self.pop()

    def pop(self, i=-1) -> T:
        """
        Remove and return the element at the specified index.
        Time complexity: O(1) for ends, O(n) for middle.
        """
        assert 0 <= i <= self._size or -self._size <= i <= -1
        assert self._size > 0
        if i < 0:
            i += self._size
        self._size -= 1

        if i == self._size:
            if len(self._r) - self._r_delled > 0:
                return self._r.pop()
            else:
                self._l_delled += 1
                return self._l[self._l_delled - 1]
        else:
            if i < len(self._l) - self._l_delled:
                return self._l.pop(~i)
            else:
                return self._r.pop(self._r_delled + i - (len(self._l) - self._l_delled))

    def popleft(self) -> T:
        """
        Remove and return the leftmost element of the deque.
        Time complexity: O(1).
        """
        assert self._size > 0
        self._size -= 1
        if len(self._l) - self._l_delled > 0:
            return self._l.pop()
        else:
            self._r_delled += 1
            return self._r[self._r_delled - 1]

    def extend(self, v: Iterable[T]) -> None:
        """
        Extend the deque to the right with the elements from the iterable.
        Time complexity: O(k), where k is the length of the iterable.
        """
        for i in v:
            self.append(i)

    def extendleft(self, v: Iterable[T]) -> None:
        """
        Extend the deque to the left with the elements from the iterable.
        Time complexity: O(k), where k is the length of the iterable.
        """
        for i in v:
            self.appendleft(i)

    def insert(self, i: int, x: T) -> None:
        """
        Insert an element at the specified position.
        Time complexity: O(n).
        """
        assert self._size < self._maxlen
        assert 0 <= i <= self._size or -self._size <= i <= -1
        if i < 0:
            i += self._size
        self._size += 1
        if i < len(self._l) - self._l_delled:
            self._l.insert(len(self._l) - i, x)
        else:
            self._r.insert(self._r_delled + i - (len(self._l) - self._l_delled), x)

    def remove(self, x: T) -> None:
        """
        Remove the first occurrence of the specified element.
        Time complexity: O(n).
        """
        assert self._size > 0
        self.pop(self.index(x))

    def rotate(self, k: int = 1) -> None:
        """
        Rotate the deque n steps to the right. Negative values rotate to the left.
        Time complexity: O(k).
        """
        if self._size == 0:
            return
        k %= self._size
        if k > 0:
            for _ in range(k):
                self.appendleft(self.pop())
        else:
            for _ in range(-k):
                self.append(self.popleft())

    @property
    def garbage_size(self) -> int:
        """
        Return the number of unused elements (garbage) in the deque.
        Time complexity: O(1).
        """
        return len(self._l) + len(self._r) - self._size

    @property
    def maxlen(self) -> int:
        """
        Return the maximum allowable size of the deque.
        Time complexity: O(1).
        """
        return self._maxlen

    @maxlen.setter
    def maxlen(self, x: int) -> None:
        """
        Update the maximum size of the deque.
        Raises an error if the current size exceeds the new maxlen.
        Time complexity: O(1).
        """
        assert self._size <= x
        self._maxlen = x

    def clean(self) -> None:
        """
        Remove unused elements (garbage) and reorganize the deque.
        Time complexity: O(n), where n is the number of elements in the deque.
        """
        if self.garbage_size == 0:
            return
        tmp = list(self)
        mid = self._size >> 1
        self._l = tmp[:mid][::-1]
        self._r = tmp[mid:]
        self._l_delled = 0
        self._r_delled = 0


class TupleHash:
    def __init__(self, *args):
        """
        args: 各要素の取りうる値の最大値
        """
        self.bit_len = [-1] * len(args)
        self.mask = [-1] * len(args)
        for index, i in enumerate(args):
            l = len(bin(i)) - 2
            self.bit_len[index] = l
            self.mask[index] = (1 << l) - 1
        if sum(self.bit_len) > 63:
            from sys import stderr

            print("数字が大きすぎるため、低速になる可能性があります。", file=stderr)

        self.sum_bit_len = [0]
        for i in self.bit_len[1:][::-1]:
            self.sum_bit_len.append(self.sum_bit_len[-1] + i)
        self.sum_bit_len = self.sum_bit_len[::-1]

    def encode(self, *args):
        """
        タプルを整数にエンコード
        """
        assert len(self.bit_len) == len(args), "引数の数が一致しません。"
        assert all(0 <= i for i in args), f"引数に負の値が含まれています。引数: {args}"
        res = 0
        for a, l in zip(args, self.sum_bit_len):
            res |= a << l
        return res

    def deocde(self, res, index=None):
        """
        整数から元のタプルにデコード
        index: 特定の要素だけ取得する場合（省略時は全要素を取得）
        """
        assert index == None or 0 <= index < len(self.bit_len), "idxの値が不正です。"
        if index == None:
            return (res >> l & m for l, m in zip(self.sum_bit_len, self.mask))
        else:
            return res >> self.sum_bit_len[index] & self.mask[index]


h, w = MII()
sx, sy = MII()
gx, gy = MII()
sx -= 1
sy -= 1
gx -= 1
gy -= 1
s = [input() for _ in range(h)]
visited = [[[1 << 60] * 4 for _ in range(1000)] for _ in range(1000)]
deq = SmartDeque()
# from collections import deque

# deq = deque()
for i in range(4):
    visited[sx][sy][i] = 0
    deq.append((0, sx, sy, i))
while deq:
    d, x, y, v = deq.popleft()
    if x == gx and y == gy:
        break
    if d > visited[x][y][v]:
        continue
    for index, (i, j) in enumerate(around4):
        nx = x + i
        ny = y + j
        if v == index:
            nd = d
        else:
            nd = d + 1
        if (
            nx in range(h)
            and ny in range(w)
            and s[nx][ny] == "."
            and nd < visited[nx][ny][index]
        ):
            visited[nx][ny][index] = nd
            if d == nd:
                deq.appendleft((nd, nx, ny, index))
            else:
                deq.append((nd, nx, ny, index))

ans = inf
for i in range(4):
    ans = min(ans, visited[gx][gy][i])
print(ans)
