# def get_S(h, w):
#     SMS = SortedMultiset()

#     amari = len(h) * len(w) - N != 0
#     tmp = 0
#     for idx_h, i in enumerate(h):
#         for idx_w, j in enumerate(w):
#             if idx_h == len(h) - 1 and len(w) - amari <= idx_w:
#                 tmp += i * j
#             else:
#                 SMS.add(i * j)
#     if tmp != 0:
#         SMS.add(tmp)
#     return SMS


# def get_Bunkatu(N):
#     tmp = [
#         (2, 3),
#         (2, 3),
#         (3, 3),
#         (3, 3),
#         (3, 3),
#         (3, 4),
#         (3, 4),
#         (3, 4),
#         (4, 4),
#         (4, 4),
#         (4, 4),
#         (4, 4),
#         (4, 5),
#         (4, 5),
#         (4, 5),
#         (4, 5),
#         (5, 5),
#         (5, 5),
#         (5, 5),
#         (5, 5),
#         (5, 5),
#         (5, 6),
#         (5, 6),
#         (5, 6),
#         (5, 6),
#         (5, 6),
#         (6, 6),
#         (6, 6),
#         (6, 6),
#         (6, 6),
#         (6, 6),
#         (6, 6),
#         (6, 7),
#         (6, 7),
#         (6, 7),
#         (6, 7),
#         (6, 7),
#         (6, 7),
#         (7, 7),
#         (7, 7),
#         (7, 7),
#         (7, 7),
#         (7, 7),
#         (7, 7),
#         (7, 7),
#         (7, 8),
#     ]
#     # for i in range(45):
#     #     print(i + 5, tmp[i][0] * tmp[i][1])
#     return tmp[N - 5]


# def get_cost(h, w, idx):
#     SMS = get_S(h, w)
#     cost = 0
#     # print(len(SMS))
#     for i in range(N):
#         # print(SMS)
#         s = A[idx * N + i][1]
#         tmp = SMS.ge(s)
#         if tmp == None:
#             cost += s - SMS.pop(-1)
#         else:
#             SMS.discard(tmp)
#     return cost


# def yamanobori(h, w, idx):
#     cost = get_cost(h, w, idx)

#     t = time.perf_counter()
#     while cost != 0:
#         # h.sort()
#         # w.sort()
#         h_w = random.choice([0, 1])
#         if h_w == 0:
#             give = random.choice(range(len(h)))
#             take = random.choice(range(len(h)))
#             num = random.choice(range(h[give] // 2))
#             # print(give, take, h[take], h[give], num)
#             h[give] -= num
#             h[take] += num
#         elif h_w == 1:
#             give = random.choice(range(len(w)))
#             take = random.choice(range(len(w)))
#             num = random.choice(range(w[give] // 2))
#             # print(give, take, w[take], w[give], num)

#             w[give] -= num
#             w[take] += num

#         new_cost = get_cost(h, w, idx)

#         if cost > new_cost:
#             cost = new_cost
#         else:
#             if h_w == 0:
#                 h[give] += num
#                 h[take] -= num
#             elif h_w == 1:
#                 w[give] += num
#                 w[take] -= num
#         print(cost)
#     print(h, w)


# def get_h_w(h_num, w_num):
#     h = [0] * h_num
#     w = [0] * w_num
#     for i in range(h_num):
#         if i == 0:
#             h[i] = 1000 // h_num + 1000 % h_num
#         else:
#             h[i] = 1000 // h_num

#     for i in range(w_num):
#         if i == 0:
#             w[i] = 1000 // w_num + 1000 % w_num
#         else:
#             w[i] = 1000 // w_num

#     return h, w


# 入力
import math


def Input():
    global W, D, N, A, h, hight
    W, D, N = map(int, input().split())
    h_num = math.ceil(N**0.5)
    w_num = -(-N / h_num)
    A = []
    avr = [0] * h_num
    for _ in range(D):
        tmp = list(map(int, input().split()))[::-1]
        for i in range(N):
            avr[int(i // w_num)] += tmp[i]
        # rslt.append(1000**2 - sum(tmp))
        # tmp = [[i, j] for i, j in enumerate(tmp)]
        A.append(tmp)
    h = []
    avr_sum = sum(avr)
    for i in avr[:-2]:
        h.append(1000 * i // avr_sum)
    h.append(1000 - sum(h))
    hight = [0]
    for i in h:
        hight.append(hight[-1] + i)
    # print(hight)
    # print(h)
    # print(rslt)


def put(A):
    w = [0] * len(h)
    rslt = []
    for i in A:
        puted = False
        for j in range(len(h)):
            width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = True
                rslt.append([hight[j], w[j], hight[j + 1], w[j] + width])
                w[j] += width
                break
        if not puted:
            s = 0
            for j in range(len(h)):
                width = -(-i // h[j])
                if width * i > s:
                    s = width * i
                    tmp = [hight[j], w[j], hight[j + 1], min(1000, w[j] + width)]
            rslt.append(tmp)
    return rslt[::-1]


def solve():
    ans = []
    for i in A:
        ans.append(put(i))
    return ans


def Output(ans):
    for i in ans:
        for j in i:
            print(*j)


def main():
    # 方針1NG
    # エリアをN個の区画に分ける
    # 縦横グリッド上に分けるので、分け目の座標を焼きなます
    # 方針2
    # 良い感じに縦の分割を固定
    # 横のみの変更
    Input()
    ans = solve()
    Output(ans)
    pass


if __name__ == "__main__":
    import time

    main()
