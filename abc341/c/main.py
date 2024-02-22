# coding: utf-8
# Your code here!

h, w, n = map(int, input().split())

t = input()


# ↑ → ↓ ← (4方向)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
lrud = {"L": 3, "R": 1, "U": 0, "D": 2}

tmp = []
for i in t:
    tmp.append(lrud[i])
t = tmp

grid = []


def is_walk(t, y, x):
    yy = y
    xx = x
    for i in t:
        yy += dy[i]
        xx += dx[i]

        if not (0 <= yy < h - 1 and 0 <= xx <= w - 1 and grid[yy][xx] != "#"):
            return False

    return True


ans = 0

for y in range(h):
    grid.append(list(input()))

for y in range(h):
    for x in range(w):
        if grid[y][x] != "#":
            if is_walk(t, y, x):
                ans += 1


print(ans)
