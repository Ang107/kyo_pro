n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]


def solve_1(xy):
    def isnot_180_over(a, b, c):
        return (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0]) > 0

    def get_s(a, b, c):
        return abs((a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])) / 2

    xy_n = []
    xy_hekomi = []
    for i in range(n):
        if isnot_180_over(xy[i - 1], xy[i], xy[(i + 1) % n]):
            xy_n.append(xy[i])
        else:
            xy_hekomi.append((xy[i - 1], xy[i], xy[(i + 1) % n]))
    ans = 0

    for i in range(1, len(xy_n) - 1):
        ans += get_s(xy_n[0], xy_n[i], xy_n[i + 1])

    for a, b, c in xy_hekomi:
        ans -= get_s(a, b, c)
    return ans


def solve_2(coords):
    """多角形の面積を計算する関数。座標は(x, y)のタプルのリストとして渡される。"""
    n = len(coords)
    area = 0
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]  # 最後の点の次は最初の点に戻る
        area += x1 * y2 - y1 * x2
    return abs(area) / 2


print(solve_1(xy), solve_2(xy))
