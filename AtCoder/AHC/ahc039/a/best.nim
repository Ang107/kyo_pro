# AHC用のテンプレート
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
proc chmin(x: var int, y: int) {.inline.} =
    if x > y:
        x = y

proc chmax(x: var int, y: int) {.inline.} =
    if x < y:
        x = y

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
    TIME_LIMIT = 1.95
    N = 5000
    UDLR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # TODO


# 二次元セグツリーっぽいやつ
type RangeTreeNode = ref object
    x_list: seq[int]
    y_list: seq[int]
    left: RangeTreeNode
    right: RangeTreeNode

proc new_RangeTreeNode(x_list, y_list: seq[int]): RangeTreeNode =
    return RangeTreeNode(x_list: x_list, y_list: y_list)

proc build_range_tree(points: seq[(int, int)]): RangeTreeNode =
    if points.len() == 0:
        return nil
    var points = points
    points.sort(proc (x, y: (int, int)): int = cmp(x[0], y[0]))
    var
        x_list = newSeq[int](len(points))
        y_list = newSeq[int](len(points))
    for i, (x, y) in points:
        x_list[i] = x
        y_list[i] = y
    y_list.sort()
    var node = new_RangeTreeNode(x_list, y_list)
    if len(points) > 1:
        var mid = len(points) div 2
        node.left = build_range_tree(points[0..<mid])
        node.right = build_range_tree(points[mid ..< points.len()])
    return node

proc query(self: RangeTreeNode, x_min, y_min, x_max, y_max: int): int =
    if isNil(self):
        return 0
    if self.x_list[^1] < x_min or self.x_list[0] > x_max:
        return 0
    if x_min <= self.x_list[0] and self.x_list[^1] <= x_max:
        var
            left = self.y_list.lowerBound(y_min)
            right = self.y_list.upperBound(y_max)
        return right - left
    return query(self.left, x_min, y_min, x_max, y_max) +
            query(self.right, x_min, y_min, x_max, y_max)

proc coord_comp(points: seq[(int, int)]): (seq[(int, int)], seq[int], seq[int]) =
    var
        x_values = newSeq[int](points.len())
        y_values = newSeq[int](points.len())
    for i, (x, y) in points:
        x_values[i] = x
        y_values[i] = y
    x_values.sort()
    x_values = x_values.deduplicate(true)
    y_values.sort()
    y_values = y_values.deduplicate(true)
    var x_dict = initTable[int, int](points.len())
    var y_dict = initTable[int, int](points.len())
    for i, x in x_values:
        x_dict[x] = i
    for i, y in y_values:
        y_dict[y] = i
    var comp_points = newSeq[(int, int)](points.len())
    for i, (x, y) in points:
        comp_points[i] = (x_dict[x], y_dict[y])
    return (comp_points, x_values, y_values)





# -----------------------------------------------------------------------

    # 入力を管理するオブジェクト
type Input = object
    sa: seq[(int, int)]
    iw: seq[(int, int)]

    # TODO

proc input(self: var Input) =
    var
        n = ii()
        sa = newSeq[(int, int)](n)
        iw = newSeq[(int, int)](n)
        fi = newSeqOfCap[(int, int)](n*2)
    for i in 0..<n:
        sa[i][0] = ii()
        sa[i][1] = ii()
        fi.add(sa[i])
    for i in 0..<n:
        iw[i][0] = ii()
        iw[i][1] = ii()
        fi.add(iw[i])

    self.sa = sa
    self.iw = iw
# -----------------------------------------------------------------------

# zobrist hash
var zobrist_hash: seq[seq[uint64]]


proc make_zobrist_hash(input: Input, split_num: int) =
    zobrist_hash = newSeqWith(split_num, newseq[uint64](split_num))
    for i in 0..<split_num:
        for j in 0..<split_num:
            zobrist_hash[i][j] = rand(uint64)
# -----------------------------------------------------------------------

# 出力を管理するオブジェクト
type Output = object
    # TODO

proc output(self: Output) =
    # TODO
    discard

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
        v: int

    # コンストラクタ
proc new_action(v: int): Action {.inline.} =
    # TODO
    return Action(v: v)

proc `==`(self, other: Action): bool =
    #TODO
    discard

# -----------------------------------------------------------------------

# 状態のコストを評価するためのオブジェクト
# メモリ使用量をできるだけ小さくしてください
type
    Evaluator = object
        score: int

    # コンストラクタ
proc new_evaluator(score: int): Evaluator {.inline.} =
    # TODO
    return Evaluator(score: score)

# 低いほど良い
proc evaluate(self: Evaluator): Cost =
    return self.score

# -----------------------------------------------------------------------

# 展開するノードの候補を表すオブジェクト
type Candidate = object
    action: Action
    evaluator: Evaluator
    hash: Hash
    parent: int

# コンストラクタ
proc new_candidate(action: Action, evaluator: Evaluator,
                    hash: Hash, parent: int): Candidate {.inline.} =
    return Candidate(action: action, evaluator: evaluator,
                    hash: hash, parent: parent)

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
        costs: seq[(Cost, int)]
        st: MaxSegTree
        finished_candidates: seq[Candidate]

# コンストラクタ
proc new_selector(config: Config): Selector =
    var
        beam_width = config.beam_width
        candidates = newSeqOfCap[Candidate](beam_width)
        hash_to_idx = initTable[Hash, int](config.hashmap_capacity)
        full = false
        costs = newSeq[(Cost, int)](beam_width)
        finished_candidates = newSeqOfCap[Candidate](config.beam_width)
    for i in 0..<beam_width:
        costs[i] = (0, i)
    return Selector(beam_width: beam_width, candidates: candidates,
                    hash_to_idx: hash_to_idx, full: full, costs: costs,
                    finished_candidates: finished_candidates)

# beam幅を変更（減少）させる
proc change_beam_width(self: var Selector, new_beam_width: int) =
    self.beam_width = new_beam_width
    self.costs = newSeq[(Cost, int)](new_beam_width)
    for i in 0..<new_beam_width:
        self.costs[i] = (0, i)

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
    visited: seq[seq[int]]
    main: seq[seq[int]]
    split_num: int
    x: int
    y: int

# コンストラクタ 初期状態の作成
proc new_state(split_num: int, main: seq[seq[int]], x, y: int): State =
    var visited = newSeqWith(split_num, newseq[int](split_num))
    visited[x][y] = 1
    return State(visited: visited, split_num: split_num, main: main, x: x, y: y)

# EvaluatorとHashの初期値を返す
proc make_initial_node(self: State): (Evaluator, Hash) =
    var
        hash: uint64 = 0
        score = 0
    for i in 0..<self.split_num:
        for j in 0..<self.split_num:
            if self.visited[i][j] == 1:
                score -= self.main[i][j]
                hash ^= zobrist_hash[i][j]
    return (new_evaluator(score), hash)

# 次の状態候補を全てselectorに追加する
# 引数
#   evaluator : 今の評価器
#   hash      : 今のハッシュ値
#   parent    : 今のノードID（次のノードにとって親となる）
# 速度にかなり寄与する部分なので大事
proc expand(self: State, evaluator: Evaluator, hash: Hash, parent: int,
            selector: var Selector){.inline.} =
    for action, (i, j) in UDLR:
        var
            score = evaluator.score
            nhash = hash
        if i == 0 and j == 0:
            selector.push(new_candidate(new_action(action), new_evaluator(score), nhash, parent), false)
        else:
            var
                nx = self.x+i
                ny = self.y+j
            if 0 <= nx and nx < self.split_num and
                0 <= ny and ny < self.split_num and self.visited[nx][ny] == 0:
                score -= self.main[nx][ny]
                nhash ^= zobrist_hash[nx][ny]
                selector.push(new_candidate(new_action(action), new_evaluator(score), nhash, parent), false)


# actionを実行して次の状態に遷移する
proc move_forward(self: var State, action: Action) =
    self.x += UDLR[action.v][0]
    self.y += UDLR[action.v][1]
    self.visited[self.x][self.y] = 1

# actionを実行する前の状態に遷移する
# 今の状態は、親からactionを実行して遷移した状態である
proc move_backward(self: var State, action: Action) =
    self.visited[self.x][self.y] = 0
    self.x -= UDLR[action.v][0]
    self.y -= UDLR[action.v][1]


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
proc beam_search(config: Config, state: State, time: Time): seq[Action] =
    var
        tree = new_tree(state, config)
        selector = new_selector(config)
    for turn in 0..<config.max_turn:
        # 時間等に応じて動的にビーム幅の調整
        # selector.change_beam_width()

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
            echo best_candidate
            return ret

        # 木を更新する。
        tree.update(selector.select())
        selector.clear()
# -----------------------------------------------------------------------

# 倍率は問題に合わせて調整
const
    # TODO
    max_turn = 2000
    beam_width = 1000
    tour_capacity = 10 * beam_width
    hashmap_capacity = 2 * beam_width

# -----------------------------------------------------------------------

type Solver = object
    input: Input
    time: Time
type Fish = object
    points: seq[(int, int)]
    comp_points: seq[(int, int)]
    x_values: seq[int]
    y_values: seq[int]
    root: RangeTreeNode

proc new_solver(input: Input, time: Time): Solver =
    return Solver(input: input, time: time)
proc get_comp_coord_min(value_list: seq[int], value: int): int =
    var index = lowerBound(value_list, value)
    return index
proc get_comp_coord_max(value_list: seq[int], value: int): int =
    var index = lowerBound(value_list, value)
    if index < value_list.len() and value_list[index] != value:
        index -= 1
    return index
proc solve(self: var Solver, output: var Output) =
    var
        block_len = 2000
        block_num = 100000 // block_len + 1
        score = newSeqWith(block_num+2, newseq[int](block_num+2))
        b = newSeqWith(block_num+2, newseq[int](block_num+2))
    for (x, y) in self.input.sa:
        score[x//block_len+1][y//block_len+1] += 1
    for (x, y) in self.input.iw:
        score[x//block_len+1][y//block_len+1] -= 1
    var cnt = 0
    var min_x, min_y = INF64
    var max_x, max_y = -INF64
    for i in 1..block_num:
        for j in 1..<block_num:
            if score[i][j] > 0:
                chmin(min_x, i)
                chmin(min_y, j)
                chmax(max_x, i)
                chmax(max_y, j)
    for i in min_x..max_x:
        for j in min_y..max_y:
            b[i][j] = 1
    var around_len = ((max_x - min_x + 1) + (max_y - min_y + 1)) * 2 * block_len
    proc change_ok(x, y: int): int =
        #削除
        if b[x][y] == 1:
            var tmp = 0
            for (i, j) in UDLR:
                if b[x+i][y+j] == 1:
                    tmp += 1
            if tmp == 0 or tmp == 4:
                return -1
            elif tmp == 1:
                return tmp
            elif tmp == 3:
                if b[x-1][y] == 1 and b[x+1][y] == 1:
                    if (b[x-1][y-1] == 1 and b[x][y-1] == 1 and b[x+1][y-1] == 1) or
                        (b[x-1][y+1] == 1 and b[x][y+1] == 1 and b[x+1][y+1] == 1):
                        return tmp
                    else:
                        return -1
                else:
                    if (b[x-1][y-1] == 1 and b[x-1][y] == 1 and b[x-1][y+1] == 1) or
                        (b[x+1][y-1] == 1 and b[x+1][y] == 1 and b[x+1][y+1] == 1):
                        return tmp
                    else:
                        return -1

            elif tmp == 2:
                if b[x-1][y] == b[x+1][y]:
                    return -1
                else:
                    if b[x-1][y] == 1 and b[x][y-1] == 1 and b[x-1][y-1] == 1:
                        return tmp
                    elif b[x-1][y] == 1 and b[x][y+1] == 1 and b[x-1][y+1] == 1:
                        return tmp
                    elif b[x+1][y] == 1 and b[x][y-1] == 1 and b[x+1][y-1] == 1:
                        return tmp
                    elif b[x+1][y] == 1 and b[x][y+1] == 1 and b[x+1][y+1] == 1:
                        return tmp
                    return -1
        # 追加
        else:
            var tmp = 0
            for (i, j) in UDLR:
                if b[x+i][y+j] == 0:
                    tmp += 1
            if tmp == 0 or tmp == 4:
                return -1
            elif tmp == 1:
                return 4 - tmp
            elif tmp == 3:
                if b[x-1][y] == 0 and b[x+1][y] == 0:
                    if (b[x-1][y-1] == 0 and b[x][y-1] == 0 and b[x+1][y-1] == 0) or
                        (b[x-1][y+1] == 0 and b[x][y+1] == 0 and b[x+1][y+1] == 0):
                        return 4 - tmp
                    else:
                        return -1
                else:
                    if (b[x-1][y-1] == 0 and b[x-1][y] == 0 and b[x-1][y+1] == 0) or
                        (b[x+1][y-1] == 0 and b[x+1][y] == 0 and b[x+1][y+1] == 0):
                        return 4 - tmp
                    else:
                        return -1

            elif tmp == 2:
                if b[x-1][y] == b[x+1][y]:
                    return -1
                else:
                    if b[x-1][y] == 0 and b[x][y-1] == 0 and b[x-1][y-1] == 0:
                        return 4-tmp
                    elif b[x-1][y] == 0 and b[x][y+1] == 0 and b[x-1][y+1] == 0:
                        return 4-tmp
                    elif b[x+1][y] == 0 and b[x][y-1] == 0 and b[x+1][y-1] == 0:
                        return 4-tmp
                    elif b[x+1][y] == 0 and b[x][y+1] == 0 and b[x+1][y+1] == 0:
                        return 4-tmp
                    return -1

    var
        start_temp = 30
        end_temp = 0
        temp: float
    while true:
        if cnt mod 100 == 0:
            var now = self.time.get_passed_time()
            if now > 1.95:
                break
            temp = start_temp + (end_temp - start_temp) * now / TIME_LIMIT
        cnt += 1
        var x = rand(min_x..max_x)
        var y = rand(min_y..max_y)
        var tmp = change_ok(x, y)
        if tmp == -1:
            continue
        var l: int
        if b[x][y] == 1:
            l = 2 * (tmp-2) * block_len
        else:
            l = -2 * (tmp-2) * block_len
        if around_len + l > 400000:
            continue
        if b[x][y] == 1:
            if score[x][y] <= 0:
                b[x][y] = 0
                around_len += l
                # echo tmp
                # for i in b:
                #     echo i
            else:
                # echo (b[x][y], score[x][y], temp, exp(-score[x][y]/temp))
                if (-score[x][y]/temp) > rand(1.0):
                    b[x][y] = 0
                    around_len += l
                    # echo tmp

                    # for i in b:
                    #     echo i
            # echo (l, around_len)
            # for i in b:
            #     echo i

        elif b[x][y] == 0:
            if score[x][y] >= 0:
                b[x][y] = 1
                around_len += l
                # echo tmp

                # for i in b:
                #     echo i
            else:
                # echo (b[x][y], score[x][y], temp, exp(-score[x][y]/temp))
                if exp(score[x][y]/temp) > rand(1.0):
                    b[x][y] = 1
                    around_len += l
                    # echo tmp

                    # for i in b:
                    #     echo i


    var edge = initTable[(int, int), seq[(int, int)]]()
    var sx, sy: int
    var last_score = 0
    for i in 1..block_num:
        for j in 1..<block_num:
            if b[i][j] == 1:
                last_score += score[i][j]
                var
                    x_min = (i-1) * block_len
                    x_max = i * block_len
                    y_min = (j-1) * block_len
                    y_max = j * block_len
                for v, (p, q) in UDLR:
                    if b[i+p][j+q] == 0:
                        if v == 0:
                            sx = x_min
                            sy = y_min
                            if (x_min, y_min) notin edge:
                                edge[(x_min, y_min)] = newSeqOfCap[(int, int)](0)
                            if (x_min, y_max) notin edge:
                                edge[(x_min, y_max)] = newSeqOfCap[(int, int)](0)
                            edge[(x_min, y_min)].add((x_min, y_max))
                            edge[(x_min, y_max)].add((x_min, y_min))
                        elif v == 1:
                            if (x_max, y_min) notin edge:
                                edge[(x_max, y_min)] = newSeqOfCap[(int, int)](0)
                            if (x_max, y_max) notin edge:
                                edge[(x_max, y_max)] = newSeqOfCap[(int, int)](0)
                            edge[(x_max, y_min)].add((x_max, y_max))
                            edge[(x_max, y_max)].add((x_max, y_min))
                        elif v == 2:
                            if (x_min, y_min) notin edge:
                                edge[(x_min, y_min)] = newSeqOfCap[(int, int)](0)
                            if (x_max, y_min) notin edge:
                                edge[(x_max, y_min)] = newSeqOfCap[(int, int)](0)
                            edge[(x_min, y_min)].add((x_max, y_min))
                            edge[(x_max, y_min)].add((x_min, y_min))
                        elif v == 3:
                            if (x_min, y_max) notin edge:
                                edge[(x_min, y_max)] = newSeqOfCap[(int, int)](0)
                            if (x_max, y_max) notin edge:
                                edge[(x_max, y_max)] = newSeqOfCap[(int, int)](0)
                            edge[(x_min, y_max)].add((x_max, y_max))
                            edge[(x_max, y_max)].add((x_min, y_max))

    var vs = newSeqOfCap[(int, int)](len(edge))
    var visited = initHashSet[(int, int)](len(edge))
    vs.add((sx, sy))
    visited.incl((sx, sy))
    var fin = false
    while not fin:
        fin = true
        for (nx, ny) in edge[vs[^1]]:
            if (nx, ny) notin visited:
                visited.incl((nx, ny))
                vs.add((nx, ny))
                fin = false
                break
    stdout.writeLine(len(vs))
    for (x, y) in vs:
        stdout.writeLine(x, " ", y)
    stderr.writeLine(last_score)


    # for i in b:
    #     echo i
    # echo tmp

















#-----------------------------------------------------------------------

proc main() =
    var
        time = new_time(TIME_LIMIT)
        input = Input()
        output = Output()
    input.input()
    var solver = new_solver(input, time)
    solver.solve(output)
    output.output()
    # time.out_paased_time()
main()
