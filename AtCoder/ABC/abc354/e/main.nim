import macros
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"

var
    n = ii()
    ab = newSeqOfCap[(int, int)](n)
    memo = initTable[(int, int), int]()

for _ in 0..<n:
    ab.add((ii(), ii()))

proc f(turn: int, b: int): int =

    if (turn, b) in memo:
        return memo[(turn, b)]

    if turn == 0:
        result = -1
        for i in range(n):
            for j in range(i+1, n):
                if (b >> i) & 1 == 0 and (b >> j) & 1 == 0 and (ab[i][0] == ab[j][0] or ab[i][1] == ab[j][1]):
                    result = max(result, f(turn ^ 1, b | (1<<i) | (1 << j)))
    else:
        result = 1
        for i in range(n):
            for j in range(i+1, n):
                if (b >> i) & 1 == 0 and (b >> j) & 1 == 0 and (ab[i][0] == ab[j][0] or ab[i][1] == ab[j][1]):

                    result = min(result, f(turn ^ 1, b | (1<<i) | (1 << j)))

    memo[(turn, b)] = result
    return result

if f(0, 0) == 1:
    echo "Takahashi"
else:
    echo "Aoki"
