import macros
macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"

var
    n = ii()
    ab = newSeqOfCap[(int, int)](n)
    time = newSeqOfCap[float](n)
    acc_time = newSeqOfCap[float](n+1)
    acc_len = newSeqOfCap[int](n+1)

acc_time.add(0.0)
acc_len.add(0)

for i in range(n):
    var a, b = ii()
    ab.add((a, b))
    time.add(a/b)

    acc_len.add(acc_len[^1]+a)
    acc_time.add(acc_time[^1] + a/b)

var
    half_time = sum(time) / 2
for idx, i in acc_time:
    if half_time < i:
        echo acc_len[idx-1] + ab[idx-1][1] * (half_time - acc_time[idx-1])
        quit()






# var ab_rev = ab.reversed()

# # echo acc_time
# # echo ab_time
# # echo acc_len


# for idx, (a, b) in ab:
#     var
#         t = acc_time[idx]
#         r_idx: int
#     # echo t
#     for i in countdown(n-1, 0, 1):
#         if t - ab_time[i] > 0:
#             t -= ab_time[i]
#         else:
#             r_idx = i
#             break

#     # echo (idx, r_idx)
#     if r_idx <= idx:
#         var t_r: float
#         for i in countdown(n-1, idx+1, 1):
#             t_r += ab_time[i]
#         if acc_time[idx-1] <= t_r:
#             var
#                 ans = 0.0
#                 l = float(acc_len[idx-1])
#                 add = b * (t_r - acc_time[idx-1])
#                 half = (a-add)/2
#             # echo (l, add, half)
#             ans = l + add + half
#             echo ans
#             quit()

#         else:
#             var
#                 ans = 0.0
#                 l = float(acc_len[idx-1])
#                 dl = b * (acc_time[idx-1] - t_r)
#                 half = (a-dl)/2
#             # echo (l, half)
#             ans = l + half
#             echo ans
#             quit()













# for idx, (a, b) in ab:
#     if idx == 0:
#         time[idx][0] = a/b
#     else:
#         time[idx][0] = time[idx-1][0] + a/b

# for idx, (a, b) in ab_rev:
#     if idx == 0:
#         time[^(idx+1)][1] = a/b
#     else:
#         time[^(idx+1)][1] = time[^idx][1] + a/b

# time = @[(0.0, 0.0)] & time & @[(0.0, 0.0)]
# echo time
# for idx, (l, r) in time:
#     if l > r:
#         if time[idx-1][0] > time[idx+1][1]:
#             var tmp = ab[idx-1][1] * abs(time[idx-1][0] - time[idx+1][1])
#             tmp = ab[idx-1][0] - tmp
#             echo acc_len[idx-2] + tmp / 2
#         else:
#             var tmp = ab[idx-1][1] * abs(time[idx-1][0] - time[idx+1][1])
#             # tmp = ab[idx-1][0] - tmp
#             echo acc_len[idx-2] + tmp + (ab[idx-1][0] - tmp)/2











