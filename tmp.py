n, q = map(int, input().split())
import string
import functools
from functools import cache
from itertools import permutations

alp = string.ascii_uppercase
ans = list(alp[:n])


@cache
def compare(x, y):
    print(f"? {x} {y}")
    rslt = input()
    if rslt == "<":
        return -1
    else:
        return 1


if n == 26:
    ans.sort(key=functools.cmp_to_key(compare))
    print("!", "".join(ans))
else:
    all_ = []
    for i in permutations(ans):
        all_.append(i)
    tmp = "ABCDE"
    while len(all_) > 1:
        new_all = []
        min_ = 1 << 32
        rslt = None
        # print(len(all_))
        # print(all_)
        for i in range(5):
            for j in range(i + 1, 5):
                cnt = 0
                for k in all_:
                    if k.index(tmp[i]) < k.index(tmp[j]):
                        cnt += 1
                if min_ > abs(cnt - len(all_) / 2):
                    min_ = abs(cnt - len(all_) / 2)
                    rslt = i, j
        i, j = rslt
        print(f"? {tmp[i]} {tmp[j]}")
        a = input()
        if a == "<":
            for k in all_:
                if k.index(tmp[i]) < k.index(tmp[j]):
                    new_all.append(k)
        else:
            for k in all_:
                if k.index(tmp[i]) > k.index(tmp[j]):
                    new_all.append(k)

        all_ = new_all

    print(f"! {''.join(all_[0])}")
