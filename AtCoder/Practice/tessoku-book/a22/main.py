from heapq import heappop, heappush

n = int(input())
a = list(map(int, input().split()))
a = [i - 1 for i in a]
b = list(map(int, input().split()))
b = [i - 1 for i in b]
assert all(i <= a[i] <= b[i] for i in range(n - 1))
heap = [(0, 0)]
visited = [-(1 << 63)] * n
visited[0] = 0
cnt = 0
while heap:
    print(len(heap))
    s, v = heappop(heap)
    cnt += 1
    s = -s
    if s < visited[v]:
        continue
    if s + 100 > visited[a[v]]:
        visited[a[v]] = s + 100
        if a[v] < n - 1:
            heappush(heap, (-(s + 100), a[v]))
    if s + 150 > visited[b[v]]:
        visited[b[v]] = s + 150
        if b[v] < n - 1:
            heappush(heap, (-(s + 150), b[v]))
print(visited[n - 1])
print(cnt)
