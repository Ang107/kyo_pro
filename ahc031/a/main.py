# 入力
import time

start = time.perf_counter()
import random


def Input():
    W, D, N = map(int, input().split())
    A = []
    for _ in range(D):
        tmp = list(map(int, input().split()))[::-1]
        A.append(tmp)
    return W, D, N, A


# その日のエリア配置
def put(a, h, hight):
    isover = False
    w = [0] * len(h)
    rslt = []
    cost = 1000 * (len(h) - 1)
    for i in a:
        puted = False
        Hi = 10**18
        for j in range(len(h)):
            width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = True
                hi = max(width, h[j]) / min(width, h[j])
                if Hi > hi:
                    rs = j, width, [hight[j], w[j], hight[j + 1], w[j] + width]
                    break
                    # rslt.append()
                    # w[j] += width
                    # cost += h[j]

        if puted:
            j, width, tmp = rs
            w[j] += width
            cost += h[j]
            rslt.append(tmp)
        else:
            isover = True
            s = 0
            tmp = None
            for j in range(len(h)):
                width = min(1000 - w[j], -(-i // h[j]))
                if width * i > s:
                    s = width * i
                    tmp = (
                        j,
                        width,
                        [hight[j], w[j], hight[j + 1], min(1000, w[j] + width)],
                    )
            if tmp == None:
                tmp = 1
                while rslt[-tmp][3] - rslt[-tmp][1] < 2:
                    tmp += 1

                rslt[-tmp][3] = rslt[-tmp][1] + 1
                cost += 100 * (
                    i - (1000 - rslt[-tmp][3]) * (rslt[-tmp][2] - rslt[-tmp][0])
                )
                cost += 100 * ((1000 - rslt[-tmp][3]) * (rslt[-tmp][2] - rslt[-tmp][0]))
                cost += rslt[-tmp][2] - rslt[-tmp][0]

                rs = rslt[-tmp][:]
                rs[1], rs[3] = rs[3], 1000
                rslt.append(rs)
            else:
                idx, width, rs = tmp
                cost += 100 * (i - width * h[idx])
                cost += h[idx]
                w[idx] = 1000
                rslt.append(rs)

    return rslt[::-1], cost, isover


# 渡されたhで配置した場合のコストと答えの取得
def get_ans(A, h, hight):
    ans = []
    cost = 0
    over = []
    for idx, i in enumerate(A):
        rslt, c, is_over = put(i, h, hight)
        ans.append(rslt)
        cost += c
        if is_over:
            over.append(idx)

    return ans, cost, over


# 出力
def Output(ans):
    for i in ans:
        for j in i:
            print(*j)


# 指定された時間、hを元に山登りする
def yamanobori(A, h, time_limit):
    cnt = 0
    lh = len(h)
    hight = [0] * (lh + 1)
    for i, j in enumerate(h):
        hight[i + 1] = hight[i] + j
    ans, cost, over = get_ans(A, h, hight)
    if len(h) == 1:
        return ans, cost, over, h, hight
    over = []
    while True:
        give_idx, take_idx = random.choice(range(lh)), random.choice(range(lh))
        if give_idx == take_idx:
            continue

        h_n = h[:]
        num = random.choice(range(h[give_idx] // 2))
        h_n[give_idx] -= num
        h_n[take_idx] += num
        h_n.sort(reverse=True)

        hight_n = [0] * (lh + 1)
        for i, j in enumerate(h_n):
            hight_n[i + 1] = hight_n[i] + j

        ans_n, cost_n, over_n = get_ans(A, h_n, hight_n)
        if cost_n < cost:
            # print(hight, hight_n, cost, cost_n, cnt)
            h = h_n
            hight = hight_n
            cost = cost_n
            ans = ans_n
            over = over_n

        cnt += 1

        if cnt % 100 == 0:
            if time.perf_counter() - start > time_limit:
                return ans, cost, over, h, hight


# hの個数をプラマイ一個で山登りを呼び出す
def solve(W, D, N, A):
    h_num = int(N**0.5)
    time_limit = [0.5, 1.0, 1.5]
    cost = 10**18

    # 初期解生成
    # 縦のみの保険用
    w_num = -(-N / 1)
    avr = [0] * 1
    for tmp in A:
        tmp = tmp[::-1]
        for j in range(N):
            avr[int(j // w_num)] += tmp[j]

    h = []
    avr = [int(i**0.5) for i in avr]
    avr_sum = sum(avr)
    for j in avr[:-1]:
        h.append(1000 * j // avr_sum)
    h.append(1000 - sum(h))

    ans_hoken, _, over_hoken, _, _ = yamanobori(A, h, 0)
    # print(over_hoken)

    for i in range(3):
        # 初期解生成
        h_num_n = h_num + 1 - i
        w_num = -(-N / h_num_n)
        avr = [0] * h_num_n
        for tmp in A:
            tmp = tmp[::-1]
            for j in range(N):
                avr[int(j // w_num)] += tmp[j]

        h = []
        avr = [int(i**0.5) for i in avr]
        avr_sum = sum(avr)
        for j in avr[:-1]:
            h.append(1000 * j // avr_sum)
        h.append(1000 - sum(h))

        ans_n, cost_n, over_n, h_n, hight_n = yamanobori(A, h, time_limit[i])

        # print(cost_n)
        if cost > cost_n:
            ans = ans_n
            cost = cost_n
            over = over_n
            rs_h = h_n
            rs_hight = hight_n

    # print(over)
    over_hoken = set(over_hoken)
    for i in over:
        if i not in over_hoken:
            ans[i] = ans_hoken[i]

    return ans, ans_hoken, rs_h, rs_hight, over, over_hoken


# def change_ans(A, ans, ans_hoken, rs_h, rs_hight, over, over_hoken):
#     # 二つを合わせて一個とマッチングとかも可能ではある
#     # とりあえず一個拡張を試みる
#     a = A[0]
#     b = A[1]
#     a_SMS = SortedMultiset(a)
#     b_SMS = SortedMultiset(b)
#     diff = []
#     same = []
#     for i in a_SMS:
#         l = b_SMS.le(i)
#         r = b_SMS.ge(i)
#         if abs(i - l) > abs(i - r):
#             diff.append((abs(i - r), i, r))
#         else:
#             diff.append((abs(i - l), i, l))

#     diff.sort(key=lambda x: x[0])
#     d, i, j = diff[0]
#     if i == j:
#         same.append(i)
#         if is_OK():
#             pass
#         else:
#             pass


def is_OK():
    return False

    # for i in range(1,len(A)):


def main():
    # 方針1
    # 縦の分割数をいくつか決めて、それぞれで幅を山登りする
    # その過程で得られたスコアが最も良いものを答えにする

    # TODO
    # 現在では日にちを跨いで柵を使いまわすようなことを考慮していない

    W, D, N, A = Input()
    ans, ans_hoken, rs_h, rs_hight, over, over_hoken = solve(W, D, N, A)

    Output(ans)
    pass


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


if __name__ == "__main__":
    main()
