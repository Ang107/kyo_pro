from sys import stdin, stderr, setrecursionlimit, set_int_max_str_digits
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase
import random
import time

START = time.perf_counter()

DEBUG = True
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
set_int_max_str_digits(0)
abc = ascii_lowercase
ABC = ascii_uppercase
dxy4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
dxy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x, file=stderr) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
YN = lambda x: print("Yes") if x else print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))
dxy = []
for i in range(-2, 3):
    for j in range(-2, 3):
        if abs(i) + abs(j) <= 2:
            dxy.append((i, j))
STATION_COST = 5000
LINE_COST = 100
N, M, K, T = MII()
c = [list(map(int, input().split())) for _ in range(M)]
real_score = 0
for si, sj, ti, tj in c:
    real_score += abs(si - ti) + abs(sj - tj)
cleared_cnt = 0
not_reach_cnt = M
by_station_cnt = 0
# print(f"{real_score=}")
point = [[[[0] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
for si, sj, ti, tj in c:
    for i, j in dxy:
        for ii, jj in dxy:
            if (
                si + i in range(N)
                and sj + j in range(N)
                and ti + ii in range(N)
                and tj + jj in range(N)
            ):
                point[si + i][sj + j][ti + ii][tj + jj] += abs(si - ti) + abs(sj - tj)

max_p = 0
min_t = inf
best = (-1, -1, -1, -1)
for i in range(N):
    for j in range(N):
        for ii in range(N):
            for jj in range(N):
                if (
                    point[i][j][ii][jj] != 0
                    and abs(i - ii) + abs(j - jj) - 1 <= (K - 10000) // 100
                    # and point[i][j][ii][jj] > max_p
                    and abs(i - ii) + abs(j - jj) + 7500 / point[i][j][ii][jj]
                    < min_t  # 7500円貯めるまでにかかる時間
                ):
                    max_p = point[i][j][ii][jj]
                    min_t = abs(i - ii) + abs(j - jj) + 7500 / point[i][j][ii][jj]
                    best = ((i, j), (ii, jj))


def calc_score(ni, nj, by_station, not_reach):
    # ni,njに駅を増設したとして，増加するスコアを計算する．
    score = 0
    sub_score = 0
    bi = ni // 5
    bj = nj // 5
    for p in range(-1, +2):
        for q in range(-1, +2):
            ii = bi + p
            jj = bj + q
            if ii in range(10) and jj in range(10):
                for i, j, dis in by_station[ii][jj]:
                    if abs(i - ni) + abs(j - nj) <= 2:
                        score += dis
                for si, sj, ti, tj in not_reach[ii][jj]:
                    if abs(si - ni) + abs(sj - nj) <= 2:
                        sub_score += abs(si - ti) + abs(sj - tj)
                    elif abs(ti - ni) + abs(tj - nj) <= 2:
                        sub_score += abs(si - ti) + abs(sj - tj)

    return score, sub_score


def add_station(ni, nj, by_station, not_reach):
    global cleared_cnt, not_reach_cnt, by_station_cnt
    # ni,njに駅を増設したとして，stations,not_reach,by_stationを更新する．

    nby_station = [[by_station[i][j][:] for j in range(10)] for i in range(10)]
    nnot_reach = [[not_reach[i][j][:] for j in range(10)] for i in range(10)]
    add_score = 0
    bi = ni // 5
    bj = nj // 5
    will_del = []
    for p in range(-1, +2):
        for q in range(-1, +2):
            ii = bi + p
            jj = bj + q
            if ii in range(10) and jj in range(10):
                nby_station[ii][jj] = []
                for i, j, dis in by_station[ii][jj]:
                    if abs(i - ni) + abs(j - nj) <= 2:
                        add_score += dis
                        cleared_cnt += 1
                        by_station_cnt -= 1
                        pass
                    else:
                        nby_station[ii][jj].append((i, j, dis))
    for p in range(-1, +2):
        for q in range(-1, +2):
            ii = bi + p
            jj = bj + q
            if ii in range(10) and jj in range(10):
                nnot_reach[ii][jj] = []
                for si, sj, ti, tj in not_reach[ii][jj]:
                    if abs(si - ni) + abs(sj - nj) <= 2:
                        nby_station[ti // 5][tj // 5].append(
                            (ti, tj, abs(si - ti) + abs(sj - tj))
                        )
                        not_reach_cnt -= 1
                        by_station_cnt = +1
                        will_del.append((si, sj, ti, tj))
                    else:
                        nnot_reach[ii][jj].append((si, sj, ti, tj))
    for si, sj, ti, tj in will_del:
        nnot_reach[ti // 5][tj // 5].remove((ti, tj, si, sj))
    # print(f"{not_reach_cnt=}, {by_station_cnt=}, {cleared_cnt=}")
    return add_score, nby_station, nnot_reach


stations = []

not_reach = [[[] for _ in range(10)] for _ in range(10)]
by_station = [[[] for _ in range(10)] for _ in range(10)]

for si, sj, ti, tj in c:
    not_reach[si // 5][sj // 5].append((si, sj, ti, tj))
    not_reach[ti // 5][tj // 5].append((ti, tj, si, sj))

# print(f"{not_reach_cnt=}, {by_station_cnt=}, {cleared_cnt=}")

score_a_day = 0
dis = [[inf] * N for _ in range(N)]
stations.append(best[0])
add_score, by_station, not_reach = add_station(*best[0], by_station, not_reach)


score_a_day += add_score
stations.append(best[1])
add_score, by_station, not_reach = add_station(*best[1], by_station, not_reach)
score_a_day += add_score

for i in range(N):
    for j in range(N):
        for x, y in stations:
            dis[i][j] = min(dis[i][j], abs(x - i) + abs(y - j))

while len(by_station) + len(not_reach) > 0:
    best_ij = (-1, -1)
    best_score = (0, 0, 0)
    for i in range(N):
        for j in range(N):
            d = inf
            for p, q in stations:
                d = min(d, abs(i - p) + abs(j - q))
            score, sub_score = calc_score(i, j, by_station, not_reach)
            if score == sub_score == 0:
                continue
            if best_score[0] < (score * 8 + sub_score):
                best_score = (score * 8 + sub_score, score, sub_score)
                best_ij = (i, j)
    # print(best_score, best_ij)
    if best_score[0] == 0:
        break

    stations.append(best_ij)
    add_score, by_station, not_reach = add_station(*best_ij, by_station, not_reach)
    # print(add_score, best_score)
    assert add_score == best_score[1]
    score_a_day += add_score


def add_path(ans, route, map):
    for i in range(1, len(route) - 1):
        dx1 = route[i][0] - route[i - 1][0]
        dx2 = route[i + 1][0] - route[i][0]
        dy1 = route[i][1] - route[i - 1][1]
        dy2 = route[i + 1][1] - route[i][1]
        if dx1 == dx2 == 0:
            ans.append((1, route[i][0], route[i][1]))
        elif dy1 == dy2 == 0:
            ans.append((2, route[i][0], route[i][1]))
        elif (dx1 == 0 and dx2 == 1 and dy1 == 1 and dy2 == 0) or (
            dx1 == -1 and dx2 == 0 and dy1 == 0 and dy2 == -1
        ):
            ans.append((3, route[i][0], route[i][1]))
        elif (dx1 == 0 and dx2 == -1 and dy1 == 1 and dy2 == 0) or (
            dx1 == 1 and dx2 == 0 and dy1 == 0 and dy2 == -1
        ):
            ans.append((4, route[i][0], route[i][1]))
        elif (dx1 == 1 and dx2 == 0 and dy1 == 0 and dy2 == 1) or (
            dx1 == 0 and dx2 == -1 and dy1 == -1 and dy2 == 0
        ):
            ans.append((5, route[i][0], route[i][1]))
        elif (dx1 == -1 and dx2 == 0 and dy1 == 0 and dy2 == 1) or (
            dx1 == 0 and dx2 == 1 and dy1 == -1 and dy2 == 0
        ):
            ans.append((6, route[i][0], route[i][1]))


def get_line_num(ai, aj, bi, bj, ci, cj):
    dx1 = bi - ai
    dx2 = ci - bi
    dy1 = bj - aj
    dy2 = cj - bj
    if dx1 == dx2 == 0:
        return (1, bi, bj)
    elif dy1 == dy2 == 0:
        return (2, bi, bj)
    elif (dx1 == 0 and dx2 == 1 and dy1 == 1 and dy2 == 0) or (
        dx1 == -1 and dx2 == 0 and dy1 == 0 and dy2 == -1
    ):
        return (3, bi, bj)
    elif (dx1 == 0 and dx2 == -1 and dy1 == 1 and dy2 == 0) or (
        dx1 == 1 and dx2 == 0 and dy1 == 0 and dy2 == -1
    ):
        return (4, bi, bj)
    elif (dx1 == 1 and dx2 == 0 and dy1 == 0 and dy2 == 1) or (
        dx1 == 0 and dx2 == -1 and dy1 == -1 and dy2 == 0
    ):
        return (5, bi, bj)
    elif (dx1 == -1 and dx2 == 0 and dy1 == 0 and dy2 == 1) or (
        dx1 == 0 and dx2 == 1 and dy1 == -1 and dy2 == 0
    ):
        return (6, bi, bj)


def bfs(si, sj, map, weight):
    weight[si][sj] = 0
    if map[si][sj] == 0:
        return [(si, sj)]
    map[si][sj] = 1

    frm = [[-1] * N for _ in range(N)]
    dis = [[-1] * N for _ in range(N)]
    sum_weight = [[-1] * N for _ in range(N)]
    best_weight = -1
    gx, gy = -1, -1
    min_dis = inf
    dis[si][sj] = 0
    frm[si][sj] = (-1, -1)
    sum_weight[si][sj] = 0
    deq = deque()
    deq.append((si, sj))

    while deq:
        x, y = deq.popleft()
        for i, j in dxy4:
            nx = x + i
            ny = y + j
            if nx in range(N) and ny in range(N) and map[nx][ny] != 0:
                if map[nx][ny] == 1 and (nx != si or ny != sj):
                    min_dis = dis[x][y] + 1
                    dis[nx][ny] = dis[x][y] + 1
                    if sum_weight[x][y] + weight[nx][ny] > best_weight:
                        frm[nx][ny] = (x, y)
                        gx, gy = nx, ny
                elif dis[x][y] + 1 <= min_dis:
                    if dis[nx][ny] == -1:
                        dis[nx][ny] = dis[x][y] + 1
                        deq.append((nx, ny))
                    if (
                        dis[nx][ny] == dis[x][y] + 1
                        and sum_weight[x][y] + weight[nx][ny] > sum_weight[nx][ny]
                    ):
                        frm[nx][ny] = (x, y)
                        sum_weight[nx][ny] = sum_weight[x][y] + weight[nx][ny]
    # assert gx != -1
    if gx == -1:
        return []
    x, y = gx, gy
    route = [(x, y)]
    for _ in range(dis[gx][gy]):
        x, y = frm[x][y]
        route.append((x, y))

    return route


def make_ans(stations):
    ans = []
    stations = stations[:]

    # 状態の初期化
    free = True
    fin = False
    index1 = 1
    index2 = 1
    now_K = K
    now_turn = 0
    score_a_day = 0
    map = [[-1] * N for _ in range(N)]
    weight = [[0] * N for _ in range(N)]
    for index, (i, j) in enumerate(stations):
        weight[i][j] = (len(stations) - index) ** 0.5
    not_reach = [[[] for _ in range(10)] for _ in range(10)]
    by_station = [[[] for _ in range(10)] for _ in range(10)]

    for si, sj, ti, tj in c:
        not_reach[si // 5][sj // 5].append((si, sj, ti, tj))
        not_reach[ti // 5][tj // 5].append((ti, tj, si, sj))

    # 1ターン目の処理
    ans.append((0, stations[0][0], stations[0][1]))
    map[stations[0][0]][stations[0][1]] = 1
    weight[stations[0][0]][stations[0][1]] = 0
    add_score, by_station, not_reach = add_station(*stations[0], by_station, not_reach)
    now_K -= 5000
    now_turn += 1
    score_a_day += add_score
    gain = []
    for t in range(1, T):
        if fin or index1 == len(stations):
            break
        if free and index1 < len(stations):
            while index1 < len(stations):
                route = bfs(*stations[index1], map, weight)
                if len(route) == 0:
                    index1 += 1
                else:
                    break
            if route:
                add_score, by_station, not_reach = add_station(
                    *stations[index1], by_station, not_reach
                )
                for i, j in route[1:-1]:
                    map[i][j] = 0
                # print(route)

                if len(route) > 1:
                    index2 = 1
                    if index1 > 1:
                        minus = (len(route) - 2) * LINE_COST + STATION_COST
                        complete_turn = t + max(
                            len(route) - 2,
                            ceil(
                                ((len(route) - 2) * LINE_COST + STATION_COST - now_K)
                                // score_a_day
                            ),
                        )
                        plus = (T - complete_turn) * add_score
                        # if minus > plus:
                        #     fin = True

                else:
                    index2 = 0
                    if index1 > 1:
                        minus = STATION_COST
                        complete_turn = t + max(
                            0,
                            ceil((STATION_COST - now_K) // score_a_day),
                        )
                        plus = (T - complete_turn) * add_score
                        # if minus > plus:
                        #     fin = True
            else:
                fin = True
            free = False
        if fin or index1 == len(stations):
            break

        if index2 < len(route) - 1:
            if now_K >= LINE_COST:
                now_K -= LINE_COST
                ans.append(
                    get_line_num(*route[index2 - 1], *route[index2], *route[index2 + 1])
                )
                index2 += 1
            else:
                ans.append((-1,))
        elif index2 == len(route) - 1:
            if now_K >= STATION_COST:
                now_K -= STATION_COST
                ans.append((0, *stations[index1]))
                free = True
                index1 += 1
                score_a_day += add_score
                gain.append(
                    (T - t) * add_score
                    - max(0, len(route) - 1) * LINE_COST
                    - STATION_COST
                )
            else:
                ans.append((-1,))
        now_K += score_a_day
    while gain and gain[-1] < 0:
        gain.pop()
        ans.pop()
        while ans[-1][0] >= 1:
            ans.pop()

    return ans, sum(gain)


best_ans = []
best_score = 0
ans, score = make_ans(stations)
best_score = score
best_ans = ans

# while time.perf_counter() - START < 2.7:
#     i = random.randrange(2, len(stations))
#     j = random.randrange(2, len(stations))
#     stations[i], stations[j] = stations[j], stations[i]
#     ans, score = make_ans(stations)
#     deb(score, best_score)
#     if score > best_score:
#         best_score = score
#         best_ans = ans
#     else:
#         stations[i], stations[j] = stations[j], stations[i]

while len(best_ans) < 800:
    best_ans.append((-1,))
for i in best_ans:
    print(*i)
    deb(*i)
# print(score)
deb(time.perf_counter() - START)
# make_map(stations)
