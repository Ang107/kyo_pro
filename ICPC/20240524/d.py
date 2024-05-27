ans = []
while True:
    N, M = map(int, input().split())
    if N == 0:
        break
    from collections import defaultdict

    dd = defaultdict(int)
    for _ in range(N):
        d, v = map(int, input().split())
        dd[d] = max(dd[d], v)
    ans.append(sum(dd.values()))
for i in ans:
    print(i)
