from sys import stdin, setrecursionlimit

DEBUG = False
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")
# 外部ライブラリ
# from sortedcontainers import SortedSet, SortedList, SortedDict
setrecursionlimit(10**7)
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
x = LMII()
a = LMII()
next = [i - 1 for i in x]


class FunctionalGraph:
    # O(N√N)
    def __init__(self, n: int, next: list[int]) -> None:
        self.n = n
        self.sqrt_n = int(n**0.5)
        self.nexts = next
        self.prevs = [-1] * n
        for i, j in enumerate(next):
            self.prevs[j] = i
        self.jumps = [-1] * self.n
        self.visited = [False] * self.n
        self.cycles = [-1] * self.n
        self.dis_to_cycle = [-1] * self.n

        self.calc_cycles()
        self.calc_jumps()

    def calc_jumps(self) -> None:
        self.dis_to_cycle_sorted = [(j, i) for i, j in enumerate(self.dis_to_cycle)]
        self.dis_to_cycle_sorted.sort(key=lambda x: x[0], reverse=True)
        for _, s in self.dis_to_cycle_sorted:
            now = s
            if self.prevs[now] != -1 and self.jumps[self.prevs[now]] != -1:
                self.jumps[s] = self.nexts[self.jumps[self.prevs[now]]]
            else:
                for _ in range(self.sqrt_n):
                    now = next[now]
                self.jumps[s] = now

    def calc_cycles(self) -> None:
        for s in range(self.n):
            if not self.visited[s]:
                path, cycle = self.dfs(s)
                for i, v in enumerate(cycle):
                    self.cycles[v] = cycle
                    self.dis_to_cycle[v] = -i
                if cycle:
                    for i, v in enumerate(path[::-1], start=1):
                        self.cycles[v] = cycle
                        self.dis_to_cycle[v] = i
                else:
                    dis = self.dis_to_cycle[self.nexts[path[-1]]]
                    for i, v in enumerate(path[::-1], start=1):
                        self.cycles[v] = self.cycles[self.nexts[path[-1]]]
                        self.dis_to_cycle[v] = dis + i

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

    # 頂点sのk個先の頂点を返す O(√N)
    def get_next(self, s: int, k: int) -> int:
        if k == 0:
            return s
        now = s

        if k >= self.dis_to_cycle[now]:
            cycle_len = len(self.cycles[now])
            return self.cycles[now][(k - self.dis_to_cycle[now]) % cycle_len]

        while self.dis_to_cycle[now] > 0 and k > 0:
            if k >= self.sqrt_n:
                k -= self.sqrt_n
                now = self.jumps[now]
            else:
                k -= 1
                now = self.nexts[now]
        return now

    # 頂点sのk個先の頂点を返す O(N√N)
    def get_next_all(self, k: int) -> int:
        if k == 0:
            return list(range(self.n))
        result = [-1] * n
        for _, s in self.dis_to_cycle_sorted:
            now = s
            if self.prevs[now] != -1 and result[self.prevs[now]] != -1:
                result[s] = self.nexts[result[self.prevs[now]]]
                continue
            if k >= self.dis_to_cycle[now]:
                cycle_len = len(self.cycles[now])
                result[s] = self.cycles[now][(k - self.dis_to_cycle[now]) % cycle_len]
                continue

            while k > 0:
                if k >= self.sqrt_n:
                    k -= self.sqrt_n
                    now = self.jumps[now]
                else:
                    k -= 1
                    now = self.nexts[now]
            result[s] = now

        return result


FG = FunctionalGraph(n, next)
ans = [FG.get_next(i, k) for i in range(n)]
for i in range(n):
    ans[i] = a[ans[i]]
print(*ans)
