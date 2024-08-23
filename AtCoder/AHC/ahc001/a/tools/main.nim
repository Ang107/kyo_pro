# AHC用のテンプレート
import std/times
import std/random
import atcoder/segtree
# import nimprof
{.checks: off.}
import macros
# randomize()
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
    TIME_LIMIT = 4.9
    # TODO

# -----------------------------------------------------------------------

# 入力を管理するオブジェクト
type Input = object
    n: int
    xyr: seq[(int, int, int)]

proc input(self: var Input) =
    self.n = ii()
    self.xyr = newSeqOfCap[(int, int, int)](self.n)
    for i in 0..<self.n:
        var x, y, r = ii()
        self.xyr.add((x, y, r))




# -----------------------------------------------------------------------

# 出力を管理するオブジェクト
type Output = object
    ans: seq[array[4, int]]
proc new_output(input: Input): Output =
    var ans = newSeq[array[4, int]](input.n)
    return Output(ans: ans)
# indexの面積を返す。
proc get_s(self: Output, index: int): int =
    return (self.ans[index][2] - self.ans[index][0]) * (self.ans[index][3] -
            self.ans[index][1])

proc output(self: Output) =
    for i in self.ans:
        stdout.writeLine(i.join(" "))

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
proc calc_initial_solution(input: Input, output: var Output) =
    for i, (x, y, r) in input.xyr:
        output.ans[i] = [x, y, x+1, y+1]

proc is_duplicate(output: Output, index: int): bool =
    proc is_overlapping(x1_a, y1_a, x2_a, y2_a, x1_b, y1_b, x2_b,
            y2_b: int): bool =
        return not (x2_a <= x1_b or # 矩形Aが矩形Bの左側にある
            x1_a >= x2_b or # 矩形Aが矩形Bの右側にある
            y2_a <= y1_b or # 矩形Aが矩形Bの上側にある
            y1_a >= y2_b) # 矩形Aが矩形Bの下側にある

    var
        ai = output.ans[index][0]
        bi = output.ans[index][1]
        ci = output.ans[index][2]
        di = output.ans[index][3]

    for i, abcd in output.ans:
        var
            a = abcd[0]
            b = abcd[1]
            c = abcd[2]
            d = abcd[3]
        if i == index:
            continue
        if is_overlapping(ai, bi, ci, di, a, b, c, d):
            return true
    return false


proc optimize(input: Input, output: var Output, time: Time) =
    var
        cnt = 0
        start_temp = 4000
        end_temp = 0
        now_time: float
        prob: float
        temp: float
    while true:
        if cnt % 100 == 0:
            now_time = time.get_passed_time()
            temp = start_temp + (end_temp - start_temp) * now_time / TIME_LIMIT
            # if now_time < 3.5:
            #     temp = 1000000
            # # elif now_time < 4:
            # #     temp = 1000000
            # else:
            #     temp = 0
            if now_time > TIME_LIMIT:
                break
        var mode = rand(1)
        # ランダムに長方形を選ぶ
        var index = rand(input.n-1)
        # ランダムに上下左右の辺を選ぶ
        var uldr = rand(3)
        # 動かす方向をランダムに選ぶ
        var d = sample([-1, 1])

        var
            r = input.xyr[index][2]
            s = output.get_s(index)
            # 遷移前のスコア (小さいほど良い)
            prv_score = abs(r - s)

        # 遷移後の座標
        output.ans[index][uldr] += d
        if mode == 1:
            output.ans[index][(uldr+2) % 4] += d


        s = output.get_s(index)
        if s == 0:
            output.ans[index][uldr] -= d
            if mode == 1:
                output.ans[index][(uldr+2) % 4] -= d
            continue
        # 悪化したなら
        var new_score = abs(r-s)

        if prv_score < new_score and r < s:
            output.ans[index][uldr] -= d
            if mode == 1:
                output.ans[index][(uldr+2) % 4] -= d
            continue
        prob = exp((prv_score - new_score)/temp)
        # echo (prv_score, new_score, prob, rand(1.0))
        if prob < rand(1.0):
            output.ans[index][uldr] -= d
            if mode == 1:
                output.ans[index][(uldr+2) % 4] -= d
            continue

        if output.ans[index][0] > input.xyr[index][0] or input.xyr[index][0] >=
                output.ans[index][2]:
            output.ans[index][uldr] -= d
            if mode == 1:
                output.ans[index][(uldr+2) % 4] -= d
            continue
        if output.ans[index][1] > input.xyr[index][1] or input.xyr[index][1] >=
                output.ans[index][3]:
            output.ans[index][uldr] -= d
            if mode == 1:
                output.ans[index][(uldr+2) % 4] -= d
            continue

        # 範囲外なら
        if output.ans[index][uldr] < 0 or 10000 < output.ans[index][uldr]:
            output.ans[index][uldr] -= d
            if mode == 1:
                output.ans[index][(uldr+2) % 4] -= d
            continue
        if output.ans[index][(uldr+2) % 4] < 0 or 10000 < output.ans[index][(
                uldr+2) % 4]:
            output.ans[index][uldr] -= d
            if mode == 1:
                output.ans[index][(uldr+2) % 4] -= d
            continue

        # 重複しないか
        if is_duplicate(output, index):
            output.ans[index][uldr] -= d
            if mode == 1:
                output.ans[index][(uldr+2) % 4] -= d
            continue






    # -----------------------------------------------------------------------

type Solver = object
    input: Input
    time: Time

proc new_solver(input: Input, time: Time): Solver =
    return Solver(input: input, time: time)

proc solve(self: var Solver, output: var Output) =
    calc_initial_solution(self.input, output)
    optimize(self.input, output, self.time)
    for i in 0..<self.input.n:
        stderr.writeLine(i, self.input.xyr[i], output.ans[i], output.get_s(i))


# -----------------------------------------------------------------------

proc main() =
    var
        time = new_time(TIME_LIMIT)
        input = Input()
    input.input()
    var output = new_output(input)
    var solver = new_solver(input, time)
    solver.solve(output)
    output.output()
    time.out_paased_time()
main()
