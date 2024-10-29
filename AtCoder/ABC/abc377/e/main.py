from sys import stdin, setrecursionlimit
from collections import deque, defaultdict
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from math import ceil, floor, log, log2, sqrt, gcd, lcm
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from functools import cache
from string import ascii_lowercase, ascii_uppercase

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
alph_s = ascii_lowercase
alph_l = ascii_uppercase
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 上下左右
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float("inf")
mod = 998244353
input = lambda: stdin.readline().rstrip()
pritn = lambda *x: print(*x)
deb = lambda *x: print(*x) if DEBUG else None
PY = lambda: print("Yes")
PN = lambda: print("No")
SI = lambda: input()
IS = lambda: input().split()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(map(int, input().split()))


n, k = MII()
p = LMII()
next = [i - 1 for i in p]


class FunctionalGraph:
    def __init__(self, n: int, next: list[int]) -> None:
        self.n = n
        self.sqrt_n = int(n**0.5)
        self.nexts = next
        self.jumps = [-1] * self.n
        self.visited = [False] * self.n
        self.cycles = [-1] * self.n
        self.cycles_index = [-1] * self.n
        self.calc_cycles()
        self.calc_jumps()

    def calc_jumps(self) -> None:
        for s in range(self.n):
            now = s
            for _ in range(self.sqrt_n):
                now = next[now]
            self.jumps[s] = now

    def calc_cycles(self) -> None:
        for s in range(self.n):
            if not self.visited[s]:
                path, cycle = self.dfs(s)
                for i, v in enumerate(cycle):
                    self.cycles[v] = cycle
                    self.cycles_index[v] = i

    def dfs(self, s: int) -> tuple[list[int], list[int]]:
        stack = [s]
        path = [s]
        cycle = []
        self.visited[s] = True
        while stack:
            now = stack.pop()
            next = self.nexts[now]
            if not self.visited[next]:
                stack.append(next)
                self.visited[next] = True
                path.append(next)
        next = self.nexts[path[-1]]
        index = 0
        while index < len(path):
            if path[index] == next:
                path, cycle = path[:index], path[index:]
                break
            index += 1
        return path, cycle

    # 頂点sのk個先の頂点を返す
    def get_next(self, s: int, k: int) -> int:
        now = s
        while self.cycles[now] == -1 and k > 0:
            if k >= self.sqrt_n:
                k -= self.sqrt_n
                now = self.jumps[now]
            else:
                k -= 1
                now = self.nexts[now]
        if k == 0:
            return now
        cycle_len = len(self.cycles[now])
        now = self.cycles[now][
            (self.cycles_index[now] + pow(2, k, cycle_len)) % cycle_len
        ]
        return now


FG = FunctionalGraph(n, next)
ans = [-1] * n
for i in range(n):
    ans[i] = FG.get_next(i, k) + 1
print(*ans)
