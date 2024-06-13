import sys


def booking_confirmation(not_used: list[tuple[int, int]], n: int, l: int, r: int):
    def isOK(mid):
        return l <= not_used[mid][1]

    def binary_search(ng, ok):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if isOK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    # 二分探索を用いて、予約を入れられる可能性のある枠のインデックス番号を取得
    index = binary_search(-1, len(not_used) - 1)
    rslt = max(l, not_used[index][0])
    if rslt <= r and rslt <= not_used[index][1]:
        return rslt
    else:
        return -1


def main(lines: list[str]):
    n, m = map(int, lines[0].split())

    # 使用可能な枠番号を求める時の番兵として左端に0、右端にn+1を追加
    a = [0] + list(map(int, lines[1].split())) + [n + 1]
    q = int(lines[2])

    # 使用済みの枠番号
    # 連続しているところは左端と右端のみ管理
    used = []
    for i in range(m + 2):
        if not used or a[i - 1] + 1 < a[i]:
            used.append([a[i], a[i]])
        else:
            used[-1][1] = a[i]

    # 使用可能な枠番号
    # 連続しているところは左端と右端のみ管理
    not_used = []
    for i in range(1, len(used)):
        not_used.append((used[i - 1][1] + 1, used[i][0] - 1))

    for i in range(q):
        l, r = map(int, lines[3 + i].split())
        rslt = booking_confirmation(not_used, n, l, r)
        print(rslt)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
