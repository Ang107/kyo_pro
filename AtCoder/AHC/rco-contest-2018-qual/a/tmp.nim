# 差分更新のビームサーチ
# 参考: https://eijirou-kyopro.hatenablog.com/entry/2024/02/01/115639
# 参考: https://atcoder.jp/contests/rco-contest-2018-qual/submissions/50083337
# TODO セグツリーをheapqにして速度がどうなるかを見る。その他高速化に寄与できる部分を探す。

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

# uint64用のbit演算定義
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

# -----------------------------------------------------------------------
const
    TIMELIMIT = 3.9
    N = 100
    K = 8
    H = 50
    W = 50
    T = 2500
    DI = [-W, W, -1, 1]
    UDLR = "UDLR"
type Input = object
    grids: array[N, string]

proc input(self: var Input) =
    discard lii(5)
    for i in 0..<N:
        for j in 0..<H:
            self.grids[i] &= si()

proc evaluate_grid(grid: string): int =
    return 2 * grid.count('x') + grid.count('#')

proc select_grids(input: Input): array[K, int] =
    var costs: array[N, (int, int)]
    for i in 0..<N:
        costs[i] = (evaluate_grid(input.grids[i]), i)
    costs.sort(proc (x, y: (int, int)): int = cmp(x[0], y[0]))
    for i in 0..<K:
        result[i] = costs[i][1]
    return result

# ビームサーチの設定
type Config = object
    max_turn: int
    beam_width: int
    tour_capacity: int

proc new_config(max_turn, beam_width, tour_capacity: int): Config =
    return Config(max_turn: max_turn, beam_width: beam_width, tour_capacity: tour_capacity)


# 型のエイリアス
type
    Cost = int
    Hash = uint64
    HashMap = Table

# -----------------------------------------------------------------------

# 連想配列
# Keyにハッシュ関数を適用しない
# open addressing with linear probing
# unordered_mapよりも速い
# nは格納する要素数よりも16倍ほど大きくする
# type HashMap_faster = ref object

# -----------------------------------------------------------------------

# 状態遷移を行うために必要な情報を持つオブジェクト
# メモリ使用量をできるだけ小さくしてください
type
    Action = uint64
        # TODO
const
    eval_c1 = -2
    eval_c2 = 1
    #     # コンストラクタ
    # proc new_action(): Action =
    #     # TODO
    #     return Action()

    # proc `==`(self, other: Action): bool =
    #     #TODO
    #     discard

# -----------------------------------------------------------------------

# 状態のコストを評価するためのオブジェクト
# メモリ使用量をできるだけ小さくしてください
type
    Evaluator = object
        score: int
        penalty: int

# コンストラクタ
proc new_evaluator(score, penalty: int): Evaluator =
    return Evaluator(score: score, penalty: penalty)

# 低いほど良い
proc evaluate(self: Evaluator): Cost =
    return eval_c1 * self.score + eval_c2 * self.penalty

# -----------------------------------------------------------------------

# 展開するノードの候補を表すオブジェクト
type Candidate = object
    action: Action
    evaluator: Evaluator
    hash: Hash
    parent: int

# コンストラクタ
proc new_candidate(action: Action, evaluator: Evaluator, hash: Hash, parent: int): Candidate =
    return Candidate(action: action, evaluator: evaluator, hash: hash, parent: parent)

# -----------------------------------------------------------------------

proc op(a, b: (int, int)): (int, int) =
    if a[0] >= b[0]:
        return a
    else:
        return b
# ノードの候補から実際に追加するものを選ぶクラス
# ビーム幅の個数だけ、評価がよいものを選ぶ
# ハッシュ値が一致したものについては、評価がよいほうのみを残す
type
    MaxSegTree = SegTreeType[(int, int)](op, () => (-2147483648, -1))
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
        hash_to_idx = initTable[Hash, int](beam_width*2)
        full = false
        costs = newSeq[(int, int)](beam_width)
    for i in 0..<beam_width:
        costs[i] = (0, i)
    return Selector(beam_width: beam_width, candidates: candidates, hash_to_idx: hash_to_idx, full: full, costs: costs)

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
    # if self.full:
    #     var best = 0
    #     for i in 0..<self.beam_width:
    #         if self.st.get(i)[0] < self.st.get(best)[0]:
    #             best = i
    #     return self.candidates[best]
    # else:
    #     var best = 0
    #     for i in 0..<self.beam_width:
    #         if self.costs[i][0] < self.costs[best][0]:
    #             best = i
    #     return self.candidates[best]
    var best = 0
    for i in 0..<self.candidates.len():
        if self.candidates[i].evaluator.score > self.candidates[best].evaluator.score:
            best = i
    return self.candidates[best]

proc clear(self: var Selector) =
    self.candidates.setLen(0)
    self.hash_to_idx.clear()
    self.full = false

# -----------------------------------------------------------------------

# 深さ優先探索に沿って更新する情報をまとめたオブジェクト
type State = object
    m: array[K, int]
    edges: array[K, seq[int]]
    visited: array[K, seq[int]]
    positions: array[K, int]

# コンストラクタ
proc new_state(input: Input): State =
    var
        m = select_grids(input)
        edges: array[K, seq[int]]
        visited: array[K, seq[int]]
        positions: array[K, int]
    for i in 0..<K:
        var grid = input.grids[m[i]]
        positions[i] = grid.find('@')
        visited[i] = newseq[int](H*W)
        visited[i][positions[i]] = 1
        edges[i] = newseqwith(4*H*W, -1)
        for j in 0..<H*W:
            if grid[j] == 'x' or grid[j] == '#':
                continue
            for d in 0..<4:
                if grid[j+DI[d]] == 'x':
                    discard
                elif grid[j+DI[d]] == '#':
                    edges[i][4*j+d] = j
                else:
                    edges[i][4*j+d] = j+DI[d]
    return State(m: m, edges: edges, visited: visited, positions: positions)


# EvaluatorとHashの初期値を返す
proc make_initial_node(self: State): (Evaluator, Hash) =
    return ((new_evaluator(0, 0)), 0)

# 次の状態候補を全てselectorに追加する
# 引数
#   evaluator : 今の評価器
#   hash      : 今のハッシュ値
#   parent    : 今のノードID（次のノードにとって親となる）
# 速度にかなり寄与する部分が大きいので大事
proc expand(self: State, evaluator: Evaluator, hash: Hash, parent: int, selector: var Selector) =
    for d in 0..<4:
        var
            action: Action
            score = evaluator.score
            penalty = 0
            game_over = false

        for i in 0..<K:
            var
                fr = self.positions[i]
                to = self.edges[i][4*fr+d]
            if to == -1:
                game_over = true
                break
            if fr != to:
                action |= uint64(1 << i)
                if self.visited[i][to] == 0:
                    score += 1
            penalty += self.visited[i][to]
        if game_over:
            continue
        action |= uint64((d & 1) << K)
        action |= uint64((d >> 1) << (K+1))

        var
            pos1 = self.positions[0]
            pos2 = self.positions[1]
            pos3 = self.positions[2]
            pos4 = self.positions[3]
            pos5 = self.positions[4]

        if action[0]:
            pos1 += DI[d]
        if action[1]:
            pos2 += DI[d]
        if action[2]:
            pos3 += DI[d]
        if action[3]:
            pos4 += DI[d]
        if action[4]:
            pos5 += DI[d]

        var hash: Hash = uint64((pos5 << 48) | (pos4 << 36) | (pos3 << 24) | (pos2 << 12) | pos1)

        selector.push(new_candidate(action, new_evaluator(score, penalty), hash, parent), false)


# actionを実行して次の状態に遷移する
proc move_forward(self: var State, action: Action) =
    var d = action >> K
    for i in 0..<K:
        if action[i]:
            self.positions[i] += DI[d]
        self.visited[i][self.positions[i]] += 1


# actionを実行する前の状態に遷移する
# 今の状態は、親からactionを実行して遷移した状態である
proc move_backward(self: var State, action: Action) =
    var d = action >> K

    for i in 0..<K:
        self.visited[i][self.positions[i]] -= 1
        if action[i]:
            self.positions[i] -= DI[d]

proc get_m(self: State): array[K, int] =
    return self.m


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
    return Tree(state: state, curr_tour: curr_tour, next_tour: next_tour, leaves: leaves, buckets: buckets)

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
        self.buckets[candidate.parent].add((candidate.action, candidate.evaluator, candidate.hash))

    # 一本道を反復しないようにする
    var it = 0
    while self.curr_tour[it][0] == -1 and self.curr_tour[it][1] == self.curr_tour[^1][1]:
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

# 倍率は問題に合わせて調整
const
    max_turn = T
    beam_width = 2200
    tour_capacity = 16 * beam_width

type Solver = object
    input: Input
    m: array[K, int]
    output: string

proc new_solver(input: Input): Solver =
    return Solver(input: input)

proc solve(self: var Solver) =
    var
        config = new_config(max_turn, beam_width, tour_capacity)
        state = new_state(self.input)
        actions = beam_search(config, state)
    self.m = state.get_m()
    self.output = newStringOfCap(actions.len())
    for i in 0..<actions.len():
        var d = actions[i] >> K
        self.output.add(UDLR[d])

proc print(self: Solver) =
    stdout.writeLine(self.m.join(" "))
    stdout.writeLine(self.output)

proc main() =
    var START = cpuTime()
    var input = Input()
    input.input()
    var solver = new_solver(input)
    solver.solve()
    solver.print()
    stderr.writeLine($(cpuTime() - START))
# main()
var x: uint64
echo (x, x.int.toBin(8))











