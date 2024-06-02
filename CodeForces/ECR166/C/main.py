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

t = II()
ans_list = []
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional

T = TypeVar("T")


class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        n = self.size = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [
            a[n * i // num_bucket : n * (i + 1) // num_bucket]
            for i in range(num_bucket)
        ]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]:
                break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a, b, i = self._position(x)
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]

    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a:
            del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x:
            return False
        self._pop(a, b, i)
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self.a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0:
                    return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a):
                    return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


for _ in range(t):
    n, m = MII()
    a = LMII()
    b = LMII()
    ab = [(i, j) for i, j in zip(a, b)]
    # プログラミング得意、テスト得意でグループ分け
    pr_good = []
    ts_good = []
    for idx, (i, j) in ab:
        if i > j:
            pr_good.append((idx, i, j))
        else:
            ts_good.append((idx, i, j))
    # それぞれのスキル値で累積和
    pr_good_pr = [0]
    pr_good_ts = [0]
    ts_good_pr = [0]
    ts_good_ts = [0]
    for i, j in pr_good:
        pr_good_pr.append(pr_good_pr[-1] + i)
        pr_good_pr.append(pr_good_ts[-1] + j)
    for i, j in ts_good:
        ts_good_pr.append(ts_good_pr[-1] + i)
        ts_good_pr.append(ts_good_ts[-1] + j)
    ans = []
    for i in range(n + m + 1):
        r = 0
        # iさん抜きで考える
        # プログラミングが得意なら
        if ab[i][0] > ab[i][1]:
            if i <= pr_good[n-1]:
                r += pr_good_pr[min(n)]
            else:
                
            # プログラミング得意でプログラミングをする人数
            p_p = min(n, len(pr_good_pr) - 1)
            # プログラミング苦手でプログラミングをする人数
            pn_p = n - p_p
            # テスト得意でテストをする人数
            t_t = min(m, len(ts_good_ts))
            # テスト苦手でテストをする人数
            t_nt = m - t_t
        else:
            # プログラミング得意でプログラミングをする人数
            p_p = min(n, len(pr_good_pr))
            # プログラミング苦手でプログラミングをする人数
            pn_p = n - p_p
            # テスト得意でテストをする人数
            t_t = min(m, len(ts_good_ts) - 1)
            # テスト苦手でテストをする人数
            t_nt = m - t_t

    # pro = []
    # test = []
    # for idx, (i, j) in enumerate(zip(a, b)):
    #     if i < j:
    #         pro.append((i, j))
    #     else:
    #         test.append((i, j))

    # pro_good = []
    # ts_good = []
    # for idx, (i, j) in enumerate(ab):
    #     if i > j:
    #         pro_good.append(idx)
    #     else:
    #         ts_good.append(idx)

    # ans = 0
    # pr = SortedMultiset()
    # ts = SortedMultiset()
    # pr_umari = [0]
    # ts_umari = [0]
    # for idx, (i, j) in enumerate(zip(a[:-1], b[:-1])):
    #     if pr_umari[-1] == n:
    #         pr_umari.append(n)
    #         ts_umari.append(ts_umari[-1] + 1)
    #     elif ts_umari[-1] == m:
    #         pr_umari.append(pr_umari[-1] + 1)
    #         ts_umari.append(m)
    #     else:
    #         if i < j:
    #             ts_umari.append(ts_umari[-1] + 1)
    #             pr_umari.append(pr_umari[-1])
    #         else:
    #             ts_umari.append(ts_umari[-1])
    #             pr_umari.append(pr_umari[-1] + 1)
    # # プログラミング苦手なのにプログラミングやってる人
    # pr_bad = deque()
    # ts_bad = deque()
    # for idx, (i, j) in enumerate(zip(a[1:], b[1:])):
    #     if len(pr) == n:
    #         ans += j
    #         ts.add(idx + 1)
    #         if i > j:
    #             ts_bad.append(idx +  1)
    #     elif len(ts) == m:
    #         ans += i
    #         pr.add(idx + 1)
    #         if i < j:
    #             pr_bad.append(idx + 1)
    #     else:
    #         if i < j:
    #             ts.add(idx + 1)
    #             ans += j
    #         else:
    #             pr.add(idx + 1)
    #             ans += i

    # rslt = [ans]
    # pr_ple = set()
    # haizoku = [-1] * (n + m + 1)
    # if a[0] < b[0]:
    #     if m != 0:
    #         haizoku[0] = 1
    #     else:
    #         haizoku[0] = 0
    # else:
    #     if n != 0:
    #         haizoku[0] = 0
    #     else:
    #         haizoku[0] = 1
    # # print(pr_umari)
    # # print(ts_umari)
    # # print(pr)
    # # print(ts)
    # # print(haizoku)
    # for i in range(1, n + m + 1):
    #     if a[i] < b[i]:
    #         if m != ts_umari[i - 1]:
    #             haizoku[i] = 1
    #         else:
    #             haizoku[i] = 0
    #     else:
    #         if n != pr_umari[i - 1]:
    #             haizoku[i] = 0
    #         else:
    #             haizoku[i] = 1
    #     # print(haizoku)
    #     if haizoku[i] == haizoku[i - 1]:
    #         if haizoku[i] == 0:
    #             pr.discard(i)
    #             pr.add(i - 1)
    #         else:
    #             ts.discard(i)
    #             ts.add(i - 1)

    #         ans += ab[i - 1][haizoku[i - 1]]
    #         ans -= ab[i][haizoku[i]]
    #     else:
    #         ans += ab[i - 1][haizoku[i - 1]]
    #         ans -= ab[i][haizoku[i]]

    #         if haizoku[i] == 0:
    #             pr.discard(i)
    #             ts.add(i - 1)

    #             # 嘘解法かも
    #             # プログラミングに空き
    #             # プログラミング行きたかったけど行けなかった人か、テストの最後の人
    #             tmp = -1
    #             while ts_bad and ts_bad[0] <= i:
    #                 ts_bad.popleft()
    #             if ts_bad:
    #                 tmp = ts_bad.popleft()
    #             if tmp == -1:
    #                 tmp = ts.pop()
    #             ts.discard(tmp)
    #             pr.add(tmp)

    #             ans += ab[tmp][0]
    #             ans -= ab[tmp][1]
    #         else:
    #             ts.discard(i)
    #             pr.add(i - 1)
    #             tmp = -1
    #             while pr_bad and pr_bad[0] <= i:
    #                 pr_bad.popleft()
    #             if pr_bad:
    #                 tmp = pr_bad.popleft()
    #             if tmp == -1:
    #                 tmp = pr.pop()
    #             pr.discard(tmp)
    #             ts.add(tmp)

    #             ans += ab[tmp][1]
    #             ans -= ab[tmp][0]

    #     rslt.append(ans)
    # ans_list.append(rslt)

for i in ans_list:
    print(*i)
