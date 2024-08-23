# 状態をコピーするビームサーチ
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
    # TODO

# -----------------------------------------------------------------------

# 入力を管理するオブジェクト
type Input = object
    # TODO

proc input(self: var Input) =
    # TODO
    discard

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
    hashmap_capacity: int


proc new_config(max_turn, beam_width, hashmap_capacity: int): Config =
    return Config(max_turn: max_turn, beam_width: beam_width,
            hashmap_capacity: hashmap_capacity)

# -----------------------------------------------------------------------

# 型のエイリアス
type
    Cost = int
    Hash = uint64
    HashMap = Table

# -----------------------------------------------------------------------

# 状態遷移を行うために必要な情報を持つオブジェクト
type
    Action = object
        # TODO

    # コンストラクタ
proc new_action(): Action {.inline.} =
    # TODO
    return Action()

proc `==`(self, other: Action): bool =
    #TODO
    discard

# -----------------------------------------------------------------------
# 状態のコストを評価するための情報を管理するオブジェクト

type
    Evaluator = object
        final_cost: Cost
        # TODO

    # コンストラクタ
proc new_evaluator(): Evaluator {.inline.} =
    # TODO
    return Evaluator()

# 低いほど良い
# コストを計算してfinal_costを更新し、その値を返す。
proc evaluate(self: Evaluator): Cost =
    # TODO
    discard

# -----------------------------------------------------------------------

# 状態自体を管理するオブジェクト
type State = object
    # TODO

# コンストラクタ
proc new_state(): State {.inline.} =
    discard

# -----------------------------------------------------------------------

# 展開するノードの候補を表すオブジェクト
type Candidate = ref object
    action: Action
    evaluator: Evaluator
    state: State
    hash: Hash
    parent: Candidate
proc op(a, b: (Candidate, int)): (Candidate, int) =
    if a[0].evaluator.evaluate() >= b[0].evaluator.evaluate():
        return a
    else:
        return b
# ノードの候補から実際に追加するものを選ぶクラス
# ビーム幅の個数だけ、評価がよいものを選ぶ
# ハッシュ値が一致したものについては、評価がよいほうのみを残す
type
    MaxSegTree = SegTreeType[(Candidate, int)](op, () => (-INF64, -1))
    Selector = object
        beam_width: int
        max_turn: int
        now_candidates: seq[Candidate]
        next_candidates: seq[(Candidate, int)]
        hash_to_idx: HashMap[Hash, int]
        full: bool
        st: MaxSegTree
        finished_candidates: seq[Candidate]

# 前方宣言
proc can_push(self: Selector, cost: Cost): bool
proc push(self: var Selector, candidate: Candidate, finished: bool)

# コンストラクタ
proc new_candidate(action: Action, evaluator: Evaluator, state: State,
                    hash: Hash, parent: Candidate,
                            have_parent: bool = true): Candidate {.inline.} =
    if have_parent:
        return Candidate(action: action, evaluator: evaluator,
                        state: state, hash: hash, parent: parent)
    else:
        # アクションはダミー、parentはnilの根のノードを作る。
        return Candidate(action: action, evaluator: evaluator,
                        state: state, hash: hash)

# 基本的にはself.evaluator.final_costのコストを返す。（ターンで評価方法を変える云々はよしなに）
proc evaluate(self: Candidate): Cost =
    # TODO
    return self.evaluator.final_cost

# 遷移先をselectorにpushする。実際に追加する前に遷移後のスコアを計算し、価値がある場合のみ状態をコピーして次の状態を作る。
proc expands(self: Candidate, selector: var Selector) =
    # TODO
    discard

# 行動列を復元して返す。
proc restore_action(self: Candidate): seq[Action] =
    var
        candidate = self
        #ターン数を指定
        turn = -1
        ret = newSeqOfCap[Action](turn)

    while not candidate.parent.isNil():
        ret.add(candidate.action)
        candidate = candidate.parent

    #行動順を戻す。
    ret.reverse()
    return ret
# -----------------------------------------------------------------------



# コンストラクタ
proc new_selector(config: Config): Selector =
    var
        beam_width = config.beam_width
        max_turn = config.max_turn
        now_candidates = newSeqOfCap[Candidate](beam_width)
        next_candidates = newSeqOfCap[(Candidate, int)](beam_width)
        hash_to_idx = initTable[Hash, int](config.hashmap_capacity)
        full = false
        finished_candidates = newSeqOfCap[Candidate](config.beam_width)

    return Selector(beam_width: beam_width, max_turn: max_turn, now_candidates: now_candidates,
                    next_candidates: next_candidates, hash_to_idx: hash_to_idx,
                    full: full, finished_candidates: finished_candidates)

# beam幅を変更（減少）させる
proc change_beam_width(self: var Selector, new_beam_width: int) =
    self.beam_width = new_beam_width

# 追加される可能性があるか判定
proc can_push(self: Selector, cost: Cost): bool =
    if self.full and cost >= self.st.all_prod()[0].evaluate():
        return false
    return true

# 候補を追加する
# ターン数最小化型の問題で、candidateによって実行可能解が得られる場合にのみ finished = true とする
# ビーム幅分の候補をCandidateを追加したときにsegment treeを構築する
proc push(self: var Selector, candidate: Candidate, finished: bool) =
    if finished:
        self.finished_candidates.add(candidate)
        return

    var cost = candidate.evaluate()
    if self.full and cost >= self.st.all_prod()[0].evaluate():
        # 保持しているどの候補よりもコストが小さくないとき
        return

    if candidate.hash in self.hash_to_idx:
        # ハッシュ値が等しいものが存在しているとき
        var j = self.hash_to_idx[candidate.hash]
        if candidate.hash == self.next_candidates[j][0].hash:
            if self.full:
                # segment treeが構築されている場合
                if cost < self.st.get(j)[0].evaluate():
                    self.next_candidates[j][0] = candidate
                    self.st.set(j, (candidate, j))
            else:
                # segment treeが構築されていない場合
                if cost < self.next_candidates[j][0].evaluate():
                    self.next_candidates[j] = (candidate, j)

            return
    if self.full:
        # segment treeが構築されている場合
        var j = self.st.all_prod()[1]
        self.hash_to_idx[candidate.hash] = j
        self.st.set(j, (candidate, j))
    else:
        # segment treeが構築されていない場合
        var j = self.next_candidates.len()
        self.hash_to_idx[candidate.hash] = j
        self.next_candidates.add((candidate, j))
        if self.next_candidates.len() == self.beam_width:
            # 保持している候補がビーム幅分になったときにsegment treeを構築する
            self.full = true
            self.st = MaxSegTree.init(self.next_candidates)

# 遷移先を選んでターンを一つ進める。
proc advance(self: var Selector) =
    for candidate in self.now_candidates:
        candidate.expands(self)

# 次のターンに進めるため、次ターンの候補をnow_candidatesに移す。
proc select(self: var Selector) =
    self.now_candidates.setLen(0)
    if self.full:
        for i in 0..<self.beam_width:
            self.now_candidates.add(self.st.get(i)[0])
    else:
        for i in 0..<self.next_candidates.len():
            self.now_candidates.add(self.next_candidates[i][0])
    self.next_candidates.setLen(0)

# 実行可能解が見つかったか
proc have_finished(self: Selector): bool =
    return self.finished_candidates.len() > 0

# 実行可能解に到達するCandidateを返す
proc get_finished_candidates(self: Selector): seq[Candidate] =
    return self.finished_candidates

# 最もよいCandidateを返す
proc caluculate_best_candidate(self: Selector): Candidate =
    var best = 0
    for i in 0..<self.now_candidates.len():
        if self.now_candidates[i].evaluator.evaluate() < self.now_candidates[
                best].evaluator.evaluate():
            best = i
    return self.now_candidates[best]

proc clear(self: var Selector) =
    self.hash_to_idx.clear()
    self.full = false




# -----------------------------------------------------------------------

# ビームサーチを行う関数
proc beam_search(config: Config, time: Time): seq[Action] =
    var
        selector = new_selector(config)
    for turn in 0..<config.max_turn:
        # 動的にビーム幅の調整

        # 次のターンの候補を選ぶ
        selector.advance()
        selector.select()
        if selector.have_finished():
            # ターン数最小化型の問題で実行可能解が見つかったとき
            var
                candidate = selector.get_finished_candidates()[0]
                ret = candidate.restore_action()
            return ret

        if turn == config.max_turn-1:
            # ターン数固定の問題で全ターンが終了したとき
            var
                best_candidate = selector.caluculate_best_candidate()
                ret = best_candidate.restore_action()
            return ret
        selector.clear()
    # -----------------------------------------------------------------------

    # 倍率は問題に合わせて調整
const
    # TODO
    max_turn = 1000
    beam_width = 2000
    tour_capacity = 10 * beam_width
    hashmap_capacity = 2 * beam_width

# -----------------------------------------------------------------------

type Solver = object
    input: Input
    time: Time

proc new_solver(input: Input, time: Time): Solver =
    return Solver(input: input, time: time)

proc solve(self: var Solver, output: var Output) =
    # TODO
    discard

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
    time.out_paased_time()
main()
