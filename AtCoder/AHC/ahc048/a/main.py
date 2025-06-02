# ------------------------------------------------------------
# 1. 入力読み込み
# ------------------------------------------------------------
from math import sqrt, ceil
from copy import deepcopy

N, K, H, T, D = map(int, input().split())
tubes = [tuple(map(float, input().split())) for _ in range(K)]
targets = [tuple(map(float, input().split())) for _ in range(H)]


class State:
    def __init__(self, tube_index, amount, C, M, Y):
        self.amounts = [0] * K
        self.amounts[tube_index] += amount
        self.amount_sum = amount
        self.C = C
        self.M = M
        self.Y = Y

    def __str__(self):
        return f"{self.amount_sum=} {self.C=} {self.M=} {self.Y=} {self.amounts}"

    def add_paint(self, tube_index, amount, C, M, Y):
        if amount == 0:
            return
        self.amounts[tube_index] += amount
        self.C = (self.C * self.amount_sum + C * amount) / (self.amount_sum + amount)
        self.M = (self.M * self.amount_sum + M * amount) / (self.amount_sum + amount)
        self.Y = (self.Y * self.amount_sum + Y * amount) / (self.amount_sum + amount)
        self.amount_sum += amount

    def calc_error(self, C, M, Y):
        return sqrt((self.C - C) ** 2 + (self.M - M) ** 2 + (self.Y - Y) ** 2)

    def get_color_index(self, step):
        return (int(self.C // step), int(self.M // step), int(self.Y // step))

    def get_amount_sum_index(self, step):
        return int(self.amount_sum // step)

    def calc_need_paint(self, palette):
        res = 0
        for i in range(K):
            res += ceil(max(0, self.amounts[i] - palette[i]))
        return res

    def calc_cost(self, palette, C, M, Y):
        return D * (self.calc_need_paint(palette) - 1) + self.calc_error(C, M, Y) * 1000


def calc_coefficients(target, tubes, palette):
    # 絵具の量がiで色のベクトルが(j,k,l)のときのState
    color_step = 0.05
    color_cnt = int((1 // color_step)) + 1
    amount_max = 2
    amount_step = 0.05
    amount_cnt = int((amount_max // amount_step)) + 1
    dp: list[list[list[list[State | int]]]] = [
        [[[-1] * color_cnt for _ in range(color_cnt)] for _ in range(color_cnt)]
        for _ in range(amount_cnt)
    ]
    dp[0][0][0][0] = State(0, 0, 0, 0, 0)

    for i in range(K):
        for amount in reversed(range(amount_cnt)):
            for c in range(color_cnt):
                for m in range(color_cnt):
                    for y in range(color_cnt):
                        if type(dp[amount][c][m][y]) != State:
                            continue
                        for add_amount in range(amount_cnt):
                            new_state = deepcopy(dp[amount][c][m][y])
                            new_state.add_paint(i, add_amount * amount_step, *tubes[i])

                            amount_index = new_state.get_amount_sum_index(amount_step)
                            c_idx, m_idx, y_idx = new_state.get_color_index(color_step)

                            if amount_index < amount_cnt:
                                if type(dp[amount_index][c_idx][m_idx][y_idx]) != State:
                                    dp[amount_index][c_idx][m_idx][y_idx] = new_state
                                elif dp[amount_index][c_idx][m_idx][y_idx].calc_cost(
                                    palette, *target
                                ) > new_state.calc_cost(palette, *target):
                                    dp[amount_index][c_idx][m_idx][y_idx] = new_state
    res = -1
    min_cost = 1 << 60
    for amount in reversed(range(amount_cnt)):
        for c in range(color_cnt):
            for m in range(color_cnt):
                for y in range(color_cnt):
                    if type(dp[amount][c][m][y]) != State:
                        continue
                    if (
                        dp[amount][c][m][y].amount_sum >= 1
                        and dp[amount][c][m][y].calc_cost(palette, *target) < min_cost
                    ):
                        min_cost = dp[amount][c][m][y].calc_cost(palette, *target)
                        res = dp[amount][c][m][y]
    return res


def main():
    """
    縦に区切って各列に対して各チューブを割り当てる
    予め各列で量を調整し、必要な絵具は最上段のしきりを取ることで混ぜる
    """
    # パレットの各列の絵具残量
    palette = [0] * N
    for target in targets:
        state = calc_coefficients(target, tubes, palette)
        print(
            target,
            state,
            state.calc_error(*target) * 1000,
            (state.calc_need_paint(palette) - 1) * D,
        )


if __name__ == "__main__":
    main()
