p = list(map(int, input().split()))


def f(p, q):
    n = len(p)
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if sum(p[i:j]) == sum(q[i:j]):
                cnt += 1
    return cnt


ans_list = []
min_score = 1 << 63
from itertools import permutations

for q in permutations(p):
    r = f(p, q)
    if min_score > f(p, q):
        min_score = r
        ans_list = [q]
    elif min_score == r:
        ans_list.append(q)
print(min_score)
print(ans_list)
