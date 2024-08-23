# 状態をコピーするビームサーチ
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
    TIME_LIMIT = 1.9
    N = 9
    M = 20
    K = 81
    comb_num = [1, 20, 210, 1540, 8855, 42504, 177100, 657800]
    MOD = 998244353

# -----------------------------------------------------------------------
# 色んな情報を管理するオブジェクト
type Info = object
    stamps_comb_sum: array[8, seq[array[3, array[3, int]]]]
    stamps_comb_index: array[8, seq[seq[int]]]
    pq: array[49, (int, int)]
    limit: array[49, int]
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
proc dfs(depth, size, min, max: int, stamps: array[M, array[3, array[3, int]]],
        info: var Info, comb: var seq[int]) =
    if depth == size:
        var tmp: array[3, array[3, int]]
        for i in comb:
            for j in 0..<3:
                for k in 0..<3:
                    tmp[j][k] = (tmp[j][k] + stamps[i][j][k]) % MOD
        info.stamps_comb_sum[size].add(tmp)
        info.stamps_comb_index[size].add(comb & @[info.stamps_comb_index[
                size].len()])
    else:
        for i in min..max:
            comb[depth] = i
            dfs(depth+1, size, i, max, stamps, info, comb)

proc calc_stamps_comb(info: var Info, input: Input) =
    for i in 0..<8:
        info.stamps_comb_sum[i] = newSeqOfCap[array[3, array[3, int]]](comb_num[i])
    var comb: seq[int]

    for i in 0..<7:
        comb = newSeq[int](i)
        dfs(0, i, 0, 19, input.stamps, info, comb)
        let localCopy = info.stamps_comb_sum[i]
        info.stamps_comb_index[i].sort(proc (a, b: seq[int]): int = cmp(
        localCopy[a[^1]][0][0],
        localCopy[b[^1]][0][0]))
        info.stamps_comb_sum[i].sort(proc (a, b: array[3, array[3,
                int]]): int = cmp(
        a[0][0],
        b[0][0]))

proc setup(info: var Info, input: Input) =
    # pq = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
    #     (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
    #     (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
    #     (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
    #     (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
    #     (3, 2), (4, 2), (5, 2), (6, 2),
    #     (3, 3), (3, 4), (3, 5), (3, 6),
    #     (4, 3), (5, 3), (6, 3),
    #     (4, 4), (4, 5), (4, 6),
    #     (5, 4), (6, 4),
    #     (5, 5), (5, 6),
    #     (6, 5),
    #     (6, 6)]
    var tmp = 0
    for i in 0..<6:
        for j in 0..<6:
            info.pq[tmp] = (i, j)
            tmp += 1
    for i in 0..<6:
        info.pq[tmp] = (i, 6)
        tmp += 1
    for i in 0..<6:
        info.pq[tmp] = (6, i)
        tmp += 1
    info.pq[tmp] = (6, 6)

    calc_stamps_comb(info, input)
    for i in 0..<36:
        info.limit[i] = 1 + 5 + i
    for i in 36..<48:
        info.limit[i] = 36 + 3 + (i - 36) * 3 + 5
    info.limit[48] = 81
# -----------------------------------------------------------------------

# 出力を管理するオブジェクト
type Output = object
    used_stamps: seq[(int, int, int)]

proc output(self: Output) =
    stdout.writeLine(self.used_stamps.len())
    for (i, j, k) in self.used_stamps:
        stdout.writeLine([i, j, k].join(" "))

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
        stamp_num: int
        index: int
        p: int
        q: int

# コンストラクタ
proc new_action(stamp_num, index, p, q: int): Action {.inline.} =
    return Action(stamp_num: stamp_num, index: index, p: p, q: q)

proc `==`(self, other: Action): bool =
    #TODO
    discard

# -----------------------------------------------------------------------
# 状態のコストを評価するための情報を管理するオブジェクト

type
    Evaluator = object
        final_cost: Cost
        cost: Cost
        # TODO

    # コンストラクタ
proc new_evaluator(cost: Cost): Evaluator {.inline.} =
    # TODO
    return Evaluator(cost: cost)

# 低いほど良い
# コストを計算してfinal_costを更新し、その値を返す。
proc evaluate(self: Evaluator): Cost {.inline.} =
    return self.cost
    # TODO

# -----------------------------------------------------------------------

# 状態自体を管理するオブジェクト
type State = object
    bord: array[9, array[9, int]]
    used_num: int
    now_turn: int

# コンストラクタ
proc new_state(input: Input): State {.inline.} =
    return State(bord: input.bord, used_num: 0, now_turn: 0)


# -----------------------------------------------------------------------

# 展開するノードの候補を表すオブジェクト
type Candidate = ref object
    action: Action
    evaluator: Evaluator
    state: State
    hash: Hash
    parent: Candidate

# コンストラクタ 初ターン用のcandidateを作る。stateのみ初期化する。
proc new_candidate(input: Input): Candidate {.inline.} =
    var
        state = new_state(input)
    return Candidate(state: state)


#セグツリーに載せるための偽のcandidate
proc dummy_candidate(): Candidate =
    return Candidate()



proc op(a, b: (Cost, Candidate, int)): (Cost, Candidate, int) =
    if a[0] >= b[0]:
        return a
    else:
        return b
# ノードの候補から実際に追加するものを選ぶクラス
# ビーム幅の個数だけ、評価がよいものを選ぶ
# ハッシュ値が一致したものについては、評価がよいほうのみを残す
type
    MaxSegTree = SegTreeType[(Cost, Candidate, int)](op, () => (-INF,
            dummy_candidate(), -1))
    Selector = object
        beam_width: int
        max_turn: int
        now_candidates: seq[Candidate]
        next_candidates: seq[(Cost, Candidate, int)]
        hash_to_idx: HashMap[Hash, int]
        full: bool
        st: MaxSegTree
        finished_candidates: seq[Candidate]

# 前方宣言
proc can_push(self: Selector, cost: Cost): bool
proc push(self: var Selector, candidate: Candidate, finished: bool)


# 基本的にはself.evaluator.evaluate()を返す。（ターンで評価方法を変える云々はよしなに）
proc evaluate(self: Candidate): Cost =
    # TODO
    return self.evaluator.evaluate()

# 遷移先をselectorにpushする。実際に追加する前に遷移後のスコアを計算し、価値がある場合のみ状態をコピーして次の状態を作る。
proc expands(self: Candidate, selector: var Selector, info: Info) =
    var
        lim = info.limit[self.state.now_turn] - self.state.used_num
        (p, q) = info.pq[self.state.now_turn]
    if p < 6 and q < 6:
        lim = min(lim, 3)
    elif p >= 6 and q >= 6:
        lim = min(lim, 5)
    else:
        lim = min(lim, 6)

    for i in 0..lim:
        var tmp = info.stamps_comb_sum[i].lowerBound(800000000-self.state.bord[
                p][q], proc (a: array[3, array[3, int]], b: int): int = cmp(a[
                        0][0], b))
        for j in tmp..<info.stamps_comb_index[i].len():
            var
                cost = self.evaluate()
                hash: Hash

            if p < 6 and q < 6:
                var
                    tmp = (self.state.bord[p][q] + info.stamps_comb_sum[i][j][
                            0][0])
                    tmp_mod = tmp % MOD
                if tmp_mod <= 900000000:
                    continue
                elif tmp > MOD:
                    break
                hash = uint64(tmp_MOD)
                cost -= tmp_MOD
            elif p >= 6 and q >= 6:
                if (self.state.bord[p][q] + info.stamps_comb_sum[i][j][0][0]) >
                        MOD and self.state.bord[p][q] < 800000000:
                    break
                var tmp = 0
                for k in 0..<3:
                    for l in 0..<3:
                        tmp += (self.state.bord[p+k][q+l] +
                        info.stamps_comb_sum[i][j][k][l]) % MOD
                if tmp <= 900000000 * 9:
                    continue
                hash = uint64(tmp)
                cost -= tmp
            elif p < 6:
                if (self.state.bord[p][q] + info.stamps_comb_sum[i][j][0][0]) >
                        MOD and self.state.bord[p][q] < 800000000:
                    break
                var tmp = 0
                for l in 0..<3:
                    tmp += (self.state.bord[p][q+l] +
                    info.stamps_comb_sum[i][j][0][l]) % MOD
                if tmp <= 900000000 * 3:
                    continue
                hash = uint64(tmp)
                cost -= tmp
            elif q < 6:
                if (self.state.bord[p][q] + info.stamps_comb_sum[i][j][0][0]) >
                        MOD and self.state.bord[p][q] < 800000000:
                    break
                var tmp = 0
                for k in 0..<3:
                    tmp += (self.state.bord[p+k][q] +
                    info.stamps_comb_sum[i][j][k][0]) % MOD
                if tmp <= 900000000 * 3:
                    continue
                hash = uint64(tmp)
                cost -= tmp

            if selector.can_push(cost):
                #追加されるなら次の状態を作る。
                var next_candidate = self.deepCopy()
                next_candidate.action = new_action(i, j, p, q)
                next_candidate.evaluator.cost = cost
                next_candidate.hash = hash
                next_candidate.parent = self
                next_candidate.state.now_turn += 1
                next_candidate.state.used_num += i
                for k in 0..<3:
                    for l in 0..<3:
                        next_candidate.state.bord[p+k][q+l] = (
                            self.state.bord[p+k][q+l] +
                            info.stamps_comb_sum[i][j][k][l]) % MOD
                selector.push(next_candidate, false)

    discard

# 行動列を復元して返す。
proc restore_action(self: Candidate): seq[Action] =
    var
        candidate = self
        #ターン数を指定
        turn = 49
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
        next_candidates = newSeqOfCap[(Cost, Candidate, int)](beam_width)
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
    if self.full and cost >= self.st.all_prod()[0]:
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
    if self.full and cost >= self.st.all_prod()[0]:
        # 保持しているどの候補よりもコストが小さくないとき
        return

    if candidate.hash in self.hash_to_idx:
        # ハッシュ値が等しいものが存在しているとき
        var j = self.hash_to_idx[candidate.hash]
        if candidate.hash == self.next_candidates[j][1].hash:
            if self.full:
                # segment treeが構築されている場合
                if cost < self.st.get(j)[0]:
                    self.next_candidates[j][1] = candidate
                    self.st.set(j, (candidate.evaluate(), candidate, j))
            else:
                # segment treeが構築されていない場合
                if cost < self.next_candidates[j][1].evaluate():
                    self.next_candidates[j] = (candidate.evaluate(), candidate, j)

            return
    if self.full:
        # segment treeが構築されている場合
        var j = self.st.all_prod()[2]
        self.hash_to_idx[candidate.hash] = j
        self.st.set(j, (candidate.evaluate(), candidate, j))
    else:
        # segment treeが構築されていない場合
        var j = self.next_candidates.len()
        self.hash_to_idx[candidate.hash] = j
        self.next_candidates.add((candidate.evaluate(), candidate, j))
        if self.next_candidates.len() == self.beam_width:
            # 保持している候補がビーム幅分になったときにsegment treeを構築する
            self.full = true
            self.st = MaxSegTree.init(self.next_candidates)

proc push_root_candidate(self: var Selector, input: Input) =
    self.push(new_candidate(input), false)

# 遷移先を選んでターンを一つ進める。
proc advance(self: var Selector, info: Info) =
    for candidate in self.now_candidates:
        candidate.expands(self, info)

# 次のターンに進めるため、次ターンの候補をnow_candidatesに移す。
proc select(self: var Selector) =
    self.now_candidates.setLen(0)
    if self.full:
        for i in 0..<self.beam_width:
            self.now_candidates.add(self.st.get(i)[1])
    else:
        for i in 0..<self.next_candidates.len():
            self.now_candidates.add(self.next_candidates[i][1])
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
proc beam_search(config: Config, time: Time, info: Info, input: Input): seq[Action] =
    var
        selector = new_selector(config)
    selector.push_root_candidate(input)
    selector.select()

    for turn in 0..<config.max_turn:
        # 動的にビーム幅の調整
        # 次のターンの候補を選ぶ
        selector.advance(info)
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
    max_turn = 49
    beam_width = 1000
    hashmap_capacity = 15 * beam_width

# -----------------------------------------------------------------------

type Solver = object
    input: Input
    time: Time

proc new_solver(input: Input, time: Time): Solver =
    return Solver(input: input, time: time)

proc solve(self: var Solver, output: var Output) =
    var
        config = new_config(max_turn, beam_width, hashmap_capacity)
        info = Info()
    info.setup(self.input)
    var actions = beam_search(config, self.time, info, self.input)
    for action in actions:
        for i in 0..<info.stamps_comb_index[action.stamp_num][
                action.index].len()-1:
            output.used_stamps.add(
                (info.stamps_comb_index[action.stamp_num][action.index][i],
                        action.p, action.q))



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
