import time

start = time.perf_counter()
import random
from collections import defaultdict


# hの長さの分散小さくしたやつ
def Input():
    W, D, N = map(int, input().split())
    A = []
    for _ in range(D):
        tmp = list(map(int, input().split()))
        A.append(tmp)

    # 余りの面積の割合(%)
    avr_amari = sum([1000000 - sum(i) for i in A]) / D / 10000
    max_amari = max([1000000 - sum(i) for i in A])
    # print(avr_amari)
    # exit()
    return W, D, N, A, avr_amari, max_amari


# その日のエリア配置
def put(a, h, hight):
    isover = False
    w = [0] * len(h)
    rslt = []
    cost = 0
    for i in a[::-1]:
        puted = False
        Hi = 10**18
        for j in range(len(h)):
            width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = True
                hi = max(width, h[j]) / min(width, h[j])
                if Hi > hi:
                    Hi = hi
                    rs = j, width, [hight[j], w[j], hight[j + 1], w[j] + width]

                    # rslt.append()
                    # w[j] += width
                    # cost += h[j]
        # 配置可能な場合
        if puted:
            j, width, tmp = rs
            w[j] += width
            cost += h[j]
            rslt.append(tmp)
        # 収まらない場合
        else:
            isover = True
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
            # スペースが０の場合
            if tmp == None:
                tmp = 1
                while rslt[-tmp][3] - rslt[-tmp][1] < 2:
                    tmp += 1

                rslt[-tmp][3] = rslt[-tmp][1] + 1
                cost += 1000 * (
                    i - (1000 - rslt[-tmp][3]) * (rslt[-tmp][2] - rslt[-tmp][0])
                )
                cost += 1000 * (
                    (1000 - rslt[-tmp][3]) * (rslt[-tmp][2] - rslt[-tmp][0])
                )
                cost += rslt[-tmp][2] - rslt[-tmp][0]

                rs = rslt[-tmp][:]
                rs[1], rs[3] = rs[3], 1000
                rslt.append(rs)
            # スペースが存在する場合
            else:
                idx, width, rs = tmp
                cost += 1000 * (i - width * h[idx])
                cost += h[idx]
                w[idx] = 1000
                rslt.append(rs)
    cost -= 1000
    for i in range(len(w) - 1):
        if w[i] == 0 and w[i + 1] == 0:
            cost += 1000

    return rslt[::-1], cost, isover


# 渡されたhで配置した場合のコストと答えの取得
def get_ans(A, h, hight):
    ans = []
    cost = 0
    over = []
    for idx, i in enumerate(A):
        rslt, c, is_over = put(i, h, hight)
        ans.append(rslt)
        cost += c
        if is_over:
            over.append(idx)

    return ans, cost, over


# 出力
def Output(ans):

    for i in ans:
        for j in i:
            print(*j)


def most_rihgt_line_change(ans):

    d = defaultdict(int)
    d_idx = {}
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if d[(i, ans[i][j][0])] < ans[i][j][3]:
                d[(i, ans[i][j][0])] = ans[i][j][3]
                d_idx[(i, ans[i][j][0])] = (i, j)

    # print(d_idx)
    for i, j in d_idx.values():
        ans[i][j][3] = 1000


# 指定された時間、hを元に山登りする
def yamanobori(A, h, time_limit):
    cnt = 0
    lh = len(h)
    hight = [0] * (lh + 1)
    for i, j in enumerate(h):
        hight[i + 1] = hight[i] + j
    ans, cost, over = get_ans(A, h, hight)
    if len(h) == 1:
        return ans, cost, over, h, hight

    cost = 10**18
    bunsan = 10**18
    avr = 1000 / len(h)
    tmp_time = time.perf_counter()

    not_over_got = False
    while True:
        give_idx, take_idx = random.choice(range(lh)), random.choice(range(lh))
        if give_idx == take_idx:
            continue

        h_n = h[:]
        num = random.choice(range(h[give_idx] // 4))
        h_n[give_idx] -= num
        h_n[take_idx] += num

        hight_n = [0] * (lh + 1)
        for i, j in enumerate(h_n):
            hight_n[i + 1] = hight_n[i] + j

        ans_n, cost_n, over_n = get_ans(A, h_n, hight_n)

        # print(over_n, len(h))
        if len(over_n) == 0:
            not_over_got = True

        if cost_n < cost:
            if not_over_got:
                bunsan_n = sum([(i - avr) ** 2 for i in h_n])
                if bunsan_n < bunsan:
                    # print(cost_n)
                    bunsan = bunsan_n
                    h = h_n
                    hight = hight_n
                    cost = cost_n
                    ans = ans_n
                    over = over_n
            else:
                # print(cost_n)
                h = h_n
                hight = hight_n
                cost = cost_n
                ans = ans_n
                over = over_n

        cnt += 1

        if cnt % 100 == 0:
            if time.perf_counter() - tmp_time > time_limit:
                print(cnt)
                return ans, cost, over, h, hight


# hの個数をプラマイ一個で山登りを呼び出す
def solve(W, D, N, A):

    h_num = int((N**0.5) * 1.75)
    # time_limit = [1.2]
    cost = 10**18

    # 初期解生成
    # 縦のみの保険用
    h = [1000]
    ans_hoken, _, over_hoken, _, _ = yamanobori(A, h, 0)

    l = int(N**0.5) - 1
    if max_amari < 20:
        r = N
    else:
        r = -(-N // 2) + 1
    while r - l > 1:
        # 初期解生成
        h_num_n = (l + r) // 2
        w_num = -(-N / h_num_n)
        avr = [0] * h_num_n
        for tmp in A:
            for j in range(N):
                avr[int(j // w_num)] += tmp[j]

        h = []
        avr = [int(i**0.25) for i in avr]
        avr_sum = sum(avr)
        for j in avr[:-1]:
            h.append(1000 * j // avr_sum)
        h.append(1000 - sum(h))

        # print(h)
        ans_n, cost_n, over_n, h_n, hight_n = yamanobori(A, h, 0.4)
        # print(l, r, len(h), over_n, cost_n, over_n, h_n, hight_n)
        if len(over_n) > 0:
            r = h_num_n
        else:
            l = h_num_n
        if cost > cost_n:
            ans = ans_n
            cost = cost_n
            over = over_n
            rs_h = h_n
            rs_hight = hight_n

    over_hoken = set(over_hoken)
    over = set(over)
    for i in over:
        if i not in over_hoken:
            ans[i] = ans_hoken[i]

    return ans, ans_hoken, rs_h, rs_hight, over, over_hoken


def change_ans_v2(A, h, hight, ans, over, Mode, test, A_tenti):
    # Output(ans)
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    if len(over) > 0:
        return [-100, -100]
    # 区間加算・区間最大値取得^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    op = lambda a, b: max(a, b)
    e = -1

    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ST = [SegTree(op, e, A_tenti[i]) for i in range(len(A_tenti))]
    more_good = [0, 0]
    Mode = [-1, -1]
    for mode in Mode:

        if mode == 1:
            Idx_l = 0
            Idx_r = 2
        elif mode == -1:
            Idx_l = len(A) - 2
            Idx_r = len(A)

        prv_len_same = 0
        prv_same = []

        while True:
            same = []
            idx = len(A[0]) - 1

            # print(len(same), same, mode, idx, Idx_l, Idx_r)
            # 現在見ている区間で最大値を取る操作の最大可能個数
            while idx >= 0:
                same.append(ST[idx].prod(Idx_l, Idx_r))

                if all(
                    [is_OK_v2(same, A[i], h, hight)[0] for i in range(Idx_l, Idx_r)]
                ):
                    idx -= 1
                else:
                    same.pop()
                    break

            # print(Idx_l, Idx_r, same, mode)

            if len(same) > len(A[0]) / 2:
                # print("zokkou")

                prv_len_same = len(same)
                prv_same = same

                if mode == 1:
                    Idx_r += 1
                else:
                    Idx_l -= 1

                if Idx_r > len(ans) or Idx_l < 0:
                    # print(Idx_l, Idx_r, prv_len_same)
                    if mode == 1:
                        more_good[0] += (Idx_r - Idx_l - 2) * prv_len_same
                    else:
                        more_good[1] += (Idx_r - Idx_l - 2) * prv_len_same

                    if not test:
                        if mode == 1:
                            for i in range(Idx_l, Idx_r - 1):
                                OK, rslt = is_OK_v2(prv_same, A[i], h, hight)
                                print(OK)
                                ans[i] = rslt
                        else:
                            for i in range(Idx_l + 1, Idx_r):
                                OK, rslt = is_OK_v2(prv_same, A[i], h, hight)
                                print(OK)

                                ans[i] = rslt

                    break

            else:
                # print("tyuudan")
                # print(Idx_l, Idx_r, prv_len_same)
                if mode == 1:

                    more_good[0] += (Idx_r - Idx_l - 2) * prv_len_same
                else:
                    more_good[1] += (Idx_r - Idx_l - 2) * prv_len_same

                if not test:
                    if mode == 1:
                        for i in range(Idx_l, Idx_r - 1):
                            OK, rslt = is_OK_v2(prv_same, A[i], h, hight)
                            print(OK)

                            ans[i] = rslt
                    else:
                        for i in range(Idx_l + 1, Idx_r):
                            OK, rslt = is_OK_v2(prv_same, A[i], h, hight)
                            print(OK)

                            ans[i] = rslt

                prv_same = []
                prv_len_same = 0
                if mode == 1:
                    Idx_l = Idx_r - 1
                    Idx_r = Idx_l + 2
                else:
                    Idx_r = Idx_l
                    Idx_l = Idx_r - 2

                if Idx_r > len(ans) or Idx_l < 0:
                    break

    # Output(ans)
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    return more_good


def is_OK_v2(same, a, h, hight):

    OK = True
    w = [0] * len(h)
    rslt = [None] * (len(a))
    a_rev = a[::-1]
    for idx in range(len(a)):
        if idx < len(same):
            i = same[idx]
        else:
            i = a_rev[idx]

        Hi = 10**18
        puted = False

        for j in range(len(h)):
            width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = True
                hi = max(width, h[j]) / min(width, h[j])
                if Hi > hi:
                    Hi = hi
                    rs = j, width, [hight[j], w[j], hight[j + 1], w[j] + width]
        # 配置可能な場合
        if puted:
            j, width, tmp = rs
            w[j] += width
            rslt[idx] = tmp
        else:
            return False, rslt

    return OK, rslt[::-1]


def change_ans(A, ans, ans_hoken, h, hight, over, over_hoken, Mode, test):
    # 二つを合わせて一個とマッチングとかも可能ではある
    # とりあえず一個拡張を試みる
    # prv = None

    more_good = [0, 0]
    for mode in Mode:
        for i in range(mode, len(ans) - 1, 2):
            if i in over or i + 1 in over:
                continue

            rslt_a = None
            rslt_b = None
            a = A[i]
            b = A[i + 1]

            a_idx = SortedMultiset(range(len(a)))
            b_idx = SortedMultiset(range(len(b)))
            a_SMS = SortedMultiset(a)
            b_SMS = SortedMultiset(b)

            same_a = []
            same_b = []

            while True:
                diff = []
                for i_idx, j in zip(a_idx, a_SMS):
                    l = b_SMS.le(j)
                    r = b_SMS.ge(j)
                    if l == None:
                        diff_l = 10**8
                    else:
                        diff_l = abs(j - l)

                    if r == None:
                        diff_r = 10**8
                    else:
                        diff_r = abs(j - r)

                    if diff_l > diff_r:
                        j_idx = b_idx[b_SMS.index_right(j)]
                        diff.append((diff_r, j, r, i_idx, j_idx))
                    else:
                        j_idx = b_idx[b_SMS.index_right(j) - 1]
                        diff.append((diff_l, j, l, i_idx, j_idx))

                _, j, k, j_idx, k_idx = min(diff, key=lambda x: x[0])

                same_a.append([max(j, k), j_idx])
                same_b.append([max(j, k), k_idx])
                a_idx.discard(j_idx)
                b_idx.discard(k_idx)
                a_SMS.discard(j)
                b_SMS.discard(k)

                ok_a, rslt_a_n = is_OK(same_a, list(a_SMS), list(a_idx), h, hight)
                ok_b, rslt_b_n = is_OK(same_b, list(b_SMS), list(b_idx), h, hight)

                if ok_a and ok_b:
                    rslt_a, rslt_b = rslt_a_n, rslt_b_n

                else:
                    more_good[mode] += len(same_a) - 1
                    if rslt_a and rslt_b and not test:
                        ans[i] = rslt_a
                        ans[i + 1] = rslt_b
                    break

                if len(a_SMS) == 0:
                    more_good[mode] += len(same_a) - 1
                    if rslt_a and rslt_b and not test:
                        ans[i] = rslt_a
                        ans[i + 1] = rslt_b
                    break

    return more_good


def is_OK(same, other, Idx, h, hight):

    isover = False
    w = [0] * len(h)
    rslt = [None] * (len(same) + len(other))

    for i, idx in same:
        Hi = 10**18
        puted = False
        for j in range(len(h)):
            width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = True
                hi = max(width, h[j]) / min(width, h[j])
                if Hi > hi:
                    Hi = hi
                    rs = j, width, [hight[j], w[j], hight[j + 1], w[j] + width]
        # 配置可能な場合
        if puted:
            j, width, tmp = rs
            w[j] += width

            rslt[idx] = tmp
        else:
            isover = True
            return not isover, rslt[::-1]

    for i, idx in zip(other[::-1], Idx[::-1]):
        Hi = 10**18
        puted = False
        for j in range(len(h)):
            width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = True
                hi = max(width, h[j]) / min(width, h[j])
                if Hi > hi:
                    Hi = hi

                    rs = j, width, [hight[j], w[j], hight[j + 1], w[j] + width]
        # 配置可能な場合
        if puted:
            j, width, tmp = rs
            w[j] += width
            rslt[idx] = tmp
        else:
            isover = True
            return not isover, rslt[::-1]

    return not isover, rslt


from collections import deque


# 答えから縦の分かれ目と答えの並びを取得
def get_info_from_ans(ans, hight):
    # 空の行にも面積があるとして追加
    # そのうちの上位N個を使用するようにする
    # 偶数行目は左右反転する
    rslt = [[SortedSet([0]) for _ in range(len(hight) - 1)] for _ in range(len(ans))]
    S = [SortedMultiset() for _ in range(len(ans))]
    hight_to_idx = [-1] * 1001
    for i, j in enumerate(hight):
        hight_to_idx[j] = i

    for idx, i in enumerate(ans):
        for k in i:
            s = (k[2] - k[0]) * (k[3] - k[1])
            # マイナスで保管
            S[idx].add(-s)
            rslt[idx][hight_to_idx[k[0]]].add(k[3])

    for i in range(len(ans)):
        for j in range(len(hight) - 1):
            if len(rslt[i][j]) == 1:
                rslt[i][j].add(1000)
                s = 1000 * (hight[j + 1] - hight[j])
                S[i].add(-s)

    return rslt, S


def yamanobori2(ans, line, over, h, S, A):
    cnt = 0
    len_ans = len(ans)
    len_h = len(h)
    more_good_0 = 0
    more_good_1 = 0

    A_minus = [sorted(map(lambda x: -x, i)) for i in A]

    # print(have_time)
    # print(over)
    # 現在は片方を片方に合わせる形だがそれでは変化が急なので、中間位置に移動させるという手もある
    # tmp_time = time.perf_counter()

    tmp_time = time.perf_counter() - start
    Timeover = 2.87
    start_temp = 200
    end_temp = 0
    temp = start_temp + (end_temp - start_temp) * tmp_time / Timeover
    e = 2.71828

    # デバッグ用
    # score = None
    # mode_score = [0, 0, 0, 0, 0, 0]

    mode = 0
    while True:
        # デバッグ用^^^^^^^^^^^^^^^^^^^^^^^^^
        # score_n = get_score(tate_haiti, h)
        # if score == None:
        #     score = score_n
        # elif score > score_n:
        #     mode_score[mode] += score_n - score
        #     print("+++", mode, score_n - score)
        #     score = score_n
        #     print(score)
        # elif score < score_n:
        #     mode_score[mode] += score_n - score
        #     print("---", mode, score_n - score)
        #     score = score_n
        #     print(score)
        # デバッグ用^^^^^^^^^^^^^^^^^^^^^^^^^^^

        cnt += 1
        if cnt % 100 == 0:
            tmp_time = time.perf_counter() - start
            temp = start_temp + (end_temp - start_temp) * tmp_time / Timeover
            if tmp_time > Timeover:
                break

        # ランダムに一つの縦線を選択

        idx1 = random.choice(range(len_ans))
        idx2 = random.choice(range(len_h))
        rev = random.choice([1, -1])

        if not 0 <= idx1 - rev < len_ans:
            continue
        if idx1 in over or idx1 - rev in over:
            continue

        # mode = random.choice([0, 0, 0, 1, 3, 3, 4, 4, 4])
        mode = random.choice([0, 0, 0, 1, 2, 3, 4, 4, 6])

        if mode == 6:
            # 左右反転
            tmp = line[idx1][idx2]
            if len(tmp) == 2:
                continue

            score_diff = 0
            for i in tmp:
                if 0 < i < 1000:
                    if 0 <= idx1 - 1 < len_ans:
                        if i in line[idx1 - 1][idx2]:
                            score_diff -= 1
                        if 1000 - i in line[idx1 - 1][idx2]:
                            score_diff += 1
                    if 0 <= idx1 + 1 < len_ans:
                        if i in line[idx1 + 1][idx2]:
                            score_diff -= 1
                        if 1000 - i in line[idx1 + 1][idx2]:
                            score_diff += 1
            if score_diff < 0:
                continue
            line[idx1][idx2] = SortedSet([1000 - i for i in tmp])

        if mode == 5:
            while True:
                idx3 = random.choice(range(len_h))
                if idx2 != idx3:
                    break

            tmp1 = set(line[idx1][idx2])
            tmp2 = set(line[idx1][idx3])

            if len(tmp1) == 2 and len(tmp2) == 2:
                continue

            # スコアの変化量 + -> スコア改善、- ->スコア改悪
            score_diff = (h[idx2] * (len(tmp1) - 2) + h[idx3] * (len(tmp2) - 2)) - (
                h[idx2] * (len(tmp2) - 2) + h[idx3] * (len(tmp1) - 2)
            )
            score_diff *= 2

            if score_diff >= 0:
                seni = True
            else:
                seni = e ** (score_diff / temp) > random.random()

            if not seni:
                continue

            if 0 <= idx1 - 1 < len_ans:
                if (
                    len(tmp1 & set(line[idx1 - 1][idx2])) != 2
                    or len(tmp2 & set(line[idx1 - 1][idx3])) != 2
                ):
                    continue

            if 0 <= idx1 + 1 < len_ans:
                if (
                    len(tmp1 & set(line[idx1 + 1][idx2])) != 2
                    or len(tmp2 & set(line[idx1 + 1][idx3])) != 2
                ):
                    continue

            s = S[idx1]
            # 面積を一旦書き換え
            for i in tmp1:
                if i != 0:
                    s.discard(-(i - prv) * h[idx2])
                    s.add(-(i - prv) * h[idx3])
                prv = i

            for i in tmp2:
                if i != 0:
                    s.discard(-(i - prv) * h[idx3])
                    s.add(-(i - prv) * h[idx2])
                prv = i

            if all([i >= j for i, j in zip(A_minus[idx1], s)]):
                line[idx1][idx2], line[idx1][idx3] = (
                    line[idx1][idx3],
                    line[idx1][idx2],
                )

            else:
                for i in tmp1:
                    if i != 0:
                        s.add(-(i - prv) * h[idx2])
                        s.discard(-(i - prv) * h[idx3])
                    prv = i

                for i in tmp2:
                    if i != 0:
                        s.add(-(i - prv) * h[idx3])
                        s.discard(-(i - prv) * h[idx2])
                    prv = i

        # 行の異なる一致点への移動
        if mode == 4:
            if len(line[idx1][idx2]) == 2:
                continue
            idx3 = random.choice(range(1, len(line[idx1][idx2]) - 1))
            tmp = line[idx1][idx2]
            l, m, r = tmp[idx3 - 1], tmp[idx3], tmp[idx3 + 1]
            while True:
                idx4 = random.choice(range(len_h))
                if idx2 != idx4:
                    break
            flag1, flag2 = False, False
            if idx1 - 1 in range(len(ans)):
                if m in line[idx1 - 1][idx2]:
                    flag1 = True
            if idx1 + 1 in range(len(ans)):
                if m in line[idx1 + 1][idx2]:
                    flag2 = True

            if flag1 and flag2:
                continue

            other = line[idx1 - rev][idx4]

            s = S[idx1]

            for i in other:
                if 1 <= i < 1000 and i not in line[idx1][idx4]:
                    prv_l_1 = h[idx2] * (m - l)
                    prv_r_1 = h[idx2] * (r - m)
                    nxt_lr_1 = h[idx2] * (r - l)

                    l_2 = line[idx1][idx4].le(i)
                    r_2 = line[idx1][idx4].ge(i)

                    prv_lr_2 = h[idx4] * (r_2 - l_2)
                    nxt_l_2 = h[idx4] * (i - l_2)
                    nxt_r_2 = h[idx4] * (r_2 - i)

                    # 一旦面積情報の書き換え
                    s.discard(-prv_l_1)
                    s.discard(-prv_r_1)
                    s.discard(-prv_lr_2)
                    s.add(-nxt_lr_1)
                    s.add(-nxt_l_2)
                    s.add(-nxt_r_2)

                    if all([i >= j for i, j in zip(A_minus[idx1], s)]):
                        tmp.discard(m)
                        line[idx1][idx4].add(i)
                        break
                    else:
                        # 面積情報の訂正
                        s.add(-prv_l_1)
                        s.add(-prv_r_1)
                        s.add(-prv_lr_2)
                        s.discard(-nxt_lr_1)
                        s.discard(-nxt_l_2)
                        s.discard(-nxt_r_2)

        elif mode == 3:
            # ランダムな数字だけ横にずらす
            if len(line[idx1][idx2]) == 2:
                continue
            idx3 = random.choice(range(1, len(line[idx1][idx2]) - 1))
            tmp = line[idx1][idx2]
            l, m, r = tmp[idx3 - 1], tmp[idx3], tmp[idx3 + 1]

            s = S[idx1]

            w = 30
            # print(max(l, w - 10), min(r, w + 10))
            num = random.choice(range(max(l, m - w), min(r, m + w)))
            score_diff = 0
            if 0 <= idx1 - rev < len_ans:
                if m in line[idx1 - rev][idx2]:
                    score_diff -= 1
                if num in line[idx1 - rev][idx2]:
                    score_diff += 1
            if 0 <= idx1 + rev < len_ans:
                if m in line[idx1 + rev][idx2]:
                    score_diff -= 1
                if num in line[idx1 + rev][idx2]:
                    score_diff += 1

            if score_diff < 0:
                continue
            prv_l = h[idx2] * (m - l)
            nxt_l = h[idx2] * (num - l)
            prv_r = h[idx2] * (r - m)
            nxt_r = h[idx2] * (r - num)

            # 一旦面積情報の書き換え
            s.discard(-prv_l)
            s.discard(-prv_r)
            s.add(-nxt_l)
            s.add(-nxt_r)

            if all([i >= j for i, j in zip(A_minus[idx1], s)]):
                tmp.discard(m)
                tmp.add(num)

            else:
                # 面積情報の訂正
                s.add(-prv_l)
                s.add(-prv_r)
                s.discard(-nxt_l)
                s.discard(-nxt_r)

        elif mode == 2:
            # 横並びの二つの長方形のスワップ
            # スワップする部分を乱択で選ぶ
            if len(line[idx1][idx2]) == 2:
                continue

            idx3 = random.choice(range(1, len(line[idx1][idx2]) - 1))
            tmp = line[idx1][idx2]
            l, m, r = tmp[idx3 - 1], tmp[idx3], tmp[idx3 + 1]

            score_diff = 0
            if 0 <= idx1 - rev < len_ans:
                if m in line[idx1 - rev][idx2]:
                    score_diff -= 1
                if l + r - m in line[idx1 - rev][idx2]:
                    score_diff += 1
            if 0 <= idx1 + rev < len_ans:
                if m in line[idx1 + rev][idx2]:
                    score_diff -= 1
                if l + r - m in line[idx1 + rev][idx2]:
                    score_diff += 1

            if score_diff < 0:
                continue

            tmp.discard(m)
            tmp.add(l + r - m)
            # print(2)

        elif mode == 0:

            tmp = line[idx1][idx2]
            flag_l = True
            flag_r = True

            if len(tmp) >= 3:
                idx3 = random.choice(range(1, len(tmp) - 1))
                num = tmp[idx3]
            else:
                continue

            # 一個前の答えの左右の縦線と一致させたとき、面積が許容できるか

            tmp_l = tmp.lt(num)
            tmp_r = tmp.gt(num)
            other_l = line[idx1 - rev][idx2].le(num)
            other_r = line[idx1 - rev][idx2].ge(num)

            s = S[idx1]

            # print(sum(s), s)
            # print(tate_haiti[idx1])

            # 左にずらす場合
            # 面積の変化を追う
            if num == other_l:
                flag_l = False

            score_diff_l = 0
            if 0 <= idx1 - rev < len_ans:
                if num in line[idx1 - rev][idx2]:
                    score_diff_l -= 1
                score_diff_l += 1

            if 0 <= idx1 + rev < len_ans:
                if num in line[idx1 + rev][idx2]:
                    score_diff_l -= 1
                if other_l in line[idx1 + rev][idx2]:
                    score_diff_l += 1

            if score_diff_l < 0:
                flag_l = False

            if flag_l:
                prv_l = h[idx2] * (num - tmp_l)
                nxt_l = h[idx2] * (other_l - tmp_l)

                prv_r = h[idx2] * (tmp_r - num)
                nxt_r = h[idx2] * (tmp_r - other_l)

                if prv_l < 0 or nxt_l < 0 or prv_r < 0 or nxt_r < 0:
                    flag_l = False

            if flag_l:
                # 一旦面積情報の書き換え
                s.discard(-prv_l)
                s.discard(-prv_r)
                s.add(-nxt_l)
                s.add(-nxt_r)

                # 変更しても面積に問題が無いなら
                if all([i >= j for i, j in zip(A_minus[idx1], s)]):
                    more_good_0 += 1
                    tmp.discard(num)
                    tmp.add(other_l)

                    continue
                else:
                    # 面積情報の訂正
                    s.add(-prv_l)
                    s.add(-prv_r)
                    s.discard(-nxt_l)
                    s.discard(-nxt_r)

            # 右にずらす場合

            if num == other_r:
                flag_r = False

            score_diff_r = 0
            if 0 <= idx1 - rev < len_ans:
                if num in line[idx1 - rev][idx2]:
                    score_diff_r -= 1
                score_diff_r += 1

            if 0 <= idx1 + rev < len_ans:
                if num in line[idx1 + rev][idx2]:
                    score_diff_r -= 1
                if other_r in line[idx1 + rev][idx2]:
                    score_diff_r += 1

            if score_diff_r < 0:
                flag_r = False

            if flag_r:
                prv_l = h[idx2] * (num - tmp_l)
                nxt_l = h[idx2] * (other_r - tmp_l)

                prv_r = h[idx2] * (tmp_r - num)
                nxt_r = h[idx2] * (tmp_r - other_r)

                if prv_l < 0 or nxt_l < 0 or prv_r < 0 or nxt_r < 0:
                    flag_r = False

            if flag_r:
                # 一旦面積情報の書き換え
                s.discard(-prv_l)
                s.discard(-prv_r)
                s.add(-nxt_l)
                s.add(-nxt_r)

                # 変更しても面積に問題が無いなら
                if all([i >= j for i, j in zip(A_minus[idx1], s)]):
                    more_good_0 += 1
                    tmp.discard(num)
                    tmp.add(other_r)
                    continue
                else:
                    # 面積情報の訂正
                    s.add(-prv_l)
                    s.add(-prv_r)
                    s.discard(-nxt_l)
                    s.discard(-nxt_r)

        elif mode == 1:
            tmp = line[idx1][idx2]
            other = line[idx1 - rev][idx2]
            flag_l = True
            flag_r = True
            if len(tmp) >= 3:
                idx3 = random.choice(range(1, len(tmp) - 1))
                num = tmp[idx3]
            else:
                continue

            # 一個前の答えの左右の縦線と一致させたとき、面積が許容できるか

            tmp_l = tmp.lt(num)
            tmp_r = tmp.gt(num)
            other_l = other.le(num)
            other_r = other.ge(num)

            # 既にペア
            if num == other_l:
                continue

            # 相手が0,1000
            if other_l == 0:
                flag_l = False
            if other_r == 1000:
                flag_r = False

            # 反対側とペアなら
            if idx1 + rev in range(len_ans):
                if num in line[idx1 + rev][idx2]:
                    continue

            if idx1 - 2 * rev in range(len_ans):
                if other_l in line[idx1 - 2 * rev][idx2]:
                    flag_l = False
                    continue

            if idx1 - 2 * rev in range(len_ans):
                if other_r in line[idx1 - 2 * rev][idx2]:
                    flag_r = False
                    continue

            s = S[idx1]
            s_other = S[idx1 - rev]

            # 左との中間をとる場合
            if flag_l:
                mid = (num + other_l) // 2
                if mid in tmp or mid in other:
                    flag_l = False

                # 注目してる方の面積状態の確認
                prv_l = h[idx2] * (num - tmp_l)
                nxt_l = h[idx2] * (mid - tmp_l)

                prv_r = h[idx2] * (tmp_r - num)
                nxt_r = h[idx2] * (tmp_r - mid)

                if prv_l < 0 or nxt_l < 0 or prv_r < 0 or nxt_r < 0:
                    flag_l = False

                # 他方の面積状態の確認
                other_l_l = other.lt(other_l)
                prv_l_other = h[idx2] * (other_l - other_l_l)
                nxt_l_other = h[idx2] * (mid - other_l_l)
                other_l_r = other.gt(other_l)
                prv_r_other = h[idx2] * (other_l_r - other_l)
                nxt_r_other = h[idx2] * (other_l_r - mid)

                if (
                    prv_l_other < 0
                    or nxt_l_other < 0
                    or prv_r_other < 0
                    or nxt_r_other < 0
                ):
                    flag_l = False

            if flag_l:
                # 一旦面積情報の書き換え
                s.discard(-prv_l)
                s.discard(-prv_r)
                s.add(-nxt_l)
                s.add(-nxt_r)

                # 一旦面積情報の書き換え
                s_other.discard(-prv_l_other)
                s_other.discard(-prv_r_other)
                s_other.add(-nxt_l_other)
                s_other.add(-nxt_r_other)

                # 変更しても面積に問題が無いなら
                if all([i >= j for i, j in zip(A_minus[idx1], s)]) and all(
                    [i >= j for i, j in zip(A_minus[idx1 - rev], s_other)]
                ):
                    more_good_1 += 1
                    tmp.discard(num)
                    tmp.add(mid)
                    other.discard(other_l)
                    other.add(mid)
                    # print(1, get_tyouhuku_num(tate_haiti))
                    continue
                else:

                    # 面積情報の訂正
                    s.add(-prv_l)
                    s.add(-prv_r)
                    s.discard(-nxt_l)
                    s.discard(-nxt_r)

                    s_other.add(-prv_l_other)
                    s_other.add(-prv_r_other)
                    s_other.discard(-nxt_l_other)
                    s_other.discard(-nxt_r_other)

            # 右との中間をとる場合
            if flag_r:
                mid = (num + other_r) // 2

                if mid in tmp or mid in other:
                    flag_r = False

                prv_l = h[idx2] * (num - tmp_l)
                nxt_l = h[idx2] * (mid - tmp_l)

                prv_r = h[idx2] * (tmp_r - num)
                nxt_r = h[idx2] * (tmp_r - mid)

                if prv_l < 0 or nxt_l < 0 or prv_r < 0 or nxt_r < 0:
                    flag_r = False

                # 他方の面積状態の確認
                other_r_l = other.lt(other_r)
                prv_l_other = h[idx2] * (other_r - other_r_l)
                nxt_l_other = h[idx2] * (mid - other_r_l)

                other_r_r = other.gt(other_r)
                prv_r_other = h[idx2] * (other_r_r - other_r)
                nxt_r_other = h[idx2] * (other_r_r - mid)

                if (
                    prv_l_other < 0
                    or nxt_l_other < 0
                    or prv_r_other < 0
                    or nxt_r_other < 0
                ):
                    flag_r = False

            if flag_r:
                # 一旦面積情報の書き換え
                s.discard(-prv_l)
                s.discard(-prv_r)
                s.add(-nxt_l)
                s.add(-nxt_r)
                # 一旦面積情報の書き換え
                s_other.discard(-prv_l_other)
                s_other.discard(-prv_r_other)
                s_other.add(-nxt_l_other)
                s_other.add(-nxt_r_other)

                # 変更しても面積に問題が無いなら
                if all([i >= j for i, j in zip(A_minus[idx1], s)]) and all(
                    [i >= j for i, j in zip(A_minus[idx1 - rev], s_other)]
                ):
                    more_good_1 += 1
                    tmp.discard(num)
                    tmp.add(mid)
                    other.discard(other_r)
                    other.add(mid)
                    # print(1, get_tyouhuku_num(tate_haiti))

                    continue
                else:
                    # 面積情報の訂正
                    s.add(-prv_l)
                    s.add(-prv_r)
                    s.discard(-nxt_l)
                    s.discard(-nxt_r)

                    s_other.add(-prv_l_other)
                    s_other.add(-prv_r_other)
                    s_other.discard(-nxt_l_other)
                    s_other.discard(-nxt_r_other)

        # デバッグ用
        # if sum([len(i) - 1 for i in tate_haiti[idx1]]) < len(ans[0]):
        #     print(mode)
        #     exit()

    # print(get_tyouhuku_num(tate_haiti))
    # exit()]
    # print(get_add_score(tate_haiti, h))
    # print(h)
    # print(score, get_tyouhuku_num(tate_haiti))
    # print(mode_score)
    return line


def get_score(tate_haiti, h):
    rslt = 0
    tmp = tate_haiti[0]
    for i in range(1, len(tate_haiti)):
        for j in range(len(tate_haiti[0])):
            rslt += h[j] * (len(set(tate_haiti[i - 1][j]) ^ set(tate_haiti[i][j])))

    return rslt


def get_add_score(tate_haiti, h):
    rslt = 0
    tmp = tate_haiti[0]
    for i in range(1, len(tate_haiti)):
        for j in range(len(tate_haiti[0])):
            rslt += h[j] * (len(set(tate_haiti[i - 1][j]) & set(tate_haiti[i][j])) - 2)

    return rslt


def get_ans_from_tatehaiti(N, tate_haiti, hight, over, ans_hoken, over_hoken):
    ans = [[] for _ in range(len(tate_haiti))]

    for i, j in enumerate(tate_haiti):
        if i in over and i not in over_hoken:
            ans[i] = ans_hoken[i]
        else:
            for k, l in enumerate(j):
                # print(l)
                l_n = list(l)
                for m in range(1, len(l_n)):
                    tmp = [hight[k], l_n[m - 1], hight[k + 1], l_n[m]]
                    ans[i].append(tmp)

    for i in ans:

        i.sort(key=lambda x: (x[3] - x[1]) * (x[2] - x[0]), reverse=True)
        # print([(x[3] - x[1]) * (x[2] - x[0]) for x in i])

        # 多すぎる分の削除
        while len(i) > N:
            i.pop()
        i.sort(key=lambda x: (x[3] - x[1]) * (x[2] - x[0]))
        # print([(x[3] - x[1]) * (x[2] - x[0]) for x in i])

    return ans


def kotei(A_tenti, h):
    idx = 0
    while True:
        tmp = min(A_tenti[idx])


def main():
    # 方針1
    # 縦の分割数をいくつか決めて、それぞれで幅を山登りする
    # その過程で得られたスコアが最も良いものを答えにする

    # TODO
    # 現在では日にちを跨いで柵を使いまわすようなことを考慮していない
    # した
    # 二日の塊としてが、三日四日と大きい方が有利？スコア計算だけど、内部で計算できれば割といいかも
    # どんどん取り込んでいく形もあり
    # 収まるか同課の判定は面積の内方されているかで確認できる
    # 縦長でも面積を納められない場合の収納方法の計算

    # 山上りの前の調整は意義がある
    # 山登り自体も改善できるかも
    global avr_amari, max_amari

    # 配置可能な限界まで縦の数を増やして細めるのもあり
    # 近傍の追加
    # 前後未使用の縦線を選択し、前後であったら嬉しい場所に移動させて、面積の確認
    # 山登りのスコアの増減の確認
    # 現在の山登りは適当
    # 改善案
    # チェンジAnsの改良
    # 山登りの改良、近傍追加など
    # 左右反転、上下移動など
    # 縦分割、即ち面積配置方法の改良
    # 山登り部分のバグ解消
    # 一段空きスペースみたいな場合もあるので、面積管理が色々考えられる
    # SMSにはマイナスで入れといて扱うとか
    # 一部完全固定する
    # 乱択で詰め込める順番を求める
    # 初期解の貪欲部分の改善
    # 幅決定の最適化
    # 焼きなまし高速化
    # 焼きなましの温度調整
    # スコア遷移のグラフ化
    # 縦分割は分散が小さいほど、行跨ぎの遷移がしやすいかも
    W, D, N, A, avr_amari, max_amari = Input()
    ans, ans_hoken, h, hight, over, over_hoken = solve(W, D, N, A)

    A_tenti = list(zip(*A))

    more_good1 = change_ans(A, ans, ans_hoken, h, hight, over, over_hoken, [0, 1], True)
    more_good2 = change_ans_v2(A, h, hight, ans, over, [1, -1], True, A_tenti)
    print(more_good1, more_good2)
    # Output(ans)
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    if max(more_good1) <= max(more_good2):
        if more_good2[0] <= more_good2[1]:
            change_ans_v2(A, h, hight, ans, over, [-1], False, A_tenti)
        else:
            change_ans_v2(A, h, hight, ans, over, [1], False, A_tenti)
    else:
        if more_good1[0] <= more_good1[1]:
            change_ans(A, ans, ans_hoken, h, hight, over, over_hoken, [1], False)
        else:
            change_ans(A, ans, ans_hoken, h, hight, over, over_hoken, [0], False)

    most_rihgt_line_change(ans)

    Output(ans)
    exit()
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # exit()

    tate_haiti, S = get_info_from_ans(ans, hight)
    # for i in tate_haiti:
    #     print(i)
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    tate_haiti = yamanobori2(ans, tate_haiti, over, h, S, A)
    ans = get_ans_from_tatehaiti(N, tate_haiti, hight, over, ans_hoken, over_hoken)
    Output(ans)

    pass


# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional

T = TypeVar("T")
import typing


def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


def _bsf(n: int) -> int:
    x = 0
    while n % 2 == 0:
        x += 1
        n //= 2

    return x


class SegTree:
    def __init__(
        self,
        op: typing.Callable[[typing.Any, typing.Any], typing.Any],
        e: typing.Any,
        v: typing.Union[int, typing.List[typing.Any]],
    ) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int, f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        n = self.size = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [
            a[n * i // num_bucket : n * (i + 1) // num_bucket]
            for i in range(num_bucket)
        ]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]:
                break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a, b, i = self._position(x)
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]

    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a:
            del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x:
            return False
        self._pop(a, b, i)
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self.a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0:
                    return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a):
                    return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


class SortedSet(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [
            a[n * i // num_bucket : n * (i + 1) // num_bucket]
            for i in range(num_bucket)
        ]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]:
                break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x:
            return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]
        return True

    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a:
            del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x:
            return False
        self._pop(a, b, i)
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self.a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0:
                    return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a):
                    return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


if __name__ == "__main__":
    main()
