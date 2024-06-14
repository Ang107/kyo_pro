import sys


def main(lines):
    # weight, height, target_bmi = map(int, lines[0].split())
    weight, height, target_bmi = lines
    for i in range(1, 101):
        if 10000 * i / (height**2) <= target_bmi:
            # BMIが目標BMI以下になる最大の体重
            target_weight = i
        else:
            break

    # 現在の身長・体重で目標BMIを達成している場合
    if target_weight >= weight:
        # print(0)
        return 0
    else:
        # print(weight - target_weight)
        return weight - target_weight


def main1(lines):
    w, h, b = lines
    return max(0, w - (b * h**2 // 10000))


import random

for _ in range(10**6):
    w = random.choice(range(20, 101))
    h = random.choice(range(100, 201))
    b = random.choice(range(10, 31))
    ans = main([w, h, b])
    ans1 = main1([w, h, b])
    print(ans, ans1)
    if ans != ans1:
        print("bug")
        exit()
    else:
        print("ok")

if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
