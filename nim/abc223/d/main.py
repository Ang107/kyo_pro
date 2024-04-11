import heapq


def read_ints():
    return map(int, input().split())


n, m = read_ints()
ab = [set() for _ in range(n + 1)]
ba = [set() for _ in range(n + 1)]
ans = []
all_num = set(range(1, n + 1))

for _ in range(m):
    a, b = read_ints()
    ba[b].add(a)
    ab[a].add(b)
    all_num.discard(b)

hq = list(all_num)
heapq.heapify(hq)

while hq:
    tmp = heapq.heappop(hq)
    ans.append(tmp)
    if ab[tmp]:
        for i in list(ab[tmp]):
            ba[i].discard(tmp)
            if not ba[i]:
                heapq.heappush(hq, i)

if len(ans) == n:
    print(" ".join(map(str, ans)))
else:
    print(-1)
