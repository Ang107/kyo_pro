def solve1(n, m, s):
    ans = 0
    if m == 1:
        for i in range(n):
            ans = max(ans, sum([s[i][0], s[i][1], s[i][2]]))
    elif m == 2:
        s_vi = sorted(s, reverse=True, key=lambda x: x[0])
        s_d = sorted(s, reverse=True, key=lambda x: x[1])
        s_vo = sorted(s, reverse=True, key=lambda x: x[2])
        for i in range(n):
            ans = max(
                ans,
                max(s_vi[0][0], s_d[i][0])
                + max(s_vi[0][1], s_d[i][1])
                + max(s_vi[0][2], s_d[i][2]),
            )
        for i in range(n):
            ans = max(
                ans,
                max(s_d[0][0], s_vi[i][0])
                + max(s_d[0][1], s_vi[i][1])
                + max(s_d[0][2], s_vi[i][2]),
            )
        for i in range(n):
            ans = max(
                ans,
                max(s_vo[0][0], s_d[i][0])
                + max(s_vo[0][1], s_d[i][1])
                + max(s_vo[0][2], s_d[i][2]),
            )
    else:
        ma, mb, mc = 0, 0, 0
        for i in range(n):
            ma = max(ma, s[i][0])
            mb = max(mb, s[i][1])
            mc = max(mc, s[i][2])
        ans = ma + mb + mc
    return ans


def solve2(N, M, ABC):
    # 入力

    if M == 1:
        # 一人の場合は各アイドルの Vi + Da + Vo の最大値が答えとなる。
        ans = -1
        for abc in ABC:
            ans = max(ans, sum(abc))
    elif M == 2:
        max_status = [0] * (1 << 3)
        for mask in range(1 << 3):
            for abc in ABC:
                tmp = 0
                for i in range(3):
                    if mask >> i & 1:
                        tmp += abc[i]
                max_status[mask] = max(max_status[mask], tmp)
        ans = -1
        for mask in range(1 << 3):
            ans = max(ans, max_status[mask] + max_status[7 - mask])
    else:
        # 3人以上選べる場合、Vi、Da、Voそれぞれの最大値を持つ人を全員採用することができる
        A = []
        B = []
        C = []
        for a, b, c in ABC:
            A.append(a)
            B.append(b)
            C.append(c)
        ans = max(A) + max(B) + max(C)
    return ans


import random

while True:
    n = random.randrange(2, 100)
    m = 2
    abc = [
        [random.randrange(1, 100), random.randrange(1, 100), random.randrange(1, 100)]
        for _ in range(n)
    ]
    if solve1(n, m, abc) != solve2(n, m, abc):
        print(n, m)
        print(abc)
        exit()
    else:
        print("OK")
