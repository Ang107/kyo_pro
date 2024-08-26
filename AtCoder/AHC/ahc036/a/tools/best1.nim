# AHC用のテンプレート
import std/times
import std/random
import atcoder/segtree
# import nimprof
# {.checks: off.}


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
    TIME_LIMIT = 3.0
    N = 600
    T = 600


# -----------------------------------------------------------------------

# 入力を管理するオブジェクト
type Input = object
    N: int
    M: int
    T: int
    LA: int
    LB: int
    TS: array[T+1, int]
    G: array[N, seq[int]]
    xy: array[N, (int, int)]



proc new_input(): Input =
    var
        _, M, _, LA, LB = ii()
        G: array[N, seq[int]]
        TS: array[T+1, int]
        xy: array[N, (int, int)]
    for _ in 0..<M:
        var u, v = ii()
        G[u].add(v)
        G[v].add(u)
    var ts = lii(T)
    for i, j in ts:
        TS[i+1] = j
    for i in 0..<N:
        xy[i] = (ii(), ii())
    return Input(N: N, M: M, T: T, LA: LA, LB: LB, TS: TS, G: G, xy: xy)


# -----------------------------------------------------------------------

# 出力を管理するオブジェクト
type Output = object
    A: seq[int]
    actions: seq[(string, int, int, int)]
proc new_output(input: Input): Output =
    var
        A = newSeqOfCap[int](input.LA)
        actions = newSeqOfCap[(string, int, int, int)](100000)

    return Output(A: A, actions: actions)
proc output(self: Output) =
    stdout.writeLine(self.A.join(" "))
    for i in self.actions:
        if i[0] == "s":
            stdout.writeLine(i[0], " ", i[1], " ", i[2], " ", i[3])
        else:
            stdout.writeLine(i[0], " ", i[1])


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
# s to g の最短経路
proc bfs(input: Input, s, g: int, v: array[N, bool], use_visited: bool): seq[int] =
    var
        deq = initDeque[int](N)
        visited: array[N, (int, int)]
    for i in 0..<N:
        visited[i] = (-1, -1)
    # g -> sで経路を求める。（復元時にreverseが不要になる）
    deq.addLast(g)
    visited[g] = (0, -1)
    while deq.len() > 0:
        var now = deq.popFirst()
        if now == s:
            break
        for next in input.G[now]:
            if visited[next][0] == -1 and (not use_visited or not v[next] or
                    next == g):
                deq.addLast(next)
                visited[next] = (visited[now][0] + 1, now)
    var root = newSeqOfCap[int](visited[g][0])
    var now = s
    while now != -1:
        root.add(now)
        now = visited[now][1]
    return root

# s からスタートしたときのvisitedを返す。
proc bfss(input: Input, s: int): array[N, (int, int)] =
    var
        deq = initDeque[int](N)
        visited: array[N, (int, int)]
    for i in 0..<N:
        visited[i] = (-1, -1)
    deq.addLast(s)
    visited[s] = (0, -1)
    while deq.len() > 0:
        var now = deq.popFirst()
        for next in input.G[now]:
            if visited[next][0] == -1:
                deq.addLast(next)
                visited[next] = (visited[now][0] + 1, now)

    return visited

proc make_root(visited: array[N, (int, int)], g: int): seq[int] =
    var root = newSeqOfCap[int](visited[g][0])
    var now = g
    while now != -1:
        root.add(now)
        now = visited[now][1]
    root.reverse()
    return root

proc distance(xy1, xy2: (int, int)): int =
    return ((xy1[0]-xy2[0]) ** 2) + ((xy1[1]-xy2[1]) ** 2)

proc make_A(input: Input, output: var Output) =
    var
        visited: array[N, bool]
        target = [(0, 0), (0, 250), (0, 500), (0, 750), (0, 1000),
                    (750, 1000), (500, 1000), (250, 1000), (1000, 1000),
                    (1000, 750), (1000, 500), (1000, 250), (1000, 0),
                    (750, 0), (500, 0), ((250, 0))]

        center = (500, 500)
        # 距離、インデックス
        by_center = (INF64, -1)
        by_target: array[16, (int, int)]
        mid_by_target: array[16, int]
    for i in 0..<16:
        by_target[i] = (INF64, -1)
    for index, xy in input.xy:
        var dis = distance(center, xy)
        if dis < by_center[0]:
            by_center = (dis, index)
        for index2, t in target:
            var dis = distance(t, xy)
            if dis < by_target[index2][0]:
                by_target[index2] = (dis, index)
    # echo "#", by_target
    for i, (_, index) in by_target:
        if i & 1 == 0:
            var root = bfs(input, index, by_center[1], visited, false)
            mid_by_target[i] = root[root.len()//2]
            for index in 0..<root.len():
                visited[root[index]] = true
                output.A.add(root[index])
        else:
            var root = bfs(input, by_center[1], index, visited, false)
            mid_by_target[i] = root[root.len()//2]
            for index in 1..<root.len():
                visited[root[index]] = true
                output.A.add(root[index])


    # for i in 0..<16:
    #     var
    #         s = by_target[i][1]
    #         g = by_target[(i+1)%16][1]
    #     if i == 0:
    #         var root = bfs(input, s, g, visited, false)
    #         for index in 0..<root.len():
    #             visited[root[index]] = true
    #             output.A.add(root[index])
    #     else:
    #         var root = bfs(input, s, g, visited, false)
    #         for index in 1..<root.len():
    #             visited[root[index]] = true
    #             output.A.add(root[index])

    # for i in 0..<16:
    #     var
    #         s = mid_by_target[i]
    #         g = mid_by_target[(i+1)%16]
    #     if i == 0:
    #         var root = bfs(input, s, g, visited, false)
    #         for index in 0..<root.len():
    #             visited[root[index]] = true
    #             output.A.add(root[index])
    #     else:
    #         var root = bfs(input, s, g, visited, false)
    #         for index in 1..<root.len():
    #             visited[root[index]] = true
    #             output.A.add(root[index])

    # 移動回数の最小値、スタート地点、インデックス
    var dis: array[N, (int, int, int)]
    for i in 0..<N:
        dis[i] = (INF64, -1, i)

    for i in 0..<N:
        if visited[i]:
            var v = bfss(input, i)
            for j in 0..<N:
                if dis[j][0] > v[j][0]:
                    dis[j][0] = v[j][0]
                    dis[j][1] = i
    var is_need_area: array[N, bool]
    for i in input.TS[1..^1]:
        is_need_area[i] = true

    dis.sort(proc (a, b: (int, int, int)): int = cmp(b[0], a[0]))
    for (d, s, index) in dis:
        if not visited[index] and is_need_area[index]:
            var root = bfs(input, s, index, visited, false)
            for i in root[1..^1]:
                output.A.add(i)
                visited[i] = true

    for i in 0..<T:
        var
            s = input.TS[i]
            g = input.TS[i+1]
        var root = bfs(input, s, g, visited, false)
        for i in root[1..^1]:
            output.A.add(i)
        if len(output.A) >= input.LA:
            break
    while output.A.len() < input.LA:
        output.A.add(0)
    while output.A.len() > input.LA:
        discard output.A.pop()

    # proc dfs(output: var Output, now: int, depth: int) =
    #     output.A.add(now)
    #     all_visited[now] = true
    #     if depth == input.LB:
    #         return

    #     for next in input.G[now]:
    #         if not all_visited[next]:
    #             dfs(output, next, depth+1)
    #             break
    # proc dfs2(output: var Output, now, fr: int, depth: int) =
    #     output.A.add(now)
    #     if depth == input.LB:
    #         return
    #     for next in input.G[now]:
    #         if next != fr:
    #             dfs2(output, next, now, depth+1)
    #             break


    # for i in 0..<N:
    #     if not all_visited[i]:
    #         dfs(output, i, 0)
    # while output.A.len() < input.LA:
    #     dfs2(output, sample(input.TS), -1, 0)

    # while output.A.len() > input.LA:
    #     discard output.A.pop()

    # echo output.A


proc make_index_list(input: Input, output: Output): array[N, seq[int]] =
    for idx, i in output.A:
        result[i].add(idx)
    # for i in 0..<N:
    #     echo "#", (i, result[i])
    return result
type Node1 = object
    v_index: int
    times: int # そこまでの信号変化の回数の最小値
    change_signal: int # ここに来る直前に使った信号変化のインデックス(使用していない場合は-1)
    frm: (int, int) # どこから来たか
proc new_node1(v_index, times, change_signal: int, frm: (int, int)): Node1 =
    return Node1(v_index: v_index, times: times, frm: frm,
            change_signal: change_signal)
type Node2 = object
    times: int   # 使用した回数
    v_index: int # 頂点のインデックス
    signal_state: int #信号の状態
proc new_node2(times, v_index, signal_state: int): Node2 =
    return Node2(times: times, v_index: v_index, signal_state: signal_state)
proc `<`(a, b: Node2): bool =
    a.times < b.times
proc dijkstra(input: Input, output: var Output, index_list: array[N, seq[int]],
        s, g: int, last_colorchange_signal: seq[int]): seq[int] =
    # i番目の頂点に、信号がjの状態で、到達する場合のnode
    var
        visited = newSeq[Table[int, Node1]()](N)
        heap = initHeapQueue[Node2]()
        init_signal: int
    if last_colorchange_signal.len() == 0:
        init_signal = -1
    else:
        #オリジナル
        init_signal = -2
    visited[s][init_signal] = new_node1(s, 0, -1, (-1, -1))
    heap.push(new_node2(0, s, init_signal))
    while heap.len() > 0:
        var node2 = heap.pop()
        var tmp = visited[node2.v_index][node2.signal_state]
        if node2.v_index == g:
            break
        if node2.times > tmp.times:
            continue
        var blues: seq[int]
        if node2.signal_state >= 0:
            var
                l = node2.signal_state
                r = min(input.LA, l+input.LB)
            blues = output.A[l..<r]
        elif node2.signal_state == -2:
            blues = last_colorchange_signal
        for next in input.G[node2.v_index]:
            if next in blues:
                if node2.signal_state notin visited[next] or
                    node2.times < visited[next][node2.signal_state].times:
                    heap.push(new_node2(node2.times, next, node2.signal_state))
                    visited[next][node2.signal_state] =
                        new_node1(next, node2.times, -1, (node2.v_index,
                                node2.signal_state))
            else:
                for i in index_list[next]:
                    var
                        l = max(0, i-input.LB+1)
                        r = i
                    for j in 0..<2:
                        var index: int
                        if j == 1:
                            index = l
                        else:
                            index = r
                        var blues =
                            output.A[index..<min(input.LA, index+input.LB)]
                        if index notin visited[next] or
                            node2.times+1 < visited[next][index].times:
                            heap.push(new_node2(node2.times+1, next, index))
                            visited[next][index] =
                                new_node1(next, node2.times+1, index, (
                                        node2.v_index, node2.signal_state))
    var
        actions = newSeqOfCap[(string, int, int, int)](100)
        now = new_node1(-1, INF64, -1, (-1, -1))
    for signal_state, node1 in visited[g]:
        if node1.times < now.times:
            now = node1
    var
        cnt = 0
        s_index = newSeqOfCap[int](10)
        last_signal: seq[int]
    while now.frm[0] != -1:
        actions.add(("m", now.v_index, -1, -1))
        if now.change_signal != -1:
            cnt += 1
            if cnt == 1:
                last_signal = output.A[now.change_signal..<now.change_signal+min(
                        input.LB, input.LA-now.change_signal)]
            s_index.add(actions.len())
            actions.add(("s", min(input.LB, input.LA-now.change_signal),
                now.change_signal, 0))
        now = visited[now.frm[0]][now.frm[1]]

    proc dfs(s: int, blues: seq[int]): int =
        var
            deq = newSeqOfCap[int](blues.len())
            visited = newSeqOfCap[int](blues.len())
        deq.add(s)
        visited.add(s)
        while deq.len() > 0:
            var v = deq.pop()
            for next in input.G[v]:
                if next in blues and next notin visited:
                    visited.add(next)
                    deq.add(next)

        return visited.len()
    if s_index.len() > 0:
        var
            must_vs = newSeqOfCap[int](s_index[0])
            blues: seq[int]
            index: int
            v = now.v_index
            max_num = -1
        for i in 0..<s_index[0]:
            must_vs.add(actions[i][1])

        if s_index.len() == 1:
            blues = last_colorchange_signal


        elif s_index.len() >= 2:
            blues = output.A[actions[s_index[1]][2]..<min(actions[s_index[1]][
                                        2]+actions[s_index[1]][2], input.LA)]

        for i in actions[s_index[0]][2]..<actions[s_index[0]][2] + input.LB:
            if output.A[i] == g:
                index = i
                break
        for l in max(0, index-input.LB+1)..index:
            for r in index..min(index+input.LB-1, input.LA-1):
                var length = r - l + 1
                for i in 0..<input.LB-length:
                    var nblues = blues
                    if nblues.len() == input.LB:
                        nblues[i..<i+length] = output.A[l..r]
                    else:
                        nblues = output.A[l..r]
                    var ok = true
                    for j in must_vs:
                        if j in nblues:
                            discard
                        else:
                            ok = false
                            break
                    if not ok:
                        continue
                    var ret = dfs(g, nblues)
                    if ret > max_num:
                        max_num = ret
                        actions[s_index[0]][1] = length
                        actions[s_index[0]][2] = l
                        actions[s_index[0]][3] = i
                        last_signal = nblues
                        echo "#", (ret, actions[s_index[0]])

    actions.reverse()
    stdout.writeLine("#", cnt)
    for i in actions:
        output.actions.add(i)
    return last_signal







# proc dijkstra(input: Input, output: var Output, index_list: array[N, seq[int]],
#         s, g, last_colorchange_signal: int) =
#     # 信号を変えた回数、信号変更を使った履歴(index,どこで使ったか)、どこから来たか
#     var
#         visited = newSeqWith(N, (INF64, newSeq[(int, int)](0), -1, newSeq[int](0)))
#         heap = initHeapQueue[(int, int)]()
#     visited[s] = (0, @[(last_colorchange_signal, -1)], -1, @[s])
#     heap.push((0, s))
#     while heap.len() > 0:
#         var (times, now) = heap.pop()
#         if now == g:
#             break
#         if times > visited[now][0]:
#             continue
#         var blues: seq[int]
#         if visited[now][1][^1][0] != -1:
#             var
#                 l = visited[now][1][^1][0]
#                 r = min(input.LA, l+input.LB)
#             if l != -1:
#                 blues = output.A[l..<r]
#         for next in input.G[now]:
#             if next in blues:
#                 if times < visited[next][0]:
#                     heap.push((times, next))
#                     visited[next] = (times, visited[now][1], now, visited[now][
#                             3] & @[next])
#             else:
#                 for i in index_list[next]:
#                     var
#                         l = max(0, i - input.LB + 1)
#                         r = i
#                     for j in 0..<2:
#                         var index: int
#                         if j == 1:
#                             index = l
#                         else:
#                             index = r
#                         var blues = output.A[index ..<
#                         min(input.LA, index+input.LB)]
#                         var
#                             # 今、一個前
#                             nexts = newSeqOfCap[(int, int)](blues.len())
#                             vis = newSeqOfCap[int](blues.len())
#                             deq = initDeque[(int, int)](blues.len())
#                         deq.addLast((next, now))
#                         vis.add(next)
#                         nexts.add((next, now))
#                         while deq.len() > 0:
#                             var (now, frm) = deq.popFirst()
#                             for next in input.G[now]:
#                                 if next in blues and next notin vis:
#                                     vis.add(next)
#                                     deq.addLast((next, now))
#                                     nexts.add((next, now))
#                         for (next, n) in nexts:
#                             if times + 1 < visited[next][0]:
#                                 heap.push((times+1, next))
#                                 visited[next] = (times+1, visited[now][1] & @[(
#                                         index, now)], n, visited[n][3] & @[next])

#     # # 行動の復元
#     # var
#     #     num = input.LB * visited[g][1].len()
#     #     root = newSeqOfCap[int](num)
#     #     frm: array[N, int]
#     #     deq = initDeque[(int, seq[int])](num)
#     #     index = 1
#     #     first_cand: seq[int]
#     # frm.fill(-1)
#     # if visited[g][1][0][0] != -1:
#     #     first_cand = output.A[visited[g][1][0][0]..<min(input.LA, visited[g][1][
#     #             0][0]+input.LB)]

#     # deq.addLast((s, first_cand))
#     # echo visited[g][1]
#     # echo deq
#     # while deq.len() > 0:
#     #     var (now, cand) = deq.popLast()
#     #     echo (now, cand)
#     #     for (i, j) in visited[g][1]:
#     #         if j == now:
#     #             cand = output.A[i..<min(input.LA, i+input.LB)]
#     #             echo (i, j, now, output.A[i..<min(input.LA, i+input.LB)])
#     #             echo input.G[now]

#     #     for next in input.G[now]:
#     #         if next in cand and frm[next] == -1:
#     #             deq.addLast((next, cand))
#     #             frm[next] = now
#     # echo frm
#     # root.add(g)
#     # echo (root, s, g)
#     # while root[^1] != s:
#     #     root.add(frm[root[^1]])
#     var root = visited[g][3]
#     var index = 1
#     # echo root
#     # echo visited[g][1]
#     if index < visited[g][1].len() and s == visited[g][1][index][1]:
#         output.actions.add(("s", min(input.LB, input.LA-visited[g][1][index][
#                 0]), visited[g][1][index][0], 0))
#         index += 1
#     for i in root[1..^1]:
#         output.actions.add(("m", i, -1, -1))
#         var tmp = (-1, -1)
#         if index < visited[g][1].len():
#             tmp = visited[g][1][index]
#         if i == tmp[1]:
#             output.actions.add(("s", min(input.LB, input.LA-tmp[0]), tmp[0], 0))
#             index += 1




    # var
    #     actions = newSeqOfCap[(string, int, int, int)](100)
    #     now = g
    #     index = 1

    # while now != s:
    #     if visited[now][1][^1][1] == visited[now][2]:
    #         actions.add(("m", now, 0, 0))
    #         # actions.add(("s", min(input.LB, input.LA-visited[now][1][^1][0]),
    #         #         visited[now][1][^1][0], 0))
    #     else:
    #         actions.add(("m", now, 0, 0))
    #     now = visited[now][2]
    # actions.reverse()
    # echo actions
    # echo visited[g][1]
    # if index < visited[g][1].len() and s == visited[g][1][index][1]:
    #     output.actions.add(("s", min(input.LB, input.LA-visited[g][1][index][0]),
    #                     visited[g][1][index][0], 0))
    #     index += 1
    # for i in actions:
    #     output.actions.add(i)
    #     if index < visited[g][1].len() and visited[g][1][index][1] == i[1]:
    #         output.actions.add(("s", min(input.LB, input.LA-visited[g][1][index][0]),
    #                     visited[g][1][index][0], 0))
    #         index += 1














proc make_actions(input: Input, output: var Output, index_list: array[N, seq[int]]) =
    var color_change_signal: seq[int] = @[]
    for i in 0..<T:
        var
            s = input.TS[i]
            g = input.TS[i+1]
        color_change_signal = dijkstra(input, output, index_list, s, g, color_change_signal)


proc deb(input: Input, output: var Output) =
    for i in 0..<input.LA-input.LB+1:
        output.actions.add(("s", input.LB, i, 0))




# -----------------------------------------------------------------------


type Solver = object

proc new_solver(): Solver =
    return Solver()

proc solve(self: Solver, input: Input, output: var Output, time: Time) =
    make_A(input, output)
    var index_list = make_index_list(input, output)
    # make_actions(input, output, index_list)
    deb(input, output)
    discard

# -----------------------------------------------------------------------

proc main() =
    var
        time = new_time(TIME_LIMIT)
        input = new_input()
        output = new_output(input)
    var solver = new_solver()
    solver.solve(input, output, time)
    output.output()
    time.out_paased_time()
main()
