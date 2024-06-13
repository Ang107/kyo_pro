import sys

from sortedcontainers import SortedSet


def main(lines: list[str]):
    n, q = map(int, lines[0].split())
    LR = [list(map(int, lines[1 + i].split())) for i in range(n)]
    # 常にソートした順番で管理でき、削除・追加がO(logN)で行えるSortedSetを用いる。
    # スコアが同じ場合、番号が小さいほどスコアが高くなることを考慮するため、タプルで管理する。
    L = SortedSet([(-l, idx) for idx, (l, r) in enumerate(LR)])
    R = SortedSet([(-r, idx) for idx, (l, r) in enumerate(LR)])

    for i in range(q):
        query = list(map(int, lines[1 + n + i].split()))
        if query[0] == 1:
            x, l_new, r_new = query[1:]
            x -= 1
            l_old, r_old = LR[x]
            L.discard((-l_old, x))
            L.add((-l_new, x))
            R.discard((-r_old, x))
            R.add((-r_new, x))
            LR[x] = [l_new, r_new]
        else:
            x = query[1]
            result = 0
            # x位以上になるための最低スコア
            border = L[x - 1]
            result = R.bisect_right(border)
            print(result)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
