import sys


def main(lines: list[str]):
    s = lines[0]
    # i番目までで連続してj人が座っている場合の総数
    dp = [[0] * 3 for _ in range(len(s) + 1)]
    dp[0][0] = 1
    for i in range(len(s)):
        for j in range(3):
            # 最初から空席の場合
            if s[i] == "o":
                dp[i + 1][0] += dp[i][j]
            # 人がいる場合
            else:
                # 返す場合
                dp[i + 1][0] += dp[i][j]
                # 返さない場合
                if j != 2:
                    dp[i + 1][j + 1] = dp[i][j]
    # print(dp)
    print(sum(dp[-1]))


main([input()])
# if __name__ == "__main__":
#     lines = []
#     for l in sys.stdin:
#         lines.append(l.rstrip("\r\n"))
#     main(lines)
