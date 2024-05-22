from collections import deque, defaultdict

# 初期カードの配置：5つの山それぞれに5枚のカード
decks = [list(map(int, input().split())) for i in range(5)]
# 手札の初期状態
first_hand = [decks[i][0] for i in range(5)]


def get_hand_num(hand):
    hand = set(hand)
    rslt = 0
    for i in range(5):
        cnt_flag = False
        for j in range(5):
            if i * 5 + j in hand:
                if cnt_flag:
                    rslt += 1
            else:
                cnt_flag = True
    return rslt


print(4 * 5**0 + 4 * 5**1 + 4 * 5**2 + 4 * 5**3 + 4 * 5**4)
# 状態iからスタートした場合の手札の枚数の最大値
dp = [25] * 3125
dp[0] = 0
# 山の残り枚数の状況がiの時に引くべき山の番号
best_move = [-1] * 3125

for v in range(1, 3125):
    # 遷移先とのmin
    best = -1

    v_n = v
    tmp = []
    for i in [4, 3, 2, 1, 0]:
        j = v_n // 5**i
        v_n = v_n % 5**i
        tmp.append(j)
        if j > 0:
            if dp[v] > dp[v - 5**i]:
                dp[v] = min(dp[v], dp[v - 5**i])
                best = i

    tmp = tmp[::-1]
    print(v, tmp)
    # 自分とのmax
    # ハンドを再現
    hand = first_hand[:]
    hand.extend(decks[0][1 : 5 - tmp[0]])
    hand.extend(decks[1][1 : 5 - tmp[1]])
    hand.extend(decks[2][1 : 5 - tmp[2]])
    hand.extend(decks[3][1 : 5 - tmp[3]])
    hand.extend(decks[4][1 : 5 - tmp[4]])
    dp[v] = max(dp[v], get_hand_num(hand))
    best_move[v] = best


print(dp)
print(best_move)


# n = int(input())
# decks = [list(map(int, input().split())) for i in range(5)]
# ans = 4 * 25
# for i in range(5):
#     for j in range(5):
#         ans += abs(decks[i][j] // 5 - i)
# print("理論値", ans, ans / 5)
