import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n, d = MII()
xy = [LMII() for _ in range(n)]
ans = 0
x_list = [i for i, j in xy]
y_list = [j for i, j in xy]
x_list.sort()
y_list.sort()
x_l = [0]
for i in range(1, n):
    x_l.append(x_l[-1] + abs(x_list[i] - x_list[0]))
x_r = [0]
for i in reversed(range(n - 1)):
    x_r.append(x_r[-1] + abs(x_list[i] - x_list[-1]))
x_r = x_r[::-1]
y_l = [0]
for i in range(1, n):
    y_l.append(y_l[-1] + abs(y_list[i] - y_list[0]))
y_r = [0]
for i in reversed(range(n - 1)):
    y_r.append(y_r[-1] + abs(y_list[i] - y_list[-1]))
y_r = y_r[::-1]


def f(xy, num):
    if xy == "x":
        if num <= x_list[0]:
            return x_l[-1] + abs(x_list[0] - num) * n
        elif x_list[-1] <= num:
            return x_r[0] + abs(x_list[-1] - num) * n
        else:
            rslt = 0
            tmp = bisect_left(x_list, num)
            rslt += x_l[-1] - x_l[tmp - 1] - abs(x_list[0] - num) * (n - tmp)
            rslt += x_r[0] - x_r[tmp] - abs(x_list[-1] - num) * tmp
            return rslt
    else:
        if num <= y_list[0]:
            return y_l[-1] + abs(y_list[0] - num) * n
        elif y_list[-1] <= num:
            return y_r[0] + abs(y_list[-1] - num) * n
        else:
            rslt = 0
            tmp = bisect_left(y_list, num)
            rslt += y_l[-1] - y_l[tmp - 1] - abs(y_list[0] - num) * (n - tmp)
            rslt += y_r[0] - y_r[tmp] - abs(y_list[-1] - num) * tmp
            return rslt


memo_x = [-1] * (4 * 10**6 + 3)
for i in range(4 * 10**6 + 3):
    memo_x[i] = f("x", i - 2000001)
memo_y = [-1] * (4 * 10**6 + 3)
for i in range(4 * 10**6 + 3):
    memo_y[i] = f("y", i - 2000001)


def isOK(mid):
    return tmp + memo_y[mid + 2000001] <= d


def meguru(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    return ok


if n % 2 == 1:
    x_mean = x_list[n // 2]
    y_mean = y_list[n // 2]
else:
    x_mean = (x_list[n // 2] + x_list[n // 2 - 1]) // 2
    y_mean = (y_list[n // 2] + y_list[n // 2 - 1]) // 2


i = 0
prv1 = -2 * 10**6
prv2 = 2 * 10**6

while True:
    tmp = memo_x[x_mean + i + 2000001]
    if tmp + memo_y[y_mean + 2000001] <= d:
        tmp1 = meguru(prv1 - 1, y_mean)
        tmp2 = meguru(prv2 + 1, y_mean)
        prv1 = tmp1
        prv2 = tmp2
        ans += max(0, tmp2 - tmp1 + 1)
    else:
        break
    i += 1
i = -1
prv1 = -2 * 10**6
prv2 = 2 * 10**6
while True:
    tmp = memo_x[x_mean + i + 2000001]
    if tmp + memo_y[y_mean + 2000001] <= d:
        tmp1 = meguru(prv1 - 1, y_mean)
        tmp2 = meguru(prv2 + 1, y_mean)
        prv1 = tmp1
        prv2 = tmp2
        ans += max(0, tmp2 - tmp1 + 1)

    else:
        break
    i -= 1
print(ans)
