import sys
import time

START = time.perf_counter()

# product : bit全探索 product(range(2),repeat=n)
# permutations : 順列全探索
# combinations : 組み合わせ（重複無し）
# combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
P = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

n, m = MII()
d = [[True] * n for _ in range(n)]
relation = [[] for _ in range(n)]
# 有り得ない順位を順次確定
for _ in range(m):
    a, b, c = MII()
    a -= 1
    b -= 1
    for i in range(0, c):
        d[a][i] = False
    for i in range(n - c, n):
        d[b][i] = False
    relation[a].append((b, -c))
    relation[b].append((a, +c))
ans = {}


# 一人を除き全てFalse -> Trueで確定
# 乱択で選ぶ
import random

d_tenti = [[None] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        d_tenti[j][i] = d[i][j]

kakutei_person = [-2] * n
kakutei_number = [-2] * n
cnt = 0


def kakutei(number, person):
    kakutei_person[person] = number
    kakutei_number[number] = person
    for i in range(n):
        if i != person:
            d[i][number] = False
            d_tenti[number][i] = False
    for p, diff in relation[person]:
        if kakutei_person[p] == -2:
            # print(number, diff, number + diff)
            kakutei(p, number + diff)


while True:
    cnt += 1
    if cnt % 100 == 0 and time.perf_counter() - START > 1.8:
        break
    tateyoko = random.choice(range(2))

    if tateyoko == 0:
        person = random.choice(range(n))
        if kakutei_person[person] != -2:
            continue
        tmp = [i for i in range(n) if d[person][i]]
        number = tmp[0]
        if len(tmp) == 1:
            kakutei(number, person)
    else:
        number = random.choice(range(n))
        if kakutei_number[number] != -2:
            continue
        tmp = [i for i in range(n) if d_tenti[number][i]]
        person = tmp[0]
        if len(tmp) == 1:
            kakutei(number, person)

print(*[i + 1 for i in kakutei_person])
