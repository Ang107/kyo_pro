# AHC用のテンプレート
import std/times
import std/random
import atcoder/segtree
# import nimprof
{.checks: off.}
# when not declared CPLIB_TMPL_QCFIUM:
#     const CPLIB_TMPL_QCFIUM* = 1
#     {.emit: """
#     #pragma GCC target ("avx2")
#     #pragma GCC optimize("O3")
#     #pragma GCC optimize("unroll-loops")
#     """.}
# when not defined(second_compile):
#     static:
#         echo staticExec("nim cpp -d:danger -o:a.out -d:second_compile --opt:speed --multimethods:on --warning[SmallLshouldNotBeUsed]:off  --hints:off Main.nim")
#         quit()
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
type Node1 = object
    v_index: int
    times: int # そこまでの信号変化の回数の最小値
    change_signal: int # ここに来る直前に使った信号変化のインデックス(使用していない場合は-1)
    frm: (int, int) # どこから来たか
proc new_node1(v_index, times, change_signal: int, frm: (int,
        int)): Node1 =
    return Node1(v_index: v_index, times: times, frm: frm,
            change_signal: change_signal)
type Node2 = object
    times: int   # 使用した回数
    v_index: int # 頂点のインデックス
    signal_state: int #信号の状態
proc new_node2(times, v_index, signal_state: int): Node2 =
    return Node2(times: times, v_index: v_index,
            signal_state: signal_state)
proc `<`(a, b: Node2): bool =
    a.times < b.times
proc `<`(a, b: Node1): bool =
    a.times < b.times
proc min(t: Table[int, Node1]): (int, Node1) =
    var
        signal = -1
        node1 = new_node1(-1, INF32, -1, (-1, -1))
    for s, n in t:
        if n < node1:
            node1 = n
            signal = s
    return (signal, node1)
# -----------------------------------------------------------------------
type HashMap = object
    s: seq[(int, Node1)]

proc new_hashmap(): HashMap =
    return HashMap(s: newSeqOfCap[(int, Node1)](10))
proc `[]`(self: HashMap, p: int): (int, Node1) =
    return self.s[p]
proc `[]=`(self: var HashMap, p: int, kv: (int, Node1)) =
    if p == -1:
        self.s.add(kv)
    else:
        self.s[p][1] = kv[1]
proc add(self: var HashMap, k: int, v: Node1) =
    self.s.add((k, v))
# 見つかったらインデックスを、無ければマイナス1を返す。
proc index(self: HashMap, key: int): int =
    for i, (k, v) in self.s:
        if k == key:
            return i
    return -1


# -----------------------------------------------------------------------

# 定数
const
    TIME_LIMIT = 3.0
    N = 600
    T = 600
var
    roots: array[N, array[N, (int, int)]]
    fin_time: float
    a_index: seq[seq[int]]
    need_signal_change_times: array[N, array[N, HashMap]]
    can_go: array[N, bool]

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
        actions = newSeqOfCap[(string, int, int, int)](20000)
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

# s からスタートしたときのvisitedを返す。
proc bfss(input: Input, s: int): array[N, (int, int)] =
    var
        deq = initDeque[int](N)
        # 距離,どこから来たか
        visited: array[N, (int, int)]

    visited.fill((-1, -1))
    deq.addLast(s)
    visited[s] = (0, -1)
    while deq.len() > 0:
        var now = deq.popFirst()
        for next in input.G[now]:
            if visited[next][0] == -1:
                deq.addLast(next)
                visited[next] = (visited[now][0] + 1, now)
    return visited

proc bfs(s, g: int): seq[int] =
    var
        v = roots[g]
    var root = newSeqOfCap[int](v[s][0])
    var now = s
    while now != -1:
        root.add(now)
        now = v[now][1]
    return root

proc distance(xy1, xy2: (int, int)): int =
    return ((xy1[0]-xy2[0]) ** 2) + ((xy1[1]-xy2[1]) ** 2)
#tspの経路を求める
proc tsp(input: Input, output: Output, time: Time): seq[int] =
    #diss[i] = iからの（距離、どこから来たか、座標）
    var diss: array[N, seq[(int, int)]]
    for i in 0..<N:
        diss[i] = newSeqOfCap[(int, int)](N)
        for j in 0..<N:
            diss[i].add((roots[i][j][0], j))
        diss[i].sort(proc (a, b: (int, int)): int = cmp(a[0], b[0]))



    proc in_tsp(target_seq: seq[int], split_num: int): seq[int] =
        # 貪欲
        var
            A = newSeqOfCap[int](input.LA)
            target = target_seq.sorted().deduplicate(isSorted = true)
            visited: array[N, bool]
            s = target_seq[0]
            order = newSeqOfCap[int](target.len()+1)
        order.add(s)
        visited[s] = true
        while order.len() < target.len():
            for (d, i) in diss[order[^1]]:
                if i in target and visited[i] == false:
                    order.add(i)
                    visited[i] = true
                    break

        proc get_all_dis(order: seq[int]): int =
            for i in 0..<order.len()-1:
                var
                    s = order[i]
                    g = order[(i+1)%order.len()]
                result += roots[s][g][0]

        # 2opt
        var all_dis = get_all_dis(order)
        var updated = true
        while updated:
            updated = false
            for i in 0..<order.len()-1:
                for j in i+1..<order.len():
                    var prv, nxt: int
                    if i == 0 and j == order.len() - 1:
                        continue
                    elif i == 0:
                        prv = roots[order[j]][order[(j+1)%order.len()]][0]
                        nxt = roots[order[i]][order[(j+1)%order.len()]][0]
                    elif j == order.len() - 1:
                        prv = roots[order[i-1]][order[i]][0]
                        nxt = roots[order[i-1]][order[j]][0]
                    else:
                        prv = roots[order[i-1]][order[i]][0] + roots[order[j]][
                            order[(j+1)%order.len()]][0]
                        nxt = roots[order[i-1]][order[j]][0] + roots[order[i]][
                            order[(j+1)%order.len()]][0]
                    if prv > nxt:
                        order[i..j] = order[i..j].reversed()
                        updated = true
                        all_dis += nxt - prv

        # 経路の構築
        A.setLen(0)
        for i in 0..<order.len()-1:
            var
                s = order[i]
                g = order[(i+1)%order.len()]
            if i == order.len() - 2:
                for j in bfs(s, g):
                    A.add(j)
            else:
                for j in bfs(s, g)[0 ..< ^1]:
                    A.add(j)
        var nA = newSeqOfCap[int](A.len())
        for index, i in A:
            if nA.len() >= 2 and nA[^2] == i:
                continue
            nA.add(i)
        return nA


    result = in_tsp(input.TS.toSeq(), 1)
    # stderr.writeLine(result.len())
    return result

#tspの経路を求める
# proc tsp(input: Input, output: Output, time: Time): seq[int] =


#     #diss[i] = iからの（距離、座標）
#     var diss: array[N, seq[(int, int)]]
#     for i in 0..<N:
#         diss[i] = newSeqOfCap[(int, int)](N)
#         for j in 0..<N:
#             diss[i].add((roots[i][j][0], j))
#         diss[i].sort(proc (a, b: (int, int)): int = cmp(a[0], b[0]))



#     proc in_tsp(target_seq: seq[int], split_num: int): seq[int] =
#         # 貪欲
#         var
#             A = newSeqOfCap[int](input.LA)
#             target = target_seq.deduplicate()
#             visited: array[N, bool]
#             s = target_seq[0]
#             order = newSeqOfCap[int](target.len())
#             to_index: array[N, int]
#         order.add(s)
#         visited[s] = true
#         while order.len() < target.len():
#             for (d, i) in diss[order[^1]]:
#                 if i in target and visited[i] == false:
#                     order.add(i)
#                     visited[i] = true
#                     break
#         for i, j in order:
#             to_index[j] = i


#         proc get_all_dis(order: seq[int]): int =
#             for i in 0..<order.len()-1:
#                 var
#                     s = order[i]
#                     g = order[(i+1)%order.len()]
#                 result += roots[s][g][0]


#         # var all_dis = get_all_dis(order)

#         # 2opt
#         proc two_opt(o: seq[int]): seq[int] =
#             var
#                 order = o
#                 updated = true
#                 sum_change = 0
#             while updated:
#                 updated = false
#                 for index in 0..<order.len()-1:
#                     var i = index
#                     if i - 1 >= 0:
#                         for (d, v) in diss[order[i-1]]:
#                             var j = to_index[v]
#                             if i == j:
#                                 break
#                             if j < i:
#                                 continue

#                             var prv, nxt: int
#                             if i == 0 and j == order.len() - 1:
#                                 continue
#                             elif i == 0:
#                                 prv = roots[order[j]][order[(j+1)%order.len()]][0]
#                                 nxt = roots[order[i]][order[(j+1)%order.len()]][0]
#                             elif j == order.len() - 1:
#                                 prv = roots[order[i-1]][order[i]][0]
#                                 nxt = roots[order[i-1]][order[j]][0]
#                             else:
#                                 prv = roots[order[i-1]][order[i]][0] + roots[
#                                         order[j]][
#                                     order[(j+1)%order.len()]][0]
#                                 nxt = roots[order[i-1]][order[j]][0] + roots[
#                                         order[i]][
#                                     order[(j+1)%order.len()]][0]
#                             if prv > nxt:
#                                 order[i..j] = order[i..j].reversed()
#                                 for k in i..j:
#                                     to_index[order[k]] = k
#                                 updated = true
#                                 sum_change += nxt - prv


#                     for (d, v) in diss[order[i]]:
#                         var j = to_index[v]
#                         if i-1 == j:
#                             break
#                         j -= 1
#                         if j < i:
#                             continue
#                         var prv, nxt: int
#                         if i == 0 and j == order.len() - 1:
#                             continue
#                         elif i == 0:
#                             prv = roots[order[j]][order[(j+1)%order.len()]][0]
#                             nxt = roots[order[i]][order[(j+1)%order.len()]][0]
#                         elif j == order.len() - 1:
#                             prv = roots[order[i-1]][order[i]][0]
#                             nxt = roots[order[i-1]][order[j]][0]
#                         else:
#                             prv = roots[order[i-1]][order[i]][0] + roots[order[
#                                     j]][
#                                 order[(j+1)%order.len()]][0]
#                             nxt = roots[order[i-1]][order[j]][0] + roots[order[
#                                     i]][
#                                 order[(j+1)%order.len()]][0]
#                         if prv > nxt:
#                             order[i..j] = order[i..j].reversed()
#                             for k in i..j:
#                                 to_index[order[k]] = k
#                             updated = true
#                             sum_change += nxt - prv
#             return order
#         proc kick(o: seq[int]): seq[int] =
#             var
#                 stop = false
#                 order = newSeqOfCap[int](o.len())
#                 edges: array[4, int]
#             while not stop:
#                 stop = true
#                 edges = [rand(o.len()-2),
#                             rand(o.len()-2),
#                             rand(o.len()-2),
#                             rand(o.len()-2)]
#                 edges.sort()
#                 for i in 0..<3:
#                     if edges[i] + 1 < edges[i+1]:
#                         discard
#                     else:
#                         stop = false
#             for i in 0..edges[0]:
#                 order.add(o[i])
#             for i in edges[2]+1..edges[3]:
#                 order.add(o[i])
#             for i in edges[1]+1..edges[2]:
#                 order.add(o[i])
#             for i in edges[0]+1..edges[1]:
#                 order.add(o[i])
#             for i in edges[3]+1..<o.len():
#                 order.add(o[i])
#             return order


#         order = two_opt(order)
#         # while time.get_passed_time() < 1.0:
#         # for _ in 0..<30:
#         #     var o = order
#         #     o = kick(o)
#         #     o = two_opt(o)
#         #     var best_score = get_all_dis(order)
#         #     var new_score = get_all_dis(o)
#         #     # echo "# score", (best_score, new_score)
#         #     if new_score < best_score:
#         #         best_score = new_score
#         #         order = o
#         # 経路の構築
#         A.setLen(0)
#         for i in 0..<order.len()-1:
#             var
#                 s = order[i]
#                 g = order[(i+1)%order.len()]
#             if i == order.len() - 2:
#                 for j in bfs(s, g):
#                     A.add(j)
#             else:
#                 for j in bfs(s, g)[0 ..< ^1]:
#                     A.add(j)
#         var nA = newSeqOfCap[int](A.len())
#         for index, i in A:
#             if nA.len() >= 2 and nA[^2] == i:
#                 continue
#             nA.add(i)
#         return nA


#     result = in_tsp(input.TS.toSeq(), 1)
#     stderr.writeLine(result.len())
#     return result


proc make_A(input: Input, output: var Output, time: Time) =
    output.A = tsp(input, output, time)
    var all_root = newSeqOfCap[int](10000)
    for i in 0..<T:
        var
            s = input.TS[i]
            g = input.TS[i+1]
        var root = bfs(s, g)
        for i in root[1..^1]:
            #往復は無視
            if all_root.len() >= 2 and all_root[^2] == i:
                continue
            all_root.add(i)


    var
        can_use_len = input.LA - output.A.len()
        ret: int
        cnt: array[N, int]
        max_cnt = 0
        now_cnt = 0

    for i in 0..<can_use_len:
        cnt[all_root[i]] += 1
        if cnt[all_root[i]] == 1:
            now_cnt += 1

    # 理想の動きのなかで、最も色んな頂点を通る部分を追加
    # 中に含まれる各スパンの数が多いやつとかもありかも
    for i in 0..<all_root.len() - can_use_len:
        cnt[all_root[i]] -= 1
        if cnt[all_root[i]] == 0:
            now_cnt -= 1
        cnt[all_root[i+can_use_len]] += 1
        if cnt[all_root[i+can_use_len]] == 1:
            now_cnt += 1
        if now_cnt > max_cnt:
            max_cnt = now_cnt
            ret = i
    for i in ret..<ret+can_use_len:
        output.A.add(all_root[i])

    while output.A.len() < input.LA:
        output.A.add(0)
    output.A = output.A[0..<input.LA]




proc make_index_list(input: var Input, output: Output): array[N, seq[int]] =
    can_go[0] = true
    for idx, i in output.A:
        can_go[i] = true
        result[i].add(idx)
    var newG: array[N, seq[int]]
    for i in 0..<N:
        for j in input.G[i]:
            if can_go[j]:
                newG[i].add(j)
    input.G = newG

    return result

proc make_a_index(input: Input, output: Output) =
    a_index = newSeqOfCap[newSeqOfCap[int](input.LB)](input.LA)
    for i in 0..<input.LA:
        a_index.add(output.A[i..<min(i+input.LB, input.LA)])

proc normal_dijkstra(input: Input, output: var Output, index_list: array[N, seq[
        int]], s, g, next_g: int, last_colorchange_signal: seq[int],
                time: Time): seq[int] =
    # i番目の頂点に、信号がjの状態で、到達する場合のnode
    var
        visited: array[N, HashMap]
        deq = initDeque[Node2]()
    visited.fill(new_hashmap())
    visited[s].add(-1, new_node1(s, 0, -1, (-1, -1)))
    deq.addLast(new_node2(0, s, -1))
    result = last_colorchange_signal
    while deq.len() > 0:
        var node2 = deq.popFirst()
        var tmp = visited[node2.v_index][visited[node2.v_index].index(
                        node2.signal_state)][1]

        if node2.times > tmp.times:
            continue
        if node2.v_index == g:
            break
        var blues: seq[int]
        if node2.signal_state == -1:
            blues = last_colorchange_signal
        else:
            blues = a_index[node2.signal_state]

        for next in input.G[node2.v_index]:
            if next in blues:
                var index = visited[next].index(node2.signal_state)
                if index == -1 or
                    node2.times < visited[next][index][1].times:
                    deq.addFirst(new_node2(node2.times, next,
                            node2.signal_state))
                    visited[next][index] =
                        (node2.signal_state, new_node1(next,
                                node2.times, -1, (node2.v_index,
                                        node2.signal_state)))
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
                        var blues = a_index[index]
                        var tmp = visited[next].index(index)
                        if tmp == -1 or
                            node2.times+1 < visited[next][tmp][1].times:
                            deq.addLast(new_node2(node2.times+1, next, index))
                            visited[next][tmp] = (index, new_node1(next, node2.times+1, index, (
                                        node2.v_index, node2.signal_state)))
    var
        now = new_node1(-1, INF64, -1, (-1, -1))
        actions = newSeqOfCap[(string, int, int, int)](50)
        flag = true
    if next_g != -1 and time.get_passed_time() < 1.8:
        var
            nodes = newSeqOfCap[Node1](4)
            evaluation = initTable[(int, int, int, int, int), int](0)
            #信号を最後に使う直前のインデックス、直前の信号の状態、長さ、Aのインデックス、Bのインデックス
            best_action = (-1, -1, -1, -1, -1)
            best_score = INF64

        proc evalueate(now_index, g, next_g: int, blues: seq[int]): int =
            var visited = newSeqOfCap[int](0)
            var deq = newSeqOfCap[int](0)
            deq.add(now_index)
            result = INF64
            while deq.len() > 0:
                var v = deq.pop()
                for next in input.G[v]:
                    if next in blues and next notin visited:
                        visited.add(next)
                        deq.add(next)
            if g notin visited:
                return result
            for i in visited:
                result = min(result, roots[i][next_g][0])
            return result


        nodes.add(new_node1(-1, INF64, -1, (-1, -1)))
        for (signal_state, node1) in visited[g].s:
            if node1.times < nodes[0].times:
                nodes = @[node1]
            elif node1.times == nodes[0].times:
                nodes.add(node1)

        # それぞれで最後に信号変化を使用するところまでさかのぼる
        for i in 0..<nodes.len():
            while nodes[i].change_signal == -1 and nodes[i].frm[0] != -1:
                var index = visited[nodes[i].frm[0]].index(nodes[i].frm[1])
                nodes[i] = visited[nodes[i].frm[0]][index][1]
        var added = initHashSet[(int, int, int)](0)
        for i in 0..<nodes.len():
            if nodes[i].change_signal == -1:
                continue
            else:
                flag = false
            var
                (frm, signal_state) = nodes[i].frm
                after_signal = nodes[i].change_signal
                blues: seq[int]
                ail: int
            if signal_state == -1:
                blues = last_colorchange_signal
            else:
                blues = a_index[signal_state]
            while blues.len() < input.LB:
                blues.add(-1)
            if output.A[after_signal] == g:
                ail = max(0, after_signal-input.LB+1)
            else:
                ail = after_signal

            for ai in ail..<min(ail+input.LB, input.LA):
                for bi in 0..<input.LB:
                    for l in 1..min(input.LB-bi, input.LA-ai):
                        if g notin output.A[ai..<ai+l] or (l, ai, bi) in added:
                            continue
                        var nblues = blues
                        nblues[bi..<bi+l] = output.A[ai..<ai+l]
                        added.incl((l, ai, bi))
                        var ret = evalueate(frm, g, next_g, nblues)
                        if ret != INF64:
                            evaluation[(frm, signal_state, l, ai, bi)] = ret
        if not flag:
            for state, ev in evaluation.pairs:
                if best_score > ev:
                    best_action = state
                    best_score = ev
            var (frm, signal_state, l, ai, bi) = best_action
            if signal_state == -1:
                result = last_colorchange_signal
            else:
                result = a_index[signal_state]
            while result.len() < input.LB:
                result.add(-1)
            result[bi..<bi+l] = output.A[ai..<ai+l]
            now = visited[frm][visited[frm].index(signal_state)][1]
            var visited = initTable[int, int](result.len())
            var deq = newSeqOfCap[int](result.len())
            deq.add(frm)
            visited[frm] = -1
            while deq.len() > 0:
                var v = deq.pop()
                for next in input.G[v]:
                    if next in result and next notin visited:
                        visited[next] = v
                        deq.add(next)
            var now = g
            while visited[now] != -1:
                actions.add(("m", now, -1, -1))
                now = visited[now]
            actions.add(("s", l, ai, bi))
    #特殊な形状でないなら
    if flag:
        for (signal_state, node1) in visited[g].s:
            if node1.times < now.times:
                now = node1

    while now.frm[0] != -1:
        actions.add(("m", now.v_index, -1, -1))
        if now.change_signal != -1:
            if flag:
                result = a_index[now.change_signal]
                while result.len() < input.LB:
                    result.add(-1)
                flag = false
            actions.add(("s", min(input.LB, input.LA-now.change_signal),
                    now.change_signal, 0))
        var index = visited[now.frm[0]].index(now.frm[1])
        now = visited[now.frm[0]][index][1]
    actions.reverse()
    for i in actions:
        output.actions.add(i)
    return result

proc normal_make_actions(input: Input, output: var Output, time: Time,
        index_list: array[N, seq[int]]) =
    var color_change_signal = -1
    var last_colorchange_signal = newSeq[int](input.LB)
    last_colorchange_signal.fill(-1)
    for i in 0..<T:
        var
            s = input.TS[i]
            g = input.TS[i+1]
            next_g = -1
        if i+2 < input.TS.len():
            next_g = input.TS[i+2]
        last_colorchange_signal = normal_dijkstra(input, output, index_list, s,
                g, next_g, last_colorchange_signal, time)
        echo "#", (i, last_colorchange_signal)

proc fast_dijkstra(input: Input, output: var Output, index_list: array[N, seq[
        int]], s, g, last_colorchange_signal: int) =

    var blues: seq[int]
    if last_colorchange_signal != -1:
        blues = a_index[last_colorchange_signal]
    # 現在地とbluesから到達可能な点を列挙
    var
        cand = newSeqOfCap[int](input.LB)
        deq = newSeqOfCap[int](input.LB)
        frm = initTable[int, int](0)
    cand.add(s)
    deq.add(s)
    frm[s] = -1
    while deq.len() > 0:
        var v = deq.pop()
        for next in input.G[v]:
            if next in blues and next notin cand:
                frm[next] = v
                cand.add(next)
                deq.add(next)
    var
        #ベストな解、スタート、ゴール時点での信号の状態
        best_action: (int, int)
        best_score = INF64
    for s in cand:
        for (signal_state, node1) in need_signal_change_times[s][g].s:
            if node1.times < best_score:
                best_score = node1.times
                best_action = (s, signal_state)

    var
        actions = newSeqOfCap[(string, int, int, int)](100)
        index = need_signal_change_times[best_action[0]][g].index(best_action[1])
        now = need_signal_change_times[best_action[0]][g][index][1]

    while now.frm[0] != -1:
        actions.add(("m", int(now.v_index), -1, -1))
        if now.change_signal != -1:
            actions.add(("s", min(input.LB, input.LA-now.change_signal),
                    int(now.change_signal), 0))
        var index = need_signal_change_times[best_action[0]][now.frm[0]].index(
                now.frm[1])
        now = need_signal_change_times[best_action[0]][now.frm[0]][index][1]

    #初期の信号状態からsまでの経路を追加
    var v = best_action[0]
    while frm[v] != -1:
        actions.add(("m", v, -1, -1))
        v = frm[v]
    actions.reverse()
    for i in actions:
        output.actions.add(i)


proc fast_make_actions(input: Input, output: var Output, index_list: array[N,
        seq[int]]) =
    var color_change_signal = -1
    for i in 0..<T:
        var
            s = input.TS[i]
            g = input.TS[i+1]
        fast_dijkstra(input, output, index_list, s, g, color_change_signal)
        for j in 1..output.actions.len():
            if output.actions[^j][0] == "s":
                color_change_signal = output.actions[^j][2]
                break

proc deb(input: Input, output: var Output) =
    for i in 0..<input.LA-input.LB+1:
        output.actions.add(("s", input.LB, i, 0))


proc make_need_signal_change_times(input: Input, output: Output,
                                    index_list: array[N, seq[int]]) =

    proc dijkstra(input: Input, output: Output,
                index_list: array[N, seq[int]], s: int): array[N, HashMap] =
        # i番目の頂点に、信号がjの状態で、到達する場合のnode
        var
            visited: array[N, HashMap]
            min_times: array[N, int]
            deq = initDeque[Node2]()
        visited.fill(new_hashmap())
        min_times.fill(INF64)
        visited[s].add(-1, new_node1(s, 0, -1, (-1, -1)))
        deq.addLast(new_node2(0, s, -1))
        while deq.len() > 0:
            var node2 = deq.popFirst()
            var tmp =
                visited[node2.v_index][visited[node2.v_index].index(
                        node2.signal_state)][1]
            if node2.times > tmp.times:
                continue
            var blues: seq[int]
            if node2.signal_state != -1:
                blues = a_index[node2.signal_state]

            for next in input.G[node2.v_index]:
                if next in blues:
                    var index = visited[next].index(node2.signal_state)
                    if index == -1 or (node2.times < visited[next][
                                index][1].times and
                        node2.times <= min_times[next]):
                        deq.addFirst(new_node2(node2.times, next,
                                node2.signal_state))
                        visited[next][index] =
                            (node2.signal_state, new_node1(next, int(
                                    node2.times), -1, (int(node2.v_index), int(
                                            node2.signal_state))))
                        if node2.times < min_times[next]:
                            min_times[next] = node2.times
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
                            var blues = a_index[index]
                            var tmp = visited[next].index(index)
                            if tmp == -1 or
                                (node2.times+1 < visited[next][tmp][1].times and
                                node2.times+1 <= min_times[next]):
                                deq.addLast(new_node2(node2.times+1, next, index))
                                visited[next][tmp] = (index, new_node1(next, node2.times+1, index, (
                                            node2.v_index, node2.signal_state)))
                            if node2.times < min_times[next]:
                                min_times[next] = node2.times + 1
        return visited

    for i in 0..<N:
        if can_go[i]:
            need_signal_change_times[i] = dijkstra(input, output, index_list, i)


            # -----------------------------------------------------------------------


type Solver = object

proc new_solver(): Solver =
    return Solver()

proc solve(self: Solver, input: var Input, output: var Output, time: Time) =
    for i in 0..<N:
        roots[i] = bfss(input, i)
    make_A(input, output, time)
    var index_list = make_index_list(input, output)
    make_a_index(input, output)
    if true:
        make_need_signal_change_times(input, output, index_list)
        fast_make_actions(input, output, index_list)
    else:
        normal_make_actions(input, output, time, index_list)

    # deb(input, output)
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
    # time.out_paased_time()
    stderr.writeLine(time.get_passed_time(), " ", input.M, " ", input.LA, " ", input.LB)
main()
