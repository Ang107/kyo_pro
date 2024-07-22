import sys

from heapq import heapify, heappop, heappush


# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
pritn = lambda *x: print(*x)
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))

h, w, p = MII()
a = [LMII() for _ in range(h)]
heap = []
visited = [[False] * w for _ in range(h)]
mask = (1 << 11) - 1
# print(bin(mask)[2:])


def hash(num, x, y):
    rslt = 0
    rslt |= num << 22
    rslt |= x << 11
    rslt |= y
    return rslt


def restore_hash(hash):
    num = (hash >> 22) & mask
    x = (hash >> 11) & mask
    y = hash & mask
    return num, x, y


for i in range(h):
    if 0 <= w - 1 < w and not visited[i][w - 1]:
        heap.append(hash(a[i][w - 1], i, w - 1))
        visited[i][w - 1] = True
    if not visited[i][0]:
        heap.append(hash(a[i][0], i, 0))
        visited[i][0] = True

for i in range(w):
    if 0 <= h - 1 < h and not visited[h - 1][i]:
        heap.append(hash(a[h - 1][i], h - 1, i))
        visited[h - 1][i] = True
    if not visited[0][i]:
        heap.append(hash(a[0][i], 0, i))
        visited[0][i] = True
heap.sort()

ans = h * w
for i in range(1, p + 1):
    while heap and heap[0] < ((i + 1) << 22):
        ans -= 1
        _, x, y = restore_hash(heappop(heap))
        for j, k in around4:
            nx, ny = x + j, y + k
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                visited[nx][ny] = True
                heappush(heap, hash(a[nx][ny], nx, ny))

    print(ans)
