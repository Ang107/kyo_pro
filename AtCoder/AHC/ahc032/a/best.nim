# 差分更新のビームサーチ
# 参考: https://eijirou-kyopro.hatenablog.com/entry/2024/02/01/115639
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
    N = 9
    M = 20
    K = 81
    comb_num = [1, 20, 210, 1540, 8855, 42504, 177100, 657800]
    MOD = 998244353

# -----------------------------------------------------------------------

# 入力を管理するオブジェクト
type Input = object
    bord: array[9, array[9, int]]
    stamps: array[M, array[3, array[3, int]]]


proc input(self: var Input) =
    discard lii(3)
    for i in 0..<N:
        var tmp = lii(N)
        for j in 0..<N:
            self.bord[i][j] = tmp[j]
    for i in 0..<M:
        for j in 0..<3:
            var tmp = lii(3)
            for k in 0..<3:
                self.stamps[i][j][k] = tmp[k]



# -----------------------------------------------------------------------

# 出力を管理するオブジェクト
type Output = object
    used_stamps: seq[(int, int, int)]

proc output(self: Output) =
    stdout.writeLine(self.used_stamps.len())
    for (i, j, k) in self.used_stamps:
        stdout.writeLine([i, j, k].join(" "))

# -----------------------------------------------------------------------

# ビームサーチの設定
type Config = object
    max_turn: int
    beam_width: int
    tour_capacity: int
    hashmap_capacity: int

proc new_config(max_turn, beam_width, tour_capacity,
        hashmap_capacity: int): Config =
    return Config(max_turn: max_turn, beam_width: beam_width,
            tour_capacity: tour_capacity, hashmap_capacity: hashmap_capacity)

# -----------------------------------------------------------------------

# 型のエイリアス
type
    Cost = int
    Hash = uint64
    HashMap = Table

# -----------------------------------------------------------------------

# 状態遷移を行うために必要な情報を持つオブジェクト
# メモリ使用量をできるだけ小さくしてください
type
    Action = object
        stamp_num: int
        index: int
        p: int
        q: int

    # コンストラクタ
proc new_action(stamp_num, index, p, q: int): Action =
    return Action(stamp_num: stamp_num, index: index, p: p, q: q)

proc `==`(self, other: Action): bool =
    #TODO
    discard

# -----------------------------------------------------------------------

# 状態のコストを評価するためのオブジェクト
# メモリ使用量をできるだけ小さくしてください
type
    Evaluator = object
        # 確定したコスト
        cost: int

    # コンストラクタ
proc new_evaluator(cost: int): Evaluator =
    return Evaluator(cost: cost)

# 低いほど良い
proc evaluate(self: Evaluator): Cost =
    return self.cost


# -----------------------------------------------------------------------

# 展開するノードの候補を表すオブジェクト
type Candidate = object
    action: Action
    evaluator: Evaluator
    hash: Hash
    parent: int

# コンストラクタ
proc new_candidate(action: Action, evaluator: Evaluator, hash: Hash,
        parent: int): Candidate =
    return Candidate(action: action, evaluator: evaluator, hash: hash,
            parent: parent)

# -----------------------------------------------------------------------

proc op(a, b: (Cost, int)): (Cost, int) =
    if a[0] >= b[0]:
        return a
    else:
        return b
# ノードの候補から実際に追加するものを選ぶクラス
# ビーム幅の個数だけ、評価がよいものを選ぶ
# ハッシュ値が一致したものについては、評価がよいほうのみを残す
type
    MaxSegTree = SegTreeType[(Cost, int)](op, () => (-INF64, -1))
    Selector = object
        beam_width: int
        candidates: seq[Candidate]
        hash_to_idx: HashMap[Hash, int]
        full: bool
        costs: seq[(int, int)]
        st: MaxSegTree
        finished_candidates: seq[Candidate]

# コンストラクタ
proc new_selector(config: Config): Selector =
    var
        beam_width = config.beam_width
        candidates = newSeqOfCap[Candidate](beam_width)
        hash_to_idx = initTable[Hash, int](config.hashmap_capacity)
        full = false
        costs = newSeq[(int, int)](beam_width)
        finished_candidates = newSeqOfCap[Candidate](config.beam_width)
    for i in 0..<beam_width:
        costs[i] = (0, i)
    return Selector(beam_width: beam_width, candidates: candidates,
            hash_to_idx: hash_to_idx, full: full, costs: costs,

finished_candidates: finished_candidates)

# 候補を追加する
# ターン数最小化型の問題で、candidateによって実行可能解が得られる場合にのみ finished = true とする
# ビーム幅分の候補をCandidateを追加したときにsegment treeを構築する
proc push(self: var Selector, candidate: Candidate, finished: bool) =
    if finished:
        self.finished_candidates.add(candidate)
        return

    var cost = candidate.evaluator.evaluate()
    if self.full and cost >= self.st.all_prod()[0]:
        # 保持しているどの候補よりもコストが小さくないとき
        return

    if candidate.hash in self.hash_to_idx:
        # ハッシュ値が等しいものが存在しているとき
        var j = self.hash_to_idx[candidate.hash]
        if candidate.hash == self.candidates[j].hash:
            if self.full:
                # segment treeが構築されている場合
                if cost < self.st.get(j)[0]:
                    self.candidates[j] = candidate
                    self.st.set(j, (cost, j))
            else:
                # segment treeが構築されていない場合
                if cost < self.costs[j][0]:
                    self.candidates[j] = candidate
                    self.costs[j][0] = cost
            return
    if self.full:
        # segment treeが構築されている場合
        var j = self.st.all_prod()[1]
        self.hash_to_idx[candidate.hash] = j
        self.candidates[j] = candidate
        self.st.set(j, (cost, j))
    else:
        # segment treeが構築されていない場合
        var j = self.candidates.len()
        self.hash_to_idx[candidate.hash] = j
        self.candidates.add(candidate)
        self.costs[j][0] = cost
        if self.candidates.len() == self.beam_width:
            # 保持している候補がビーム幅分になったときにsegment treeを構築する
            self.full = true
            self.st = MaxSegTree.init(self.costs)

# 選んだ候補を返す
proc select(self: Selector): seq[Candidate] =
    return self.candidates

# 実行可能解が見つかったか
proc have_finished(self: Selector): bool =
    return self.finished_candidates.len() > 0

# 実行可能解に到達するCandidateを返す
proc get_finished_candidates(self: Selector): seq[Candidate] =
    return self.finished_candidates

# 最もよいCandidateを返す
proc caluculate_best_candidate(self: Selector): Candidate =
    if self.full:
        var best = 0
        for i in 0..<self.beam_width:
            if self.st.get(i)[0] < self.st.get(best)[0]:
                best = i
        return self.candidates[best]
    else:
        var best = 0
        for i in 0..<self.beam_width:
            if self.costs[i][0] < self.costs[best][0]:
                best = i
        return self.candidates[best]

proc clear(self: var Selector) =
    self.candidates.setLen(0)
    self.hash_to_idx.clear()
    self.full = false

# -----------------------------------------------------------------------

# 深さ優先探索に沿って更新する情報をまとめたオブジェクト
type State = object
    bord: array[9, array[9, int]]
    used_num: int
    now_turn: int
    limit: array[49, int]
    stamps_comb_sum: array[8, seq[array[3, array[3, int]]]]
    stamps_comb_index: array[8, seq[seq[int]]]
    pq: array[49, (int, int)]

proc dfs(depth, size, min, max: int, stamps: array[M, array[3, array[3, int]]],
        stamps_comb_sum: var array[8, seq[array[3, array[3, int]]]],
        stamps_comb_index: var array[8, seq[seq[int]]], comb: var seq[int]) =
    if depth == size:
        var tmp: array[3, array[3, int]]
        for i in comb:
            for j in 0..<3:
                for k in 0..<3:
                    tmp[j][k] = (tmp[j][k] + stamps[i][j][k]) % MOD
        stamps_comb_sum[size].add(tmp)
        stamps_comb_index[size].add(comb & @[stamps_comb_index[size].len()])
    else:
        for i in min..max:
            comb[depth] = i
            dfs(depth+1, size, i, max, stamps, stamps_comb_sum,
                    stamps_comb_index, comb)

proc calc_stamps_comb(stamps_comb_sum: var array[8, seq[array[3, array[3,
        int]]]], stamps_comb_index: var array[8, seq[seq[int]]], input: Input) =
    for i in 0..<8:
        stamps_comb_sum[i] = newSeqOfCap[array[3, array[3, int]]](comb_num[i])
    var comb: seq[int]

    for i in 0..<7:
        comb = newSeq[int](i)
        dfs(0, i, 0, 19, input.stamps, stamps_comb_sum, stamps_comb_index, comb)
        let localCopy = stamps_comb_sum[i]
        stamps_comb_index[i].sort(proc (a, b: seq[int]): int = cmp(
        localCopy[a[^1]][0][0],
        localCopy[b[^1]][0][0]))
        stamps_comb_sum[i].sort(proc (a, b: array[3, array[3, int]]): int = cmp(
        a[0][0],
        b[0][0]))

# コンストラクタ 初期状態の作成
proc new_state(input: Input): State =
    var
        bord = input.bord
        used_num = 0
        now_turn = 0
        limit: array[49, int]
        stamps_comb_sum: array[8, seq[array[3, array[3, int]]]]
        stamps_comb_index: array[8, seq[seq[int]]]
        pq: array[49, (int, int)]
    # pq = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),
    #     (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),
    #     (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),
    #     (2,1),(3,1),(4,1),(5,1),(6,1),
    #     (2,2),(2,3),(2,4),(2,5),(2,6),
    #     (3,2),(4,2),(5,2),(6,2)
    #     (3,3),(3,4),(3,5),(3,6),
    #     (4,3),(5,3),(6,3),
    #     (4,4),(4,5),(4,6),
    #     (5,4),(6,4),
    #     (5,5),(5,6),
    #     (6,5),
    #     (6,6)]
    var tmp = 0
    for i in 0..<6:
        for j in 0..<6:
            pq[tmp] = (i, j)
            tmp += 1
    for i in 0..<6:
        pq[tmp] = (i, 6)
        tmp += 1
    for i in 0..<6:
        pq[tmp] = (6, i)
        tmp += 1
    pq[tmp] = (6, 6)

    calc_stamps_comb(stamps_comb_sum, stamps_comb_index, input)
    for i in 0..<36:
        limit[i] = 1 + 5 + i
    for i in 36..<48:
        limit[i] = 36 + 3 + (i - 36) * 3 + 5
    limit[48] = 81

    return State(bord: bord, used_num: used_num, now_turn: now_turn,
            limit: limit, stamps_comb_sum: stamps_comb_sum,
            stamps_comb_index: stamps_comb_index, pq: pq)



# EvaluatorとHashの初期値を返す
proc make_initial_node(self: State): (Evaluator, Hash) =
    return (new_evaluator(0), 0)

# 次の状態候補を全てselectorに追加する
# 引数
#   evaluator : 今の評価器
#   hash      : 今のハッシュ値
#   parent    : 今のノードID（次のノードにとって親となる）
# 速度にかなり寄与する部分なので大事
proc expand(self: State, evaluator: Evaluator, hash: Hash, parent: int,
        selector: var Selector){.inline.} =
    var
        lim = self.limit[self.now_turn] - self.used_num
        (p, q) = self.pq[self.now_turn]
    if p < 6 and q < 6:
        lim = min(lim, 3)
    elif p >= 6 and q >= 6:
        lim = min(lim, 6)
    else:
        lim = min(lim, 6)
    for i in 0..lim:
        var tmp = self.stamps_comb_sum[i].lowerBound(800000000-self.bord[p][q],
                proc (a: array[3, array[3, int]], b: int): int = cmp(a[0][0], b))
        for j in tmp..<self.stamps_comb_index[i].len():
            var
                cost = evaluator.cost
                hash: Hash

            if p < 6 and q < 6:
                var
                    tmp = (self.bord[p][q] + self.stamps_comb_sum[i][j][0][0])
                    tmp_mod = tmp % MOD
                if tmp_mod <= 900000000:
                    continue
                elif tmp > MOD:
                    break
                hash = uint64(tmp_MOD)
                cost -= tmp_MOD
            elif p >= 6 and q >= 6:
                if (self.bord[p][q] + self.stamps_comb_sum[i][j][0][0]) >
                        MOD and self.bord[p][q] < 800000000:
                    break
                var tmp = 0
                for k in 0..<3:
                    for l in 0..<3:
                        tmp += (self.bord[p+k][q+l] +
                        self.stamps_comb_sum[i][j][k][l]) % MOD
                if tmp <= 900000000 * 9:
                    continue
                hash = uint64(tmp)
                cost -= tmp
            elif p < 6:
                if (self.bord[p][q] + self.stamps_comb_sum[i][j][0][0]) >
                        MOD and self.bord[p][q] < 800000000:
                    break
                var tmp = 0
                for l in 0..<3:
                    tmp += (self.bord[p][q+l] +
                    self.stamps_comb_sum[i][j][0][l]) % MOD
                if tmp <= 900000000 * 3:
                    continue
                hash = uint64(tmp)
                cost -= tmp
            elif q < 6:
                if (self.bord[p][q] + self.stamps_comb_sum[i][j][0][0]) >
                        MOD and self.bord[p][q] < 800000000:
                    break
                var tmp = 0
                for k in 0..<3:
                    tmp += (self.bord[p+k][q] +
                    self.stamps_comb_sum[i][j][k][0]) % MOD
                if tmp <= 900000000 * 3:
                    continue
                hash = uint64(tmp)
                cost -= tmp

            selector.push(new_candidate(new_action(i, j, p, q),
            new_evaluator(cost), hash, parent), false)





# actionを実行して次の状態に遷移する
proc move_forward(self: var State, action: Action) =
    var
        p = action.p
        q = action.q
        stamp_num = action.stamp_num
        index = action.index
    self.now_turn += 1
    self.used_num += stamp_num
    for i in 0..<3:
        for j in 0..<3:
            self.bord[p+i][q+j] = (self.bord[p+i][q+j] +
            self.stamps_comb_sum[stamp_num][index][i][j]) % MOD

# actionを実行する前の状態に遷移する
# 今の状態は、親からactionを実行して遷移した状態である
proc move_backward(self: var State, action: Action) =
    var
        p = action.p
        q = action.q
        stamp_num = action.stamp_num
        index = action.index
    self.now_turn -= 1
    self.used_num -= stamp_num
    for i in 0..<3:
        for j in 0..<3:
            self.bord[p+i][q+j] = (self.bord[p+i][q+j] -
            self.stamps_comb_sum[stamp_num][index][i][j]) % MOD

# -----------------------------------------------------------------------

type Tree = object
    state: State
    curr_tour: seq[(int, Action)]
    next_tour: seq[(int, Action)]
    leaves: seq[(Evaluator, Hash)]
    buckets: seq[seq[(Action, Evaluator, Hash)]]
    direct_road: seq[Action]

# コンストラクタ
proc new_tree(state: State, config: Config): Tree =
    var
        state = state
        curr_tour = newSeqOfCap[(int, Action)](config.tour_capacity)
        next_tour = newSeqOfCap[(int, Action)](config.tour_capacity)
        leaves = newSeqOfCap[(Evaluator, Hash)](config.beam_width)
        buckets = newSeq[seq[(Action, Evaluator, Hash)]](config.beam_width)
    return Tree(state: state, curr_tour: curr_tour, next_tour: next_tour,
            leaves: leaves, buckets: buckets)

# 状態を更新しながら深さ優先探索を行い、次のノードの候補を全てselectorに追加する
proc dfs(self: var Tree, selector: var Selector) =
    if self.curr_tour.len() == 0:
        # 最初のターン
        var (evaluator, hash) = self.state.make_initial_node()
        self.state.expand(evaluator, hash, 0, selector)
        return

    for (leaf_index, action) in self.curr_tour:
        if leaf_index >= 0:
            # 葉
            self.state.move_forward(action)
            var (evaluator, hash) = self.leaves[leaf_index]
            self.state.expand(evaluator, hash, leaf_index, selector)
            self.state.move_backward(action)
        elif leaf_index == -1:
            # 前進辺
            self.state.move_forward(action)
        else:
            # 後退辺
            self.state.move_backward(action)

proc update(self: var Tree, candidates: seq[Candidate]) =
    self.leaves.setLen(0)
    if self.curr_tour.len() == 0:
        # 最初のターン
        for candidate in candidates:
            self.curr_tour.add((self.leaves.len(), candidate.action))
            self.leaves.add((candidate.evaluator, candidate.hash))
        return

    for candidate in candidates:
        self.buckets[candidate.parent].add((candidate.action,
                candidate.evaluator, candidate.hash))

    # 一本道を反復しないようにする
    var it = 0
    while self.curr_tour[it][0] == -1 and self.curr_tour[it][1] ==
            self.curr_tour[^1][1]:
        var action = self.curr_tour[it][1]
        it += 1
        self.state.move_forward(action)
        self.direct_road.add(action)
        discard self.curr_tour.pop()

    # 葉の追加や不要な辺の削除をする
    for i in it..<self.curr_tour.len():
        var (leaf_index, action) = self.curr_tour[i]
        if leaf_index >= 0:
            # 葉
            if self.buckets[leaf_index].len() == 0:
                continue
            self.next_tour.add((-1, action))
            for (new_action, evaluator, hash) in self.buckets[leaf_index]:
                var new_leaf_index = self.leaves.len()
                self.next_tour.add((new_leaf_index, new_action))
                self.leaves.add((evaluator, hash))
            self.buckets[leaf_index].setLen(0)
            self.next_tour.add((-2, action))

        elif leaf_index == -1:
            # 前進辺
            self.next_tour.add((-1, action))

        else:
            # 後退辺
            var (old_leaf_index, old_action) = self.next_tour[^1]
            if old_leaf_index == -1:
                discard self.next_tour.pop()
            else:
                self.next_tour.add((-2, action))
    swap(self.curr_tour, self.next_tour)
    self.next_tour.setLen(0)

# 根からのパスを取得する
proc calculate_path(self: Tree, parent: int, turn: int): seq[Action] =
    var ret = self.direct_road
    for (leaf_index, action) in self.curr_tour:
        if leaf_index >= 0:
            if leaf_index == parent:
                ret.add(action)
                return ret
        elif leaf_index == -1:
            ret.add(action)
        else:
            discard ret.pop()

# -----------------------------------------------------------------------

# ビームサーチを行う関数
proc beam_search(config: Config, state: State): seq[Action] =
    var
        tree = new_tree(state, config)
        selector = new_selector(config)
    for turn in 0..<config.max_turn:
        # Euler Tourでselectorに候補を追加する
        tree.dfs(selector)
        if selector.have_finished():
            # ターン数最小化型の問題で実行可能解が見つかったとき
            var
                candidate = selector.get_finished_candidates()[0]
                ret = tree.calculate_path(candidate.parent, turn+1)
            ret.add(candidate.action)
            return ret

        if turn == config.max_turn-1:
            # ターン数固定の問題で全ターンが終了したとき
            var
                best_candidate = selector.caluculate_best_candidate()
                ret = tree.calculate_path(best_candidate.parent, turn+1)
            ret.add(best_candidate.action)
            return ret

        # 木を更新する。
        tree.update(selector.select())
        selector.clear()
# -----------------------------------------------------------------------

# 倍率は問題に合わせて調整
const
    # TODO
    max_turn = 49
    beam_width = 4500
    tour_capacity = 5 * beam_width
    hashmap_capacity = 15 * beam_width

# -----------------------------------------------------------------------

type Solver = object
    input: Input

proc new_solver(input: Input): Solver =
    return Solver(input: input)

proc solve(self: var Solver, output: var Output) =
    var
        config = new_config(max_turn, beam_width, tour_capacity, hashmap_capacity)
        state = new_state(self.input)
        actions = beam_search(config, state)
    output.used_stamps = newSeqOfCap[(int, int, int)](81)
    for action in actions:
        for i in 0..<state.stamps_comb_index[action.stamp_num][
                action.index].len()-1:
            output.used_stamps.add(
                (state.stamps_comb_index[action.stamp_num][action.index][i],
                        action.p, action.q))



# -----------------------------------------------------------------------

proc main() =
    var
        START = cpuTime()
        input = Input()
        output = Output()
    input.input()
    var solver = new_solver(input)
    solver.solve(output)
    output.output()
    stderr.writeLine($(cpuTime() - START))
main()
