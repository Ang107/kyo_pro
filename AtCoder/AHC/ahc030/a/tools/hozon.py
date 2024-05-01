import sys
from collections import deque
from itertools import accumulate

input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))
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
    global N, M, E, D, D_size, limit, hensa
    N, M, E = input().split()
    N, M = int(N), int(M)
    E = float(E)
    D = []

    limit = 1500000 / N**2
    for i in range(M):
        tmp = LMII()
        zahyou = []
        for i in range(2, len(tmp), 2):
            zahyou.append((tmp[i - 1], tmp[i]))
        D.append([zahyou, len(zahyou), [True] * (N**2)])

    D.sort(key=lambda x: x[1], reverse=True)
    D_size = [i for _, i, _ in D]
    D_size = list(accumulate(D_size[::-1]))[::-1]

    hensa = get_hensa()


def get_hensa():
    hensa = {}
    for k in range(2, (N**2 + 1) // 2):
        tmp = (k * E * (1 - E)) ** 0.5
        hensa[(k, E)] = tmp
    return hensa


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
            if B[i * N + j] >= 1:
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


# todo 現状、クエリは独立している。->この組のクエリでパターンを絞れる、みたいな連携したクエリを送れるとよいかも
def solve():
    global B, Tarn
    visited_hukusuu = [False] * (N**2)
    B = [-100] * (N**2)

    Tarn = 0
    count = 0
    next = calc_next()

    while True:
        if Tarn % 5 == 0:
            visited = [False] * (N**2)
            for i in range(N):
                for j in range(N):
                    if not visited[i * N + j] and B[i * N + j] == -100:
                        flag, ans = bfs(i, j, visited)
                        num = len(ans)
                        if (
                            flag
                            and not visited_hukusuu[ans[0][0] * N + ans[0][1]]
                            and 4 <= num < N**2 // 2
                            and get_min_num_in_closed(ans) >= hensa[(num, E)] * 4
                        ):
                            for x, y in ans:
                                visited_hukusuu[x * N + y] = True
                            n = Output_Input(ans)
                            if n < num - (hensa[(num, E)] * 3 + 1) // 2:
                                for x, y in ans:
                                    B[x * N + y] = 0
                                    print(f"#c {x} {y} gray")

        # 答えの候補の取得
        flag, ans_list = get_Ans(B)

        # 絞り込めたなら
        # ans_listの数の上限の決め方を吟味する->現在期待値5だが、一回のクエリで絞り込めるならそっちがお得
        if flag and 1 <= len(ans_list) <= 5:
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
            if flag:
                count += 1
                next = calc_next_from_ans(ans_list)
            else:
                next = calc_next()

        if len(next) == 0:
            Exit()

        # クエリを送信、Bの更新
        if Tarn <= 150:
            num = 1
        elif Tarn <= 250:
            num = 2
        else:
            num = 3

        for i in range(num):
            while True:
                if next:
                    x, y = next.pop()
                else:
                    break

                if B[x * N + y] == -100:
                    Tarn += 1
                    B[x * N + y] = Output_Input([(x, y)])
                    break


def calc_next_from_ans(ans_list):
    next = [0] * (N**2)
    for ans in ans_list:
        tmp = set()
        for idx, (x, y) in enumerate(ans):
            for i, j in D[idx][0]:
                tmp.add((x + i, y + j))

        for i, j in tmp:
            next[i * N + j] += 1

    tmp = []
    for i in range(N):
        for j in range(N):
            if next[i * N + j] and B[i * N + j] == -100:
                tmp.append((next[i * N + j], i, j))
            elif next[i * N + j] == 0 and B[i * N + j] == -100:
                B[i * N + j] = 0
                print(f"#c {i} {j} green")

    tmp.sort(key=lambda x: abs(x[0] - len(ans_list) / 2), reverse=True)

    return [(j, k) for i, j, k in tmp]


# 確定で0になるやつだけでなく、確定で１以上になるものなども記録できるとよい
# 送るクエリ計算
# 既に1以上確定している場所はそれを消化しなければいけないという視点
def calc_next():

    next = [0] * (N**2)
    Plus_sum = 0
    for i in range(N):
        for j in range(N):
            if B[i * N + j] >= 1:
                Plus_sum += B[i * N + j]

    for d, size, visited in D:
        count = 0
        for i in range(N):
            for j in range(N):
                if not visited[i * N + j]:
                    continue
                tmp = []
                flag = 0
                for x, y in d:
                    if i + x in range(N) and j + y in range(N):
                        if B[(i + x) * N + (j + y)] == -100:
                            tmp.append((i + x, j + y))
                        elif B[(i + x) * N + (j + y)] >= 1:
                            flag += 1
                        else:
                            flag = -1
                            break
                    else:
                        flag = -1
                        break

                if flag >= 0 and D_size[0] - size >= Plus_sum - flag:
                    count += 1
                    for p, q in tmp:
                        next[p * N + q] += 1
                else:
                    visited[i * N + j] = False

    tmp = []

    for i in range(N):
        for j in range(N):
            if next[i * N + j] and B[i * N + j] == -100:
                tmp.append((next[i * N + j], i, j))
            elif next[i * N + j] == 0 and B[i * N + j] == -100:
                B[i * N + j] = 0
                print(f"#c {i} {j} blue")

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
    B_n = B[:]
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
        Sum = 0
        for i in range(N):
            for j in range(N):
                if B[i * N + j] >= 1:
                    Sum += 1

        for i in range(N):
            for j in range(N):
                if not visited[i * N + j]:
                    continue
                flag = True
                for x, y in shape:
                    if (
                        i + x in range(N)
                        and j + y in range(N)
                        and (
                            B[(i + x) * N + (j + y)] <= -100
                            or B[(i + x) * N + (j + y)] >= 1
                        )
                    ):
                        pass
                    else:
                        flag = False
                        break

                if flag:
                    prv_n = prv[:]
                    prv_n.append((i, j))
                    B_n = B[:]
                    if idx == M - 1:
                        for x, y in shape:
                            B_n[(i + x) * N + (j + y)] -= 1
                        if max(B_n) <= 0:
                            big_flag = True
                            ans.append(prv_n)
                    else:
                        tmp = 0
                        for x, y in shape:
                            B_n[(i + x) * N + (j + y)] -= 1
                            if B_n[(i + x) * N + (j + y)] >= 0:
                                tmp += 1

                        if max(B_n) <= M - idx - 1 and D_size[idx + 1] >= Sum - tmp:
                            big_flag = True
                            deq.append((idx + 1, B_n, prv_n))

                        if len(deq) >= limit:
                            return False, []
        if big_flag == False and D[0][2][x * N + y]:
            x, y = prv[0]
            D[0][2][x * N + y] = False
            # print(f"#c {x} {y} red")

    return True, ans


def bfs(i, j, visited):
    deq = deque([(i, j)])
    visited[i * N + j] = True
    ans = [(i, j)]
    flag = True
    while deq:
        x, y = deq.popleft()
        for i, j in around4:
            if (
                x + i in range(N)
                and y + j in range(N)
                and not visited[(x + i) * N + (y + j)]
            ):
                if B[(x + i) * N + (y + j)] == -100:
                    visited[(x + i) * N + (y + j)] = True
                    deq.append((x + i, y + j))
                    ans.append((x + i, y + j))
                elif B[(x + i) * N + (y + j)] >= 1:
                    flag = False
    return flag, ans


def get_min_num_in_closed(ans):
    min_x, min_y = 100, 100
    max_x, max_y = -1, -1
    for i, j in ans:
        min_x, max_x = min(min_x, i), max(max_x, i)
        min_y, max_y = min(min_y, j), max(max_y, j)
    num = 0
    for d, size, visited in D:
        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                if not visited[i * N + j]:
                    continue
                flag = True
                for x, y in d:
                    if i + x in range(N) and j + y in range(N):
                        if B[(i + x) * N + (j + y)] == -100:
                            pass
                        else:
                            flag = False
                            break
                    else:
                        flag = False
                        break
                if flag:
                    num = max(num, size)
                    i = max_x
    return num


import random


def main():
    FirstInput()
    solve()


if __name__ == "__main__":
    main()
