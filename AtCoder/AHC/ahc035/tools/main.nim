import macros
import std/times
import std/random
randomize()
# import nimprof
# {.checks: off.}
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"
const
    rd = [(1, 0), (0, 1)]
    udlr = [(0, -1), (0, 1), (-1, 0), (1, 0)]
const
    n = 6
    m = 15
    t = 10
    h = 2 * n * (n-1)
discard si()

var
    x: array[h, array[m+1, int]]
    ans: array[n, array[n, int]]
    order: array[n*n, (int, int)]
    use: array[36, int]
    dont_use: array[24, int]
for i in 0..<n:
    for j in 0..<n:
        order[i*n+j] = (i, j)
order.sort(proc (x, y: (int, int)): int = cmp(abs(x[0] - 3) + abs(x[1] - 3), abs(y[0] - 3) + abs(y[1] - 3)))
var tmp: array[n, array[n, int]]
for i, a in order:
    tmp[a[0]][a[1]] = i
# for i in tmp:
#     echo i
proc update_x() =
    for i in 0..<h:
        x[i][0] = i
        for j, a in lii(m):
            x[i][j+1] = a

proc output() =
    for i in 0..<n:
        echo ans[i].join(" ")

proc evaluation(t: int): int =
    var
        sum_score = 0
        max_solo_score = 0
    for i in 0..<n:
        for j in 0..<n:
            for (p, q) in rd:
                if i+p < n and j+q < n:
                    var solo_score = 0
                    for s in 1..<m+1:
                        sum_score += max(x[ans[i][j]][s], x[ans[i+p][j+q]][s])
                        var tmp = (x[ans[i][j]][s] + x[ans[i+p][j+q]][s])
                        solo_score += tmp
                        sum_score += tmp
                    max_solo_score = max(max_solo_score, solo_score)

    if t < 5:
        return sum_score + max_solo_score * 120
    else:
        return sum_score + max_solo_score * 240

# proc evaluation(t, mode, a, b, c, d: int): int =
#     if mode == 0:
#         var
#             sum_avr_score = 0
#             sum_max_score = 0

#         #差分計算
#         for (i, j) in udlr:
#             if 0 <= a+i and a+i < n and 0 <= b+j and b+j < n:
#                 for s in 1..<m+1:
#                     sum_max_score += max(x[ans[a][b]][s], x[ans[a+i][b+j]][s])
#                     sum_avr_score += (x[ans[a][b]][s] + x[ans[a+i][b+j]][s]) div 2


#             if 0 <= c+i and c+i < n and 0 <= d+j and d+j < n:
#                 for s in 1..<m+1:
#                     sum_max_score += max(x[ans[c][d]][s], x[ans[c+i][d+j]][s])
#                     sum_avr_score += (x[ans[c][d]][s] + x[ans[c+i][d+j]][s]) div 2


#         if t < 4:
#             return sum_max_score
#         else:
#             return sum_max_score
    # else:
    #     var
    #         sum_score = 0
    #         max_solo_score = 0
    #     #差分計算
    #     for (i, j) in udlr:
    #         var solo_score_ab: int
    #         if 0 <= a+i and a+i < n and 0 <= b+j and b+j < n:
    #             for s in 1..<m+1:
    #                 sum_score += max(x[ans[a][b]][s], x[ans[a+i][b+j]][s])
    #                 sum_score += (x[ans[a][b]][s] + x[ans[a+i][b+j]][s]) div 2
    #                 solo_score_ab += (x[ans[a][b]][s] + x[ans[a+i][b+j]][s]) div 2
    #         max_solo_score = max(max_solo_score, solo_score_ab)

    #     return sum_score










proc yamanobori(t: int) =
    var best_score = evaluation(t)
    while cpuTime() < (t+1) * 0.19:
        var
            i = rand(n-1)
            j = rand(n-1)
            p = rand(n-1)
            q = rand(n-1)
        if i != j or p != q:
            swap(ans[i][j], ans[p][q])
            var new_score = evaluation(t)
            if best_score <= new_score:
                best_score = new_score
                discard
            else:
                swap(ans[i][j], ans[p][q])

# proc yamanobori(t: int) =
#     var
#         cnt = 0

#     while cpuTime() < (t+1) * 0.19:
#         var mode = 0
#         # if mode == 0:
#         var
#             i = rand(n-1)
#             j = rand(n-1)
#             p = rand(n-1)
#             q = rand(n-1)
#         if i != j or p != q:
#             var prv_score = evaluation(t, 0, i, j, p, q)
#             swap(ans[i][j], ans[p][q])
#             var new_score = evaluation(t, 0, i, j, p, q)
#             if prv_score <= new_score:
#                 cnt += 1
#                 discard
#             else:
#                 swap(ans[i][j], ans[p][q])
    # elif mode == 1:
    #     var
    #         i = rand(n-1)
    #         j = rand(n-1)
    #         idx = rand(23)
    #         change = dont_use[idx]
    #         prv_idx = ans[i][j]
    #     var prv_score = evaluation(mode, i, j, -1, -1)
    #     ans[i][j] = change
    #     var new_score = evaluation(mode, i, j, -1, -1)
    #     if prv_score <= new_score:
    #         dont_use[idx] = prv_idx
    #         cnt += 1
    #         discard
    #     else:
    #         ans[i][j] = prv_idx
        # stderr.write($dont_use)

    # stderr.write($cnt, "\n")



# order.shuffle()
proc make_ans(t: int) =

    x.sort(proc (x, y: array[m+1, int]): int = cmp(sum(sorted(y[1..m])[8..<15]) * 7 + max(y[1..m])*m, sum(sorted(x[1..m])[8..<15]) * 7 + max(x[1..m])*m))


    for o, (i, j) in order:
        ans[i][j] = x[o][0]

    x.sort(proc (x, y: array[m+1, int]): int = cmp(x[0], y[0]))
    yamanobori(t)


# proc solve() =

proc main() =
    update_x()
    for i in 0..<t:
        make_ans(i)
        output()
        update_x()


main()





