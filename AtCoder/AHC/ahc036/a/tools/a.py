from collections import deque

n, m, t, la, lb = map(int, input().split())
print(m, la, lb)
# ed = [[] for _ in range(n)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     ed[u].append(v)
#     ed[v].append(u)
# ts = [0] + list(map(int, input().split()))


# def bfs(s, g):
#     deq = deque()
#     visited = [-1] * n
#     deq.append(s)
#     visited[s] = 0
#     while deq:
#         now = deq.popleft()
#         if now == g:
#             break
#         for next in ed[now]:
#             if visited[next] == -1:
#                 deq.append(next)
#                 visited[next] = visited[now] + 1
#     return visited[g]


# diss = []
# for i in range(t):
#     diss.append(bfs(ts[i], ts[i + 1]))
# print(m, sum(diss), diss)
