ans = []
while 1:
    N, M = map(int, input().split())
    if not N:
        break
    point_max = [0] * (N + 1)
    point_min = [0] * (N + 1)
    for _ in range(M):
        tmp = list(map(int, input().split()))
        s = int(tmp[0])
        k = tmp[2:]
        if len(k) == 1:
            point_min[k[0]] += s
        for i in k:
            point_max[int(i)] += s
    # print(point_max[1:])
    # print(point_min[1:])
    important_p = []
    max_ = 0
    tmp = sorted(zip(point_max[1:], point_min[1:]), key=lambda x: (-x[0], -x[1]))
    # print(tmp)
    mx = [i for i, j in tmp]
    mn = [j for i, j in tmp]

    # for i, j in zip(point_max[1:], point_min[1:]):
    #     if max_ < i:
    #         max_ = i
    #         important_p = [[i, j]]
    #     elif max_ == i:
    #         important_p.append([i, j])

    ans.append(mx[0] - min(mn[1:]) + 1)
for i in ans:
    print(i)
