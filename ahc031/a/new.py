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
                    Hi = hi
                    rs = j, width, [hight[j], w[j], hight[j + 1], w[j] + width]

                    # rslt.append()
                    # w[j] += width
                    # cost += h[j]
        # 配置可能な場合
        if puted:
            j, width, tmp = rs
            w[j] += width
            cost += h[j]
            rslt.append(tmp)
        # 収まらない場合
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
            # スペースが０の場合
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
            # スペースが存在する場合
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
    from collections import defaultdict

    d = defaultdict(int)
    d_idx = {}
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if d[(i, ans[i][j][0])] < ans[i][j][3]:
                d[(i, ans[i][j][0])] = ans[i][j][3]
                d_idx[(i, ans[i][j][0])] = (i, j)

    # print(d_idx)
    for i, j in d_idx.values():
        ans[i][j][3] = 1000

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
    time_limit = [0.8, 1.5, 2.2]
    cost = float("inf")

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
        h_num_n = max(2, h_num + 1 - i)
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

        # print(len(h), cost_n)
        if cost > cost_n:
            ans = ans_n
            cost = cost_n
            over = over_n
            rs_h = h_n
            rs_hight = hight_n

    # print(over)
    over_hoken = set(over_hoken)
    over = set(over)
    for i in over:
        if i not in over_hoken:
            ans[i] = ans_hoken[i]

    # Output(ans)
    # print("3333333333333333333333333333333333333333333333333333")

    return ans, ans_hoken, rs_h, rs_hight, over, over_hoken


def change_ans(A, ans, ans_hoken, h, hight, over, over_hoken):
    # 二つを合わせて一個とマッチングとかも可能ではある
    # とりあえず一個拡張を試みる
    # prv = None
    for i in range(0, len(A) - 1, 2):
        if i in over or i + 1 in over:
            continue

        rslt_a = None
        rslt_b = None
        a = A[i]
        # if i == 0 or prv == None:
        #     a = A[i]
        # else:
        # a = prv
        # prv = None
        b = A[i + 1]
        a_idx = SortedMultiset(range(len(a)))
        b_idx = SortedMultiset(range(len(b)))
        a_SMS = SortedMultiset(a)
        b_SMS = SortedMultiset(b)

        same_a = []
        same_b = []
        while True:
            # print(a_SMS.a)
            # print(b_SMS.a)
            diff = []
            for i_idx, j in zip(a_idx, a_SMS):

                l = b_SMS.le(j)
                r = b_SMS.ge(j)
                if l == None:
                    diff_l = 10**8
                else:
                    diff_l = abs(j - l)

                if r == None:
                    diff_r = 10**8
                else:
                    diff_r = abs(j - r)

                if diff_l > diff_r:
                    j_idx = b_idx[b_SMS.index_right(j)]
                    diff.append((diff_r, j, r, i_idx, j_idx))
                else:
                    j_idx = b_idx[b_SMS.index_right(j) - 1]
                    diff.append((diff_l, j, l, i_idx, j_idx))

            _, j, k, j_idx, k_idx = min(diff, key=lambda x: x[0])
            # print(A[i], A[i + 1], a_SMS, b_SMS)
            # print(j, k, A[i][-j_idx - 1], A[i + 1][-k_idx - 1])
            same_a.append([max(j, k), j_idx])
            same_b.append([max(j, k), k_idx])
            a_idx.discard(j_idx)
            b_idx.discard(k_idx)
            a_SMS.discard(j)
            b_SMS.discard(k)

            # print(j, k, j_idx, k_idx)
            # print(same_a, a_SMS)
            # print(same_b, b_SMS)
            # print(a_idx)
            # print(b_idx)
            # print([(i, j) for i, j in enumerate(A[i][::-1])])
            # print([(i, j) for i, j in enumerate(A[i + 1][::-1])])
            ok_a, rslt_a_n = is_OK(same_a, list(a_SMS), list(a_idx), h, hight)
            ok_b, rslt_b_n = is_OK(same_b, list(b_SMS), list(b_idx), h, hight)

            if ok_a and ok_b:
                # print(rslt_b_n)
                rslt_a, rslt_b = rslt_a_n, rslt_b_n
                # prv = []
                # for j, k in same_b:
                #     prv.append(j)
                # for j in b_SMS:
                #     prv.append(j)

            else:
                if rslt_a and rslt_b:
                    # print(rslt_a)
                    ans[i] = rslt_a
                    ans[i + 1] = rslt_b

                break

            if len(a_SMS) == 0:
                if rslt_a and rslt_b:
                    # print(rslt_a)
                    ans[i] = rslt_a
                    ans[i + 1] = rslt_b
                break


def is_OK(same, other, Idx, h, hight):

    isover = False
    w = [0] * len(h)
    rslt = [None] * (len(same) + len(other))

    for i, idx in same:
        # print(i, idx, rslt, w)
        Hi = 10**18
        puted = False
        # if A[A_idx][-idx - 1] > i:
        #     print(A[A_idx][-idx - 1], i, idx)
        #     print("er")
        #     print(same, other, [(i, j) for i, j in enumerate(A[A_idx][::-1])])
        #     exit()
        for j in range(len(h)):
            width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = True
                hi = max(width, h[j]) / min(width, h[j])
                if Hi > hi:
                    Hi = hi
                    rs = j, width, [hight[j], w[j], hight[j + 1], w[j] + width]
        # 配置可能な場合
        if puted:
            j, width, tmp = rs
            w[j] += width
            # cost += h[j]
            # print(len(rslt) - idx - 1, len(rslt), idx)
            rslt[idx] = tmp
        else:
            isover = True
            return not isover, rslt[::-1]

    for i, idx in zip(other[::-1], Idx[::-1]):
        Hi = 10**18
        puted = False
        # if A[A_idx][-idx - 1] > i:
        #     print(A[A_idx][-idx - 1], i)
        #     print("er")
        # # exit()
        for j in range(len(h)):
            width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = True
                hi = max(width, h[j]) / min(width, h[j])
                if Hi > hi:
                    Hi = hi

                    rs = j, width, [hight[j], w[j], hight[j + 1], w[j] + width]
        # 配置可能な場合
        if puted:
            j, width, tmp = rs
            w[j] += width
            # cost += h[j]
            rslt[idx] = tmp
        else:
            isover = True
            return not isover, rslt[::-1]

    return not isover, rslt


def main():
    # 方針1
    # 縦の分割数をいくつか決めて、それぞれで幅を山登りする
    # その過程で得られたスコアが最も良いものを答えにする

    # TODO
    # 現在では日にちを跨いで柵を使いまわすようなことを考慮していない
    global A
    W, D, N, A = Input()
    ans, ans_hoken, h, hight, over, over_hoken = solve(W, D, N, A)
    change_ans(A, ans, ans_hoken, h, hight, over, over_hoken)

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
