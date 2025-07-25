
import macros
import std/times
import std/random
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"
randomize(0)

#定数
const
    H = 30
    W = 30
    END_TURN = 100
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

#ハッシュ
type Zobrist_hash = object
    points: array[H, array[W, array[10, uint64]]]
    chara: array[H, array[W, uint64]]

#コンストラクタ
proc new_zobrist_hash(): Zobrist_hash =
    var
        points: array[H, array[W, array[10, uint64]]]
        chara: array[H, array[W, uint64]]
    for x in 0..<H:
        for y in 0..<W:
            for p in 0..<10:
                points[x][y][p] = uint64(rand(uint64))
            chara[x][y] = uint(rand(uint64))
    return Zobrist_hash(points: points, chara: chara)

#乱数の配置
var zobrist_hash = new_zobrist_hash()

proc `^=`(a: var uint64, b: uint64) =
    a = a xor b

#座標を持つオブジェクト
type Coord = object
    x: int
    y: int


#時間を管理するオブジェクト
type TimeKeeper = object
    start_time: float
    time_threshold: float


#コンストラクタ
proc new_time_keeper(time_threshold: float): TimeKeeper =
    return TimeKeeper(start_time: cpuTime(), time_threshold: time_threshold)

#時間超過かを判定
proc is_time_over(self: TimeKeeper): bool =
    var diff = cpuTime() - self.start_time
    return diff >= self.time_threshold



#盤面の情報を持つオブジェクト
type State = ref object
    points: array[H, array[W, int]]
    turn: int
    chara: Coord
    game_score: int
    first_action: int
    evaluated_score: int
    hash: uint64

proc `<`(state1: State, state2: State): bool =
    return state1.evaluated_score > state2.evaluated_score

#コンストラクタ
proc new_State(): State =
    var
        points: array[H, array[W, int]]
        chara = Coord()
        first_action = -1
        hash: uint64 = 0

    chara.x = rand(H-1)
    chara.y = rand(W-1)
    for x in 0..<H:
        for y in 0..<W:
            if x == chara.x and y == chara.y:
                continue
            points[x][y] = rand(9)

    hash ^= zobrist_hash.chara[chara.x][chara.y]
    for x in 0..<H:
        for y in 0..<W:
            var p = points[x][y]
            if p > 0:
                hash ^= zobrist_hash.points[x][y][p]

    result = State(points: points, chara: chara, first_action: first_action, hash: hash)
    return result

#終了条件判定
proc isDone(self: State): bool =
    return self.turn == END_TURN

#1ターン進める
proc advance(self: State, action: int) =
    #ハッシュの変更
    self.hash ^= zobrist_hash.chara[self.chara.x][self.chara.y]

    self.chara.x += dx[action]
    self.chara.y += dy[action]
    var point = self.points[self.chara.x][self.chara.y]

    self.hash ^= zobrist_hash.chara[self.chara.x][self.chara.y]

    if point > 0:
        self.hash ^= zobrist_hash.points[self.chara.x][self.chara.y][point]
        self.game_score += point
        self.points[self.chara.x][self.chara.y] = 0
    self.turn += 1

#合法手を取得
proc legal_actions(self: State): seq[int] =
    result = newSeqOfCap[int](4)
    for i in 0..<4:
        var
            tx = self.chara.x + dx[i]
            ty = self.chara.y + dy[i]
        if 0 <= tx and tx < H and 0 <= ty and ty < W:
            result.add(i)
    return result

# 状況を文字列として取得（デバッグ用）
proc `$`(self: State): string =
    result.add("turn: " & $self.turn & "\n")
    result.add("score: " & $self.game_score & "\n")
    for i in 0..<H:
        for j in 0..<W:
            if i == self.chara.x and j == self.chara.y:
                result.add("@")
            else:
                result.add($self.points[i][j])
        result.add("\n")
    return result

#盤面を評価する関数
proc eavluate_score(self: State) =
    self.evaluated_score = self.game_score

#ランダムな合法手を返す
proc random_action(self: State): int =
    var legal_actions = legal_actions(self)
    return legal_actions[rand(len(legal_actions) - 1)]

#貪欲に選択したときの手を返す。
proc greedy_action(self: State): int =
    var
        best_score = -1
        best_action = -1
        legal_actions = legal_actions(self)
    for action in legal_actions:
        var
            x = self.chara.x + dx[action]
            y = self.chara.y + dy[action]
            new_score = self.points[x][y]
        if new_score > best_score:
            best_score = new_score
            best_action = action
    return best_action

proc hash(x: uint64): uint64 =
    return x

#ビームサーチを用いて選択したときの手を返す。
proc beamsearch_action(self: State, beam_width, beam_depth: int): int =
    var
        now_beam = initHeapQueue[State]()
        best_state: State
        hash_check = initHashSet[uint64]()

    now_beam.push(self)
    for t in 0..<beam_depth:
        var next_beam = initHeapQueue[State]()
        for i in 0..<beam_width:
            if len(now_beam) == 0:
                break
            var
                now_state = now_beam.pop()
                legal_actions = legal_actions(now_state)
            for action in legal_actions:
                var next_state = now_state.deepcopy()
                next_state.advance(action)
                if next_state.hash in hash_check:
                    continue
                hash_check.incl(next_state.hash)
                next_state.eavluate_score()
                if t == 0:
                    next_state.first_action = action
                next_beam.push(next_state)
        now_beam = next_beam
        best_state = now_beam[0]
        if best_state.isDone():
            break
    return best_state.first_action


proc play_game(seed: int = 0): int =
    randomize(seed)
    var state = new_State()
    # echo state
    while not state.isDone():
        state.advance(beamsearch_action(state, 50, 100))
        # state.advance(greedy_action(state))
        # echo state
    return state.game_score


proc test_score(game_number: int) =
    var score_mean = 0.0
    for i in 0..<game_number:
        var score = float(play_game(i))
        score_mean += score
        # echo fmt"score_{i}: {score}"
    score_mean /= float(game_number)
    echo fmt"score_mean: {score_mean}"

# echo zobrist_hash.points
# echo zobrist_hash.chara
# quit()
test_score(1)
# discard play_game(1)





