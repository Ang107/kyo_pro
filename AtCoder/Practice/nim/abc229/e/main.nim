import macros
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"

var
    n, m = ii()
    ed = newSeq[newSeqOfCap[int](n)](n)

for i in 0..<m:
    var u, v = ii()
    ed[u-1].add(v-1)

type
    UnionFind = ref object
        par: seq[int]
        rank: seq[int]
        siz: seq[int]

proc newUnionFind(n: int): UnionFind =
    var
        par = newSeqwith(n, -1)
        rank = newSeqWith(n, 0)
        siz = newSeqWith(n, -1)
        UF = UnionFind(par: par, rank: rank, siz: siz)
    return UF

proc root(UF: UnionFind, x: int): int =
    if UF.par[x] == -1:
        return x
    else:
        UF.par[x] = UF.root(UF.par[x])
        return UF.par[x]

proc issame(UF: UnionFind, x, y: int): bool =
    return UF.root(x) == UF.root(y)

proc unite(UF: UnionFind, x, y: int): bool =
    var
        rx = UF.root(x)
        ry = UF.root(y)
    if rx == ry:
        return false

    if UF.rank[rx] < UF.rank[ry]:
        swap(rx, ry)
    UF.par[ry] = rx
    if UF.rank[rx] == UF.rank[ry]:
        UF.rank[rx] += 1
    UF.siz[rx] += UF.siz[ry]

    return true

proc size(UF: UnionFind, x: int): int =
    return UF.siz[UF.root(x)]

var
    UF = newUnionFind(n)
    ans = newseqofcap[int](n)
    num = 0
ans.add(0)
for i in countdown(n-1, 1, 1):
    num += 1
    for j in ed[i]:
        if not UF.issame(i, j):
            discard UF.unite(i, j)
            num -= 1
    ans.add(num)
ans.reverse()
for i in ans:
    echo i







