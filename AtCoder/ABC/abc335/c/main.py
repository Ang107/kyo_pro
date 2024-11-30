from typing import Generic, Iterable, Iterator, List, TypeVar

T = TypeVar("T")


class MyDeque(Generic[T]):
    """
    インデックスアクセスがO(1)な両端キュー
    """

    def __init__(self, v: Iterable[T] = (), maxlen=1 << 60):
        assert len(v) <= maxlen
        self.maxlen = maxlen
        self._size = len(v)
        self._l: List[T] = []
        self._r: List[T] = []
        for i in range(self._size):
            if i < self._size >> 1:
                self._l.append(v[i])
            else:
                self._r.append(v[i])
        self._l.reverse()
        self._l_delled = 0
        self._r_delled = 0

    def __iter__(self) -> Iterator[T]:
        for i in reversed(range(self._l_delled, len(self._l))):
            yield self._l[i]
        for i in range(self._r_delled, len(self._r)):
            yield self._r[i]

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(range(self._r_delled, len(self._r))):
            yield self._r[i]
        for i in range(self._l_delled, len(self._l)):
            yield self._l[i]

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return f"MyDeque: {list(self)}"

    def __contains__(self, x: T) -> bool:
        return x in self._l[self._l_delled :] or x in self._r[self._r_delled :]

    def __getitem__(self, i: int) -> T:
        assert 0 <= i <= self._size or -self._size <= i <= -1
        if i < 0:
            i += self._size
        if i < len(self._l) - self._l_delled:
            return self._l[-i - 1]
        else:
            return self._r[self._r_delled + i - (len(self._l) - self._l_delled)]

    def __setitem__(self, i: int, x: T) -> None:
        assert 0 <= i <= self.size or -self.size <= i <= -1
        if i < 0:
            i += self._size
        if i < len(self._l) - self._l_delled:
            self._l[-i - 1] = x
        else:
            self._r[self._r_delled + i - (len(self._l) - self._l_delled)] = x

    def count(self, x: T) -> int:
        return self._l[self._l_delled :].count(x) + self._r[self._r_delled :].count(x)

    def append(self, x: T) -> None:
        self._size += 1
        self._r.append(x)
        if self._size > self.maxlen:
            self._size -= 1
            self.popleft()

    def pop(self) -> T:
        assert self._size > 0
        self._size -= 1
        if len(self._r) - self._r_delled > 0:
            return self._r.pop()
        else:
            self._l_delled += 1
            return self._l[self._l_delled - 1]

    def appendleft(self, x: T) -> None:
        self._size += 1
        self._l.append(x)
        if self._size > self.maxlen:
            self._size -= 1
            self.pop()

    def popleft(self) -> T:
        assert self._size > 0
        self._size -= 1
        if len(self._l) - self._l_delled > 0:
            return self._l.pop()
        else:
            self._r_delled += 1
            return self._r[self._r_delled - 1]


class GoriDeque:
    def __init__(self, src_arr=[], max_size=300000):
        self.N = max(max_size, len(src_arr)) + 1
        self.buf = list(src_arr) + [None] * (self.N - len(src_arr))
        self.head = 0
        self.tail = len(src_arr)

    def __index(self, i):
        l = len(self)
        if not -l <= i < l:
            raise IndexError("index out of range: " + str(i))
        if i < 0:
            i += l
        return (self.head + i) % self.N

    def __extend(self):
        ex = self.N - 1
        self.buf[self.tail + 1 : self.tail + 1] = [None] * ex
        self.N = len(self.buf)
        if self.head > 0:
            self.head += ex

    def is_full(self):
        return len(self) >= self.N - 1

    def is_empty(self):
        return len(self) == 0

    def append(self, x):
        if self.is_full():
            self.__extend()
        self.buf[self.tail] = x
        self.tail += 1
        self.tail %= self.N

    def appendleft(self, x):
        if self.is_full():
            self.__extend()
        self.buf[(self.head - 1) % self.N] = x
        self.head -= 1
        self.head %= self.N

    def pop(self):
        if self.is_empty():
            raise IndexError("pop() when buffer is empty")
        ret = self.buf[(self.tail - 1) % self.N]
        self.tail -= 1
        self.tail %= self.N
        return ret

    def popleft(self):
        if self.is_empty():
            raise IndexError("popleft() when buffer is empty")
        ret = self.buf[self.head]
        self.head += 1
        self.head %= self.N
        return ret

    def __len__(self):
        return (self.tail - self.head) % self.N

    def __getitem__(self, key):
        return self.buf[self.__index(key)]

    def __setitem__(self, key, value):
        self.buf[self.__index(key)] = value

    def __str__(self):
        return "Deque({0})".format(str(list(self)))


n, q = map(int, input().split())
dxy = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
a = [(i + 1, 0) for i in range(n)]
deq = MyDeque(a)
for _ in range(q):
    t, c = input().split()
    t = int(t)
    if t == 1:
        x, y = deq[0]
        deq.appendleft((x + dxy[c][0], y + dxy[c][1]))
    else:
        p = int(c) - 1
        print(*deq[p])
