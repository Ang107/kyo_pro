from heapq import heappop, heappush

inf = float("inf")


# ed=隣接リスト[(next, weight)], 初期ノード
def dijkstra(ed, st):
    # 初期化
    n = len(ed)
    visited = [False] * n
    distance = [inf] * n
    distance[st] = 0
    heap = [(0, st)]
    # ダイクストラ
    while heap:
        dis, v = heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        for next, weight in ed[v]:
            if not visited[next]:
                new_distance = distance[v] + weight
                if new_distance < distance[next]:
                    distance[next] = new_distance
                    heappush(heap, (new_distance, next))
    return distance
