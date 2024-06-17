import macros
import std/times
import std/random
randomize()
# import nimprof
# {.checks: off.}
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"
const n = 20
discard ii()
let
    ar_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    UDLR = ["U", "D", "L", "R"]
var
    h = newSeqofcap[newSeqOfCap[int](n)](n)
for _ in 0..<n:
    h.add(lii(n))
# echo h

proc make_root(): seq[int] =
    #ルートをとりあえず固定
    var root = newSeqOfCap[int](2*n*n)
    for i in 0..<n:
        if i % 2 == 0:
            for j in 0..<n-1:
                root.add(3)
        else:
            for j in 0..<n-1:
                root.add(2)

        if i != n-1:
            root.add(1)

    # for i in 0..<n:
    #     if i % 2 == 0:
    #         for j in 0..<n-1:
    #             root.add(3)
    #     else:
    #         for j in 0..<n-1:
    #             root.add(2)

    #     if i != n-1:
    #         root.add(0)
    return root

proc output(ans: seq[string]) =
    for i in ans:
        echo i

proc get_root(plus: bool, sx, sy: int): seq[int] =
    # echo h
    #直近の目標の発見
    proc bfs(): (seq[seq[int]], int, int) =
        var
            deq = initDeque[(int, int)](100)
            visited = newseqwith(n, newseqwith(n, -1))
        deq.addLast((sx, sy))
        visited[sx][sy] = -2
        # echo deq
        # visited[sx][sy] = (0, 0)
        while len(deq) > 0:
            var (x, y) = deq.popFirst()
            # echo (x, y)
            if plus and h[x][y] > 0:
                return (visited, x, y)
            elif not plus and h[x][y] < 0:
                return (visited, x, y)

            for idx, (i, j) in ar_4:
                if 0 <= x+i and x+i < n and 0 <= y+j and y+j < n and visited[x+i][y+j] == -1:
                    deq.addLast((x+i, y+j))
                    visited[x+i][y+j] = idx


        return (@[], -1, -1)
    var (visited, tx, ty) = bfs()
    #ルートの復元
    if tx == -1:
        return @[]
    # echo visited
    # echo plus
    # echo (sx, sy)
    # echo (tx, ty)
    var
        root = newSeqOfCap[int](abs(sx-tx) + abs(sy-ty))
    while visited[tx][ty] != -2:
        # echo tx, ty
        root.add(visited[tx][ty])
        if visited[tx][ty] == 0:
            tx += 1
            ty += 0

        elif visited[tx][ty] == 1:
            tx -= 1
            ty += 0

        elif visited[tx][ty] == 2:
            tx += 0
            ty += 1

        elif visited[tx][ty] == 3:
            tx += 0
            ty -= 1
    root.reverse()
    # echo root
    return root





proc solve(): seq[string] =
    var
        x, y = 0
        tank = 0
        ans = newSeqOfCap[string](4*n*n)
        plus_all_get = true
        root = make_root()
    if h[x][y] > 0:
        ans.add(fmt"+{h[x][y]}")
        tank += h[x][y]
        h[x][y] = 0

    for idx, i in root:
        # echo x, y
        x += ar_4[i][0]
        y += ar_4[i][1]
        ans.add(UDLR[i])

        if h[x][y] > 0:
            ans.add(fmt"+{h[x][y]}")
            tank += h[x][y]
            h[x][y] = 0
        elif h[x][y] < 0 and tank > 0:
            var tmp = min(-h[x][y], tank)
            ans.add(fmt"-{tmp}")
            h[x][y] += tmp
            tank -= tmp

    root = get_root(false, x, y)

    while len(root) > 0:
        for idx, i in root:
            # echo x, y
            x += ar_4[i][0]
            y += ar_4[i][1]
            ans.add(UDLR[i])

            if h[x][y] > 0:
                ans.add(fmt"+{h[x][y]}")
                tank += h[x][y]
                h[x][y] = 0
            elif h[x][y] < 0 and tank > 0:
                var tmp = min(-h[x][y], tank)
                ans.add(fmt"-{tmp}")
                h[x][y] += tmp
                tank -= tmp

            # stderr.writeLine(idx)
            # stderr.writeLine(tank)
            # for j in 0..<n:
            #     stderr.writeLine(h[j].join(" "))
        if not plus_all_get:
            root = get_root(true, x, y)
            if len(root) == 0:
                plus_all_get = true
                root = get_root(false, x, y)
        else:
            root = get_root(false, x, y)

    return ans


proc main() =
    var root = make_root()
    var ans = solve()
    # for i in root:
    #     ans.add(UDLR[i])
    # ans =
    output(ans)



main()





