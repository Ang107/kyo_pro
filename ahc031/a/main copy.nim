import atcoder/segtree
import std/times
import std/random
import macros

macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"

var false_num = -(10**9+7)
type
    SortedMultiset* = ref object
        a: seq[seq[int]]
        size*: int
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
    Sortedset* = ref object
        a: seq[seq[int]]
        size*: int
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


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#ここまでライブラリ
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
let start = cpuTime()
    #乱数リセット
    # randomize()

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

proc put(a: seq[int], h: seq[int], hight: seq[int]): (seq[array[4, int]], int, bool) =
    var
        is_over = false
        w = newSeq[int](h.len())
        rslt = newSeqOfCap[array[4, int]](a.len())
        cost = 0
    type Tmp = (int, int, array[4, int])
    var tmp: Tmp
    for i in a:
        var
            puted = false
            aspect_min = 1000000000
        for j in 0..<h.len:
            var
                width = i div h[j]
                mo = i mod h[j]
            if mo != 0:
                width += 1
            if w[j] + width <= 1000:
                puted = true
                var aspect = max(width, h[j]) div min(width, h[j])
                if aspect_min > aspect:
                    aspect_min = aspect
                    tmp = (j, width, [hight[j], w[j], hight[j + 1], w[j] + width])

        if puted:
            var (j, width, rs) = tmp
            w[j] += width
            cost += h[j]
            rslt.add(rs)
        else:
            is_over = true
            var s = 0
            tmp = (-1, -1, [-1, -1, -1, -1])
            for j in 0..<h.len():
                var
                    width = i div h[j]
                    mo = i mod h[j]
                if mo != 0:
                    width += 1
                width = min(width, 1000-w[j])

                if width * i > s:
                    s = width * i
                    tmp = (j, width, [hight[j], w[j], hight[j + 1], min(1000, w[j] + width)])

            if tmp == (-1, -1, [-1, -1, -1, -1]):
                var minus_idx = 1
                while rslt[^minus_idx][3] - rslt[^minus_idx][1] < 2:
                    minus_idx += 1

                rslt[^minus_idx][3] = rslt[^minus_idx][1] + 1
                cost += 1000 * (i-(1000 - rslt[^minus_idx][3])) * (rslt[
                        ^minus_idx][2] - rslt[^minus_idx][0])

                cost += 1000 * ((1000 - rslt[^minus_idx][3])) * (rslt[^minus_idx][2] - rslt[^minus_idx][0])

                var rs = rslt[^minus_idx]
                (rs[1], rs[3]) = (rs[3], 1000)
                rslt.add(rs)
            else:
                var (idx, width, rs) = tmp
                cost += 1000 * (i-width*h[idx])
                cost += h[idx]
                w[idx] = 1000
                rslt.add(rs)

    cost -= 1000
    for i in 0..<w.len()-1:
        if w[i] == 0 and w[i+1] == 0:
            cost += 1000

    # rslt.reverse()
    return (rslt, cost, is_over)

proc get_ans(N: int, D: int, A: seq[seq[int]], h: seq[int], height: seq[int]): (seq[seq[array[4, int]]], int, seq[int]) =
    var
        ans = newSeqofcap[newSeqOfCap[array[4, int]](N)](D)
        cost_sum = 0
        over = newSeqOfCap[int](N)

    for idx, i in A:
        var (rslt, cost, is_over) = put(i, h, height)
        ans.add(rslt)
        cost_sum += cost
        if is_over:
            over.add(idx)

    return (ans, cost_sum, over)

proc most_rihgt_line_change(ans: var seq[seq[array[4, int]]]) =
    for i in 0..<ans.len():
        var
            ta = initTable[int, int]()
            ta_idx = initTable[int, int]()
        for j in 0..<ans[i].len():
            if ta.getOrDefault(ans[i][j][0]) < ans[i][j][3]:
                ta[ans[i][j][0]] = ans[i][j][3]
                ta_idx[ans[i][j][0]] = j

        for k, v in ta_idx.pairs():
            ans[i][v][3] = 1000

proc yamanobori(N: int, D: int, A: seq[seq[int]], h: var seq[int], time_limit: float): (seq[seq[array[4, int]]], int,
        seq[int], seq[int], seq[int]) =
    var
        cnt = 0
        height = newSeq[int](h.len()+1)

    for i, j in h:
        height[i+1] = height[i] + j

    var (ans, cost, over) = get_ans(N, D, A, h, height)

    if h.len() == 1:
        return (ans, cost, over, h, height)


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

        var (ans_n, cost_n, over_n) = get_ans(N, D, A, h_n, height_n)

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
                    ans = ans_n
                    over = over_n
            else:
                h = h_n
                height = height_n
                cost = cost_n
                ans = ans_n
                over = over_n

        cnt += 1
        if cnt % 100 == 0:

            if cpuTime() - tmp_time > time_limit:
                echo cnt
                return (ans, cost, over, h, height)



proc get_h(D: int, N: int, A: seq[seq[int]], ): (seq[seq[array[4, int]]], seq[seq[array[4, int]]], seq[int], seq[int], seq[int], seq[int]) =
    var
        h = @[1000]
        (ans_ins, _, over_ins, _, _) = yamanobori(N, D, A, h, 0)
        l = int(sqrt(float32(N)))-1
        r = -(-N//2)+1

    for i in 0..<D:
        ans_ins[i].reverse()

    var
        rs_ans: seq[seq[array[4, int]]]
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

        var (ans_n, cost_n, over_n, h_n, height_n) = yamanobori(N, D, A, h, 0.3)

        if len(over_n) > 0:
            r = h_num
        else:
            l = h_num

        if rs_cost > cost_n:
            rs_ans = ans_n
            rs_cost = cost_n
            rs_over = over_n
            rs_h = h_n
            rs_height = height_n

    (rs_ans, rs_cost, rs_over, rs_h, rs_height) = yamanobori(N, D, A, rs_h, 0.3)

    for i in rs_over:
        if i notin over_ins:
            rs_ans[i] = ans_ins[i]

    for i in 0..<D:
        rs_ans[i].reverse()

    return (rs_ans, ans_ins, rs_h, rs_height, rs_over, over_ins)


proc is_OK_gr2(same, a, h, height: seq[int]): (bool, seq[array[4, int]]) =
    var
        OK = true
        w = newseq[int](h.len())
        rslt = newSeq[array[4, int]](a.len())
        a_rev = a.reversed()
        i: int
    for idx in 0..<a.len():
        if idx < len(same):
            i = same[idx]
        else:
            i = a_rev[idx]

        var
            aspect_min = 100000000.0
            puted = false
            tmp = (0, 0, [0, 0, 0, 0])

        for j in 0..<h.len():
            var width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = true
                var aspect = max(width, h[j]) / min(width, h[j])
                if aspect_min > aspect:
                    aspect_min = aspect
                    tmp = (j, width, [height[j], w[j], height[j + 1], w[j] + width])

        if puted:
            var (j, width, rs) = tmp
            w[j] += width
            rslt[idx] = rs
        else:
            return (false, rslt)

    rslt.reverse()
    return (true, rslt)

proc greedy2(D, N: int, A: seq[seq[int]], h, height: seq[int], ans: seq[seq[array[4, int]]], over: seq[int], A_tenti: seq[seq[int]]): (array[2, int], array[2,
        seq[seq[array[4, int]]]]) =
    if len(over) > 0:
        return ([-1, -1], [@[@[[-1, -1, -1, -1]]], @[@[[-1, -1, -1, -1]]]])

    type
        st_type = SegTreeType[int]((a: int, b: int)=>max(a, b), () => -1)
    var
        sts = newseq[st_type](N)
        more_good = [0, 0]
        rslt = [ans, ans]

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

proc is_OK(same: seq[array[2, int]], other: seq[(int, int)], h, height: seq[int]): (bool, seq[array[4, int]]) =
    var
        is_over = false
        w = newSeq[int](h.len())
        rslt = newSeq[array[4, int]](same.len()+other.len())

    for (i, idx) in same:
        var
            aspect_min = 10000000.0
            puted = false
            tmp: (int, int, array[4, int])
        for j in 0..<h.len():
            var width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = true
                var aspect = max(width, h[j]) / min(width, h[j])
                if aspect_min > aspect:
                    aspect_min = aspect
                    tmp = (j, width, [height[j], w[j], height[j + 1], w[j] + width])
        if puted:
            var (j, width, rs) = tmp
            w[j] += width
            rslt[idx] = rs
        else:
            return (false, rslt)

    for (i, idx) in other:
        var
            aspect_min = 10000000.0
            puted = false
            tmp: (int, int, array[4, int])
        for j in 0..<h.len():
            var width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = true
                var aspect = max(width, h[j]) / min(width, h[j])
                if aspect_min > aspect:
                    aspect_min = aspect
                    tmp = (j, width, [height[j], w[j], height[j + 1], w[j] + width])
        if puted:
            var (j, width, rs) = tmp
            w[j] += width
            rslt[idx] = rs
        else:
            return (false, rslt)


    return (true, rslt)

proc greedy1(D, N: int, A: seq[seq[int]], h, height, : seq[int], ans: seq[seq[array[4, int]]], over: seq[int]): (array[2, int], array[2, seq[seq[array[4, int]]]]) =
    var
        more_good = [0, 0]
        rslt = [ans, ans]

    for mode in [0, 1]:
        for i in countup(mode, len(ans)-2, 2):
            if i in over or i+1 in over:
                continue
            var
                rslt_a: seq[array[4, int]] = newSeq[array[4, int]]()
                rslt_b: seq[array[4, int]] = newSeq[array[4, int]]()
                a = A[i]
                b = A[i+1]
                a_sms = newSortedMultiset(a)
                b_sms = newSortedMultiset(b)
                same_a = newSeqOfCap[array[2, int]](a.len())
                same_b = newSeqOfCap[array[2, int]](a.len())
                a_idx_sms = newSortedMultiset(toseq(0..<a.len()))
                b_idx_sms = newSortedMultiset(toseq(0..<a.len()))

            while true:
                var diff = newSeqOfCap[(int, int, int, int, int)](a.len())
                for idx, j in itr(a_sms):
                    var
                        i_idx = a_idx_sms.get(idx)
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
                        var j_idx = b_idx_sms.get(b_sms.indx_right(j))
                        diff.add((diff_r, j, r, i_idx, j_idx))
                    else:
                        var j_idx = b_idx_sms.get(b_sms.indx_right(j)-1)
                        diff.add((diff_l, j, l, i_idx, j_idx))

                var
                    min_num = 10**8
                    num, j, k, j_idx, k_idx: int
                for di in diff:
                    if di[0] < min_num:
                        (num, j, k, j_idx, k_idx) = di
                        min_num = num

                same_a.add([max(j, k), j_idx])
                same_b.add([max(j, k), k_idx])
                discard a_idx_sms.remove(j_idx)
                discard b_idx_sms.remove(k_idx)
                discard a_sms.remove(j)
                discard b_sms.remove(k)

                var
                    a_other = zip(a_sms.get_all_reversed(), a_idx_sms.get_all_reversed())
                    b_other = zip(b_sms.get_all_reversed(), b_idx_sms.get_all_reversed())
                    (ok_a, rslt_a_n) = is_OK(same_a, a_other, h, height)
                    (ok_b, rslt_b_n) = is_OK(same_b, b_other, h, height)

                if ok_a and ok_b:
                    rslt_a = rslt_a_n
                    rslt_b = rslt_b_n
                else:
                    more_good[mode] += same_a.len()-1
                    if rslt_a.len() > 0 and rslt_b.len() > 0:
                        rslt[mode][i] = rslt_a
                        rslt[mode][i+1] = rslt_b
                    break

                if a_sms.size == 0:
                    more_good[mode] += same_a.len() - 1
                    if rslt_a.len() > 0 and rslt_b.len() > 0:
                        rslt[mode][i] = rslt_a
                        rslt[mode][i+1] = rslt_b
                    break
    return (more_good, rslt)




proc output(ans: seq[seq[array[4, int]]]) =
    for i in ans:
        for j in i:
            echo j.join(" ")

proc get_ans_from_line(D, N: int, line: seq[seq[Sortedset]], height, over: seq[int], ans_ins: seq[seq[array[4, int]]], over_ins: seq[int]): seq[seq[array[
        4, int]]] =
    var ans = newSeq[newSeqOfCap[array[4, int]](N)](D)
    for i, j in line:
        if i in over and i notin over_ins:
            ans[i] = ans_ins[i]
        else:
            for k, l in j:
                for _, m in itr(l):
                    var prv: int
                    if m != 0:
                        ans[i].add([height[k], prv, height[k + 1], m])
                    prv = m

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

    proc mode_0(): bool
    proc mode_2(): bool
    proc mode_3(): bool
    proc mode_4(): bool
    proc mode_6(): bool
    var
        cnt = 0
        len_h = h.len()
        A_minus = newSeq[newSeq[int](N)](D)
        Timeover = 2.9
        mode_array = [0, 0, 0, 2, 3, 4, 4, 6]


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

        if mode == 0:
            discard mode_0()
        elif mode == 2:
            discard mode_2()
        elif mode == 3:
            discard mode_3()
        elif mode == 4:
            discard mode_4()
        elif mode == 5:
            discard mode_6()


    proc all_ok(idx: int): bool =
        result = true
        for i, j in itr(surf[idx]):
            if j <= A_minus[idx][i]:
                discard
            else:
                return false
            if i == N-1:
                break
        return true


    proc mode_6(): bool =
        if line[idx1][idx2].size < 3:
            return false

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
            return false
        var rslt = newSeq[int](line[idx1][idx2].size)
        for i, j in itr(line[idx1][idx2]):
            rslt[^(i+1)] = 1000 - j
        line[idx1][idx2] = newSortedset(rslt)

        return true

    # proc mode_5() =
    #     var idx3: int
    #     while true:
    #         idx3 = rand(len_h-1)
    #         if idx2 != idx3:
    #             break

    #     if line[idx1][idx2].size == 2 and line[idx1][idx3].size == 2:
    #         return

    proc mode_4(): bool =
        if line[idx1][idx2].size < 3:
            return false
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
            return false

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


                if all_ok(idx1):
                    discard line[idx1][idx2].remove(m)
                    line[idx1][idx4].add(i)
                    return true
                else:
                    surf[idx1].add(-prv_l_1)
                    surf[idx1].add(-prv_r_1)
                    surf[idx1].add(-prv_lr_2)
                    discard surf[idx1].remove(-nxt_lr_1)
                    discard surf[idx1].remove(-nxt_l_2)
                    discard surf[idx1].remove(-nxt_r_2)
        return false

    proc mode_3(): bool =
        if line[idx1][idx2].size < 3:
            return false
        var
            idx3 = rand(1..<line[idx1][idx2].size-1)
            m = line[idx1][idx2].get(idx3)
            l = line[idx1][idx2].lt(m)
            r = line[idx1][idx2].gt(m)
            w = 30
            num = rand(max(l, m-w)..min(r, m+w))
            score_diff = 0
        if 0 <= idx1 - rev and idx1 - rev < D:
            if m in line[idx1 - rev][idx2]:
                score_diff -= 1
            if num in line[idx1 - rev][idx2]:
                score_diff += 1
        if 0 <= idx1 + rev and idx1 + rev < D:
            if m in line[idx1 + rev][idx2]:
                score_diff -= 1
            if num in line[idx1 + rev][idx2]:
                score_diff += 1

        if score_diff < 0:
            return false
        var
            prv_l = h[idx2] * (m - l)
            nxt_l = h[idx2] * (num - l)
            prv_r = h[idx2] * (r - m)
            nxt_r = h[idx2] * (r - num)

        # 一旦面積情報の書き換え
        discard surf[idx1].remove(-prv_l)
        discard surf[idx1].remove(-prv_r)
        surf[idx1].add(-nxt_l)
        surf[idx1].add(-nxt_r)

        if all_ok(idx1):
            discard line[idx1][idx2].remove(m)
            line[idx1][idx2].add(num)
            return true
        else:
            surf[idx1].add(-prv_l)
            surf[idx1].add(-prv_r)
            discard surf[idx1].remove(-nxt_l)
            discard surf[idx1].remove(-nxt_r)
        return false

    proc mode_2(): bool =
        if line[idx1][idx2].size < 3:
            return false

        var
            idx3 = rand(1..<line[idx1][idx2].size-1)
            m = line[idx1][idx2].get(idx3)
            l = line[idx1][idx2].lt(m)
            r = line[idx1][idx2].gt(m)
            score_diff = 0

        if 0 <= idx1 - rev and idx1-rev < D:
            if m in line[idx1 - rev][idx2]:
                score_diff -= 1
            if l + r - m in line[idx1 - rev][idx2]:
                score_diff += 1
        if 0 <= idx1 + rev and idx1+rev < D:
            if m in line[idx1 + rev][idx2]:
                score_diff -= 1
            if l + r - m in line[idx1 + rev][idx2]:
                score_diff += 1

        if score_diff < 0:
            return false

        discard line[idx1][idx2].remove(m)
        line[idx1][idx2].add(l+r-m)

        return true

    proc mode_0_l(l, m, r, l_other: int): bool =
        var score_diff = 0
        if l_other <= l:
            return false

        if 0 <= idx1 - rev and idx1-rev < D:
            if m in line[idx1 - rev][idx2]:
                score_diff -= 1
            score_diff += 1

        if 0 <= idx1 + rev and idx1+rev < D:
            if m in line[idx1 + rev][idx2]:
                score_diff -= 1
            if l_other in line[idx1 + rev][idx2]:
                score_diff += 1

        if score_diff < 0:
            return false

        var
            prv_l = h[idx2] * (m - l)
            nxt_l = h[idx2] * (l_other - l)

            prv_r = h[idx2] * (r - m)
            nxt_r = h[idx2] * (r - l_other)

        # if prv_l < 0 or nxt_l < 0 or prv_r < 0 or nxt_r < 0:
        #     return false

        # 一旦面積情報の書き換え
        discard surf[idx1].remove(-prv_l)
        discard surf[idx1].remove(-prv_r)
        surf[idx1].add(-nxt_l)
        surf[idx1].add(-nxt_r)


        # 変更しても面積に問題が無いなら
        if all_ok(idx1):
            discard line[idx1][idx2].remove(m)
            line[idx1][idx2].add(l_other)
            return true
        else:
            # 面積情報の訂正
            surf[idx1].add(-prv_l)
            surf[idx1].add(-prv_r)
            discard surf[idx1].remove(-nxt_l)
            discard surf[idx1].remove(-nxt_r)


    proc mode_0_r(l, m, r, r_other: int): bool =
        var score_diff = 0

        if r <= r_other:
            return false

        if 0 <= idx1 - rev and idx1-rev < D:
            if m in line[idx1 - rev][idx2]:
                score_diff -= 1
            score_diff += 1

        if 0 <= idx1 + rev and idx1+rev < D:
            if m in line[idx1 + rev][idx2]:
                score_diff -= 1
            if r_other in line[idx1 + rev][idx2]:
                score_diff += 1

        if score_diff < 0:
            return false

        var
            prv_l = h[idx2] * (m - l)
            nxt_l = h[idx2] * (r_other - l)

            prv_r = h[idx2] * (r - m)
            nxt_r = h[idx2] * (r - r_other)

        # if prv_l < 0 or nxt_l < 0 or prv_r < 0 or nxt_r < 0:
        #     return false

        # 一旦面積情報の書き換え
        discard surf[idx1].remove(-prv_l)
        discard surf[idx1].remove(-prv_r)
        surf[idx1].add(-nxt_l)
        surf[idx1].add(-nxt_r)


        # 変更しても面積に問題が無いなら
        if all_ok(idx1):
            discard line[idx1][idx2].remove(m)
            line[idx1][idx2].add(r_other)
            return true
        else:
            # 面積情報の訂正
            surf[idx1].add(-prv_l)
            surf[idx1].add(-prv_r)
            discard surf[idx1].remove(-nxt_l)
            discard surf[idx1].remove(-nxt_r)

            return false



    proc mode_0(): bool =

        if line[idx1][idx2].size < 3:
            return false
        var
            idx3 = rand(1..<line[idx1][idx2].size-1)
            m = line[idx1][idx2].get(idx3)
            l = line[idx1][idx2].lt(m)
            r = line[idx1][idx2].gt(m)
            l_other = line[idx1-rev][idx1].le(m)
            r_other = line[idx1-rev][idx1].ge(m)

        if l_other == m:
            return false

        if mode_0_l(l, m, r, l_other):
            return true
        if mode_0_r(l, m, r, r_other):
            return true
        return false

    # proc mode_1(): bool =
    #     if line[idx1][idx2].size < 3:
    #         return false
    #     var
    #         idx3 = rand(1..<line[idx1][idx2].size-1)
    #         m = line[idx1][idx2].get(idx3)
    #         l = line[idx1][idx2].lt(m)
    #         r = line[idx1][idx2].gt(m)
    #         l_other = line[idx1-rev][idx1].le(m)
    #         r_other = line[idx1-rev][idx1].ge(m)
    #     if m == l_other:
    #         return false

































# import nimprof
var
    (W, D, N, A, avr_amari) = input()
    A_reverse = newSeq[newSeq[int](N)](D)
    A_tenti = newSeqwith(N, newSeq[int](D))

for i in 0..<D:
    A_reverse[i] = A[i].reversed()

var (ans, ans_ins, h, height, over, over_ins) = get_h(D, N, A_reverse)

for i in 0..<D:
    for j in 0..<N:
        A_tenti[j][i] = A[i][j]

var
    (more_good1, rslt1) = greedy1(D, N, A, h, height, ans, over)
    (more_good2, rslt2) = greedy2(D, N, A, h, height, ans, over, A_tenti)

# echo(more_good1, more_good2)

if max(more_good1) <= max(more_good2):
    if more_good2[0] <= more_good2[1]:
        ans = rslt2[1]
    else:
        ans = rslt2[0]
else:
    if more_good1[0] <= more_good1[1]:
        ans = rslt1[1]
    else:
        ans = rslt1[0]

#あえてこれを後でやるとか
most_rihgt_line_change(ans)

var
    (line, surf) = get_line_ans_S_from_ans(D, N, ans, h, height)
yamanobori2(D, N, ans, line, over, h, surf, A)
ans = get_ans_from_line(D, N, line, height, over, ans_ins, over_ins)


output(ans)














