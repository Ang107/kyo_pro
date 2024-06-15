import sys
import math
from collections import Counter

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_idx = int(input())
nb_games = int(input())


def deb(x):
    sys.stderr.write(str(x))


ULDR = ["UP", "LEFT", "DOWN", "RIGHT"]


# スコアの正規化、マックスを1として正規化する
def evaluation_normarize(score):
    max_score = max(score)
    rslt = [0, 0, 0, 0]
    if max_score > 0:
        for i in range(4):
            rslt[i] = score[i] / max_score
    return rslt


# ハードル走
# 重要度は勝ちへの近さ？
def evaluation_0(gpu, reg_0, reg_1, reg_2, reg_3, reg_4, reg_5, reg_6):
    rslt = [0, 0, 0, 0]
    actions = [[2], [1], [1, 2], [1, 2, 3]]

    if reg_3 > 0:
        return rslt

    # stan状況でposにいる時に、actionという行動をとった後の実質位置の差分
    def f(gpu, pos, stan, action):
        if stan:
            return 0
        rslt = 0
        for i in actions[action]:
            if gpu[pos + i] == "#":
                rslt += j
                rslt -= 4
                return rslt
        return actions[action][-1]

    # 実質的なプレイヤーの位置、スタンは後退として扱う
    state = [reg_0 - 2 * reg_3, reg_1 - 2 * reg_4, reg_2 - 3 * reg_5]
    # プレイヤー1の手
    for i in range(4):
        # プレイヤー2の手
        for j in range(4):
            # プレイヤー3の手
            for k in range(4):
                new_state = state[:]
                new_state[0] += f(gpu, reg_0, reg_3, i)
                new_state[1] += f(gpu, reg_1, reg_4, j)
                new_state[2] += f(gpu, reg_2, reg_5, k)
                rslt[i] += new_state[0] * 2 - new_state[1] - new_state[2]
    return evaluation_normarize(rslt)



# アーチェリー
# 重要度はターン数？
#前半はとりあえず真ん中寄に寄せ解く
#後半は全探索して良さげな手を見つける
def evaluation_0(gpu, reg_0, reg_1, reg_2, reg_3, reg_4, reg_5, reg_6):
    rslt = [0, 0, 0, 0]


# それぞれの行動後の盤面の評価を返す
# 盤面自体の評価と、重要度
# 僅差、もしくは優勢であるほど価値が高く、既に大負けしている場合は価値は低い
# 種目ごとに均等に勝つのが良い
def evaluation(game_number, gpu, reg_0, reg_1, reg_2, reg_3, reg_4, reg_5, reg_6):
    pass


# game loop
while True:
    for i in range(3):
        score_info = input()
    co = Counter()
    for i in range(nb_games):
        inputs = input().split()
        gpu = inputs[0]
        reg_0 = int(inputs[1])
        reg_1 = int(inputs[2])
        reg_2 = int(inputs[3])
        reg_3 = int(inputs[4])
        reg_4 = int(inputs[5])
        reg_5 = int(inputs[6])
        reg_6 = int(inputs[7])
        if gpu == "GAME_OVER" or reg_3 > 0 or (reg_0 < reg_1 and reg_0 < reg_2):
            # print("RIGHT")
            continue
        added = False
        for j in range(1, 4):
            if reg_0 + j < 30 and gpu[reg_0 + j] == "#":
                co[j] += 1
                added = True
                break

    deb(co)
    if len(co) == 0:
        most = 4
    else:
        most = co.most_common(1)[0][0]
    deb(most)
    if most == 1:
        print("UP")
    elif most == 2:
        print("LEFT")
    elif most == 3:
        print("DOWN")
    else:
        print("RIGHT")
