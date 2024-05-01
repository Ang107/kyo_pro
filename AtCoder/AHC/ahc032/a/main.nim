import macros
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"

import times
var
    mod_num = 998244353
    start = cpuTime()
proc Input(): (int, int, int, ref array[9, array[9, int]], ref array[21, array[3, array[3, int]]]) =
    var
        N, M, K = ii()
        A = new array[9, array[9, int]]
        S = new array[21, array[3, array[3, int]]]

    S[0] = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

    for i in 0..<N:
        A[i] = [ii(), ii(), ii(), ii(), ii(), ii(), ii(), ii(), ii(), ]


    for i in 0..<M:
        for j in range(3):
            S[i+1][j] = [ii(), ii(), ii()]

    # var all_8times_stamp = newSeqOfCap[array[3, array[3, int]]](1771)
    # var all_3times_stamp = newSeqOfCap[array[3, array[3, int]]](3108105)
    # var all_3_kind = newSeqOfCap[array[3, int]](1771)
    # var all_8_kind = newSeqOfCap[array[8, int]](3108105)
    # for i1 in 0..<21:
    #     for i2 in i1..<21:
    #         for i3 in i2..<21:
    #             var tmp: array[3, array[3, int]]
    #             for i in 0..<3:
    #                 for j in 0..<3:
    #                     tmp[i][j] += S[i1][i][j]
    #                     tmp[i][j] = tmp[i][j] mod mod_num
    #                     tmp[i][j] += S[i2][i][j]
    #                     tmp[i][j] = tmp[i][j] mod mod_num
    #                     tmp[i][j] += S[i3][i][j]
    #                     tmp[i][j] = tmp[i][j] mod mod_num
    #             all_3times_stamp.add(tmp)
    #             all_3_kind.add([i1, i2, i3])

    # for i1 in 0..<21:
    #     for i2 in i1..<21:
    #         for i3 in i2..<21:
    #             for i4 in i3..<21:
    #                 for i5 in i4..<21:
    #                     for i6 in i5..<21:
    #                         for i7 in i6..<21:
    #                             for i8 in i7..<21:
    #                                 var tmp: array[3, array[3, int]]
    #                                 for i in 0..<3:
    #                                     for j in 0..<3:
    #                                         tmp[i][j] += S[i1][i][j]
    #                                         tmp[i][j] = tmp[i][j] mod mod_num
    #                                         tmp[i][j] += S[i2][i][j]
    #                                         tmp[i][j] = tmp[i][j] mod mod_num
    #                                         tmp[i][j] += S[i3][i][j]
    #                                         tmp[i][j] = tmp[i][j] mod mod_num
    #                                         tmp[i][j] += S[i4][i][j]
    #                                         tmp[i][j] = tmp[i][j] mod mod_num
    #                                         tmp[i][j] += S[i5][i][j]
    #                                         tmp[i][j] = tmp[i][j] mod mod_num
    #                                         tmp[i][j] += S[i6][i][j]
    #                                         tmp[i][j] = tmp[i][j] mod mod_num
    #                                         tmp[i][j] += S[i7][i][j]
    #                                         tmp[i][j] = tmp[i][j] mod mod_num
    #                                         tmp[i][j] += S[i8][i][j]
    #                                         tmp[i][j] = tmp[i][j] mod mod_num
    #                                 all_8times_stamp.add(tmp)
    #                                 all_8_kind.add([i1, i2, i3, i4, i5, i6, i7, i8])


    return (N, M, K, A, S)


#各盤面で一番利得の大きいスタンプを押す
proc greedy(N, M, K: int, A: ref array[9, array[9, int]], S: ref array[20, array[3, array[3, int]]]): seq[array[3, int]] =
    var ans = newSeqOfCap[array[3, int]](K)
    #スタンプを押す回数
    for times in 0..<K:

        #デバッグ用#########################
        # var tmp = 0
        # for x in 0..<9:
        #     for y in 0..<9:
        #         tmp += A[x][y] mod mod_num
        # echo tmp
        ################################

        #種類
        var
            add_best_score = 0
            rslt = [-1, -1, -1]
        for kind in 0..<M:
            #左上の座標
            for x in 0..<6:
                for y in 0..<6:
                    #3*3の全探索
                    var prv_score = 0
                    var new_score = 0
                    for i in 0..<3:
                        for j in 0..<3:
                            prv_score += A[x+i][y+j] mod mod_num
                            new_score += (A[x+i][y+j] + S[kind][i][j]) mod mod_num
                    if new_score - prv_score > add_best_score:
                        rslt = [kind, x, y]
        if rslt[0] != -1:
            ans.add(rslt)
            var
                kind = rslt[0]
                x = rslt[1]
                y = rslt[2]
            for i in 0..<3:
                for j in 0..<3:
                    A[x+i][y+j] += S[kind][i][j]
        else:
            break
    return ans

proc get_score(A: ref array[9, array[9, int]]): int =
    for i in 0..<9:
        for j in 0..<9:
            result += A[i][j] mod mod_num


#貪欲をビームサーチにする
proc beem(N, M, K: int, A: ref array[9, array[9, int]], S: ref array[20, array[3, array[3, int]]]): seq[array[3, int]] =
    var
        beem_width = 2
        all_beam_width = 20000
        beem_depth = 80
        beem_num = 720
        ans = newSeqOfCap[array[3, int]](K)

    # type inheap = object
    #     sc: int
    #     an: seq[array[3, int]]

    # proc `<`(a, b: inheap): bool = a.sc < b.sc

    var
        used = initHashSet[seq[array[3, int]]](100)
        chokudai_serch = newSeq[newSeqOfCap[(int, seq[array[3, int]])](20000)](82)
        exit_flag = false

    chokudai_serch[0].add((0, @[]))
    for beem in 0..<beem_num:
        if exit_flag:
            break
        for depth in 1..<beem_depth:
            if exit_flag:
                break
            for width in 0..<beem_width:
                if cpuTime() - start > 1.85:
                    exit_flag = true
                    break
                var
                    prv: (int, seq[array[3, int]])
                for i in chokudai_serch[depth-1]:
                    if i[1] notin used:
                        used.incl(i[1])
                        prv = i
                        break
                var
                    A_n = A[]
                    score = prv[0]
                for p in prv[1]:
                    var
                        kind = p[0]
                        x = p[1]
                        y = p[2]
                    for i in 0..<3:
                        for j in 0..<3:
                            A_n[x+i][y+j] = (A_n[x+i][y+j] + S[kind][i][j]) mod mod_num

                for kind in 0..<M:
                    #左上の座標
                    for x in 0..<7:
                        for y in 0..<7:
                            #3*3の全探索
                            var prv_score = 0
                            var new_score = 0
                            var ans_n = prv[1]
                            ans_n.add([kind, x, y])
                            for i in 0..<3:
                                for j in 0..<3:
                                    prv_score += A_n[x+i][y+j] mod mod_num
                                    new_score += (A_n[x+i][y+j] + S[kind][i][j]) mod mod_num

                            chokudai_serch[depth].add((score + new_score-prv_score, ans_n))

            chokudai_serch[depth] = chokudai_serch[depth].sorted(proc(x, y: (int, seq[array[3, int]])): int = cmp(-x[0], -y[0]))[0..<min(chokudai_serch[
                    depth].len(), all_beam_width)]
    chokudai_serch.reverse()
    var score = 0

    for i in 0..<81:
        chokudai_serch[i].reverse()
        if len(chokudai_serch[i]) > 0:
            var tmp = chokudai_serch[i].pop()
            if score < tmp[0]:
                score = tmp[0]
                ans = tmp[1]

    return ans





    # for times in 0..<K:
    #     if cpuTime() - start > 1.8:
    #         break
    #     var deq = initDeque[(int, seq[array[3, int]])](beem_width*3)
    #     deq.addLast((0, @[]))
    #     for depth in 0..beem_depth:
    #         var
    #             deq_n = initDeque[(int, seq[array[3, int]])](beem_width*3)
    #             deq_len = deq.len()
    #         while deq.len() > 0:
    #             var
    #                 (score, ans) = deq.popFirst()
    #                 tmp = newseqofcap[(int, seq[array[3, int]])](720)
    #                 A_tmp = A[]
    #             for i in ans:
    #                 var
    #                     kind = i[0]
    #                     x = i[1]
    #                     y = i[2]
    #                 for i in 0..<3:
    #                     for j in 0..<3:
    #                         A_tmp[x+i][y+j] = (A_tmp[x+i][y+j] + S[kind][i][j]) mod mod_num


    #             for kind in 0..<M:
    #                 #左上の座標
    #                 for x in 0..<6:
    #                     for y in 0..<6:
    #                         var
    #                             ans_n = ans

    #                         #3*3の全探索
    #                         var prv_score = 0
    #                         var new_score = 0
    #                         for i in 0..<3:
    #                             for j in 0..<3:
    #                                 prv_score += A_tmp[x+i][y+j] mod mod_num
    #                                 new_score += (A_tmp[x+i][y+j] + S[kind][i][j]) mod mod_num
    #                         var add_score = new_score - prv_score
    #                         ans_n.add([kind, x, y])
    #                         tmp.add((score+add_score, ans_n))
    #                         # deq_n.addLast((score+add_score, ans_n, A_n))
    #             tmp = tmp.sorted(proc(x, y: (int, seq[array[3, int]])): int = cmp(-x[0], -y[0]))[0..<max(3, (beem_width div deq_len)+1)]
    #             for i in tmp:
    #                 var
    #                     kind = i[1][0][0]
    #                     x = i[1][0][1]
    #                     y = i[1][0][2]

    #                 deq_n.addLast((i[0], i[1]))

    #         echo deq_n.len()
    #         deq = deq_n.toSeq().sorted(proc(x, y: (int, seq[array[3, int]])): int = cmp(-x[0], -y[0]))[0..<min(deq_n.len(),
    #                 beemwidth)].toDeque()

    #         # var tmp = newseqofcap[int](deq.len())
    #         # for i in deq:
    #         #     tmp.add(i[0])
    #         # echo tmp

    #     var rslt = deq.toSeq().sorted(proc(x, y: (int, seq[array[3, int]])): int = cmp(-x[0], -y[0]))[0]
    #     if rslt[0] > 0:
    #         ans.add(rslt[1][0])
    #         var
    #             kind = rslt[1][0][0]
    #             x = rslt[1][0][1]
    #             y = rslt[1][0][2]
    #         for i in 0..<3:
    #             for j in 0..<3:
    #                 A[x+i][y+j] += S[kind][i][j]

        # echo get_score(A)




    # else:
    #     break
    # return ans


proc greedy2(N, M, K: int, A: ref array[9, array[9, int]], S: ref array[21, array[3, array[3, int]]]): seq[array[3, int]] =
    var ans = newSeqOfCap[array[3, int]](81)
    for i in 0..<6:
        for j in 0..<6:
            var
                rslt: array[3, int]
                score_best = 0
            for kind in 0..<21:
                var score = (A[i][j] + S[kind][0][0]) mod mod_num
                if score > score_best:
                    score_best = score
                    rslt = [kind, i, j]
            if rslt[0] != 0:
                rslt[0] -= 1
                ans.add(rslt)
                for i2 in 0..<3:
                    for j2 in 0..<3:
                        A[i+i2][j+j2] += S[rslt[0]+1][i2][j2]
                        A[i+i2][j+j2] = A[i+i2][j+j2] mod mod_num
                # echo A[]


    for i in 0..<6:
        var
            rslt: array[3, int]
            score_best = 0
        for i1 in 0..<21:
            for i2 in i1..<21:
                for i3 in i2..<21:
                    var tmp: array[3, array[3, int]]
                    for i in 0..<3:
                        for j in 0..<3:
                            tmp[i][j] += S[i1][i][j]
                            tmp[i][j] = tmp[i][j] mod mod_num
                            tmp[i][j] += S[i2][i][j]
                            tmp[i][j] = tmp[i][j] mod mod_num
                            tmp[i][j] += S[i3][i][j]
                            tmp[i][j] = tmp[i][j] mod mod_num
                    var score = 0
                    for j in 0..<3:
                        score += (A[i][6+j] + tmp[0][j]) mod mod_num
                    if score > score_best:
                        score_best = score
                        rslt = [i1, i2, i3]
        for r in rslt:
            if r != 0:
                ans.add([r-1, i, 6])
                for i2 in 0..<3:
                    for j2 in 0..<3:
                        A[i+i2][6+j2] += S[r][i2][j2]
                        A[i+i2][6+j2] = A[i+i2][6+j2] mod mod_num

    for i in 0..<6:
        var
            rslt: array[3, int]
            score_best = 0
        for i1 in 0..<21:
            for i2 in i1..<21:
                for i3 in i2..<21:
                    var tmp: array[3, array[3, int]]
                    for i in 0..<3:
                        for j in 0..<3:
                            tmp[i][j] += S[i1][i][j]
                            tmp[i][j] = tmp[i][j] mod mod_num
                            tmp[i][j] += S[i2][i][j]
                            tmp[i][j] = tmp[i][j] mod mod_num
                            tmp[i][j] += S[i3][i][j]
                            tmp[i][j] = tmp[i][j] mod mod_num
                    var score = 0
                    for j in 0..<3:
                        score += (A[6+j][i] + tmp[j][0]) mod mod_num
                    if score > score_best:
                        score_best = score
                        rslt = [i1, i2, i3]
        for r in rslt:
            if r != 0:
                ans.add([r-1, 6, i])
                for i2 in 0..<3:
                    for j2 in 0..<3:
                        A[6+i2][i+j2] += S[r][i2][j2]
                        A[6+i2][i+j2] = A[6+i2][i+j2] mod mod_num


    var
        rslt: array[8, int]
        score_best = 0
    for i1 in 0..<21:
        for i2 in i1..<21:
            for i3 in i2..<21:
                for i4 in i3..<21:
                    for i5 in i4..<21:
                        for i6 in i5..<21:
                            for i7 in i6..<21:
                                for i8 in i7..<21:
                                    var tmp: array[3, array[3, int]]
                                    for i in 0..<3:
                                        for j in 0..<3:
                                            tmp[i][j] += S[i1][i][j]
                                            tmp[i][j] = tmp[i][j] mod mod_num
                                            tmp[i][j] += S[i2][i][j]
                                            tmp[i][j] = tmp[i][j] mod mod_num
                                            tmp[i][j] += S[i3][i][j]
                                            tmp[i][j] = tmp[i][j] mod mod_num
                                            tmp[i][j] += S[i4][i][j]
                                            tmp[i][j] = tmp[i][j] mod mod_num
                                            tmp[i][j] += S[i5][i][j]
                                            tmp[i][j] = tmp[i][j] mod mod_num
                                            tmp[i][j] += S[i6][i][j]
                                            tmp[i][j] = tmp[i][j] mod mod_num
                                            tmp[i][j] += S[i7][i][j]
                                            tmp[i][j] = tmp[i][j] mod mod_num
                                            tmp[i][j] += S[i8][i][j]
                                            tmp[i][j] = tmp[i][j] mod mod_num
                                    var score = 0
                                    for i in 0..<3:
                                        for j in 0..<3:
                                            score += (A[6+i][6+j] + tmp[i][j]) mod mod_num
                                    if score > score_best:
                                        score_best = score
                                        rslt = [i1, i2, i3, i4, i5, i6, i7, i8]

    for r in rslt:
        if r != 0:
            ans.add([r-1, 6, 6])


    return ans





proc Output(ans: seq[array[3, int]]) =
    echo ans.len()
    for i in ans:
        echo i.join(" ")


var

    (N, M, K, A, S) = Input()
    # ans = greedy(N, M, K, A, S)
var
    ans = greedy2(N, M, K, A, S)
Output(ans)








