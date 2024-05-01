import time

start = time.perf_counter()
from collections import deque
import sys


around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右

input = lambda: sys.stdin.readline().rstrip()
MII = lambda: map(int, input().split())


h, w = MII()
s = [input() for _ in range(h)]

around_zisyaku = [[False] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            continue
        for x, y in around4:
            if x + i in range(h) and y + j in range(w):
                if s[x + i][y + j] == "#":
                    around_zisyaku[i][j] = True


def dfs(x, y):
    deq = deque()
    visited_local = set()
    deq.append((x, y))
    visited_local.add(x * w + y)
    while deq:
        x, y = deq.pop()
        # 動けないなら
        if around_zisyaku[x][y]:
            continue

        # 動けるなら
        for i, j in around4:
            if (
                x + i in range(h)
                and y + j in range(w)
                and (x + i) * w + y + j not in visited_local
                and s[x + i][y + j] != "#"
            ):
                deq.append((x + i, y + j))
                visited_local.add((x + i) * w + y + j)
    return len(visited_local)


ans = 1
import random


while time.perf_counter() - start <= 1.8:
    i = random.choice(range(h))
    j = random.choice(range(w))
    if s[i][j] != "#":
        result = dfs(i, j)
        ans = max(ans, result)


print(ans)
