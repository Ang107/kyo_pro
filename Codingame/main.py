import sys
import math
from collections import Counter

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_idx = int(input())
nb_games = int(input())


def deb(x):
    sys.stderr.write(str(x))


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
        if not added:
            co[4] += 1
    most = co.most_common(1)
    if most[0] == 1:
        print("UP")
    elif most[0] == 2:
        print("LEFT")
    elif most[0] == 3:
        print("DOWN")
    else:
        print("RIGHT")

    # deb((reg_0,reg_1,reg_2,reg_3,reg_4,reg_5))

    # if reg_0 == 0:
    #     idx = 0
    #     ans = []
    #     i = 0
    #     while i < 30:
    #         if i+1 < len(gpu) and gpu[i+1] == "#":
    #             ans.append("UP")
    #             i += 2
    #         elif i+2 < len(gpu) and gpu[i+2] == "#":
    #             ans.append("LEFT")
    #             i += 1
    #         elif i+3 < len(gpu) and gpu[i+3] == "#":
    #             ans.append("DOWN")
    #             i += 2
    #         else:
    #             ans.append("RIGHT")
    #             i += 3
    #     deb(len(gpu))
    #     deb(ans)
    #     deb(gpu)
    # deb((len(ans),idx))
    # print(ans[idx])
    # idx += 1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # print("LEFT")
