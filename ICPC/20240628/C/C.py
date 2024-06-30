from collections import defaultdict


def solve(h, w, a):
    # a_n = []
    # free = 0
    # for i in range(h):
    #     for j in range(w):
    #         if a[i][j] == "#":
    #             a_n.append(1)
    #         else:
    #             free += 1
    #             a_n.append(0)
    # bit = 0
    # for i in range(h * w):
    #     if a[i]:
    #         bit |= 1 << i

    # dp = {bit: 1}
    # for _ in range(free // 3):
    #     new_dp = defaultdict(int)
    #     for k,v in dp.items():
    #         for i in range()

    L = [
        ([0, 0], [-1, 0], [0, -1]),
        ([0, 0], [1, 0], [0, -1]),
        ([0, 0], [-1, 0], [0, 1]),
        ([0, 0], [1, 0], [0, 1]),
    ]
    L_n = []
    # print(L)
    for i in L:
        # print(i)
        for j in range(3):
            new_i = [k[:] for k in i]
            # print(i[j])
            for k in range(3):
                new_i[k][0] -= i[j][0]
                new_i[k][1] -= i[j][1]

            L_n.append(new_i)
        # print(i, new_i)
    # print(L_n)

    def f(a):
        rslt = 0
        if sum(i.count(".") for i in a) == 0:
            return 1
        for i in range(h):
            for j in range(w):
                if a[i][j] == ".":
                    for tmp in L_n:
                        can_put = True
                        new_a = [i[:] for i in a]
                        for k, l in tmp:
                            if i + k in range(h) and j + l in range(w):
                                can_put &= a[i + k][j + l] == "."
                                new_a[i + k][j + l] = "#"
                            else:
                                can_put = False
                            if not can_put:
                                break
                        if can_put:
                            rslt += f(new_a)
                    return rslt

    return f(a)


ans = []
while 1:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    a = [list(input()) for _ in range(h)]
    ans.append(solve(h, w, a))

for i in ans:
    print(i)
