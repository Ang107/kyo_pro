import sys
from collections import deque


input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
# memo
# N*Nの盤面があり、その下には、いくつかのポリオミノ 型の形のお宝があることが分かっています。その形状と向きもは分かっていますが、存在する場所は不明です。そのお宝は全てN*Nの盤面に収まっている。また、複数のお宝が一マスに重複して存在することもある。

# コストを１払うことで、指定したマスの下にあるお宝の数を知ることができる。

# 盤面の中で下にお宝があるマスを全て特定させることが目的であり、それまでにかかったコストを最小化したい。
# そのためにはどのようにマスを指定すればよいか？


# 以上の問題の厳密解を求める方法を教えて。
def dlist(*l, fill=0):
    if len(l) == 1:
        return [fill] * l[0]
    ll = l[1:]
    return [dlist(*ll, fill=fill) for _ in range(l[0])]


# 毎回Dをnextの数でソートする
def FirstInput():
    global N, M, E, D, D_size, limit
    N, M, E = input().split()
    N, M = int(N), int(M)
    E = float(E)
    D = []
    D_size = []
    limit = 2500000 / N**2.5
    for i in range(M):
        tmp = LMII()
        zahyou = []
        for i in range(2, len(tmp), 2):
            zahyou.append((tmp[i - 1], tmp[i]))
        D.append([zahyou, len(zahyou), [[True] * N for _ in range(N)]])

    D.sort(key=lambda x: x[1], reverse=True)


def Output_Input(l: list):
    tmp = []
    for i, j in l:
        tmp.append(i)
        tmp.append(j)
    print("q", len(l), *tmp, flush=True)
    n = II()
    return n


def Output_Input_add(l: list, i, j, num):
    tmp = []
    tmp.append(i)
    tmp.append(j)
    for i, j in l:
        tmp.append(i)
        tmp.append(j)
    print("q", len(l) + 1, *tmp, flush=True)
    n = II() - num
    return n


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def Exit():
    ans = []
    for i in range(N):
        for j in range(N):
            if B[i][j] >= 1:
                ans.append((i, j))
    Last_Output(ans)
    exit()


# 答えの出力
def Last_Output(l):
    tmp = []
    for i, j in l:
        tmp.append(i)
        tmp.append(j)
    print("a", len(l), *tmp, flush=True)
    n = II()
    if n == 0:
        return False
    else:
        return True


def get_Weight():
    global Weight, Bunkatu, Idx
    num = N / 3
    Idx = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    Bunkatu = [[[] for i in range(3)] for j in range(3)]
    for i in range(N):
        for j in range(N):
            x = int(i // num)
            y = int(j // num)
            Bunkatu[x][y].append((i, j))
    Weight = [0] * 9
    for i in range(3):
        for j in range(3):
            Weight[i * 3 + j] = Output_Input(Bunkatu[i][j])

    avg = sum(Weight) / 9
    Weight = [i**1.5 + avg // 2 for i in Weight]

    print("#", Weight)


# todo 現状、クエリは独立している。->この組のクエリでパターンを絞れる、みたいな連携したクエリを送れるとよいかも
def solve():
    global B, Tarn
    B = [[-100] * N for _ in range(N)]

    Tarn = 0
    count = 0
    next = calc_next()

    while True:
        print("# D", *[j for i, j, k in D])
        D.sort(key=lambda x: x[1])
        print("# D", *[j for i, j, k in D])
        if len(next) == 0:
            Exit()
        # クエリを送信、Bの更新
        if Tarn <= 150:
            num = 1
        elif Tarn <= 225:
            num = 2
        else:
            num = 3

        for i in range(num):
            while True:
                if next:
                    x, y = next.pop()
                else:
                    break

                if B[x][y] == -100:
                    Tarn += 1
                    B[x][y] = Output_Input([(x, y)])
                    break

        # 答えの候補の取得
        flag, ans_list = get_Ans(B)
        # print("# ans", len(ans_list))

        # 絞り込めたなら
        # ans_listの数の上限の決め方を吟味する->現在期待値5だが、一回のクエリで絞り込めるならそっちがお得
        if flag and 1 <= len(ans_list) <= 5:
            # print("# count", count)
            for i in ans_list:
                tmp = set()
                for idx, (j, _, _) in enumerate(D):
                    sx, sy = i[idx]
                    for x, y in j:
                        tmp.add((x + sx, y + sy))
                Tarn += 1
                if Last_Output(tmp):
                    exit()
        # 絞り込めなかった場合
        else:
            # 次に送るクエリの候補を計算
            if ans_list:
                count += 1
                next = calc_next_from_ans(ans_list)
            else:
                next = calc_next()


def calc_next_from_ans(ans_list):
    next = [[0] * N for _ in range(N)]
    for ans in ans_list:
        tmp = set()
        for idx, (x, y) in enumerate(ans):
            for i, j in D[idx][0]:
                tmp.add((x + i, y + j))

        for i, j in tmp:
            next[i][j] += 1
    tmp = []
    for i in range(N):
        for j in range(N):
            if next[i][j] and B[i][j] == -100:
                tmp.append((next[i][j], i, j))
            elif next[i][j] == 0 and B[i][j] == -100:
                B[i][j] = 0
                # print(f"#c {i} {j} green")

    tmp.sort(key=lambda x: abs(x[0] - len(ans_list) / 2), reverse=True)
    return [(j, k) for i, j, k in tmp]


# 確定で0になるやつだけでなく、確定で１以上になるものなども記録できるとよい
# 送るクエリ計算
def calc_next():

    next = [[0] * N for _ in range(N)]

    for idx, (d, _, visited) in enumerate(D):
        count = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    continue
                tmp = []
                flag = 0
                for x, y in d:
                    if i + x in range(N) and j + y in range(N):
                        if B[i + x][j + y] == -100:
                            tmp.append((i + x, j + y))
                        elif B[i + x][j + y] >= 1:
                            flag += 1
                        else:
                            flag = -1
                            break
                    else:
                        flag = -1
                        break

                if flag >= 0:
                    count += 1
                    for p, q in tmp:
                        next[p][q] += 1
                else:
                    visited[i][j] = False
        D[idx][1] = count
        print("# count", count)

    tmp = []
    # max_next = max([max(i) for i in next])
    for i in range(N):
        for j in range(N):
            # a = hex(int(255 * next[i][j] / max_next))[2:]
            # print(
            #     f"#c {i} {j} #{a}0000",
            # )
            if next[i][j] and B[i][j] == -100:
                tmp.append((next[i][j], i, j))
            elif next[i][j] == 0 and B[i][j] == -100:
                B[i][j] = 0
                # print(f"#c {i} {j} blue")

    print("# count", count)
    if Tarn > N**2 / 3:
        tmp.sort(key=lambda x: abs(x[0] - count / 2), reverse=True)
    else:
        tmp.sort(key=lambda x: x[0])

    if len(tmp) > 15:
        tmp = tmp[-14:]
    random.shuffle(tmp)
    return [(j, k) for i, j, k in tmp]


# 答えの案の出力
# 候補数が多すぎる場合打ち切っているが、上手いこと計算すれば、打ち切らずに済場合がある？
# 計算結果を保存しておくことで、同じ計算を防いで高速化＆効率化できるかも
# 既に確定した部分を利用して、多めにクエリを送って引き算すればコストを抑えられる（誤差が生まれるので、その誤算に注意する必要あり）


def get_Ans(B):
    deq = deque()
    B_n = [k[:] for k in B]
    deq.append((0, B_n, []))
    ans = []
    while deq:
        idx, B, prv = deq.popleft()
        shape = D[idx][0]
        visited = D[idx][2]
        if idx == 1:
            big_flag = False
        else:
            big_flag = True

        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    continue
                flag = True
                for x, y in shape:
                    if (
                        i + x in range(N)
                        and j + y in range(N)
                        and (B[i + x][j + y] <= -100 or B[i + x][j + y] >= 1)
                    ):
                        pass
                    else:
                        flag = False
                        break

                if flag:
                    prv_n = prv[:]
                    prv_n.append((i, j))
                    B_n = [k[:] for k in B]
                    if idx == M - 1:
                        for x, y in shape:
                            B_n[i + x][j + y] -= 1
                        if max([max(k) for k in B_n]) <= 0:
                            big_flag = True
                            ans.append(prv_n)
                    else:
                        for x, y in shape:
                            B_n[i + x][j + y] -= 1
                        if max([max(k) for k in B_n]) <= M - idx - 1:
                            big_flag = True
                            deq.append((idx + 1, B_n, prv_n))
                        if len(deq) >= limit:
                            return False, []
        if big_flag == False and D[0][2][x][y]:
            x, y = prv[0]
            D[0][2][x][y] = False
            # print(f"#c {x} {y} red")

    return True, ans


import random


def main():
    FirstInput()
    solve()


if __name__ == "__main__":
    main()
