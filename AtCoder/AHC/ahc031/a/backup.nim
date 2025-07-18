import atcoder/segtree
import std/times
import std/random
import macros

macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"

var false_num = -(10**9+7)
type
    SortedMultiset = ref object
        a: seq[seq[int]]
        size: int
        BUCKET_RATIO: int
        SPLIT_RATIO: int

proc newSortedMultiset(ini: seq[int]): SortedMultiset =
    var
        #ソート済みのみ追加可能
        # ini_sorted = ini.sorted()
        BUCKET_RATIO: int = 16
        SPLIT_RATIO: int = 24
        n = ini.len()
        num_bucekt = int(ceil(sqrt(n/BUCKET_RATIO)))
        a = newSeqOfCap[newSeqOfCap[int](20)](20)
    for i in 0..<num_bucekt:
        # a.add(ini_sorted[n*i//num_bucekt..<n*(i+1)//num_bucekt])
        a.add(ini[n*i//num_bucekt..<n*(i+1)//num_bucekt])
    var sms = SortedMultiset(a: a, size: n, BUCKET_RATIO: BUCKET_RATIO, SPLIT_RATIO: SPLIT_RATIO)
    return sms

proc get_all(sms: SortedMultiset): seq[int] =
    result = newSeqOfCap[int](sms.size)
    for i in sms.a:
        for j in i:
            result.add(j)
    return result

proc get_all_reversed(sms: SortedMultiset): seq[int] =
    result = newSeqOfCap[int](sms.size)
    for i in sms.a.reversed:
        for j in i.reversed:
            result.add(j)
    return result

proc position(sms: SortedMultiset, x: int): (int, int) =
    var
        i_rslt: int
    for i, a in sms.a:
        i_rslt = i
        if x <= a[^1]:
            break


    return (i_rslt, lowerBound(sms.a[i_rslt], x))

proc contains(sms: SortedMultiset, x: int): bool =
    if sms.size == 0:
        return false
    var (b, i) = position(sms, x)
    return i != len(sms.a[b]) and sms.a[b][i] == x


iterator itr(sms: SortedMultiset): (int, int) =
    var
        a = sms.a
        idx = 0
    for i in a:
        for j in i:
            yield (idx, j)
            idx += 1


proc add(sms: SortedMultiset, x: int) =
    if sms.size == 0:
        sms.a = @[@[x]]
        sms.size = 1
        return
    var (b, i) = position(sms, x)
    sms.a[b].insert(x, i)
    sms.size += 1
    if len(sms.a[b]) > sms.a.len * sms.SPLIT_RATIO:
        var mid = sms.a[b].len >> 1
        sms.a[b..<b+1] = [sms.a[b][0..<mid], sms.a[b][mid..^1]]

proc pop(sms: SortedMultiset, b: int, i: int) =
    sms.a[b].delete(i)
    sms.size -= 1
    if sms.a[b].len() == 0:
        sms.a.delete(b)

proc remove(sms: SortedMultiset, x: int): bool =
    if sms.size == 0:
        return false
    var (b, i) = sms.position(x)
    if i == sms.a[b].len() or sms.a[b][i] != x:
        return false
    sms.pop(b, i)
    return true

proc lt(sms: SortedMultiset, x: int): int =
    for a in sms.a.reversed:
        if a[0] < x:
            return a[lowerBound(a, x)-1]
    return false_num

proc le(sms: SortedMultiset, x: int): int =
    for a in sms.a.reversed:
        if a[0] <= x:
            return a[upperBound(a, x)-1]
    return false_num

proc gt(sms: SortedMultiset, x: int): int =
    for a in sms.a:
        if a[^1] > x:
            return a[upperBound(a, x)]
    return false_num

proc ge(sms: SortedMultiset, x: int): int =
    for a in sms.a:
        if a[^1] >= x:
            return a[lowerBound(a, x)]
    return false_num

proc get(sms: SortedMultiset, i: int): int =
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
    return false_num

proc indx(sms: SortedMultiset, x: int): int =
    var ans = 0
    for a in sms.a:
        if a[^1] >= x:
            return ans + lowerBound(a, x)
        ans += a.len()
    return ans

proc indx_right(sms: SortedMultiset, x: int): int =
    var ans = 0
    for a in sms.a:
        if a[^1] > x:
            return ans + upperBound(a, x)
        ans += a.len()
    return ans

type
    Sortedset = ref object
        a: seq[seq[int]]
        size: int
        BUCKET_RATIO: int
        SPLIT_RATIO: int

proc newSortedset(ini: seq[int]): Sortedset =
    var
        # ini_sorted = ini.sorted().deduplicate(true)
        ini_sorted = ini.deduplicate(true)
        BUCKET_RATIO: int = 16
        SPLIT_RATIO: int = 24
        n = ini_sorted.len()
        num_bucekt = int(ceil(sqrt(n/BUCKET_RATIO)))
        a = newSeqOfCap[newSeqOfCap[int](20)](20)
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
    return false_num

proc le(sms: Sortedset, x: int): int =
    for a in sms.a.reversed:
        if a[0] <= x:
            return a[upperBound(a, x)-1]
    return false_num

proc gt(sms: Sortedset, x: int): int =
    for a in sms.a:
        if a[^1] > x:
            return a[upperBound(a, x)]
    return false_num

proc ge(sms: Sortedset, x: int): int =
    for a in sms.a:
        if a[^1] >= x:
            return a[lowerBound(a, x)]
    return false_num

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

proc input(): (int, int, int, seq[seq[int]], int)
proc put(a: seq[int], h: seq[int], hight: seq[int]): (seq[seq[int]], int, bool)
proc get_line(N: int, D: int, A: seq[seq[int]], h: seq[int], height: seq[int]): (seq[seq[seq[int]]], int, seq[int])
proc most_rihgt_line_change(line: var seq[seq[seq[int]]])
proc yamanobori(N: int, D: int, A: seq[seq[int]], h: var seq[int], time_limit: float): (seq[seq[seq[int]]], int, seq[int], seq[int], seq[int])
proc get_h(D: int, N: int, A: seq[seq[int]], ): (seq[seq[seq[int]]], seq[seq[seq[int]]], seq[int], seq[int], seq[int], seq[int])
proc is_OK_gr2(same, a, h, height: seq[int]): (bool, seq[seq[int]])
proc greedy2(D, N: int, A: seq[seq[int]], h, height: seq[int], line: seq[seq[seq[int]]], over: seq[int], A_tenti: seq[seq[int]]): (array[2, int], array[2, seq[
        seq[seq[int]]]])
proc is_OK(same: seq[int], other: seq[int], h, height: seq[int]): (bool, seq[seq[int]])
proc greedy1(D, N: int, A: seq[seq[int]], h, height, : seq[int], line: seq[seq[seq[int]]], over: seq[int]): (array[2, int], array[2, seq[seq[seq[int]]]])
proc output(ans: seq[seq[array[4, int]]])
proc get_line_ans_S_from_ans(D, N: int, ans: seq[seq[array[4, int]]], h, height: seq[int]): (seq[seq[Sortedset]], seq[SortedMultiset])
proc yamanobori2(D, N: int, ans: seq[seq[array[4, int]]], line: var seq[seq[Sortedset]], over, h, : seq[int], surf: seq[SortedMultiset], A: seq[seq[int]])
proc get_ans_from_line(D, N: int, line: seq[seq[seq[int]]], height, over: seq[int], line_ins: seq[seq[seq[int]]], over_ins: seq[int]): seq[seq[array[4, int]]]

import nimprof
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#ここまでライブラリ、関数宣言
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
let start = cpuTime()
    #乱数リセット
    # randomize()

var
    (W, D, N, A, avr_amari) = input()
    (line, line_ins, h, height, over, over_ins) = get_h(D, N, A)
    A_tenti = newSeqWith(N, newseq[int](D))

quit()
for i in 0..<D:
    for j in 0..<N:
        A_tenti[j][i] = A[i][j]

# echo (h.len(), over)
# echo line

var
    (more_good1, rslt1) = greedy1(D, N, A, h, height, line, over)
    (more_good2, rslt2) = greedy2(D, N, A, h, height, line, over, A_tenti)



if max(more_good1) <= max(more_good2):
    if more_good2[0] <= more_good2[1]:
        line = rslt2[1]
    else:
        line = rslt2[0]
else:
    if more_good1[0] <= more_good1[1]:
        line = rslt1[1]
    else:
        line = rslt1[0]


#あえてこれを後でやるとか
most_rihgt_line_change(line)


var ans = get_ans_from_line(D, N, line, height, over, line_ins, over_ins)
echo cpuTime() - start
output(ans)



proc input(): (int, int, int, seq[seq[int]], int) =
    let
        W = ii()
        D = ii()
        N = ii()
    var
        A = newSeqOfCap[newSeq[int](N)](D)
        avr_amari = 0

    for i in 0 ..< D:
        A.add(lii(N))

    for i in A:
        avr_amari += 1000000 - sum(i)
    avr_amari = int(avr_amari / D / 10000)

    return (W, D, N, A, avr_amari)

proc put(a: seq[int], h: seq[int], hight: seq[int]): (seq[seq[int]], int, bool) =
    var
        is_over = false
        line = newSeq[newSeqOfCap[int](3*a.len()//h.len())](h.len())
        # rslt = newSeqOfCap[array[4, int]](a.len())
        cost = 0
    for i in 0..<h.len():
        line[i].add(0)
    type Tmp = (int, int)
    var tmp: Tmp
    for i in a.reversed():
        var
            puted = false
            aspect_min = 1000000000.0
        for j in 0..<h.len:
            var width = -(-i // h[j])
            if line[j][^1] + width <= 1000:
                puted = true
                var aspect = max(width, h[j]) / min(width, h[j])
                if aspect_min > aspect:
                    aspect_min = aspect
                    tmp = (j, width)

        if puted:
            var (j, width) = tmp
            line[j].add(line[j][^1]+width)
            cost += h[j]
        else:
            is_over = true
            var s = 0
            tmp = (-1, -1)
            for j in 0..<h.len():
                var width = min(1000 - line[j][^1], -(-i // h[j]))
                if width * i > s:
                    s = width * i
                    tmp = (j, width)
            if tmp == (-1, -1):
                var idx = 0
                while line[idx][1] - line[idx][0] < 2:
                    idx += 1

                for j in 1..<line[idx].len():
                    line[idx][j] -= 1

                cost += 1000 * i

                line[idx].add(1000)

                # var rs = rslt[^minus_idx]
                # (rs[1], rs[3]) = (rs[3], 1000)
                # rslt.add(rs)
            else:
                var (idx, width) = tmp
                cost += 1000 * (i-width*h[idx])
                cost += h[idx]
                line[idx].add(1000)
                # w[idx] = 1000
                # rslt.add(rs)

    cost -= 1000
    for i in 0..<h.len()-1:
        if line[i].len() == 0 and line[i+1].len() == 0:
            cost += 1000

    return (line, cost, is_over)

proc get_line(N: int, D: int, A: seq[seq[int]], h: seq[int], height: seq[int]): (seq[seq[seq[int]]], int, seq[int]) =
    var
        line = newSeqofcap[newSeq[newSeq[int](3*N//h.len())](N)](D)
        cost_sum = 0
        over = newSeqOfCap[int](N)

    for idx, i in A:
        var (rslt, cost, is_over) = put(i, h, height)
        line.add(rslt)
        cost_sum += cost
        if is_over:
            over.add(idx)

    return (line, cost_sum, over)

proc most_rihgt_line_change(line: var seq[seq[seq[int]]]) =
    for i in 0..<line.len():
        for j in 0..<line[i].len():
            if line[i][j][^1] == 0:
                line[i][j].add(1000)
            else:
                line[i][j][^1] = 1000




proc yamanobori(N: int, D: int, A: seq[seq[int]], h: var seq[int], time_limit: float): (seq[seq[seq[int]]], int,
        seq[int], seq[int], seq[int]) =
    var
        cnt = 0
        height = newSeq[int](h.len()+1)

    for i, j in h:
        height[i+1] = height[i] + j

    var (line, cost, over) = get_line(N, D, A, h, height)

    if h.len() == 1:
        return (line, cost, over, h, height)


    cost = 10**18
    var
        bunsan = 10**18
        avr = 1000 // len(h)
        tmp_time = cpuTime()
        no_over_got = false
    while true:
        var give_idx, take_idx = rand(0..<h.len())
        if give_idx == take_idx:
            continue

        var
            h_n = h
            num = rand(h[give_idx]//4)
        h_n[give_idx] -= num
        h_n[take_idx] += num

        var height_n = newSeq[int](h.len()+1)
        for i, j in h_n:
            height_n[i+1] = height_n[i] + j

        var (line_n, cost_n, over_n) = get_line(N, D, A, h_n, height_n)

        if over_n.len() == 0:
            no_over_got = true


        if cost_n < cost:
            if no_over_got:
                var bunsan_n = 0
                for i in h_n:
                    bunsan_n += (i-avr)**2
                if bunsan > bunsan_n:
                    # echo (h.len(), cpuTime() - start, cnt, )
                    bunsan = bunsan_n
                    h = h_n
                    height = height_n
                    cost = cost_n
                    line = line_n
                    over = over_n
            else:
                h = h_n
                height = height_n
                cost = cost_n
                line = line_n
                over = over_n

        cnt += 1
        if cnt % 100 == 0:

            if cpuTime() - tmp_time > time_limit:
                echo cnt
                return (line, cost, over, h, height)



proc get_h(D: int, N: int, A: seq[seq[int]], ): (seq[seq[seq[int]]], seq[seq[seq[int]]], seq[int], seq[int], seq[int], seq[int]) =
    var
        h = @[1000]
        (line_ins, _, over_ins, _, _) = yamanobori(N, D, A, h, 0)
        l = int(sqrt(float32(N)))-1
        r = -(-N//2)+1

    var
        rs_line: seq[seq[seq[int]]]
        rs_cost = 10**18
        rs_over: seq[int]
        rs_h: seq[int]
        rs_height: seq[int]

    while r - l > 1:
        var
            h_num = (l+r)//2
            w_num = -(-N / h_num)
            avr = newSeq[float](h_num)
        for i in A:
            for j in 0..<N:
                avr[int(j / w_num)] += float(i[j])

        h = newSeqOfCap[int](h_num)
        for idx, i in avr:
            avr[idx] = pow(float(i), 0.25)

        var avr_sum = sum(avr)
        for i in avr[0 ..< ^1]:
            h.add(int(1000*i/avr_sum))
        h.add(1000-sum(h))

        var (line_n, cost_n, over_n, h_n, height_n) = yamanobori(N, D, A, h, 0.4)
        echo (h.len(), cost_n, over_n.len())
        if len(over_n) > 0:
            r = h_num
        else:
            l = h_num

        if rs_cost > cost_n:
            rs_line = line_n
            rs_cost = cost_n
            rs_over = over_n
            rs_h = h_n
            rs_height = height_n

    (rs_line, rs_cost, rs_over, rs_h, rs_height) = yamanobori(N, D, A, rs_h, 0.3)

    # for i in rs_over:
    #     if i notin over_ins:
    #         rs_ans[i] = ans_ins[i]

    return (rs_line, line_ins, rs_h, rs_height, rs_over, over_ins)


proc is_OK_gr2(same, a, h, height: seq[int]): (bool, seq[seq[int]]) =
    var
        OK = true
        line = newseq[newSeqOfcap[int](3*a.len()//h.len())](h.len())
        a_rev = a.reversed()
        i: int
    for i in 0..<h.len():
        line[i].add(0)

    for idx in 0..<a.len():
        if idx < len(same):
            i = same[idx]
        else:
            i = a_rev[idx]

        var
            aspect_min = 100000000.0
            puted = false
            tmp = (0, 0)

        for j in 0..<h.len():
            var width = -(-i // h[j])
            if line[j][^1] + width <= 1000:
                puted = true
                var aspect = max(width, h[j]) / min(width, h[j])
                if aspect_min > aspect:
                    aspect_min = aspect
                    tmp = (j, width)

        if puted:
            var (j, width) = tmp
            line[j].add(line[j][^1]+width)
        else:
            return (false, line)

    # rslt.reverse()
    return (true, line)

proc greedy2(D, N: int, A: seq[seq[int]], h, height: seq[int], line: seq[seq[seq[int]]], over: seq[int], A_tenti: seq[seq[int]]): (array[2, int], array[2,
        seq[seq[seq[int]]]]) =
    if len(over) > 0:
        return ([-1, -1], [@[@[@[]]], @[@[@[]]]])

    type
        st_type = SegTreeType[int]((a: int, b: int)=>max(a, b), () => -1)
    var
        sts = newseq[st_type](N)
        more_good = [0, 0]
        rslt = [line, line]

    for i in range(A_tenti.len()):
        var v = A_tenti[i]
        sts[i] = st_type.init(v)

    for mode in [1, -1]:
        var Idx_l, Idx_r: int
        if mode == 1:
            Idx_l = 0
            Idx_r = 2
        else:
            Idx_l = D-2
            Idx_r = D

        var
            prv_same = newSeqOfCap[int](N)

        while true:
            var
                same = newSeqOfCap[int](N)
                idx = N-1
            while idx >= 0:
                same.add(sts[idx].prod(Idx_l..<Idx_r))
                var
                    tmp = newSeqofCap[(bool, seq[seq[int]])](N)
                    is_OK = true
                for i in Idx_l..<Idx_r:
                    var (ok, rs) = is_OK_gr2(same, A[i], h, height)
                    is_OK = is_OK and ok
                    if not is_OK:
                        break
                if is_OK:
                    idx -= 1
                else:
                    discard same.pop()
                    break

            if same.len() > N / 2:
                prv_same = same
                if mode == 1:
                    Idx_r += 1
                else:
                    Idx_l -= 1

                if Idx_r > D or Idx_l < 0:
                    if mode == 1:
                        more_good[0] += (Idx_r - Idx_l - 2) * prv_same.len()
                    else:
                        more_good[1] += (Idx_r - Idx_l - 2) * prv_same.len()

                    if mode == 1:
                        for i in Idx_l..<Idx_r-1:
                            var(ok, rs) = is_OK_gr2(prv_same, A[i], h, height)
                            rslt[0][i] = rs
                    else:
                        for i in Idx_l+1..<Idx_r:
                            var(ok, rs) = is_OK_gr2(prv_same, A[i], h, height)
                            rslt[1][i] = rs
                    break


            else:
                if mode == 1:
                    more_good[0] += (Idx_r - Idx_l - 2) * prv_same.len()
                    for i in Idx_l..<Idx_r-1:
                        var(ok, rs) = is_OK_gr2(prv_same, A[i], h, height)
                        rslt[0][i] = rs
                else:
                    more_good[1] += (Idx_r - Idx_l - 2) * prv_same.len()
                    for i in Idx_l+1..<Idx_r:
                        var(ok, rs) = is_OK_gr2(prv_same, A[i], h, height)
                        rslt[1][i] = rs

                prv_same = @[]
                if mode == 1:
                    Idx_l = Idx_r - 1
                    Idx_r = Idx_l + 2
                else:
                    Idx_r = Idx_l
                    Idx_l = Idx_r - 2

                if Idx_r > D or Idx_l < 0:
                    break
    return (more_good, rslt)

proc is_OK(same: seq[int], other: seq[int], h, height: seq[int]): (bool, seq[seq[int]]) =
    var
        is_over = false
        line = newSeq[newSeqOfCap[int]((same.len()+other.len())*3//h.len())](h.len())
    for i in 0..<h.len():
        line[i].add(0)

    for i in same:
        var
            aspect_min = 10000000.0
            puted = false
            tmp: (int, int)
        for j in 0..<h.len():
            var width = -(-i // h[j])
            if line[j][^1] + width <= 1000:
                puted = true
                var aspect = max(width, h[j]) / min(width, h[j])
                if aspect_min > aspect:
                    aspect_min = aspect
                    tmp = (j, width)
        if puted:
            var (j, width) = tmp
            line[j].add(line[j][^1]+width)
        else:
            return (false, line)

    for i in other:
        var
            aspect_min = 10000000.0
            puted = false
            tmp: (int, int)
        for j in 0..<h.len():
            var width = -(-i // h[j])
            if line[j][^1] + width <= 1000:
                puted = true
                var aspect = max(width, h[j]) / min(width, h[j])
                if aspect_min > aspect:
                    aspect_min = aspect
                    tmp = (j, width)
        if puted:
            var (j, width) = tmp
            line[j].add(line[j][^1]+width)
        else:
            return (false, line)


    return (true, line)

proc greedy1(D, N: int, A: seq[seq[int]], h, height, : seq[int], line: seq[seq[seq[int]]], over: seq[int]): (array[2, int], array[2, seq[seq[seq[int]]]]) =
    var
        more_good = [0, 0]
        rslt = [line, line]

    for mode in [0, 1]:
        for i in countup(mode, D-2, 2):
            if i in over or i+1 in over:
                continue
            var
                rslt_a = newSeq[newSeq[int](3*N//h.len())](h.len())
                rslt_b = newSeq[newSeq[int](3*N//h.len())](h.len())
                a = A[i]
                b = A[i+1]
                a_sms = newSortedMultiset(a)
                b_sms = newSortedMultiset(b)
                same = newSeqOfCap[int](a.len())

            while true:
                var diff = newSeqOfCap[(int, int, int)](a.len())
                for idx, j in itr(a_sms):
                    var
                        l = b_sms.le(j)
                        r = b_sms.ge(j)
                        diff_l, diff_r: int

                    if l == false_num:
                        diff_l = 10**8
                    else:
                        diff_l = abs(j-l)

                    if r == false_num:
                        diff_r = 10**8
                    else:
                        diff_r = abs(j-r)

                    if diff_l > diff_r:
                        diff.add((diff_r, j, r))
                    else:
                        diff.add((diff_l, j, l))

                var
                    min_num = 10**8
                    num, j, k, j_idx, k_idx: int
                for di in diff:
                    if di[0] < min_num:
                        (num, j, k) = di
                        min_num = num

                same.add(max(j, k))
                discard a_sms.remove(j)
                discard b_sms.remove(k)

                var
                    a_other = a_sms.get_all_reversed()
                    b_other = b_sms.get_all_reversed()
                    (ok_a, rslt_a_n) = is_OK(same, a_other, h, height)
                    (ok_b, rslt_b_n) = is_OK(same, b_other, h, height)

                if ok_a and ok_b:
                    rslt_a = rslt_a_n
                    rslt_b = rslt_b_n
                else:
                    more_good[mode] += same.len()-1
                    if rslt_a.len() > 0 and rslt_b.len() > 0:
                        rslt[mode][i] = rslt_a
                        rslt[mode][i+1] = rslt_b
                    break

                if a_sms.size == 0:
                    more_good[mode] += same.len() - 1
                    if all(rslt_a, proc (x: seq[int]): bool = x.len > 0) and all(rslt_b, proc (x: seq[int]): bool = x.len > 0):
                        rslt[mode][i] = rslt_a
                        rslt[mode][i+1] = rslt_b
                    break
    return (more_good, rslt)




proc output(ans: seq[seq[array[4, int]]]) =
    for i in ans:
        for j in i:
            echo j.join(" ")

proc get_ans_from_line(D, N: int, line: seq[seq[seq[int]]], height, over: seq[int], line_ins: seq[seq[seq[int]]], over_ins: seq[int]): seq[seq[array[4, int]]] =
    var ans = newSeq[newSeq[array[4, int]](N)](D)
    for i, j in line:
        if i in over and i notin over_ins:
            for k, l in line_ins[i]:
                for m in 1..<l.len():
                    ans[i].add([0, l[m - 1], 1000, l[m]])
        else:
            for k, l in j:
                for m in 1..<l.len():
                    ans[i].add([height[k], l[m - 1], height[k + 1], l[m]])

    for i in 0..<D:
        ans[i].sort(proc(x, y: array[4, int]): int = cmp(-(x[3] - x[1]) * (x[2] - x[0]), -(y[3] - y[1]) * (y[2] - y[0])))
        while ans[i].len() > N:
            discard ans[i].pop()
        ans[i].sort(proc(x, y: array[4, int]): int = cmp((x[3] - x[1]) * (x[2] - x[0]), (y[3] - y[1]) * (y[2] - y[0])))

    return ans


proc get_line_ans_S_from_ans(D, N: int, ans: seq[seq[array[4, int]]], h, height: seq[int]): (seq[seq[Sortedset]], seq[SortedMultiset]) =
    var
        line = newSeq[newSeq[Sortedset](h.len())](D)
        surf = newSeq[SortedMultiset](D)
        table = newTable[int, int]()
    for i, j in height:
        table[j] = i
    for i in 0..<D:
        surf[i] = newSortedMultiset(@[])
        for j in 0..<h.len():
            line[i][j] = newSortedset(@[])

    for idx, i in ans:
        for k in i:
            var s = (k[2] - k[0]) * (k[3] - k[1])
            surf[idx].add(-s)
            line[idx][table[k[0]]].add(k[3])

    for i in 0..<D:
        for j in 0..<h.len():
            if line[i][j].size == 1:
                line[i][j].add(1000)
                var s = 1000 * (h[j])
                surf[i].add(-s)

    return (line, surf)



proc yamanobori2(D, N: int, ans: seq[seq[array[4, int]]], line: var seq[seq[Sortedset]], over, h, : seq[int], surf: seq[SortedMultiset], A: seq[seq[int]]) =
    var
        cnt = 0
        len_h = h.len()
        A_minus = newSeq[newSeq[int](N)](D)
        Timeover = 2.9
        mode_array = [0, 0, 0, 1, 2, 3, 4, 4, 6]

    for i in 0..<D:
        for j in 0..<N:
            A_minus[i][j] = -A[i][j]

    for i in 0..D:
        A_minus[i].sort()
    var
        idx1, idx2, rev: int
    while true:
        cnt += 1
        if cnt % 100 == 0:
            if cpuTime() - start > Timeover:
                break


        idx1 = rand(D-1)
        idx2 = rand(len_h-1)
        rev = sample([1, -1])

        if not (0 <= idx1 - rev and idx1 - rev < D) or idx1 in over or idx1 - rev in over:
            continue

        var mode = sample(mode_array)


    proc mode_6() =
        if line[idx1][idx2].size == 2:
            return

        var score_diff = 0
        for idx, i in itr(line[idx1][idx2]):
            if 0 < i and i < 1000:
                if 0 <= idx1 - 1 and idx1 - 1 < D:
                    if line[idx1-1][idx2].contains(i):
                        score_diff -= 1
                    if line[idx1-1][idx2].contains(1000-i):
                        score_diff += 1
                if 0 <= idx1 + 1 and idx1 + 1 < D:
                    if line[idx1+1][idx2].contains(i):
                        score_diff -= 1
                    if line[idx1+1][idx2].contains(1000-i):
                        score_diff += 1
        if score_diff < 0:
            return
        var rslt = newSeq[int](line[idx1][idx2].size)
        for i, j in itr(line[idx1][idx2]):
            rslt[^(i+1)] = 1000 - j
        line[idx1][idx2] = newSortedset(rslt)
        return

    # proc mode_5() =
    #     var idx3: int
    #     while true:
    #         idx3 = rand(len_h-1)
    #         if idx2 != idx3:
    #             break

    #     if line[idx1][idx2].size == 2 and line[idx1][idx3].size == 2:
    #         return

    proc mode_4() =
        if line[idx1][idx2].size == 2:
            return
        var
            idx3 = rand(1..<line[idx1][idx2].size-1)
            m = line[idx1][idx2].get(idx3)
            l = line[idx1][idx2].lt(m)
            r = line[idx1][idx2].gt(m)
            idx4: int

        while true:
            idx4 = rand(len_h-1)
            if idx2 != idx4:
                break
        var
            flag1, flag2 = false
        if 0 <= idx1 - 1 and idx1 - 1 < D:
            if line[idx1-1][idx2].contains(m):
                flag1 = true
        if 0 <= idx1 + 1 and idx1 + 1 < D:
            if line[idx1+1][idx2].contains(m):
                flag2 = true

        if flag1 and flag2:
            return

        for _, i in itr(line[idx1-rev][idx4]):
            if 1 <= i and i < 1000 and not line[idx1][idx4].contains(i):
                var
                    prv_l_1 = h[idx2] * (m - l)
                    prv_r_1 = h[idx2] * (r - m)
                    nxt_lr_1 = h[idx2] * (r - l)

                    l_2 = line[idx1][idx4].le(i)
                    r_2 = line[idx1][idx4].ge(i)

                    prv_lr_2 = h[idx4] * (r_2 - l_2)
                    nxt_l_2 = h[idx4] * (i - l_2)
                    nxt_r_2 = h[idx4] * (r_2 - i)

                # 一旦面積情報の書き換え
                discard surf[idx1].remove(-prv_l_1)
                discard surf[idx1].remove(-prv_r_1)
                discard surf[idx1].remove(-prv_lr_2)
                surf[idx1].add(-nxt_lr_1)
                surf[idx1].add(-nxt_l_2)
                surf[idx1].add(-nxt_r_2)

                var flag = true
                for idx, j in itr(surf[idx1]):
                    if j <= A_minus[idx1][idx]:
                        discard
                    else:
                        flag = false
                        break
                if flag:
                    discard line[idx1][idx2].remove(m)
                    line[idx1][idx4].add(i)
                    return
                else:
                    surf[idx1].add(-prv_l_1)
                    surf[idx1].add(-prv_r_1)
                    surf[idx1].add(-prv_lr_2)
                    discard surf[idx1].remove(-nxt_lr_1)
                    discard surf[idx1].remove(-nxt_l_2)
                    discard surf[idx1].remove(-nxt_r_2)






































