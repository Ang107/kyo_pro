ans = []
while True:
    h, w = map(int, input().split())
    if h == 0:
        break
    s = [input() for _ in range(h)]
    t = input()
    # memo = {}
    # from functools import cache

    # @cache
    # def bfs(px, py, g):
    #     if (px, py, g) in memo:
    #         return memo[(px, py, g)]
    #     from collections import deque

    #     deq = deque()
    #     deq.append((px, py))
    #     visited = [[-1] * w for _ in range(h)]
    #     visited[px][py] = 0
    #     while deq:
    #         x, y = deq.popleft()
    #         if s[x][y] == g:
    #             memo[(px, py, g)] = visited[x][y], x, y
    #             return visited[x][y], x, y
    #         for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #             if (
    #                 x + i in range(h)
    #                 and y + j in range(w)
    #                 and visited[x + i][y + j] == -1
    #             ):
    #                 deq.append((x + i, y + j))
    #                 visited[x + i][y + j] = visited[x][y] + 1

    # x, y = 0, 0
    # r = 0
    # for i in t:
    #     dis, x, y = bfs(x, y, i)
    #     r += dis + 1
    # ans.append(r)
    from collections import defaultdict
    
    dis = [[defaultdict(lambda :1000000) for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            
            
for i in ans:
    print(i)
