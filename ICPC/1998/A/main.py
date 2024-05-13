n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]


def is_180_over(a, b, c):
    return (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0]) > 0


def get_s(a, b, c):
    return abs((a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])) / 2


xy_n = []
xy_hekomi = []
for i in range(n):
    if is_180_over(xy[i - 1], xy[i], xy[(i + 1) % n]):
        xy_n.append(xy[i])
    else:
        xy_hekomi.append((xy[i - 1], xy[i], xy[(i + 1) % n]))
ans = 0

for i in range(1, len(xy_n) - 1):
    ans += get_s(xy_n[0], xy_n[i], xy_n[i + 1])

for a, b, c in xy_hekomi:
    ans -= get_s(a, b, c)

print(ans)
