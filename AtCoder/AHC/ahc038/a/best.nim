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
    TIME_LIMIT = 3.0
    MOVES_S = ".LRUD"
    MOVES_D = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
var init_levaes_state: string

# -----------------------------------------------------------------------

    # 入力を管理するオブジェクト
type Input = object
    N: int
    M: int
    V: int
    s: seq[string]
    t: seq[string]

proc input(self: var Input) =
    var
        n, m, v = ii()
        s = newSeqOfCap[string](n)
        t = newSeqOfCap[string](n)
    for _ in range(n):
        s.add(si())
    for _ in range(n):
        t.add(si())
    self.N = n
    self.M = m
    self.V = v
    self.s = s
    self.t = t

    init_levaes_state = '.'.repeat(v)




# -----------------------------------------------------------------------

# 出力を管理するオブジェクト
type Output = object
    V: int
    pl: seq[(int, int)]
    x: int
    y: int
    actions: seq[string]

proc output(self: Output) =
    stdout.writeLine(self.V)
    for (p, l) in self.pl:
        stdout.writeLine(p, " ", l)
    stdout.writeLine(self.x, " ", self.y)
    for action in self.actions:
        stdout.writeLine(action)






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
# zobrist hash
# たこやきが存在する場所の集合
var zobrist_hash_s: seq[seq[uint64]]
# 原点の座標のhash
var zobrist_hash_coord: seq[seq[uint64]]

proc make_zobrist_hash(input: Input) =
    var n = input.N
    zobrist_hash_s = newSeqWith(n, newseq[uint64](n))
    zobrist_hash_coord = newSeqWith(n, newseq[uint64](n))
    for i in 0..<n:
        for j in 0..<n:
            zobrist_hash_s[i][j] = rand(uint64)
            zobrist_hash_coord[i][j] = rand(uint64)





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
        move: int
        rotate: array[2, int]
        catch: uint64



    # コンストラクタ
proc new_action(move: int, rotate: array[2, int], catch: uint64): Action {.inline.} =
    return Action(move: move, rotate: rotate, catch: catch)

# proc `==`(self, other: Action): bool =
#     #TODO
#     discard

# -----------------------------------------------------------------------

# 状態のコストを評価するためのオブジェクト
# メモリ使用量をできるだけ小さくしてください
type
    Evaluator = object
        put: int
        caught: int


    # コンストラクタ
proc new_evaluator(put, caught: int): Evaluator {.inline.} =
    # TODO
    return Evaluator(put: put, caught: caught)

# 低いほど良い
proc evaluate(self: Evaluator): Cost =
    return - (self.put << 1) - self.caught


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
    N: int
    M: int
    V: int
    # 現在のたこやきの状態(置かれているもの)
    s: seq[string]
    t: seq[string]
    # 右向きに回転した回数 (0..3)
    rotate: array[2, int]
    # 根の座標
    root: (int, int)
    edge: (int, int)
    # 葉の状態(掴んでいるか否か)
    leaves_state: uint64
    # 根が原点のときの葉の座標
    leaves_coord: seq[(int, int)]


proc make_tree(input: Input, output: var Output): seq[(int, int)] =
    result = newSeqOfCap[(int, int)](input.V-1)
    output.pl.add((0, input.N div 2))
    var st = input.N div 2
    if input.V-2 < input.N div 2:
        var tmp = input.N / 2 / (input.V-1)
        for i in 0..<input.V-2:
            result.add((0, int((i+1)*tmp)))

        output.V = input.V
        for i in 0..<input.V-2:
            output.pl.add((1, int((i+1)*tmp)))
        return result
    else:
        for i in 0..<input.V-2:
            result.add((0, i+1))

        output.V = input.V
        for i in 0..<input.V-2:
            output.pl.add((1, i+1))
        return result


proc get_root_xy(input: Input, output: var Output): (int, int) =
    var xs = newSeqOfCap[int](input.N*input.N)
    var ys = newSeqOfCap[int](input.N*input.N)
    for i in 0..<input.N:
        for j in 0..<input.N:
            if input.s[i][j] == '1':
                xs.add(i)
                ys.add(j)
            if input.t[i][j] == '1':
                xs.add(i)
                ys.add(j)
    result = (sum(xs) div len(xs), sum(ys) div len(ys))
    output.x = result[0]
    output.y = result[1]
    return result



# コンストラクタ 初期状態の作成
proc new_state(input: Input, leaves_coord: seq[(int, int)], root, edge: (int, int)): State =
    var
        N = input.N
        M = input.M
        V = input.V
        s = input.s
        t = input.t
        rotate = [0, 0]
        root = root
        edge = edge
        leaves_state = 0.uint64
        leaves_coord = leaves_coord

    return State(N: N, M: M, V: V, s: s, t: t, rotate: rotate, root: root, edge: edge, leaves_state: leaves_state, leaves_coord: leaves_coord)

# EvaluatorとHashの初期値を返す
proc make_initial_node(self: State): (Evaluator, Hash) =
    var put = 0
    var hash: Hash = 0
    hash ^= zobrist_hash_coord[self.root[0]][self.root[1]]
    for i in 0..<self.N:
        for j in 0..<self.N:
            if self.s[i][j] == '1':
                hash ^= zobrist_hash_s[i][j]
                discard
            if self.s[i][j] == '1' and self.t[i][j] == '1':
                put += 1
    return (new_evaluator(put, 0), hash)

# 次の状態候補を全てselectorに追加する
# 引数
#   evaluator : 今の評価器
#   hash      : 今のハッシュ値
#   parent    : 今のノードID（次のノードにとって親となる）
# 速度にかなり寄与する部分なので大事
proc expand(self: State, evaluator: Evaluator, hash: Hash, parent: int,
            selector: var Selector){.inline.} =
    var n_hash = hash
    n_hash ^= zobrist_hash_coord[self.root[0]][self.root[1]]
    for move in 0..<5:
        var nn_hash = n_hash
        if 0 <= self.root[0] + MOVES_D[move][0] and
            self.root[0] + MOVES_D[move][0] < self.N and
            0 <= self.root[1] + MOVES_D[move][1] and
            self.root[1] + MOVES_D[move][1] < self.N:
            nn_hash ^= zobrist_hash_coord[self.root[0]+MOVES_D[move][0]][self.root[1]+MOVES_D[move][1]]
        else:
            continue
        for rotate_1 in -1..1:
            var
                ex, ey: int
                n_rotate = [self.rotate[0] + rotate_1, self.rotate[1] + rotate_1]
            if n_rotate[0] >= 4:
                n_rotate[0] -= 4
            elif n_rotate[0] < 0:
                n_rotate[0] += 4

            if n_rotate[0] == 0:
                ex = self.edge[0] + self.root[0] + MOVES_D[move][0]
                ey = self.edge[1] + self.root[1] + MOVES_D[move][1]
            elif n_rotate[0] == 1:
                ex = self.edge[1] + self.root[0] + MOVES_D[move][0]
                ey = -self.edge[0] + self.root[1] + MOVES_D[move][1]
            elif n_rotate[0] == 2:
                ex = -self.edge[0] + self.root[0] + MOVES_D[move][0]
                ey = -self.edge[1] + self.root[1] + MOVES_D[move][1]
            elif n_rotate[0] == 3:
                ex = -self.edge[1] + self.root[0] + MOVES_D[move][0]
                ey = self.edge[0] + self.root[1] + MOVES_D[move][1]

            for rotate_2 in -1..1:
                if rotate_1 == 0 and rotate_2 == 0 and move == 0:
                    continue
                var
                    action = new_action(move, [rotate_1, rotate_2], 0)
                    evaluator = evaluator
                    nn_rotate = n_rotate
                    finished = false
                    nnn_hash = nn_hash
                nn_rotate[1] += rotate_2
                if nn_rotate[1] >= 4:
                    nn_rotate[1] -= 4
                elif nn_rotate[1] < 0:
                    nn_rotate[1] += 4

                for i, (x, y) in self.leaves_coord:
                    var nx, ny: int
                    if nn_rotate[1] == 0:
                        nx = x + ex
                        ny = y + ey
                    elif nn_rotate[1] == 1:
                        nx = y + ex
                        ny = -x + ey
                    elif nn_rotate[1] == 2:
                        nx = -x + ex
                        ny = -y + ey
                    elif nn_rotate[1] == 3:
                        nx = -y + ex
                        ny = x + ey
                    if 0 <= nx and nx < self.N and 0 <= ny and ny < self.N:
                        if self.s[nx][ny] == '0' and self.t[nx][ny] == '1' and self.leaves_state[i]:
                            evaluator.put += 1
                            evaluator.caught -= 1
                            action.catch.add(i)
                            if evaluator.put == self.M:
                                finished = true
                            nnn_hash ^= zobrist_hash_s[nx][ny]
                        elif self.s[nx][ny] == '1' and self.t[nx][ny] == '0' and not self.leaves_state[i]:
                            evaluator.caught += 1
                            action.catch.add(i)
                            nnn_hash ^= zobrist_hash_s[nx][ny]
                selector.push(new_candidate(action, evaluator, nnn_hash, parent), finished)


# actionを実行して次の状態に遷移する
proc move_forward(self: var State, action: Action) =
    self.leaves_state ^= action.catch
    self.root[0] += MOVES_D[action.move][0]
    self.root[1] += MOVES_D[action.move][1]

    for i in 0..<2:
        if i == 0:
            self.rotate[i] += action.rotate[i]
            self.rotate[1] += action.rotate[i]
        else:
            self.rotate[i] += action.rotate[i]
        if self.rotate[i] >= 4:
            self.rotate[i] -= 4
        elif self.rotate[i] < 0:
            self.rotate[i] += 4
    var ex, ey: int
    if self.rotate[0] == 0:
        ex = self.edge[0] + self.root[0]
        ey = self.edge[1] + self.root[1]
    elif self.rotate[0] == 1:
        ex = self.edge[1] + self.root[0]
        ey = -self.edge[0] + self.root[1]
    elif self.rotate[0] == 2:
        ex = -self.edge[0] + self.root[0]
        ey = -self.edge[1] + self.root[1]
    elif self.rotate[0] == 3:
        ex = -self.edge[1] + self.root[0]
        ey = self.edge[0] + self.root[1]

    for i, (x, y) in self.leaves_coord:
        if action.catch[i]:
            var nx, ny: int
            if self.rotate[1] == 0:
                nx = x + ex
                ny = y + ey
            elif self.rotate[1] == 1:
                nx = y + ex
                ny = -x + ey
            elif self.rotate[1] == 2:
                nx = -x + ex
                ny = -y + ey
            elif self.rotate[1] == 3:
                nx = -y + ex
                ny = x + ey
            if self.s[nx][ny] == '1':
                self.s[nx][ny] = '0'
            else:
                self.s[nx][ny] = '1'


# actionを実行する前の状態に遷移する
# 今の状態は、親からactionを実行して遷移した状態である
proc move_backward(self: var State, action: Action) =
    var ex, ey: int
    if self.rotate[0] == 0:
        ex = self.edge[0] + self.root[0]
        ey = self.edge[1] + self.root[1]
    elif self.rotate[0] == 1:
        ex = self.edge[1] + self.root[0]
        ey = -self.edge[0] + self.root[1]
    elif self.rotate[0] == 2:
        ex = -self.edge[0] + self.root[0]
        ey = -self.edge[1] + self.root[1]
    elif self.rotate[0] == 3:
        ex = -self.edge[1] + self.root[0]
        ey = self.edge[0] + self.root[1]

    for i, (x, y) in self.leaves_coord:
        if action.catch[i]:
            var nx, ny: int
            if self.rotate[1] == 0:
                nx = x + ex
                ny = y + ey
            elif self.rotate[1] == 1:
                nx = y + ex
                ny = -x + ey
            elif self.rotate[1] == 2:
                nx = -x + ex
                ny = -y + ey
            elif self.rotate[1] == 3:
                nx = -y + ex
                ny = x + ey
            if self.s[nx][ny] == '1':
                self.s[nx][ny] = '0'
            else:
                self.s[nx][ny] = '1'

    self.leaves_state ^= action.catch
    self.root[0] -= MOVES_D[action.move][0]
    self.root[1] -= MOVES_D[action.move][1]
    for i in 0..<2:
        if i == 0:
            self.rotate[i] -= action.rotate[i]
            self.rotate[1] -= action.rotate[i]
        else:
            self.rotate[i] -= action.rotate[i]

        if self.rotate[i] >= 4:
            self.rotate[i] -= 4
        elif self.rotate[i] < 0:
            self.rotate[i] += 4


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
        if time.get_passed_time() > 2.3:
            selector.change_beam_width(4000)

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
    max_turn = 10**5
    beam_width = 8000
    tour_capacity = 5 * beam_width
    hashmap_capacity = 5 * beam_width

# -----------------------------------------------------------------------

type Solver = object
    input: Input
    time: Time

proc new_solver(input: Input, time: Time): Solver =
    return Solver(input: input, time: time)

proc solve(self: var Solver, output: var Output) =
    make_zobrist_hash(self.input)
    var
        config = new_config(max_turn, beam_width, tour_capacity, hashmap_capacity)
        leaves_coord = make_tree(self.input, output)
        root = get_root_xy(self.input, output)
        state = new_state(self.input, leaves_coord, root, output.pl[0])
        actions = beam_search(config, state, self.time)
    for action in actions:
        var init_action = ".".repeat(self.input.V * 2)
        init_action[0] = MOVES_S[action.move]
        for i in 1..<self.input.V:
            if i == 1:
                if action.rotate[0] == -1:
                    init_action[i] = 'L'
                elif action.rotate[0] == 1:
                    init_action[i] = 'R'
            else:
                if action.rotate[1] == -1:
                    init_action[i] = 'L'
                elif action.rotate[1] == 1:
                    init_action[i] = 'R'
        for i in 0..<self.input.V-1:
            if action.catch[i]:
                init_action[self.input.V + 2 + i] = 'P'
        output.actions.add(init_action)



# -----------------------------------------------------------------------

proc main() =
    var
        time = new_time(TIME_LIMIT)
        input = Input()
        output = Output()
    input.input()
    var solver = new_solver(input, time)
    solver.solve(output)
    output.output()

main()
