import macros
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"

let
    N = ii()
    max_turn = 500
    SUDLR = [ (int8(0), int8(1)), (int8(-1), int8(0)), (int8(1), int8(0)), (int8(0), int8(-1)), (int8(0), int8(0))]
    UDLR = [(int8(0), int8(1)), (int8(-1), int8(0)), (int8(1), int8(0)), (int8(0), int8(-1)), ]
    SUDLR_s = ["R", "U", "D", "L", "."]
    SUDLR_table = {".": (int8(0), int8(0)),
                    "P": (int8(0), int8(0)),
                    "Q": (int8(0), int8(0)),
                    "U": (int8(-1), int8(0)),
                    "D": (int8(1), int8(0)),
                    "L": (int8(0), int8(-1)),
                    "R": (int8(0), int8(1))}.toTable()

var
    tmp = newSeq[newSeqOfCap[int](N)](N)
    A = newSeq[newSeqOfCap[int8](N)](N)
    space: seq[(int8, int8)] = @[(2, 3), (0, 3), (4, 3), (2, 2), (0, 2), (4, 2)]
for i in 0..<N:
    tmp[i] = lii(N)
    A[i] = mapIt(tmp[i], int8(it))
# echo A


#bの中の目標のコンテナの座標を返す
proc get_target_xy(contena_b: seq[array[5, int8]], crane_b: seq[array[5, (int8, int8)]], target: set[int8]): seq[(int8, int8)] =
    result = newSeqOfCap[(int8, int8)](5)
    for i in int8(0)..<int8(5):
        for j in int8(0)..<int8(4):
            if contena_b[i][j] in target and crane_b[i][j][1] <= 0:
                result.add((i, j))
    return result

#現在地からコンテナまでクレーンを移動するルートを取得
proc get_root_to_txy(sx, sy, tx, ty: int8, turn: int, crane_b: seq[seq[array[5, (int8, int8)]]]): (bool, seq[string]) =
    var
        deq = initDeque[(int8, int8)](25)
        visited = newSeqWith(5, newSeqwith(5, newseqofcap[string](15)))
    visited[sx][sy] = @["_"]
    deq.addLast((sx, sy))
    while len(deq) > 0:
        var
            (x, y) = deq.popFirst()
            add_turn = len(visited[x][y])
        if x == tx and y == ty:
            break

        for idx, (i, j) in SUDLR[0 ..< ^1]:
            if add_turn <= 15 and
            0 <= x+i and x+i < 5 and
            0 <= y+j and y+j < 5 and
            (i+j == 0 or len(visited[x+i][y+j]) == 0) and
            crane_b[turn + add_turn][x+i][y+j][0] == -1 and
            (crane_b[turn+add_turn-1][x+i][y+j][0] == -1 or
            crane_b[turn+add_turn-1][x+i][y+j][0] != crane_b[turn+add_turn][x][y][0]):
                visited[x+i][y+j] = visited[x][y]
                visited[x+i][y+j].add(SUDLR_s[idx])
                deq.addLast((x+i, y+j))

    if len(visited[tx][ty]) >= 1 and crane_b[turn + len(visited[tx][ty])][tx][ty][0] == -1:
        return (true, visited[tx][ty][1..^1])
    else:
        return (false, @[])

#クレーンでのコンテナを目的地に運ぶまでのルートを取得
proc get_root_to_gxy(crane_num, tx, ty, gx, gy: int8, turn: int, crane_b: seq[seq[array[5, (int8, int8)]]], contena_b: seq[seq[array[5, int8]]]): (bool,
        seq[string]) =
    var
        deq = initDeque[(int8, int8)](25)
        visited = newSeqWith(5, newSeqwith(5, newSeqOfCap[string](15)))
    visited[tx][ty] = @["P"]
    deq.addLast((tx, ty))
    while len(deq) > 0:
        var
            (x, y) = deq.popFirst()
            add_turn = len(visited[x][y])
        if x == gx and y == gy:
            break
        for idx, (i, j) in SUDLR[0 ..< ^1]:
            # if x == 2 and y == 1 and crane_num == 4:
            #     echo (x, y, x+i, y+j, tx, ty, gx, gy, turn, add_turn)
            #     for i in crane_b[turn + add_turn + 1]:
            #         echo i
            if add_turn <= 15 and
            0 <= x+i and x+i < 5 and
            0 <= y+j and y+j < 5 and
            (i+j == 0 or len(visited[x+i][y+j]) == 0) and
            crane_b[turn + add_turn + 1][x+i][y+j][0] == -1 and
            (crane_num == 0 or contena_b[turn + add_turn + 1][x+i][y+j] == -1) and
            (crane_b[turn+add_turn][x+i][y+j][0] == -1 or
            crane_b[turn+add_turn][x+i][y+j][0] != crane_b[turn+add_turn + 1][x][y][0])
            :
                visited[x+i][y+j] = visited[x][y]
                visited[x+i][y+j].add(SUDLR_s[idx])
                deq.addLast((x+i, y+j))
    if len(visited[gx][gy]) > 1 and crane_b[turn + len(visited[gx][gy]) + 1][gx][gy][0] == -1:
        visited[gx][gy].add("Q")
        return (true, visited[gx][gy])
    else:
        return (false, @[])

#大クレーンでのコンテナを目的地に運ぶまでのルートを取得
# proc get_root_to_gxy_by_big_crane(tx, ty, gx, gy: int8, turn: int, crane_b: seq[seq[array[5, (int8, int8)]]]): (bool, seq[string]) =
#     var
#         deq = initDeque[(int8, int8)](25)
#         visited = newSeqWith(5, newSeqwith(5, newSeqOfCap[string](15)))
#     visited[tx][ty] = @["P"]
#     deq.addLast((tx, ty))
#     while len(deq) > 0:
#         var
#             (x, y) = deq.popFirst()
#             add_turn = len(visited[x][y])
#         if x == gx and y == gy:
#             break
#         for idx, (i, j) in SUDLR[0 ..< ^1]:
#             if add_turn <= 15 and
#             0 <= x+i and x+i < 5 and
#             0 <= y+j and y+j < 5 and
#             (i+j == 0 or len(visited[x+i][y+j]) == 0) and
#             crane_b[turn + add_turn+1][x+i][y+j][0] == -1:
#                 visited[x+i][y+j] = visited[x][y]
#                 visited[x+i][y+j].add(SUDLR_s[idx])
#                 deq.addLast((x+i, y+j))
#     if len(visited[gx][gy]) > 1:
#         visited[gx][gy].add("Q")
#         return (true, visited[gx][gy])
#     else:
#         return (false, visited[gx][gy])

proc is_free(crane: seq[seq[(int8, int8, int8, int8)]], turn: int): bool =
    for i in 0..<5:
        if crane[i][turn][2] == -1:
            return true
    return false

proc get_contena_num(contena_b: seq[array[5, int8]]): int =
    for i in 0..<5:
        for j in 0..<5:
            if contena_b[i][j] != -1:
                result += 1
    return result

proc get_space(contena_b: seq[array[5, int8]]): seq[(int8, int8)] =
    for (i, j) in space:
        if contena_b[i][j] == -1:
            result.add((i, j))
    return result

proc get_most_near_col(A_n: seq[seq[int8]], target: set[int8]): int8 =
    var
        min_len = 100
    result = -1

    for idx, i in A_n:
        var le = 100
        for j, k in reversed(i):
            if int8(k) in target:
                le = j
                break
        # echo (idx, le)
        if min_len > le:
            min_len = le
            result = int8(idx)
    return result


proc can_put(start_turn, x, y: int, contena_b: seq[seq[array[5, int8]]]): bool =
    for i in 0..<15:
        if contena_b[start_turn + i][x][y] == -1:
            discard
        else:
            return false
    return true

proc in_root(x, y: int, crane: seq[(int8, int8, int8, int8)]): bool =
    for (x1, y1, _, _) in crane:
        if x == x1 and y == y1:
            return true
    return false
proc is_fin(contena_b: seq[array[5, int8]], ans: seq[seq[string]], turn: int): bool =
    for i in ans:
        if len(i) > turn+1:
            return false
    for i in 0..<5:
        for j in 0..<5:
            if contena_b[i][j] != -1:
                return false
    return true

proc solve(): seq[seq[string]] =
    var
        turn = 0
        ans = newseq[newSeqOfCap[string](1000)](N)
        #i ターン目のコンテナの盤面の情報
        contena_b = newseqwith(max_turn, newSeqWith(5, [int8(-1), int8(-1), int8(-1), int8(-1), int8(-1)]))
        #i ターン目のクレーンの盤面の情報(クレーン番号、状態（未予約:-1,掴んでない:0, 掴み:1）)
        crane_b = newseqwith(max_turn, newSeqWith(5, [(int8(-1), int8(-1)),
                            (int8(-1), int8(-1)),
                            (int8(-1), int8(-1)),
                            (int8(-1), int8(-1)),
                            (int8(-1), int8(-1))]))
        #クレーンiのjターン目の場所(x,y,状態,掴んでいるコンテナ番号、)
        crane = newSeqWith(5, newSeqWith(max_turn, (int8(-1), int8(-1), int8(-1), int8(-1))))
        target: set[int8]
        bomed = [false, false, false, false, false]
        A_idx = newseq[int](25)
        A_n = A
        rock = newSeqWith(5, newseqwith(5, -1))
        rock_idx = newseqwith(25, -1)
        out_time = newseqwith(25, -1)

    for i in 0..<5:
        A_n[i].reverse()
        discard A_n[i].pop()

    #初期ターゲット
    for i in 0..<5:
        target.incl(int8(5*i))

    #初期盤面
    for i in int8(0)..<int8(5):
        contena_b[0][i][0] = A[i][0]
        crane_b[0][i][0] = (i, int8(-1))
        crane[i][0] = (i, int8(0), int8(-1), int8(-1))

    for i in 0..<max_turn:
        contena_b[i] = contena_b[0]

    for i in 0..<5:
        for j in 0..<5:
            A_idx[A[i][j]] = j


    for now_turn in 0..<1000:


        # echo crane[]
        #盤面の更新
        # if now_turn > 0:
        #     contena_b[now_turn] = contena_b[now_turn-1]

        #     for i in 0..<5:
        #         #新規ターゲット追加
        #         if crane[i][now_turn-1][1] == 4 and
        #         crane[i][now_turn-1][2] == 1 and
        #         crane[i][now_turn][1] == 4 and
        #         crane[i][now_turn][2] == 0 and
        #         crane[i][now_turn-1][3] % 5 != 4:
        #             target.incl(crane[i][now_turn-1][3]+1)

        #         #コンテナの移動
        #         if i == 0:
        #             if crane[i][now_turn-1][2] == 0 and crane[i][now_turn][2] == 1:
        #                 var
        #                     prv_x = crane[i][now_turn-1][0]
        #                     prv_y = crane[i][now_turn-1][1]
        #                 contena_b[now_turn][prv_x][prv_y] = -1
        #         else:
        #             if crane[i][now_turn-1][2] == 1:
        #                 var
        #                     prv_x = crane[i][now_turn-1][0]
        #                     prv_y = crane[i][now_turn-1][1]
        #                     now_x = crane[i][now_turn][0]
        #                     now_y = crane[i][now_turn][1]

        #                 contena_b[now_turn][now_x][now_y] = contena_b[now_turn-1][prv_x][prv_y]
        #                 echo (prv_x, prv_y, now_x, now_y, contena_b[now_turn][now_x][now_y], contena_b[now_turn-1][prv_x][prv_y])
        #                 if contena_b[now_turn-1][prv_x][prv_y] == contena_b[now_turn][prv_x][prv_y]:
        #                     contena_b[now_turn][prv_x][prv_y] = -1

        #     for i in 0..<5:
        #         if contena_b[nowturn][i][0] == -1 and crane_b[now_turn][i][0][1] <= 0 and len(A[i]) > 0:
        #             contena_b[nowturn][i][0] = A[i].pop()


        # echo "now_turn", now_turn

        # for j in 0..<5:
        #     echo contena_b[now_turn][j]
        # for j in 0..<5:
        #     echo crane_b[now_turn][j]

        # for j in 0..<5:
        #     echo crane[j][now_turn]
        # for i in ans:
        #     echo i.join("")

        # for i in rock:
        #     echo i
        # echo target

        # echo bomed

        #全てのクレーンが使用中なら
        if not is_free(crane, now_turn) and not is_free(crane, now_turn+1):
            continue
        var target_xy = get_target_xy(contena_b[now_turn], crane_b[now_turn], target)



        for (tx, ty) in target_xy:
            # for i in 70..80:
            #     echo i
            #     for j in 0..<5:
            #         echo contena_b[i][j]
            #     echo()
            #     for j in 0..<5:
            #         echo crane_b[i][j]
            #     echo()
            # for i in 0..<5:
            #     echo rock[i]
            # echo rock_idx

            var
                min_len = 1000
                crane_num = -1
                t = int8(-1)
                rslt: (seq[string], seq[string])


            for i in int8(0)..<int8(5):
                if crane[i][nowturn+1][2] != -1 or bomed[i]:
                    continue
                var
                    sx = crane[i][now_turn][0]
                    sy = crane[i][now_turn][1]
                    (flag1, to_txy) = get_root_to_txy(sx, sy, tx, ty, now_turn, crane_b)
                    tmp_t = contena_b[now_turn + len(to_txy)][tx][ty]
                    gx = int8(tmp_t // 5)
                    gy = int8(4)
                # echo (rock[tx][ty], now_turn + len(to_txy))
                if flag1 and now_turn + len(to_txy) > rock[tx][ty] and
                tmp_t in target and now_turn + len(to_txy) > rock_idx[tmp_t]:
                    var (flag2, to_gxy) = get_root_to_gxy(i, tx, ty, gx, gy, now_turn+len(to_txy), crane_b, contena_b)
                    if flag2 and len(to_txy) + len(to_gxy) < min_len and
                    (tmp_t % 5 == 0 or now_turn + len(to_txy) + len(to_gxy) > out_time[tmp_t-1]):
                        min_len = len(to_txy) + len(to_gxy)
                        crane_num = i
                        rslt = (to_txy, to_gxy)
                        t = tmp_t

            if crane_num >= 0:
                # echo ("t", t)
                # echo (target)
                # echo (t in target)
                target.excl(t)
                if t % 5 != 4:
                    target.incl(t+1)

                var
                    x = crane[crane_num][now_turn][0]
                    y = crane[crane_num][now_turn][1]
                    catch = int8(0)
                    prv_x, prv_y: int8
                    p_turn: int
                    leave_left: (int, int8) = (-1, -1)


                for idx, i in rslt[0] & rslt[1]:
                    ans[crane_num].add(i)
                    x += SUDLR_table[i][0]
                    y += SUDLR_table[i][1]
                    if i == "P":
                        catch = 1
                        prv_x = x
                        prv_y = y
                        p_turn = now_turn+idx+1

                    if leave_left[0] == -1 and
                    catch == 1 and
                    (x != prv_x or y != prv_y):
                        if A_idx[t] != 4 and prv_y == 0 and len(A_n[prv_x]) > 0:
                            discard A_n[prv_x].pop()
                            leave_left = (now_turn+idx+1, A[prv_x][A_idx[t]+1])
                        else:
                            leave_left = (now_turn+idx+1, -1)
                            space.add((prv_x, int8(0)))
                            space.add((prv_x, int8(1)))

                    if i == "Q":
                        catch = 0
                        crane_b[now_turn+idx+1][x][y] = (int8(crane_num), catch)
                        crane[crane_num][now_turn+idx+1] = (x, y, catch, -1)
                        # crane_b[now_turn+idx+2][x][y] = (int8(crane_num), -1)
                        # crane[crane_num][now_turn+idx+2] = (x, y, -1, -1)
                        #ロックして他クレーンとの競合を防ぐ
                        rock[prv_x][prv_y] = leave_left[0]
                        rock_idx[t] = now_turn+idx+2
                        out_time[t] = now_turn+idx+2

                        #P ~ のcontenaの削除
                        for turn in leave_left[0]..<max_turn:
                            if contena_b[turn][prv_x][prv_y] == t:
                                contena_b[turn][prv_x][prv_y] = -1
                            else:
                                echo ("永続のコンテナの削除の際にエラーが出ます。", crane_num, turn, contena_b[turn][prv_x][prv_y], t)
                                for i in ans:
                                    echo i.join("")
                                quit()

                        #Q ~ のcontenaの追加
                        if y != 4:
                            for turn in now_turn+idx+1..<max_turn:
                                if contena_b[turn][x][y] == -1:
                                    contena_b[turn][x][y] = t
                                else:
                                    echo ("永続のコンテナの設置の際にエラーが出ます。", contena_b[turn][x][y], t)
                                    quit()

                        #追加されたコンテナの永続設置
                        if leave_left[0] != -1:
                            for turn in leave_left[0]..<max_turn:
                                if contena_b[turn][prv_x][prv_y] == -1:
                                    contena_b[turn][prv_x][prv_y] = int8(leave_left[1])
                                else:
                                    echo ("永続のコンテナの設置の際にエラーが出ます。2", contena_b[turn][prv_x][prv_y], leave_left[1])
                                    quit()


                    else:
                        crane_b[now_turn+idx+1][x][y] = (int8(crane_num), catch)
                        if catch == 1:
                            crane[crane_num][now_turn+idx+1] = (x, y, catch, t)
                            if crane_num == 0:
                                discard
                            else:
                                contena_b[now_turn+idx+1][x][y] = t
                        else:
                            crane[crane_num][now_turn+idx+1] = (x, y, catch, -1)
                        # contena_b[now_turn+idx+1][x][y] = t

        #新規の追加
        var space = get_space(contena_b[now_turn+10])

        for (gx, gy) in space:
            # for i in 0..<10:
            #     echo i
            #     for j in 0..<5:
            #         echo contena_b[i][j]
            #     echo ()
            # for i in 0..<20:
            #     echo i
            #     for j in 0..<5:
            #         echo crane_b[i][j]
            #     echo ()
            var
                min_len = 1000
                crane_num = -1
                tx = get_most_near_col(A_n, target)
                ty = int8(0)
                t: int8 = -1
                rslt: (seq[string], seq[string])
            if tx == -1:
                break

            for i in int8(0)..<int8(5):
                if crane[i][nowturn+1][2] != -1 or bomed[i]:
                    continue
                var
                    sx = crane[i][now_turn][0]
                    sy = crane[i][now_turn][1]
                    (flag1, to_txy) = get_root_to_txy(sx, sy, tx, ty, now_turn, crane_b)

                if flag1 and now_turn + len(to_txy) > rock[tx][ty] and now_turn + len(to_txy) > rock_idx[contena_b[now_turn + len(to_txy)+1][tx][ty]]:
                    var (flag2, to_gxy) = get_root_to_gxy(i, tx, ty, gx, gy, now_turn + len(to_txy), crane_b, contena_b)
                    # echo (i, tx, len(to_txy), len(to_gxy), min_len)
                    if flag2 and len(to_txy) + len(to_gxy) < min_len and
                    can_put(now_turn+len(to_txy)+len(to_gxy)-1, gx, gy, contena_b):
                        # echo ("!", now_turn, len(to_txy), to_txy, to_gxy, i)
                        # for i in 0..<5:
                        #     echo contena_b[now_turn + len(to_txy)+1][i]

                        t = contena_b[now_turn + len(to_txy)+1][tx][ty]
                        min_len = len(to_txy) + len(to_gxy)
                        crane_num = i
                        rslt = (to_txy, to_gxy)

            if crane_num >= 0:
                var
                    x = crane[crane_num][now_turn][0]
                    y = crane[crane_num][now_turn][1]
                    catch = int8(0)
                    prv_x, prv_y: int8
                    p_turn: int
                    leave_left: (int, int8) = (-1, -1)

                # echo (crane_num, rslt[0] & rslt[1])
                for idx, i in rslt[0] & rslt[1]:
                    ans[crane_num].add(i)
                    x += SUDLR_table[i][0]
                    y += SUDLR_table[i][1]

                    if i == "P":
                        catch = 1
                        prv_x = x
                        prv_y = y
                        p_turn = now_turn+idx+1

                    if leave_left[0] == -1 and
                    catch == 1 and
                    prv_y == 0 and
                    (x != prv_x or y != prv_y):
                        if A_idx[t] != 4:
                            discard A_n[prv_x].pop()
                            leave_left = (now_turn+idx+1, A[prv_x][A_idx[t]+1])
                        else:
                            leave_left = (now_turn+idx+1, -1)
                            space.add((prv_x, int8(0)))
                            space.add((prv_x, int8(1)))



                    if i == "Q":
                        catch = 0
                        crane_b[now_turn+idx+1][x][y] = (int8(crane_num), catch)
                        crane[crane_num][now_turn+idx+1] = (x, y, catch, -1)
                        # crane_b[now_turn+idx+2][x][y] = (int8(crane_num), -1)
                        # crane[crane_num][now_turn+idx+2] = (x, y, -1, -1)
                        #ロックして他クレーンとの競合を防ぐ
                        rock[prv_x][prv_y] = leave_left[0]
                        rock_idx[t] = now_turn+idx+2


                        #P ~ のcontenaの削除
                        for turn in leave_left[0]..<max_turn:
                            if contena_b[turn][prv_x][prv_y] == t:
                                contena_b[turn][prv_x][prv_y] = -1
                                # echo ("s", turn, prv_x, prv_y, contena_b[turn][prv_x][prv_y])
                            else:
                                echo ("n永続のコンテナの削除の際にエラーが出ます。", crane_num, turn, contena_b[turn][prv_x][prv_y], t, x, y)
                                echo (rslt[0] & rslt[1])
                                quit()


                        #Q ~ のcontenaの追加
                        if y != 4:
                            for turn in now_turn+idx+1..<max_turn:
                                if contena_b[turn][x][y] == -1:
                                    contena_b[turn][x][y] = t
                                    # echo ("q", turn, x, y, contena_b[turn][x][y])
                                else:
                                    echo ("n永続のコンテナの設置の際にエラーが出ます。", now_turn, contena_b[turn][x][y], turn, x, y, crane_num)
                                    echo (rslt)
                                    quit()

                        #追加されたコンテナの永続設置
                        if leave_left[0] != -1:
                            for turn in leave_left[0]..<max_turn:
                                if contena_b[turn][prv_x][prv_y] == -1:
                                    contena_b[turn][prv_x][prv_y] = int8(leave_left[1])
                                    # echo ("n", turn, prv_x, prv_y, contena_b[turn][prv_x][prv_y])

                                else:
                                    echo ("n永続のコンテナの設置の際にエラーが出ます。2", contena_b[turn][prv_x][prv_y], leave_left[1],
                                            turn, prv_x, prv_y)
                                    quit()

                    else:
                        crane_b[now_turn+idx+1][x][y] = (int8(crane_num), catch)

                        if catch == 1:
                            crane[crane_num][now_turn+idx+1] = (x, y, catch, t)
                            if crane_num == 0:
                                discard
                            else:
                                contena_b[now_turn+idx+1][x][y] = t
                        else:
                            crane[crane_num][now_turn+idx+1] = (x, y, catch, -1)

        #衝突回避
        for i in 0..<5:
            # echo (now_turn, i, crane[i][nowturn+1])
            if crane[i][nowturn+1][2] != -1 or bomed[i]:
                continue

            var
                x = crane[i][now_turn][0]
                y = crane[i][now_turn][1]
            # echo (x, y)

            var
                bom = crane_b[now_turn+1][x][y][0] != -1
                rslt: (int, int8, int8) = (-1, -1, -1)
                max_move_num = -1
            for idx, (p, q) in SUDLR:
                if 0 <= x+p and x+p < 5 and 0 <= y+q and y+q < 5 and
                crane_b[now_turn+1][x+p][y+q][0] == -1 and
                (crane_b[now_turn][x+p][y+q][0] == -1 or crane_b[now_turn][x+p][y+q][0] != crane_b[now_turn+1][x][y][0]):
                    bom = false
                    var tmp = 0
                    for (n, m) in UDLR:
                        if 0 <= x+p+n and x+p+n < 5 and 0 <= y+q+m and y+q+m < 5 and
                        crane_b[now_turn+2][x+p+n][y+q+m][0] == -1 and
                        (crane_b[now_turn+1][x+p+n][y+q+m][0] == -1 or crane_b[now_turn+1][x+p+n][y+q+m][0] != crane_b[now_turn+2][x+p][y+q][0]):
                            tmp += 1
                    # echo (i, idx, tmp, )
                    if tmp > max_move_num:
                        max_move_num = tmp
                        rslt = (idx, p, q)

            if bom:
                bomed[i] = true
                ans[i].add("B")
            else:

                var (idx, p, q) = rslt
                # echo (i, now_turn, SUDLR_s[idx], idx, x, p, y, q)
                ans[i].add(SUDLR_s[idx])
                crane[i][now_turn+1] = crane[i][now_turn]
                crane[i][now_turn+1][0] = x+p
                crane[i][now_turn+1][1] = y+q
                crane_b[now_turn+1][x+p][y+q] = (int8(i), int8(-1))







            # echo crane[i][now_turn+1]




        if is_fin(contena_b[now_turn], ans, now_turn):
            break



    return ans
















#運搬は大クレーンに任せる。小クレーンは追加のみ
# proc solve(): seq[seq[string]] =
#     var
#         turn = 0
#         ans = newSeq[newSeqOfCap[string](maxturn)](N)
#         #i ターン目のコンテナの盤面の情報
#         contena_b = newseqwith(max_turn+100, newSeqWith(5, [int8(-1), int8(-1), int8(-1), int8(-1), int8(-1)]))
#         #i ターン目のクレーンの盤面の情報(クレーン番号、状態（掴んでない:0, 掴み:1）)
#         crane_b = newseqwith(max_turn+100, newSeqWith(5, [(int8(-1), int8(-1)), (int8(-1), int8(-1)), (int8(-1), int8(-1)), (int8(-1), int8(-1)), (int8(-1),
#                 int8(-1))]))
#         #クレーンiのjターン目の場所(x,y,状態)
#         crane = newSeqWith(5, newSeqWith(max_turn+100, (int8(-1), int8(-1), int8(-1))))

#         target: set[int8]
#     for i in 0..<5:
#         target.incl(int8(5*i))

#     turn += 17
#     for i in 0..<5:
#         for j in 2..5:
#             contena_b[turn][i][^j] = A[i].pop()

#     crane_b[turn][0][1] = (0, 0)
#     crane[0][turn] = (0, 1, 0)

#     for i in 0..<5:
#         if i == 0:
#             ans[i].add("PRRRQLLLPRRQLLPRQ")

#         else:
#             ans[i].add("PRRRQLLLPRRQLLPRQB")
#     echo contena_b[turn]
#     var target_xy = get_target_xy_exist_in_b(contena_b[turn], crane_b[turn], target)
#     echo target_xy

#     for i in turn..<max_turn-10:
#         var target_xy = get_target_xy_exist_in_b(contena_b[i], crane_b[i], target)
#         # echo target_xy
#         if len(target_xy) == 0:
#             break
#         if crane[0][i][0] != -1:
#             continue

#         var
#             (x, y) = (crane[0][i-1][0], crane[0][i-1][1])
#             (tx, ty) = target_xy.pop()
#             root_to_txy = get_root_to_txy(crane[0][i-1][0], crane[0][i-1][1], tx, ty, i, crane_b)
#         target.excl(contena_b[i-1][tx][ty])
#         if len(A[tx]) % 5 != 4:
#             target.incl(contena_b[i-1][tx][ty] + 1)

#         # echo root_to_txy
#         ans[0].add(root_to_txy)
#         for idx, j in root_to_txy:
#             x += SUDLR_table[j][0]
#             y += SUDLR_table[j][1]
#             crane_b[i+idx+1][x][y] = (0, 0)
#             crane[0][i+idx+1] = (x, y, 0)

#         var
#             now_turn = i+len(root_to_txy)
#             root_to_gxy = get_root_to_gxy_by_big_crane(x, y, contena_b[i-1][tx][ty] div 5, 4, now_turn, crane_b)
#         ans[0].add(root_to_gxy)

#         for idx, j in root_to_gxy[0 ..< ^1]:
#             x += SUDLR_table[j][0]
#             y += SUDLR_table[j][1]
#             crane_b[now_turn+idx+1][x][y] = (0, 1)
#             crane[0][now_turn+idx+1] = (x, y, 1)

#         crane_b[now_turn+len(root_to_gxy)][x][y] = (0, 0)
#         crane[0][now_turn+len(root_to_gxy)] = (x, y, 0)
#         contena_b[now_turn+len(root_to_gxy)] = contena_b[i-1]
#         contena_b[now_turn+len(root_to_gxy)][tx][ty] = -1
#         # echo root_to_gxy

#     return ans











proc output(ans: seq[seq[string]]) =
    for i in ans:
        echo i.join("")

proc main() =
    var ans = solve()
    output(ans)
    discard

main()
