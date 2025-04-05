Input = [
    21,
    -300,
    800,
    -200,
    800,
    -100,
    800,
    0,
    800,
    100,
    800,
    200,
    800,
    300,
    800,
    -300,
    900,
    -200,
    900,
    -100,
    900,
    0,
    900,
    100,
    900,
    200,
    900,
    300,
    900,
    -300,
    1000,
    -200,
    1000,
    -100,
    1000,
    0,
    1000,
    100,
    1000,
    200,
    1000,
    300,
    1000,
]

g = 9.807

import math

sd = [
    1040,
    1030,
    1015,
    1000,
    987.5,
    975,
    962.5,
    950,
    937.5,
    925,
    912.5,
    903,
    894,
    883.4,
    866.8,
    850.2,
    833.6,
    817,
    808,
    799,
    790,
]


def plot(n, xy):
    ans = [[1, 5000, 0, 0, 2000] for _ in range(21)]
    xy = [(i + 1, x, y) for i, (x, y) in enumerate(xy)]
    xy.sort(key=lambda x: (x[2], abs(x[1])), reverse=True)

    for i in range(n):
        t, x, y = xy[i]
        sita = math.degrees(math.atan(x / y))
        d = (x**2 + y**2) ** 0.5
        diff = d - sd[i]
        ans[i][0] = t
        ans[i][1] = int(30000 + (diff * 1000 // 21))
        ans[i][2] = int(sita * 1000)
        ans[i][3] = 1

    for i in range(21):
        if i == 20:
            print(",".join(map(str, ans[i])), end=";\n")
        else:
            print(",".join(map(str, ans[i])))


n = Input[0]
xy = []
a = Input[1:]
for j in range(0, 2 * n, 2):
    tmp = (a[j], a[j + 1])
    xy.append(tmp)
plot(n, xy)
