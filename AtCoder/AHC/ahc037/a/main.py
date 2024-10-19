def main():
    import sys
    import math
    import random

    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 初期化
    operations = []
    added_points = set()
    added_points.add((0, 0))
    parents = {}
    max_operations = 5000

    # 点をソート（左下から右上へ）
    points.sort()

    # クラスタリングの準備
    cluster_size = int(math.sqrt(N))
    clusters = [[] for _ in range(cluster_size)]
    for idx, point in enumerate(points):
        clusters[idx % cluster_size].append(point)

    # 各クラスタ内で処理
    for cluster in clusters:
        cluster.sort()
        cluster_root = None
        for i, j in cluster:
            # 既存の点から最も近い点を探す
            min_cost = float("inf")
            min_point = None
            for p, q in added_points:
                if p <= i and q <= j:
                    cost = (i - p) + (j - q)
                    if cost < min_cost:
                        min_cost = cost
                        min_point = (p, q)
            if min_point is None:
                # 追加できない場合は (0, 0) を親とする
                min_point = (0, 0)
                min_cost = i + j
            # 操作を記録
            operations.append((min_point[0], min_point[1], i, j))
            added_points.add((i, j))
            parents[(i, j)] = min_point
            # 操作回数のチェック
            if len(operations) >= max_operations:
                break
        if len(operations) >= max_operations:
            break

    # 操作回数が足りない場合、ランダムに追加点を挿入してコストを削減
    while len(operations) < max_operations:
        # ランダムな点を選ぶ
        (i1, j1), (i2, j2) = random.sample(added_points, 2)
        if i1 <= i2 and j1 <= j2 and (i2, j2) not in parents:
            operations.append((i1, j1, i2, j2))
            parents[(i2, j2)] = (i1, j1)
        if len(added_points) >= N + 1000:  # 追加点が多すぎないように
            break

    # 出力
    print(len(operations))
    for op in operations:
        print(*op)


if __name__ == "__main__":
    main()
