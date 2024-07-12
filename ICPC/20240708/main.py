n = int(input())
c = list(map(int, input().split()))
ans1 = [[0] * (n // 2) for _ in range(n // 2)]
print(c[: n // 2], c[-(n // 2) :])
if set(c[: n // 2]) != set(c[-(n // 2) :]):
    print("No")
else:
    print("Yes")
    for i in range(n // 2):
        for j in range(n // 2):
            if c[i] == c[-j - 1]:
                ans1[i][j] = c[i]

    # 90度右回転させたリストを返す
    def list_rotate_R90(l):
        return list(zip(*l[::-1]))

    ans2 = list_rotate_R90(ans1)
    ans3 = list_rotate_R90(ans2)
    ans4 = list_rotate_R90(ans3)
    ans = [[0] * n for _ in range(n)]
    if n % 2 == 0:
        for i in range(n):
            for j in range(n):
                if i < n // 2:
                    if j < n // 2:
                        ans[i][j] = ans1[i][j]
                    else:
                        ans[i][j] = ans2[i][j - n // 2]

                else:
                    if j < n // 2:
                        ans[i][j] = ans4[i - n // 2][j]
                    else:
                        ans[i][j] = ans3[i - n // 2][j - n // 2]

    for i in ans:
        print(*i)

    # 90度左回転させたリストを返す
    def list_rotate_L90(l):
        return (list(zip(*l)))[::-1]
