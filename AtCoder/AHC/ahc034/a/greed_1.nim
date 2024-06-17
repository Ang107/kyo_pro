import macros
import std/times
import std/random
let START_TIME = cpuTime()
randomize()

macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"
const n = 20
discard ii()
var
    UDLR = [("U", -1, 0), ("D", 1, 0), ("L", 0, -1), ("R", 0, 1)]
var
    h = newSeqofcap[newSeqOfCap[int](n)](n)
for _ in 0..<n:
    h.add(lii(n))
var h_tmp = h

proc make_root(): seq[int8] =
    var root = newSeqOfCap[int8](2*n*n)
    for i in 0..<n:
        if i % 2 == 0:
            for j in 0..<n-1:
                root.add(3)
        else:
            for j in 0..<n-1:
                root.add(2)
        if i != n-1:
            root.add(1)
    return root

proc output(ans: seq[string]) =
    for i in ans:
        echo i

proc get_root(plus: bool, sx, sy, : int): seq[int] =
    proc bfs(): (seq[seq[int]], int, int) =
        var
            deq = initDeque
            visited = newseqwith(n, newseqwith(n, -1))
        deq.addLast((sx, sy))
        visited[sx][sy] = -2
        while len(deq) > 0:
            var (x, y) = deq.popFirst()
            if plus and h[x][y] > 0:
                return (visited, x, y)
            elif not plus and h[x][y] < 0:
                return (visited, x, y)
            for idx, (udlr, i, j) in UDLR:
                if 0 <= x+i and x+i < n and 0 <= y+j and y+j < n and visited[x+i][y+j] == -1:
                    deq.addLast((x+i, y+j))
                    visited[x+i][y+j] = idx
        return (@[], -1, -1)
    var (visited, tx, ty) = bfs()
    if tx == -1:
        return @[]
    var root = newSeqOfCap[int](abs(sx-tx) + abs(sy-ty))
    while visited[tx][ty] != -2:
        root.add(visited[tx][ty])
        if UDLR[visited[tx][ty]][0] == "U":
            tx += 1
            ty += 0
        elif UDLR[visited[tx][ty]][0] == "D":
            tx -= 1
            ty += 0
        elif UDLR[visited[tx][ty]][0] == "L":
            tx += 0
            ty += 1
        elif UDLR[visited[tx][ty]][0] == "R":
            tx += 0
            ty -= 1
    root.reverse()
    return root

proc solve(lw, hi: int): (seq[string], int) =
    var
        cost = 0
        x, y = 0
        tank = 0
        ans = newSeqOfCap[string](4*n*n)
        plus_mode = true

    if h[x][y] > 0:
        ans.add(fmt"+{h[x][y]}")
        tank += h[x][y]
        cost += h[x][y]
        h[x][y] = 0
    var root = get_root(plus_mode, x, y)
    while len(root) > 0:
        for idx, i in root:
            x += UDLR[i][1]
            y += UDLR[i][2]
            ans.add(UDLR[i][0])
            cost += 100 + tank
            if h[x][y] > 0:
                ans.add(fmt"+{h[x][y]}")
                tank += h[x][y]
                cost += h[x][y]
                h[x][y] = 0
            elif h[x][y] < 0 and tank > 0:
                var tmp = min(-h[x][y], tank)
                ans.add(fmt"-{tmp}")
                h[x][y] += tmp
                cost += tmp
                tank -= tmp

        if tank < lw:
            plus_mode = true
        elif tank > hi:
            plus_mode = false

        if plus_mode:
            shuffle(UDLR)
            root = get_root(plus_mode, x, y)
            if len(root) == 0:
                plus_mode = false
                root = get_root(plus_mode, x, y)
        else:
            shuffle(UDLR)
            root = get_root(plus_mode, x, y)
            if len(root) == 0:
                plus_mode = true
                root = get_root(plus_mode, x, y)

    return (ans, cost)

proc ikiti_find(): (seq[string], int, int) =
    var
        best_ikiti: (int, int)
        best_cost = INF
        best_ans: seq[string]
    while cpuTime() - START_TIME < 1.9:
        for lw in [0, 10]:
            for hi in [110, 120, 130, 140, 150, 160, 170, 180]:
                h = h_tmp
                var (ans, cost) = solve(lw, hi)
                if cost < best_cost:
                    best_cost = cost
                    best_ikiti = (lw, hi)
                    best_ans = ans
    stderr.writeLine(best_ikiti, best_cost)
    return (best_ans, best_ikiti[0], best_ikiti[1])

proc main() =
    var (ans, lw, hi) = ikiti_find()
    output(ans)

main()
