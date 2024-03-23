# 入力
import time

start = time.perf_counter()
import random


def Input():
    W, D, N = map(int, input().split())
    A = []
    for _ in range(D):
        tmp = list(map(int, input().split()))[::-1]
        A.append(tmp)
    return W, D, N, A


# その日のエリア配置
def put(a, h, hight):
    w = [0] * len(h)
    rslt = []
    cost = 1000 * (len(h) - 1)
    for i in a:
        puted = False
        for j in range(len(h)):
            width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = True
                rslt.append([hight[j], w[j], hight[j + 1], w[j] + width])
                w[j] += width
                cost += h[j]
                break
        if not puted:
            s = 0
            tmp = None
            for j in range(len(h)):
                width = min(1000 - w[j], -(-i // h[j]))
                if width * i > s:
                    s = width * i
                    tmp = (
                        j,
                        width,
                        [hight[j], w[j], hight[j + 1], min(1000, w[j] + width)],
                    )
            if tmp == None:
                rslt[-1][3] -= (rslt[-1][3] - rslt[-1][1]) // 2
                cost += 100 * (i - (1000 - rslt[-1][3]) * (rslt[-1][2] - rslt[-1][0]))
                cost += rslt[-1][2] - rslt[-1][0]
                rs = rslt[-1][:]
                rs[1], rs[3] = rs[3], 1000
                rslt.append(rs)
            else:
                idx, width, rs = tmp
                cost += 100 * (i - width * h[idx])
                cost += h[idx]
                w[idx] = 1000
                rslt.append(rs)

    return rslt[::-1], cost


# 渡されたhで配置した場合のコストと答えの取得
def get_ans(A, h, hight):
    ans = []
    cost = 0
    for i in A:
        rslt, c = put(i, h, hight)
        ans.append(rslt)
        cost += c
    return ans, cost


# 出力
def Output(ans):
    for i in ans:
        for j in i:
            print(*j)


# 指定された時間、hを元に山登りする
def yamanobori(A, h, time_limit):
    cnt = 0
    lh = len(h)
    hight = [0] * (lh + 1)
    for i, j in enumerate(h):
        hight[i + 1] = hight[i] + j
    ans, cost = get_ans(A, h, hight)
    if len(h) == 1:
        return ans, cost
    while True:
        give_idx, take_idx = random.choice(range(lh)), random.choice(range(lh))
        if give_idx == take_idx:
            continue

        h_n = h[:]
        num = random.choice(range(h[give_idx] // 2))
        h_n[give_idx] -= num
        h_n[take_idx] += num
        h_n.sort(reverse=True)

        hight_n = [0] * (lh + 1)
        for i, j in enumerate(h_n):
            hight_n[i + 1] = hight_n[i] + j

        ans_n, cost_n = get_ans(A, h_n, hight_n)
        if cost_n < cost:
            # print(hight, hight_n, cost, cost_n, cnt)
            h = h_n
            hight = hight_n
            cost = cost_n
            ans = ans_n

        cnt += 1

        if cnt % 100 == 0:
            if time.perf_counter() - start > time_limit:
                return ans, cost


# hの個数をプラマイ一個で山登りを呼び出す
def solve(W, D, N, A):
    h_num = int(N**0.5)
    time_limit = [1, 1.9, 2.9]
    cost = 10**18

    # 初期解生成
    w_num = -(-N / 1)
    avr = [0] * 1
    for tmp in A:
        tmp = tmp[::-1]
        for j in range(N):
            avr[int(j // w_num)] += tmp[j]

    h = []
    avr = [int(i**0.5) for i in avr]
    avr_sum = sum(avr)
    for j in avr[:-1]:
        h.append(1000 * j // avr_sum)
    h.append(1000 - sum(h))

    ans_n, cost_n = yamanobori(A, h, 0)
    # print(cost_n)
    if cost > cost_n:
        ans = ans_n
        cost = cost_n

    for i in range(3):
        # 初期解生成
        h_num_n = h_num + i - 1
        w_num = -(-N / h_num_n)
        avr = [0] * h_num_n
        for tmp in A:
            tmp = tmp[::-1]
            for j in range(N):
                avr[int(j // w_num)] += tmp[j]

        h = []
        avr = [int(i**0.5) for i in avr]
        avr_sum = sum(avr)
        for j in avr[:-1]:
            h.append(1000 * j // avr_sum)
        h.append(1000 - sum(h))

        ans_n, cost_n = yamanobori(A, h, time_limit[i])
        # print(cost_n)
        if cost > cost_n:
            ans = ans_n
            cost = cost_n

    return ans


def main():
    # 方針1
    # 縦の分割数をいくつか決めて、それぞれで幅を山登りする
    # その過程で得られたスコアが最も良いものを答えにする

    # TODO
    # 現在では日にちを跨いで柵を使いまわすようなことを考慮していない

    W, D, N, A = Input()
    ans = solve(W, D, N, A)
    Output(ans)
    pass


if __name__ == "__main__":
    main()
