ans = []
while 1:
    h, w = map(int, input().split())
    if h == 0:
        break
    v = [list(map(int, input())) for _ in range(h)]
    sum_v = sum(sum(i) for i in v)
    tmp = 0
    for idx, i in enumerate(v):
        tmp += sum(i) * (idx + 1)
    # print("r", tmp)
    r = tmp / sum_v
    tmp = 0
    v_tenti = list(zip(*v))
    # print(v_tenti)
    for idx, i in enumerate(v_tenti):
        tmp += sum(i) * (idx + 1)
    # print("c", tmp)

    c = tmp / sum_v
    ans.append((r, c))

for i in ans:
    print(*i)
