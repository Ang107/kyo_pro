import random

tmp = list(range(25))
ans = 10**18
while True:
    # ランダム生成
    random.shuffle(tmp)

    # 配置
    b = [[None] * 5 for _ in range(5)]
    for i in range(25):
        b[i // 5][i % 5] = tmp[i]
    ans_n = 0

    # コストの計算
    for i in range(3):
        for j in range(2):
            ans_n += (b[i][j] - b[i][j + 1]) ** 2
    for i in range(2):
        for j in range(3):
            ans_n += (b[i][j] - b[i + 1][j]) ** 2

    if ans > ans_n:
        ans = ans_n
        for i in b:
            print(*i)
        print(ans)
