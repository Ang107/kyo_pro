ans = []
while 1:
    n = int(input())
    if n == 0:
        break
    a, b, c, d = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(n + 1)]

    # x,yと毒無しエリアとの最短距離
    def f(x, y):
        result = 0
        if a <= x <= c:
            pass
        else:
            # print("debx", x, y, min(abs(x - a), abs(x - c)))
            result += min(abs(x - a), abs(x - c))
        if b <= y <= d:
            pass
        else:
            # print("deby", x, y, min(abs(y - b), abs(y - d)))

            result += min(abs(y - b), abs(y - d))
        return result

    result = 0
    for i in range(1, n + 1):
        prv_x, prv_y = xy[i - 1]
        now_x, now_y = xy[i]
        # 無し無し
        if (
            prv_x in range(a, c + 1)
            and prv_y in range(b, d + 1)
            and now_x in range(a, c + 1)
            and now_y in range(b, d + 1)
        ):
            pass
        # ありあり
        elif (prv_x not in range(a, c + 1) or prv_y not in range(b, d + 1)) and (
            now_x not in range(a, c + 1) or now_y not in range(b, d + 1)
        ):
            result += min(
                abs(prv_x - now_x) + abs(prv_y - now_y),
                f(prv_x, prv_y) + f(now_x, now_y) - 1,
            )
        # ありなし
        elif prv_x not in range(a, c + 1) or prv_y not in range(b, d + 1):
            result += f(prv_x, prv_y) - 1
        # なしあり
        elif now_x not in range(a, c + 1) or now_y not in range(b, d + 1):
            result += f(now_x, now_y)
        # ans.append(("t", result))
    ans.append(result)

for i in ans:
    print(i)
