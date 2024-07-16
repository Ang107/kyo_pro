from collections import defaultdict
from bisect import bisect_left, bisect_right


def f(xyi, cx, cy, rt, rd):
    x, y, i = xyi
    rt[y - x].remove(xyi)
    rd[y + x].remove(xyi)

    visited = defaultdict(lambda: False)
    v = 0
    # print(x, y)
    rslt = False
    while True:
        if v == 0:
            h = b - y
            w = a - x
            tmp = bisect_right(rt[y - x], (x, y, 0))

            if tmp < len(rt[y - x]):
                # print(x, y, v)
                # print(y - x == cy - cx and x < cx < rt[y - x][tmp][0])
                if y - x == cy - cx and x < cx < rt[y - x][tmp][0]:
                    rslt = True
                    break
                else:
                    break
            else:
                if y - x == cy - cx and x < cx:
                    rslt = True
                    break

            if h == w:
                break
            elif h < w:
                x += h
                y = b
                v = 3
            elif h > w:
                y += w
                x = a
                v = 1

            if visited[(x, y, v)]:
                break
            else:
                visited[(x, y, v)] = True

        elif v == 1:
            h = b - y
            w = x
            tmp = bisect_left(rd[y + x], (x, y, 0))
            if tmp > 0:
                # print(x, y, v)
                # print(y + x == cy + cx and rd[y + x][tmp - 1][0] < cx < x)
                if y + x == cy + cx and rd[y + x][tmp - 1][0] < cx < x:
                    rslt = True
                    break
                else:
                    break
            else:
                if y + x == cy + cx and cx < x:
                    rslt = True
                    break

            if h == w:
                break
            elif h < w:
                x -= h
                y = b
                v = 2
            elif h > w:
                y += w
                x = 0
                v = 0
            if visited[(x, y, v)]:
                break
            else:
                visited[(x, y, v)] = True

        elif v == 2:
            h = y
            w = x
            tmp = bisect_left(rt[y - x], (x, y, 0))
            if tmp > 0:
                # print(x, y, v)
                # print(y - x == cy - cx and rt[y - x][tmp - 1][0] < cx < x)
                if y - x == cy - cx and rt[y - x][tmp - 1][0] < cx < x:
                    rslt = True
                    break
                else:
                    break
            else:
                if y - x == cy - cx and cx < x:
                    rslt = True
                    break

            if h == w:
                break
            elif h < w:
                x -= h
                y = 0
                v = 1
            elif h > w:
                y -= w
                x = 0
                v = 3
            if visited[(x, y, v)]:
                break
            else:
                visited[(x, y, v)] = True

        elif v == 3:
            h = y
            w = a - x
            tmp = bisect_right(rd[y + x], (x, y, 0))
            if tmp < len(rd[y + x]):
                # print(x, y, v)
                # print(y + x == cy + cx and x < cx < rd[y + x][tmp][0])
                if y + x == cy + cx and x < cx < rd[y + x][tmp][0]:
                    rslt = True
                    break
                else:
                    break
            else:
                if y + x == cy + cx and x < cx:
                    rslt = True
                    break

            if h == w:
                break
            elif h < w:
                x += h
                y = 0
                v = 0
            elif h > w:
                y -= w
                x = a
                v = 2

            if visited[(x, y, v)]:
                break
            else:
                visited[(x, y, v)] = True
    x, y, i = xyi
    rt[y - x].append(xyi)
    rd[y + x].append(xyi)
    rt[y - x].sort()
    rd[y + x].sort()
    return rslt


def solve(a, b, cx, cy, n, xy):
    rt = defaultdict(list)
    rd = defaultdict(list)
    for i, (x, y) in enumerate(xy):
        rt[y - x].append((x, y, i))
        rd[x + y].append((x, y, i))
    ans = set()
    for i in rt:
        rt[i].sort()
    for i in rd:
        rd[i].sort()
    vec = ((1, 1), (-1, 1), (-1, -1), (1, -1))
    for i in range(4):
        visited = defaultdict(lambda: False)
        x, y = cx, cy
        v = i
        ball = None
        while True:
            if v == 0:
                h = b - y
                w = a - x
                tmp = bisect_left(rt[y - x], (x, y, 0))
                if tmp < len(rt[y - x]):
                    if f(rt[y - x][tmp], cx, cy, rt, rd):
                        ball = rt[y - x][tmp]
                        break
                    else:
                        break

                if h == w:
                    break
                elif h < w:
                    x += h
                    y = b
                    v = 3
                elif h > w:
                    y += w
                    x = a
                    v = 1

                if visited[(x, y, v)]:
                    break
                else:
                    visited[(x, y, v)] = True

            elif v == 1:
                h = b - y
                w = x
                tmp = bisect_left(rd[y + x], (x, y, 0))
                if tmp > 0:
                    if f(rd[y + x][tmp - 1], cx, cy, rt, rd):
                        ball = rd[y + x][tmp - 1]
                        break
                    else:
                        break

                if h == w:
                    break
                elif h < w:
                    x -= h
                    y = b
                    v = 2
                elif h > w:
                    y += w
                    x = 0
                    v = 0
                if visited[(x, y, v)]:
                    break
                else:
                    visited[(x, y, v)] = True

            elif v == 2:
                h = y
                w = x
                tmp = bisect_left(rt[y - x], (x, y, 0))
                if tmp > 0:
                    if f(rt[y - x][tmp - 1], cx, cy, rt, rd):
                        ball = rt[y - x][tmp - 1]
                        break
                    else:
                        break

                if h == w:
                    break
                elif h < w:
                    x -= h
                    y = 0
                    v = 1
                elif h > w:
                    y -= w
                    x = 0
                    v = 3
                if visited[(x, y, v)]:
                    break
                else:
                    visited[(x, y, v)] = True

            elif v == 3:
                h = y
                w = a - x
                tmp = bisect_left(rd[y + x], (x, y, 0))

                if tmp < len(rd[y + x]):
                    if f(rd[y + x][tmp], cx, cy, rt, rd):
                        ball = rd[y + x][tmp]
                        break
                    else:
                        break

                if h == w:
                    break
                elif h < w:
                    x += h
                    y = 0
                    v = 0
                elif h > w:
                    y -= w
                    x = a
                    v = 2

                if visited[(x, y, v)]:
                    break
                else:
                    visited[(x, y, v)] = True
        if ball:
            ans.add(ball[2] + 1)
        # print(i, ball)
    return sorted(ans)
    pass


ans = []
while 1:
    a, b, x, y, n = map(int, input().split())
    if a == b == x == y == n == 0:
        break
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans.append(solve(a, b, x, y, n, xy))

for i in ans:
    if i:
        print(*i)
    else:
        print("No")
