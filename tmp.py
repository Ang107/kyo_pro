n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
from bisect import bisect_right

for i in range(n):
    ans += bisect_right(a, a[i] + k) - i - 1
print(ans)
