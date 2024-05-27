import sys
from bisect import bisect_left, bisect_right

n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]
lr.sort()
l = [i for i, j in lr]

ans = 0
for idx, (i, j) in enumerate(lr):
    ans += bisect_right(l, j) - idx - 1

print(ans)
