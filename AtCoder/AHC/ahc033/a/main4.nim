import macros
import std/times
import std/random
{.checks: off.}
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"


let
    START_TIME = cpuTime()
    N = ii()
    max_turn = 160
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
    A_idx = newseq[int](25)

for i in 0..<N:
    tmp[i] = lii(N)
    A[i] = mapIt(tmp[i], int8(it))
for i in 0..<5:
    for j in 0..<5:
        A_idx[A[i][j]] = j



#bの中の目標のコンテナの座標を返す
# proc get_target_xy(contena_b: seq[array[5, int8]], crane_b: seq[array[5, (int8, int8)]], target: set[int8]): seq[(int8, int8)] =
#     result = newSeqOfCap[(int8, int8)](5)
#     for i in int8(0)..<int8(5):
#         for j in int8(0)..<int8(4):
#             if contena_b[i][j] in target and crane_b[i][j][1] <= 0:
#                 result.add((i, j))
#     return result

proc get_root_to_the_target(sx, sy, target: int8, turn: int, crane_b: seq[seq[array[5, (int8, int8)]]], contena_b: seq[seq[array[5, int8]]]): (bool, int8, int8,
        seq[string]) =
    var
        deq = initDeque[(int8, int8)](25)
        visited = newSeqWith(5, newSeqwith(5, newseqofcap[string](15)))
        tx, ty: int8 = -1
    visited[sx][sy] = @["_"]
    deq.addLast((sx, sy))
    while len(deq) > 0:
        var
            (x, y) = deq.popFirst()
            add_turn = len(visited[x][y])
        if contena_b[turn + add_turn-1][x][y] == target:
            tx = x
            ty = y
            break

        for idx, (i, j) in SUDLR[0 ..< ^1]:
            if add_turn <= 10 and
            0 <= x+i and x+i < 5 and
            0 <= y+j and y+j < 5 and
            (i+j == 0 or len(visited[x+i][y+j]) == 0) and
            crane_b[turn + add_turn][x+i][y+j][0] == -1 and
            (crane_b[turn+add_turn-1][x+i][y+j][0] == -1 or
            crane_b[turn+add_turn-1][x+i][y+j][0] != crane_b[turn+add_turn][x][y][0]):
                visited[x+i][y+j] = visited[x][y]
                visited[x+i][y+j].add(SUDLR_s[idx])
                deq.addLast((x+i, y+j))

    if tx != -1 and len(visited[tx][ty]) >= 1 and crane_b[turn + len(visited[tx][ty])][tx][ty][0] == -1:
        return (true, tx, ty, visited[tx][ty][1..^1])
    else:
        return (false, tx, ty, @[])



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
            if add_turn <= 10 and
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
            if add_turn <= 10 and
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

# proc get_space(contena_b: seq[array[5, int8]]): seq[(int8, int8)] =
#     for (i, j) in space:
#         if contena_b[i][j] == -1:
#             result.add((i, j))
#     return result

proc get_most_near_col(A_n: seq[seq[int8]], target: seq[int8]): int8 =
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
    for i in 0..<25:
        if contena_b[min(start_turn + i, max_turn-1)][x][y] == -1:
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

#ゴールに運ぶ
proc move_to_goal(now_turn: int,
ans: var seq[seq[string]],
contena_b: var seq[seq[array[5, int8]]],
crane_b: var seq[seq[array[5, (int8, int8)]]],
crane: var seq[seq[(int8, int8, int8, int8)]],
target: var seq[int8],
 A_n: var seq[seq[int8]],
bomed: var array[5, bool],
A_idx: seq[int],
rock: var seq[seq[int]],
rock_idx: var seq[int],
out_time: var seq[int],
space: var seq[(int8, int8)]) =
    # var target_xy = get_target_xy(contena_b[now_turn], crane_b[now_turn], target)
    var idx = 0

    while idx < len(target):
        var
            t = target[idx]
            min_len = 1000
            crane_num = -1
            rslt: (seq[string], seq[string])
            gx = int8(t // 5)
            gy = int8(4)


        for i in int8(0)..<int8(5):
            if crane[i][nowturn+1][2] != -1 or bomed[i]:
                continue
            var
                sx = crane[i][now_turn][0]
                sy = crane[i][now_turn][1]
                (flag1, tx, ty, to_txy) = get_root_to_the_target(sx, sy, t, now_turn, crane_b, contena_b)

            if flag1 and now_turn + len(to_txy) > rock[tx][ty] and
            now_turn + len(to_txy) > rock_idx[t]:
                var (flag2, to_gxy) = get_root_to_gxy(i, tx, ty, gx, gy, now_turn+len(to_txy), crane_b, contena_b)
                if flag2 and len(to_txy) + len(to_gxy) < min_len and
                (t % 5 == 0 or now_turn + len(to_txy) + len(to_gxy) > out_time[t-1]):
                    min_len = len(to_txy) + len(to_gxy)
                    crane_num = i
                    rslt = (to_txy, to_gxy)


        if crane_num >= 0:
            target.delete(target.find(t))
            if t % 5 != 4:
                target.add(t+1)

            var
                x = crane[crane_num][now_turn][0]
                y = crane[crane_num][now_turn][1]
                catch = int8(0)
                prv_x, prv_y: int8
                p_turn: int
                new_contena: int8 = -1
                left_turn: int = -1


            for idx, i in rslt[0] & rslt[1]:
                ans[crane_num].add(i)
                x += SUDLR_table[i][0]
                y += SUDLR_table[i][1]
                if i == "P":
                    catch = 1
                    prv_x = x
                    prv_y = y
                    p_turn = now_turn+idx+1

                if left_turn == -1 and
                catch == 1 and
                (x != prv_x or y != prv_y):
                    left_turn = now_turn + idx + 1
                    if prv_y == 0:
                        if len(A_n[prv_x]) > 0:
                            discard A_n[prv_x].pop()
                            new_contena = A[prv_x][A_idx[t]+1]
                        if len(A_n[prv_x]) == 1:
                            space.add((prv_x, int8(0)))
                            if prv_x == 0 or prv_x == 4:
                                space.add((prv_x, int8(1)))

                if i == "Q":
                    catch = 0
                    crane_b[now_turn+idx+1][x][y] = (int8(crane_num), catch)
                    crane[crane_num][now_turn+idx+1] = (x, y, catch, -1)

                    #ロックして他クレーンとの競合を防ぐ
                    rock[prv_x][prv_y] = left_turn
                    rock_idx[t] = now_turn+idx+2
                    out_time[t] = now_turn+idx+2

                    #P ~ のcontenaの削除
                    for turn in left_turn..<max_turn:
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
                    if left_turn != -1:
                        for turn in left_turn..<max_turn:
                            if contena_b[turn][prv_x][prv_y] == -1:
                                contena_b[turn][prv_x][prv_y] = int8(new_contena)
                            else:
                                echo ("永続のコンテナの設置の際にエラーが出ます。2", contena_b[turn][prv_x][prv_y], new_contena)
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
        else:
            idx += 1


#盤面の仮スペースまで運ぶ
proc move_to_b(now_turn: int,
ans: var seq[seq[string]],
contena_b: var seq[seq[array[5, int8]]],
crane_b: var seq[seq[array[5, (int8, int8)]]],
crane: var seq[seq[(int8, int8, int8, int8)]],
target: var seq[int8],
 A_n: var seq[seq[int8]],
bomed: var array[5, bool],
A_idx: seq[int],
rock: var seq[seq[int]],
rock_idx: var seq[int],
out_time: var seq[int],
space: var seq[(int8, int8)]) =
    while true:
        var
            min_len = 1000
            crane_num = -1
            tx = get_most_near_col(A_n, target)
            ty = int8(0)
            t: int8 = -1
            rslt: (seq[string], seq[string])
        if tx == -1:
            break

        for (gx, gy) in space:
            for i in int8(0)..<int8(5):
                if crane[i][nowturn+1][2] != -1 or bomed[i]:
                    continue
                var
                    sx = crane[i][now_turn][0]
                    sy = crane[i][now_turn][1]
                    (flag1, to_txy) = get_root_to_txy(sx, sy, tx, ty, now_turn, crane_b)

                if flag1 and now_turn + len(to_txy) > rock[tx][ty] and now_turn + len(to_txy) > rock_idx[contena_b[now_turn + len(to_txy)+1][tx][ty]]:
                    var (flag2, to_gxy) = get_root_to_gxy(i, tx, ty, gx, gy, now_turn + len(to_txy), crane_b, contena_b)
                    if flag2 and
                    len(to_txy) + len(to_gxy) + abs(gx - contena_b[now_turn + len(to_txy)+1][tx][ty]) < min_len and
                    can_put(now_turn+len(to_txy)+len(to_gxy)-1, gx, gy, contena_b):
                        t = contena_b[now_turn + len(to_txy)+1][tx][ty]
                        min_len = len(to_txy) + len(to_gxy) + abs(gx - contena_b[now_turn + len(to_txy)+1][tx][ty])
                        crane_num = i
                        rslt = (to_txy, to_gxy)

        if crane_num >= 0:
            var
                x = crane[crane_num][now_turn][0]
                y = crane[crane_num][now_turn][1]
                catch = int8(0)
                prv_x, prv_y: int8
                p_turn: int
                new_contena: int8 = -1
                left_turn: int = -1

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

                if left_turn == -1 and
                catch == 1 and
                (x != prv_x or y != prv_y):
                    left_turn = now_turn + idx + 1
                    if prv_y == 0:
                        if len(A_n[prv_x]) > 0:
                            discard A_n[prv_x].pop()
                            new_contena = A[prv_x][A_idx[t]+1]
                        if len(A_n[prv_x]) == 1:
                            space.add((prv_x, int8(0)))
                            if prv_x == 0 or prv_x == 4:
                                space.add((prv_x, int8(1)))



                if i == "Q":
                    catch = 0
                    crane_b[now_turn+idx+1][x][y] = (int8(crane_num), catch)
                    crane[crane_num][now_turn+idx+1] = (x, y, catch, -1)
                    #ロックして他クレーンとの競合を防ぐ
                    rock[prv_x][prv_y] = left_turn
                    rock_idx[t] = now_turn+idx+2


                    #P ~ のcontenaの削除
                    for turn in left_turn..<max_turn:
                        if contena_b[turn][prv_x][prv_y] == t:
                            contena_b[turn][prv_x][prv_y] = -1
                        else:
                            echo ("n永続のコンテナの削除の際にエラーが出ます。", crane_num, turn, contena_b[turn][prv_x][prv_y], t, x, y)
                            echo (rslt[0] & rslt[1])

                            quit()


                    #Q ~ のcontenaの追加
                    if y != 4:
                        for turn in now_turn+idx+1..<max_turn:
                            if contena_b[turn][x][y] == -1:
                                contena_b[turn][x][y] = t
                            else:
                                echo ("n永続のコンテナの設置の際にエラーが出ます。", now_turn, contena_b[turn][x][y], turn, t, x, y, crane_num)
                                echo (rslt)
                                for i in ans:
                                    echo i.join("")
                                echo()
                                for i in 0..turn+10:
                                    echo i
                                    for j in contena_b[i]:
                                        echo j
                                    for j in crane_b[i]:
                                        echo j
                                    for j in 0..<5:
                                        echo crane[j][i]
                                quit()

                    #追加されたコンテナの永続設置
                    if left_turn != -1:
                        for turn in left_turn..<max_turn:
                            if contena_b[turn][prv_x][prv_y] == -1:
                                contena_b[turn][prv_x][prv_y] = int8(new_contena)

                            else:
                                echo ("n永続のコンテナの設置の際にエラーが出ます。2", contena_b[turn][prv_x][prv_y], new_contena[1],
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
        else:
            break

proc collision_avoidance(now_turn: int,
ans: var seq[seq[string]],
contena_b: var seq[seq[array[5, int8]]],
crane_b: var seq[seq[array[5, (int8, int8)]]],
crane: var seq[seq[(int8, int8, int8, int8)]],
target: var seq[int8],
 A_n: var seq[seq[int8]],
bomed: var array[5, bool],
A_idx: seq[int],
rock: var seq[seq[int]],
rock_idx: var seq[int],
out_time: var seq[int]) =
    for i in 0..<5:
        if crane[i][nowturn+1][2] != -1 or bomed[i]:
            continue

        var
            x = crane[i][now_turn][0]
            y = crane[i][now_turn][1]

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

                if tmp > max_move_num:
                    max_move_num = tmp
                    rslt = (idx, p, q)

        if bom:
            bomed[i] = true
            ans[i].add("B")
        else:
            var (idx, p, q) = rslt
            ans[i].add(SUDLR_s[idx])
            crane[i][now_turn+1] = crane[i][now_turn]
            crane[i][now_turn+1][0] = x+p
            crane[i][now_turn+1][1] = y+q
            crane_b[now_turn+1][x+p][y+q] = (int8(i), int8(-1))




proc is_cant_move(now_turn: int, crane: seq[seq[(int8, int8, int8, int8)]]): bool =
    for i in 0..<5:
        if crane[i][nowturn+1][2] != -1:
            return false

    return true

proc solve(space: seq[(int8, int8)]): (bool, seq[seq[string]]) =
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
        target: seq[int8]
        bomed = [false, false, false, false, false]

        A_n = A
        rock = newSeqWith(5, newseqwith(5, -1))
        rock_idx = newseqwith(25, -1)
        out_time = newseqwith(25, -1)
        fin = false
        sp = space


    for i in 0..<5:
        A_n[i].reverse()
        discard A_n[i].pop()

    #初期ターゲット
    for i in 0..<5:
        target.add(int8(5*i))

    #初期盤面
    for i in int8(0)..<int8(5):
        contena_b[0][i][0] = A[i][0]
        crane_b[0][i][0] = (i, int8(-1))
        crane[i][0] = (i, int8(0), int8(-1), int8(-1))

    for i in 0..<max_turn:
        contena_b[i] = contena_b[0]



    for now_turn in 0..<135:
        #全てのクレーンが使用中なら
        if not is_free(crane, now_turn) and not is_free(crane, now_turn+1):
            continue

        #盤面の中のコンテナを出口に運ぶ
        move_to_goal(now_turn, ans, contena_b, crane_b, crane, target, A_n, bomed, A_idx, rock, rock_idx, out_time, sp)

        #新規の追加
        move_to_b(now_turn, ans, contena_b, crane_b, crane, target, A_n, bomed, A_idx, rock, rock_idx, out_time, sp)

        #衝突回避
        collision_avoidance(now_turn, ans, contena_b, crane_b, crane, target, A_n, bomed, A_idx, rock, rock_idx, out_time)



        if is_fin(contena_b[now_turn], ans, now_turn):
            fin = true
            break
        if is_cant_move(now_turn, crane):
            return (false, ans)

    return (fin, ans)


proc get_score(ans: seq[seq[string]]): int =
    result = 0
    for i in 0..<5:
        result = max(result, len(ans[i]))
    return result


proc trans_space(space: set[int8]): seq[(int8, int8)] =
    result = newSeqOfCap[(int8, int8)](len(space))
    for i in space:
        result.add((int8(i div 5), int8(i mod 5)))
    return result


proc climb_hill(): seq[seq[string]] =
    var
        all: seq[int8] = @[0, 1, 5, 6, 7, 8, 10, 11, 15, 16, 17, 18, 20, 21, 13, 3, 23, 12, 2, 22]
        space_not_use: set[int8] = {0, 1, 5, 6, 7, 8, 10, 11, 15, 16, 17, 18, 20, 21}
        space: set[int8] = {13, 3, 23, 12, 2, 22}
        best_score = 10000
        cnt = 0
        (ok, last_ans) = solve(trans_space(space))
    if ok:
        best_score = min(best_score, get_score(last_ans))


    while true:
        if cputime() - START_TIME > 2.85:
            break
        var mode = rand(2)
        #削除
        if mode == 0:
            var v = sample(space)
            space.excl(v)
            space_not_use.incl(v)
            var
                (ok, ans) = solve(trans_space(space))
                score = get_score(ans)
            if ok and score < best_score:
                last_ans = ans
                best_score = score
            else:
                space.incl(v)
                space_not_use.excl(v)

        #追加
        elif mode == 1:
            var v = sample(space_not_use)
            space.incl(v)
            space_not_use.excl(v)
            var
                (ok, ans) = solve(trans_space(space))
                score = get_score(ans)
            if ok and score < best_score:
                last_ans = ans
                best_score = score
            else:
                space.excl(v)
                space_not_use.incl(v)

        #場所変更
        elif mode == 2:
            var
                v = sample(space)
                w = sample(space_not_use)
            space.incl(v)
            space_not_use.excl(v)
            space.excl(w)
            space_not_use.incl(w)
            var
                (ok, ans) = solve(trans_space(space))
                score = get_score(ans)
            if ok and score < best_score:
                last_ans = ans
                best_score = score
            else:
                space.excl(v)
                space_not_use.incl(v)
                space.incl(w)
                space_not_use.excl(w)
    return last_ans




proc output(ans: seq[seq[string]]) =
    for i in ans:
        echo i.join("")

proc main() =
    var ans = climb_hill()
    output(ans)


main()
