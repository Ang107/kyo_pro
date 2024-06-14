
import macros
import std/times
import std/random
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"
randomize(0)

#座標を持つオブジェクト
type Coord = ref object
    x: int
    y: int

#定数
const
    H = 3
    W = 4
    END_TURN = 4
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
#盤面の情報を持つクラス
type State = ref object
    points: array[H, array[W, int]]
    turn: int
    chara: Coord
    score: int

#コンストラクタ
proc new_State(): State =
    var
        points: array[H, array[W, int]]
        turn = 0
        chara = Coord()
        score = 0

    chara.x = rand(H-1)
    chara.y = rand(W-1)
    for i in 0..<H:
        for j in 0..<W:
            if i == chara.x and j == chara.y:
                continue
            points[i][j] = rand(9)
    result = State(points: points, chara: chara)
    return result

#終了条件判定
proc isDone(self: State): bool =
    return self.turn == END_TURN

#1ターン進める
proc advance(self: State, action: int) =
    self.chara.x += dx[action]
    self.chara.y += dy[action]
    var point = self.points[self.chara.x][self.chara.y]
    if point > 0:
        self.score += point
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

#状況を文字列として取得（デバッグ用）
proc `$`(self: State): string =
    result.add("turn: " & $self.turn & "\n")
    result.add("score: " & $self.score & "\n")
    for i in 0..<H:
        for j in 0..<W:
            if i == self.chara.x and j == self.chara.y:
                result.add("@")
            else:
                result.add($self.points[i][j])
        result.add("\n")
    return result

#ランダムな合法手を返す
proc random_action(self: State): int =
    var legal_actions = legal_actions(self)
    return legal_actions[rand(len(legal_actions) - 1)]

proc play_game() =
    var state = new_State()
    echo state
    while not state.isDone():
        state.advance(random_action(state))
        echo state

play_game()





