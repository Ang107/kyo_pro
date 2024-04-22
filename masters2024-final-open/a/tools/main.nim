import macros
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"
var cnt: int
var got_num = 0
proc out_a(x, y: int): (int, int) =
    cnt += 1

    echo "A ", x, " ", y
    flushFile(stdout)
    var
        tmp = stdin.readLine.split
        c = tmp[0].parseInt
        h = tmp[1].parseInt
    echo "#", cnt
    if cnt == 5000:
        quit()
    return (c, h)

proc out_s(x, y: int): (int, int, int) =
    cnt += 1

    echo "S ", x, " ", y
    flushFile(stdout)
    var
        dis = stdin.readLine.parseInt
        tmp = stdin.readLine.split
        c = tmp[0].parseInt
        h = tmp[1].parseInt
    echo "#", cnt

    if cnt == 5000:
        quit()
    return (dis, c, h)

proc first_input(): (int, int, float, float, int, int, seq[(int, int)], seq[(int, int, int, int)]) =
    var
        tmp = stdin.readLine.split
        N = tmp[0].parseInt
        M = tmp[1].parseInt
        ep = tmp[2].parseFloat
        dlt = tmp[3].parseFloat
    tmp = stdin.readLine.split
    var
        sx = tmp[0].parseInt
        sy = tmp[1].parseInt
    var
        P = newseqofcap[(int, int)](10)
        L = newSeqOfCap[(int, int, int, int)](M)


    for i in 0..<N:
        tmp = stdin.readLine.split
        P.add((tmp[0].parseInt, tmp[1].parseInt))
        # echo "#", i, P


    for _ in 0..<M:
        # echo "#M", L
        tmp = stdin.readLine.split
        L.add((tmp[0].parseInt, tmp[1].parseInt, tmp[2].parseInt, tmp[3].parseInt))


    return (N, M, ep, dlt, sx, sy, P, L)


proc get_dis(a, b, c, d: int): int =
    result = ((a-c)**2 + (b-d)**2).float.sqrt().int()

proc get_order(P: seq[(int, int)]): seq[(int, int)] =
    var
        idx = (0..<10).toseq()
        best_dis = 10**18
        order: array[10, int]
        rslt: seq[int]

    while true:
        var dis = 0
        for i in 1..<10:
            dis += get_dis(P[idx[i-1]][0], P[idx[i-1]][1], P[idx[i]][0], P[idx[i]][1])
        if dis < best_dis:
            best_dis = dis
            rslt = idx
        if idx.nextPermutation():
            discard
        else:
            break
    for i in 0..<10:
        result[i] = P[rslt[i]]

    return result
proc get_xy_vec(measure_num: int, got_P: var seq[int]): (int, int, int, int) =
    var
        x_seq, y_seq = newSeqOfCap[int](measure_num)
        x_vec, y_vec = newSeqOfCap[int](measure_num)
        x_dis, y_dis, c, h: int
    for i in 0..<measure_num:
        (x_dis, c, h) = out_s(-1, 0)
        x_dis -= 100000
        x_seq.add(x_dis)
        if h != 0:
            var tmp = stdin.readLine.split.map parseInt
            got_num += tmp.len()

            for j in tmp:
                got_P[j] = 1

        if got_num == 10:
            quit()

        (y_dis, c, h) = out_s(0, -1)
        y_dis -= 100000
        y_seq.add(y_dis)
        if h != 0:
            var tmp = stdin.readLine.split.map parseInt
            got_num += tmp.len()
            for j in tmp:
                got_P[j] = 1

        if got_num == 10:
            quit()

        if i != 0:
            x_vec.add((x_seq[^1] - x_seq[^2]) div 2)
            y_vec.add((y_seq[^1] - y_seq[^2]) div 2)

    var
        x_vec_avr = sum(x_vec) div x_vec.len()
        y_vec_avr = sum(y_vec) div y_vec.len()

    var
        x = x_seq[^1] + 2 * x_vec_avr
        y = y_seq[^1] + y_vec_avr
    # echo "#x_seq", x_seq
    # echo "#y_seq", y_seq
    # echo "#x_vec", x_vec
    # echo "#y_vec", y_vec
    return (x, y, x_vec_avr, y_vec_avr)


proc get_vec(x, y, x_vec, y_vec: int, got_P: seq[int], P: seq[(int, int)]): (int, int) =
    var
        best_dis = 10**18
        x_n = x + x_vec
        y_n = y + y_vec

    for idx, (i, j) in P:
        if got_P[idx] == 0 and best_dis > get_dis(x_n, y_n, i, j):
            var
                tmp_x = i - x_n
                tmp_y = j - y_n
                current_distance_squared = tmp_x**2 + tmp_y**2
            if current_distance_squared <= 250000:
                discard
            else:
                var scale_factor = sqrt(250000 / current_distance_squared)
                tmp_x = int(tmp_x * scale_factor)
                tmp_y = int(tmp_y * scale_factor)
            result = (tmp_x, tmp_y)

proc get_center_vec(x, y, x_vec, y_vec: int): (int, int) =
    var
        x_n = x + x_vec
        y_n = y + y_vec
        tmp_x = 0 - x_n
        tmp_y = 0 - y_n
        current_distance_squared = tmp_x**2 + tmp_y**2

    if current_distance_squared <= 250000:
        discard
    else:
        var scale_factor = sqrt(250000 / current_distance_squared).int()
        tmp_x *= scale_factor
        tmp_y *= scale_factor
    result = (tmp_x, tmp_y)



proc all_got(got_P: seq[int]): bool =
    for i in got_P:
        if i == 0:
            return false
    return true

proc solve(N, M: int, ep, dlt: float, sx, sy: int, P: seq[(int, int)]) =
    var
        got_P_num = 0
        got_P = newseq[int](N)
        # cnt: int
        err: int
        err_limit = 5
        #二回以上
        measure_num = 2
        x = sx
        y = sy
        x_vec, y_vec: int

    while true:
        # echo "#cnt", cnt
        if all_got(got_P):
            return

        if err > err_limit and dlt < 0.05:

            # while x + x_vec * measure_num < -95000 or x + x_vec * measure_num > 95000 or y + y_vec * measure_num < -95000 or y + y_vec * measure_num > 95000:
            #     # if cnt + 1 >= 4999:
            #     #     break
            #     # cnt += 1
            #     var (x_vec_a, y_vec_a) = get_center_vec(x, y, x_vec, y_vec)
            #     x_vec += x_vec_a
            #     y_vec += y_vec_a
            #     x += x_vec
            #     y += y_vec
            #     var (c, h) = out_a(x_vec_a, y_vec_a)
            #     if h != 0:
            #         var tmp = lii(h)
            #         for i in tmp:
            #             got_P[i] = 1
            #     if c == 1:
            #         x -= x_vec
            #         y -= y_vec
            #         x_vec = 0
            #         y_vec = 0

            err = 0
            # if cnt + measure_num * 2 <= 5000:
            # cnt += measure_num * 2
            (x, y, x_vec, y_vec) = get_xy_vec(measure_num, got_P)
            echo "#s", (x, y, x_vec, y_vec)
            # else:
            #     break

        else:
            # if cnt + 1 <= 5000:
            err += 1
            # cnt += 1
            var (x_vec_a, y_vec_a) = get_vec(x, y, x_vec, y_vec, got_P, P)
            x_vec += x_vec_a
            y_vec += y_vec_a
            x += x_vec
            y += y_vec
            var (c, h) = out_a(x_vec_a, y_vec_a)
            if h != 0:
                var tmp = stdin.readLine.split.map parseInt
                got_num += tmp.len()
                for i in tmp:
                    got_P[i] = 1

            if got_num == 10:
                quit()
            if c == 1:
                x -= x_vec
                y -= y_vec
                x_vec = 0
                y_vec = 0
            # else:
            #     return
            echo "#a", (x, y, x_vec, y_vec)





proc main() =
    # for _ in 0..<10:
    #     var tmp = ii()
    #     echo "out", tmp
    #     flushFile(stdout)

    var
        (N, M, ep, dlt, sx, sy, P, L) = first_input()
    # echo ("#", N, M, ep, dlt, sx, sy, P, L)
        # order = get_order(P)
    solve(N, M, ep, dlt, sx, sy, P)

main()
