from itertools import (
    permutations,  # permutations : 順列全探索
)

n, k = map(int, input().split())
s = input()
ans = 0
base = ord("a")


def is_kaubun(j):
    for i in range(k // 2):
        if s[j + i] == s[j + k - 1 - i]:
            pass
        else:
            return False
    return True


def f():
    for i in range(len(s) - k + 1):
        if is_kaubun(i):
            return False
    return True


for s in permutations(s):
    if f():
        ans += 1

memo = [1] * (n + 1)
for i in range(1, n + 1):
    memo[i] = memo[i - 1] * i
cnt = [0] * 26
for i in s:
    cnt[ord(i) - base] += 1

for i in cnt:
    ans //= memo[i]
print(ans)
