# AHC用のテンプレート
import std/times
import std/random
import atcoder/segtree
# import nimprof
{.checks: off.}
import macros
macro ImportExpand(s: untyped): untyped = parseStmt($s[2])
# https://atcoder.jp/users/kemuniku さんのマクロを勝手に借りてます。
ImportExpand "cplib/tmpl/sheep.nim" <=== "when not declared CPLIB_TMPL_SHEEP:\n    const CPLIB_TMPL_SHEEP* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`*(x: int, y: int): int =\n        result = x mod y\n        if y > 0 and result < 0: result += y\n        if y < 0 and result > 0: result += y\n    proc `//`*(x: int, y: int): int{.inline.} =\n        result = x div y\n        if y > 0 and result * y > x: result -= 1\n        if y < 0 and result * y < x: result -= 1\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    #[ include cplib/utils/constants ]#\n    when not declared CPLIB_UTILS_CONSTANTS:\n        const CPLIB_UTILS_CONSTANTS* = 1\n        const INF32*: int32 = 100100111.int32\n        const INF64*: int = int(3300300300300300491)\n    const INF = INF64\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n\n    #joinが非stringでめちゃくちゃ遅いやつのパッチ\n    proc join*[T: not string](a: openArray[T], sep: string = \"\"): string = a.mapit($it).join(sep)\n"
# -----------------------------------------------------------------------

# uint64(bitset, hash)用のbit演算定義
proc `|`(x, y: uint64): uint64 {.inline.} =
    return x or y
proc `&`(x, y: uint64): uint64 {.inline.} =
    return x and y
proc `^`(x, y: uint64): uint64 {.inline.} =
    return x xor y
proc `|=`(x: var uint64, y: uint64) {.inline.} =
    x = x or y
proc `&=`(x: var uint64, y: uint64) {.inline.} =
    x = x and y
proc `^=`(x: var uint64, y: uint64) {.inline.} =
    x = x xor y
proc `>>`(x: uint64, y: int): uint64 {.inline.} =
    return x shr y
proc `<<`(x: uint64, y: int): uint64 {.inline.} =
    return x shl y
proc `>>=`(x: var uint64, y: int) {.inline.} =
    x = x shr y
proc `<<=`(x: var uint64, y: int) {.inline.} =
    x = x shl y
proc `~`(x: uint64): uint64 {.inline.} =
    return not x
proc `[]`(x: uint64, y: int): bool {.inline.} =
    return bool((x shr y) & 1)
proc `[]=`(x: var uint64, y: int, z: int) {.inline.} =
    if z == 0:
        x &= uint64(~(1 << y))
    elif z == 1:
        x |= uint64(1 << y)
    else:
        raiseAssert "zは 0,1 しか受け取れません。"
proc add(x: var uint64, y: int){.inline.} =
    x |= uint64(1 << y)
proc remove(x: var uint64, y: int){.inline.} =
    x &= uint64(~(1 << y))

# -----------------------------------------------------------------------

# 定数
const
    TIME_LIMIT = 2.0
    N = 1000
    MAXAB = 10**9-1
    # TODO

# -----------------------------------------------------------------------

# 入力を管理するオブジェクト
type Input = object
    N: int
    AB: array[N, (int, int)]

proc input(self: var Input) =
    self.N = N
    var n = ii()
    for i in 0..<n:
        var tmp = lii(2)
        self.AB[i] = (tmp[0], tmp[1])

# -----------------------------------------------------------------------

# 出力を管理するオブジェクト
type Output = object
    actions: seq[array[4, int]]
proc output(self: Output) =
    var cost = 0
    stdout.writeLine(len(self.actions))
    for i in self.actions:
        cost += i[2] + i[3] - i[0] - i[1]
        echo i.join(" ")
    stderr.writeLine(cost//100000)

# -----------------------------------------------------------------------

# 時間管理を行うオブジェクト
type Time = object
    START: float
    TIME_LIMIT: float

# コンストラクタ
proc new_time(TIME_LIMIT: float): Time =
    var START = cpuTime()
    return Time(START: START, TIME_LIMIT: TIME_LIMIT)

# 経過した時間(second)を返す
proc get_passed_time(self: Time): float =
    return cpuTime() - self.START

# 残りの時間(second)を返す
proc get_have_time(self: Time): float =
    return self.TIME_LIMIT - (cpuTime() - self.START)

# 経過時間を標準エラーに出力する。
proc out_paased_time(self: Time) =
    stderr.writeLine($(cpuTime() - self.START))

# -----------------------------------------------------------------------

type Solver = object
    input: Input
    time: Time


proc new_solver(input: Input, time: Time): Solver =
    return Solver(input: input, time: time)
proc make_actions(c: seq[(int, int)]): seq[array[4, int]] =
    var cand = c
    result = newSeqOfCap[array[4, int]](cand.len())
    cand.sort()
    cand = cand.deduplicate(isSorted = true)
    var added = newSeqOfCap[(int, int)](cand.len())
    added.add((0, 0))
    for (i, j) in cand:
        if i == 0 and j == 0:
            continue
        var
            pi, pj = -1
            min_cost = INF64
        for (k, l) in added:
            var new_cost = (i-k) + (j-l)
            if k <= i and l <= j and new_cost < min_cost:
                min_cost = new_cost
                pi = k
                pj = l
        added.add((i, j))
        result.add([pi, pj, i, j])
    return result

proc optimize_actions(cand: var seq[(int, int)], actions: var seq[array[4, int]]) =
    var
        same_root = initTable[(int, int), seq[(int, int)]]()

    for action in actions:
        var
            i = action[0]
            j = action[1]
            k = action[2]
            l = action[3]
        if (i, j) notin same_root:
            same_root[(i, j)] = newSeq[(int, int)](0)
        same_root[(i, j)].add((k, l))

    for (k, v) in same_root.pairs():
        var min_i = INF64
        var min_j = INF64
        var max_i = -1
        var max_j = -1
        for (i, j) in v:
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)
        var
            best_way = -1
            best_cost = INF64
        var cost = max_j - k[1]
        for (i, j) in v:
            cost += i - min_i
            # cand.add((min_i, j))
        if cost < best_cost:
            best_cost = cost
            best_way = 0

        cost = max_i - k[0]
        for (i, j) in v:
            cost += j - min_j
            # cand.add((i, min_j))
        if cost < best_cost:
            best_cost = cost
            best_way = 1

        cost = min_i + min_j - k[0] - k[1]
        for (i, j) in v:
            cost += i + j - min_i - min_j
            # cand.add((i, min_j))
        if cost < best_cost:
            best_cost = cost
            best_way = 2

        if best_way == 0:
            for (i, j) in v:
                cand.add((min_i, j))
        elif best_way == 1:
            for (i, j) in v:
                cand.add((i, min_j))
        elif best_way == 2:
            cand.add((min_i, min_j))


    actions = make_actions(cand)



proc clean_cand(cand: seq[(int, int)], actions: seq[array[4, int]], input: Input): seq[(int, int)] =
    var frm = initTable[(int, int), (int, int)]()
    for action in actions:
        var
            i = action[0]
            j = action[1]
            k = action[2]
            l = action[3]
        frm[(k, l)] = (i, j)
    var visited = initHashSet[(int, int)](cand.len())
    for (i, j) in input.AB:
        var
            p = i
            q = j
        while (p, q) notin visited:
            if p == 0 and q == 0:
                break
            visited.incl((p, q))
            (p, q) = frm[(p, q)]

    return visited.toSeq()


const
    SPLITNUM = 50
    LENGTH = 10**9 // SPLITNUM

proc get_cost(actions: seq[array[4, int]]): int =
    var cost = 0
    for i in actions:
        cost += i[2] + i[3] - i[0] - i[1]
    return cost

proc yamanobori(time: Time, cand: var seq[(int, int)], actions: var seq[array[4, int]]) =
    var frm = initTable[(int, int), (int, int)]()
    for action in actions:
        var
            i = action[0]
            j = action[1]
            k = action[2]
            l = action[3]
        frm[(k, l)] = (i, j)
    var cnt = 0
    var best_cost = get_cost(actions)
    while true:
        cnt += 1
        if time.get_passed_time() > 1.9:
            break
        # 適当な頂点を選ぶ
        var ij = sample(cand)
        var near = (INF64, INF64)
        var dis = INF64
        for (i, j) in cand:
            if (i, j) == ij:
                continue
            if abs(ij[0] - i) + abs(ij[1] - j) < dis:
                dis = abs(ij[0] - i) + abs(ij[1] - j)
                near = (i, j)
        cand.add((min(ij[0], near[0]), min(ij[1], near[1])))
        # スコア比較
        var new_actions = make_actions(cand)
        optimize_actions(cand, new_actions)
        var new_cost = get_cost(new_actions)
        # echo (best_cost, new_cost)
        # 良くなっていれば採用
        if new_cost < best_cost:
            best_cost = new_cost
            actions = new_actions
        else:
            cand.delete(cand.find((min(ij[0], near[0]), min(ij[1], near[1]))))



proc solve(self: var Solver, output: var Output) =
    var
        sorted_a = self.input.AB.sorted(proc (a, b: (int, int)): int = cmp(a[0], b[0]))
        sorted_b = self.input.AB.sorted(proc (a, b: (int, int)): int = cmp(a[1], b[1]))
        cand = newSeqofCap[(int, int)](5*N)
        min_sorted_a = sorted_a[^1][1]
        min_sorted_b = sorted_b[^1][0]
    for (i, j) in sorted_a.reversed():
        min_sorted_a = min(min_sorted_a, j)
        cand.add((i, min_sorted_a))
    for (i, j) in sorted_b.reversed():
        min_sorted_b = min(min_sorted_b, i)
        cand.add((min_sorted_b, j))


    # for i in 0..<SPLITNUM:
    #     cand.add((i*LENGTH, i*LENGTH))

    for i in self.input.AB:
        cand.add(i)

    var
        actions = make_actions(cand)
    optimize_actions(cand, actions)
    yamanobori(self.time, cand, actions)

    output.actions = actions












# -----------------------------------------------------------------------

proc main() =
    var
        time = new_time(TIME_LIMIT)
        input = Input()
        output = Output()
    input.input()
    var solver = new_solver(input, time)
    solver.solve(output)
    output.output()
    time.out_paased_time()
main()
