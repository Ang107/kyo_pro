import sys
from functools import cache
import resource

resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
sys.setrecursionlimit(10**7)
inf = float("inf")
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = list(map(int, input().split()))


@cache
def f(x, turn):
    if x == 0:
        return 0
    if turn == 0:
        result = 0
        for i in a:
            if i <= x:
                result = max(result, i + f(x - i, turn ^ 1))
            else:
                break
        return result
    else:
        result = inf
        for i in a:
            if i <= x:
                result = min(result, f(x - i, turn ^ 1))
            else:
                break
        return result


print(f(n, 0))
