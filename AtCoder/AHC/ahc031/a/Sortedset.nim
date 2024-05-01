import macros
import random
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"

type
    Sortedset = ref object
        a: seq[seq[int]]
        size: int
        BUCKET_RATIO: int
        SPLIT_RATIO: int

proc newSortedset(ini: seq[int]): Sortedset =
    var
        ini_sorted = ini.sorted().deduplicate(true)
        BUCKET_RATIO: int = 16
        SPLIT_RATIO: int = 24
        n = ini_sorted.len()
        num_bucekt = int(ceil(sqrt(n/BUCKET_RATIO)))
        a = newSeqOfCap[newSeqOfCap[int](2*n//num_bucekt)](num_bucekt)
    for i in 0..<num_bucekt:
        a.add(ini_sorted[n*i//num_bucekt..<n*(i+1)//num_bucekt])
    var sms = Sortedset(a: a, size: n, BUCKET_RATIO: BUCKET_RATIO, SPLIT_RATIO: SPLIT_RATIO)
    return sms

proc get_all(sms: Sortedset): seq[int] =
    result = newSeqOfCap[int](sms.size)
    for i in sms.a:
        for j in i:
            result.add(j)
    return result

proc get_all_reversed(sms: Sortedset): seq[int] =
    result = newSeqOfCap[int](sms.size)
    for i in sms.a.reversed:
        for j in i.reversed:
            result.add(j)
    return result


proc position(sms: Sortedset, x: int): (int, int) =
    var
        i_rslt: int
    for i, a in sms.a:
        i_rslt = i
        if x <= a[^1]:
            break


    return (i_rslt, lowerBound(sms.a[i_rslt], x))

proc contains(sms: Sortedset, x: int): bool =
    if sms.size == 0:
        return false
    var (b, i) = position(sms, x)
    return i != len(sms.a[b]) and sms.a[b][i] == x


iterator itr(sms: Sortedset): (int, int) =
    var
        a = sms.a
        idx = 0
    for i in a:
        for j in i:
            yield (idx, j)
            idx += 1


proc add(sms: Sortedset, x: int) =
    if sms.size == 0:
        sms.a = @[@[x]]
        sms.size = 1
        return
    var (b, i) = position(sms, x)
    if i != sms.a[b].len() and sms.a[b][i] == x:
        return

    sms.a[b].insert(x, i)
    sms.size += 1
    if len(sms.a[b]) > sms.a.len * sms.SPLIT_RATIO:
        var mid = sms.a[b].len >> 1
        sms.a[b..<b+1] = [sms.a[b][0..<mid], sms.a[b][mid..^1]]

proc pop(sms: Sortedset, b: int, i: int) =
    sms.a[b].delete(i)
    sms.size -= 1
    if sms.a[b].len() == 0:
        sms.a.delete(b)

proc remove(sms: Sortedset, x: int): bool =
    if sms.size == 0:
        return false
    var (b, i) = sms.position(x)
    if i == sms.a[b].len() or sms.a[b][i] != x:
        return false
    sms.pop(b, i)
    return true

proc lt(sms: Sortedset, x: int): int =
    for a in sms.a.reversed:
        if a[0] < x:
            return a[lowerBound(a, x)-1]
    return -(10**9+7)

proc le(sms: Sortedset, x: int): int =
    for a in sms.a.reversed:
        if a[0] <= x:
            return a[upperBound(a, x)-1]
    return -(10**9+7)

proc gt(sms: Sortedset, x: int): int =
    for a in sms.a:
        if a[^1] > x:
            return a[upperBound(a, x)]
    return -(10**9+7)

proc ge(sms: Sortedset, x: int): int =
    for a in sms.a:
        if a[^1] >= x:
            return a[lowerBound(a, x)]
    return -(10**9+7)

proc get(sms: Sortedset, i: int): int =
    var idx = i
    if idx < 0:
        for a in sms.a.reversed:
            idx += a.len()
            if idx >= 0:
                return a[idx]
    else:
        for a in sms.a:
            if idx < a.len():
                return a[idx]
            idx -= a.len()
    return -1

proc indx(sms: Sortedset, x: int): int =
    var ans = 0
    for a in sms.a:
        if a[^1] >= x:
            return ans + lowerBound(a, x)
        ans += a.len()
    return ans

proc indx_right(sms: Sortedset, x: int): int =
    var ans = 0
    for a in sms.a:
        if a[^1] > x:
            return ans + upperBound(a, x)
        ans += a.len()
    return ans





var
    tmp = @[0, 1, 2, 3, 4, 5]
    sms = newSortedset(tmp)
echo sms.a
for _ in range(10):
    var num = rand(10)
    echo ("add", num)
    sms.add(num)
    echo sms.a

for _ in range(10):
    var num = rand(10)
    echo ("discard", num)
    discard sms.remove(num)
    echo sms.a

for _ in range(10):
    var num = rand(10)
    echo (num, sms.lt(num), sms.le(num), sms.gt(num), sms.ge(num))

for _ in range(10):
    var num = rand(10)
    echo (num, sms.get(num))

for _ in range(10):
    var num = rand(10)
    echo (num, sms.contains(num))
echo sms.a
for idx, i in itr(sms):
    echo (idx, i)


