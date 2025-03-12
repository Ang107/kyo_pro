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

DEBUG = False
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
N, M, K, T = MII()
c = [list(map(int, input().split())) for _ in range(M)]

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
tmp = []
for i in range(N):
    for j in range(N):
        for ii in range(N):
            for jj in range(N):
                tmp.append(point[i][j][ii][jj])
print(sorted(tmp, reverse=True)[:300])


def calc_score(ni, nj, by_station, not_reach):
    # ni,njに駅を増設したとして，増加するスコアを計算する．
    score = 0
    for i, j, dis in by_station:
        if abs(i - ni) + abs(j - nj) <= 2:
            score += dis
    return score


def add_station(ni, nj, stations, by_station, not_reach):
    # ni,njに駅を増設したとして，stations,not_reach,by_stationを更新する．
    stations.append((ni, nj))
    nby_station = []
    nnot_reach = []

    for i, j, dis in by_station:
        if abs(i - ni) + abs(j - nj) <= 2:
            pass
        else:
            nby_station.append((i, j, dis))
    for si, sj, ti, tj in not_reach:
        if abs(si - ni) + abs(sj - nj) <= 2:
            nby_station.append((ti, tj, abs(si - ti) + abs(sj - tj)))
        elif abs(ti - ni) + abs(tj - nj) <= 2:
            nby_station.append((si, sj, abs(si - ti) + abs(sj - tj)))
        else:
            nnot_reach.append((si, sj, ti, tj))
    return nby_station, nnot_reach


# def bfs(sx, sy, visited):
#     visited = [i[:] for i in visited]
#     deq = deque()
#     deq.append((sx, sy))
#     while deq:
#         x, y = deq.popleft()
#         for i, j in dxy4:
#             nx = x + i
#             ny = y + j
#             if visited[nx][ny] == -1:
#                 deq.append((nx, ny))
#                 visited[nx][ny] = (x, y)
#             elif visited[nx][ny] == 1:
#                 route = []
#                 x, y = nx, ny
#                 while x != sx or y != sy:
#                     route.append((x, y))
#                     x, y = visited[x][y]
#                 return route[::-1]
#     return -1


# def make_root(stations):
#     # best_g = [[[] for _ in range(N)] for _ in range(N)]
#     best_visited = [[[] for _ in range(N)] for _ in range(N)]
#     min_length = inf
#     for x, y in stations:
#         length = 1
#         visited = [[-1] * N for _ in range(N)]
#         for i, j in stations:
#             visited[i][j] = 1

#         for _ in range(len(stations) - 1):
#             route = bfs(x, y, visited)
#             if route == -1:
#                 length = inf
#                 break
#             else:
#                 for nx, ny in route:
#                     visited[nx][ny] = x, y
#                     x, y = nx, ny
#                 length += len(route)
#         if min_length > length:
#             best_visited = visited
#             min_length = length
#     return length, best_visited


# def bfs(sx, sy, visited):
#     visited_c = [i[:] for i in visited]
#     deq = deque()
#     deq.append((sx, sy))
#     while deq:
#         x, y = deq.popleft()
#         for i, j in dxy4:
#             nx = x + i
#             ny = y + j
#             if visited_c[nx][ny] == -1:
#                 deq.append((nx, ny))
#                 visited_c[nx][ny] = (x, y)
#             elif visited_c[nx][ny] == 1:
#                 route = []
#                 route.append((x, y))


#                 while True:
#                     x, y = visited_c[x][y]
#                     route.append((x, y))
#                     if x == sx and y == sy:
#                         break
#                 return route[::-1]
#     return -1
def bfs(stations, visited):
    dis = [[-1] * N for _ in range(N)]
    deq = deque(stations)
    for i, j in stations:
        dis[i][j] = (0, -1, -1)
    while deq:
        x, y = deq.popleft()
        for i, j in dxy4:
            nx = x + i
            ny = y + j
            if (
                nx in range(N)
                and ny in range(N)
                and dis[nx][ny] == -1
                and visited[nx][ny] == -1
            ):
                dis[nx][ny] = (dis[x][y][0] + 1, x, y)
                deq.append((nx, ny))
    return dis


def make_route(sx, sy, dis):
    route = []
    x, y = sx, sy

    route.append((x, y))
    while True:
        d, x, y = dis[x][y]
        route.append((x, y))
        if d == 0:
            break
    return route[::-1]


def add_path(ans, route, map):
    for i in range(1, len(route) - 1):
        if map[route[i][0]][route[i][1]] == 1:
            continue

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
                    < min_t  # 5500円貯めるまでにかかる時間
                ):
                    max_p = point[i][j][ii][jj]
                    min_t = abs(i - ii) + abs(j - jj) + 7500 / point[i][j][ii][jj]
                    best = (i, j, ii, jj)
ans = []
stations = []
not_reach = [i[:] for i in c]
by_station = []
now_k = K
now_turn = 0
visited = [[-1] * N for _ in range(N)]
by_station, not_reach = add_station(best[0], best[1], stations, by_station, not_reach)
visited[best[0]][best[1]] = 1

dis = bfs(stations, visited)
route = make_route(best[2], best[3], dis)
minus = 5000 * 2 + (len(route) - 1) * 100
point_a_day = point[best[0]][best[1]][best[2]][best[3]]

plus = (800 - now_turn - 2 - (len(route) - 1)) * point_a_day
if minus < plus:
    visited[route[0][0]][route[0][1]] = 1
    add_path(ans, route)
    ans.append((0, best[0], best[1]))
    ans.append((0, best[2], best[3]))
    for i, j in route:
        visited[i][j] = 1
    by_station, not_reach = add_station(
        best[2], best[3], stations, by_station, not_reach
    )

    now_k -= 5000 * 2
    now_k -= (len(route) - 2) * 100
    now_turn = len(ans)

    while True:
        print(len(not_reach), len(by_station))
        best_last_score = 0
        best_next_7500 = inf
        best_ij = (-1, -1)
        best_score = 0
        dis = bfs(stations, visited)
        for i in range(N):
            for j in range(N):
                if dis[i][j] == -1 or dis[i][j][0] <= 0:
                    continue
                d = dis[i][j][0] - 1
                if visited[i][j] != -1:
                    d = 0
                score = calc_score(i, j, by_station, not_reach)
                minus = 5000 + (d - 1) * 100
                need_turn = max(d + 1, -(-(minus - now_k) // point_a_day))
                # print(i, j, score, minus)
                if now_turn + need_turn >= 800:
                    continue
                plus = (800 - now_turn - 2 - (d - 1)) * score
                if now_turn <= 600:
                    if best_last_score < plus - minus:
                        best_last_score = plus - minus
                        best_ij = (i, j)
                        best_score = score
                else:
                    if point_a_day * d > 7500:
                        next_7500 = d
                    else:
                        next_7500 = d + (7500 - point_a_day * d) / (point_a_day + score)
                    if plus - minus > 0 and next_7500 < best_next_7500:
                        best_next_7500 = next_7500
                        best_ij = (i, j)
                        best_score = score

        if best_ij != (-1, -1):
            i, j = best_ij
            minus = 5000 + (dis[i][j][0] - 1) * 100
            need_turn = -(-(minus - now_k) // point_a_day)
            for _ in range(need_turn - dis[i][j][0]):
                ans.append((-1,))
            route = make_route(i, j, dis)
            for i, j in route:
                visited[i][j] = 1
            add_path(ans, route)
            ans.append((0, i, j))
            by_station, not_reach = add_station(i, j, stations, by_station, not_reach)
            now_k -= minus
            now_k += need_turn * point_a_day
            now_k += best_score
            now_turn = len(ans)
            point_a_day += best_score
        else:
            break
while len(ans) < 800:
    ans.append((-1,))

for i in ans:
    print(*i)
