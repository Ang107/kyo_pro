import macros
macro Please(x): untyped = nnkStmtList.newTree()

Please use Nim-ACL
Please use Nim-ACL
Please use Nim-ACL



#[ import atcoder/segtree ]#
when not declared ATCODER_SEGTREE_HPP:
  const ATCODER_SEGTREE_HPP* = 1
  #[ import atcoder/internal_bit ]#
  when not declared ATCODER_INTERNAL_BITOP_HPP:
    const ATCODER_INTERNAL_BITOP_HPP* = 1
    import std/bitops
  
  #ifdef _MSC_VER
  #include <intrin.h>
  #endif
  
  # @param n `0 <= n`
  # @return minimum non-negative `x` s.t. `n <= 2**x`
    proc ceil_pow2*(n:SomeInteger):int =
      var x = 0
      while (1.uint shl x) < n.uint: x.inc
      return x
  # @param n `1 <= n`
  # @return minimum non-negative `x` s.t. `(n & (1 << x)) != 0`
    proc bsf*(n:SomeInteger):int =
      return countTrailingZeroBits(n)
    discard
  import std/sequtils
  import std/algorithm
  #[ import atcoder/rangeutils ]#
  when not declared ATCODER_RANGEUTILS_HPP:
    const ATCODER_RANGEUTILS_HPP* = 1
    type RangeType* = Slice[int] | HSlice[int, BackwardsIndex] | Slice[BackwardsIndex]
    type IndexType* = int | BackwardsIndex
    template halfOpenEndpoints*(p:Slice[int]):(int,int) = (p.a, p.b + 1)
    template `^^`*(s, i: untyped): untyped =
      (when i is BackwardsIndex: s.len - int(i) else: int(i))
    template halfOpenEndpoints*[T](s:T, p:RangeType):(int,int) =
      (s^^p.a, s^^p.b + 1)
    discard

  #{.push inline.}
  type SegTree*[S; p: static[tuple]] = object
    len*, size*, log*: int
    d: seq[S]

  template calc_op*[ST: SegTree](self: ST or typedesc[ST]; a, b: ST.S): auto =
    block:
      let u = ST.p.op(a, b)
      u
  template calc_e*[ST: SegTree](self: ST or typedesc[ST]): auto =
    block:
      let u = ST.p.e()
      u
  proc update[ST: SegTree](self: var ST; k: int) =
    self.d[k] = ST.calc_op(self.d[2 * k], self.d[2 * k + 1])

  proc init*[ST: SegTree](self: var ST; v: seq[ST.S]) =
    let
      n = v.len
      log = ceil_pow2(n)
      size = 1 shl log
    (self.len, self.size, self.log) = (n, size, log)
    if self.d.len < 2 * size:
      self.d = newSeqWith(2 * size, ST.calc_e())
    else:
      self.d.fill(0, 2 * size - 1, ST.calc_e())
    for i in 0..<n: self.d[size + i] = v[i]
    for i in countdown(size - 1, 1): self.update(i)
  proc init*[ST: SegTree](self: var ST; n: int) =
    self.init(newSeqWith(n, ST.calc_e()))
  proc init*[ST: SegTree](self: typedesc[ST]; v: seq[ST.S]): auto =
    result = ST()
    result.init(v)
  proc init*[ST: SegTree](self: typedesc[ST]; n: int): auto =
    self.init(newSeqWith(n, ST.calc_e()))
  template SegTreeType*[S](op0, e0: untyped): typedesc[SegTree] =
    proc op1(l, r: S): S {.gensym inline.} = op0(l, r)
    proc e1(): S {.gensym inline.} = e0()
    SegTree[S, (op: op1, e: e1)]
  template getType*(ST: typedesc[SegTree]; S: typedesc; op, e: untyped): typedesc[SegTree] =
    SegTreeType[S](op, e)

  template initSegTree*[S](v: seq[S] or int; op, e: untyped): auto =
    SegTreeType[S](op, e).init(v)

  proc set*[ST: SegTree](self: var ST; p: IndexType; x: ST.S) =
    var p = self^^p
    assert p in 0..<self.len
    p += self.size
    self.d[p] = x
    for i in 1..self.log: self.update(p shr i)

  proc get*[ST: SegTree](self: ST; p: IndexType): ST.S =
    let p = self^^p
    assert p in 0..<self.len
    return self.d[p + self.size]

  proc prod*[ST: SegTree](self: ST; p: RangeType): ST.S =
    var (l, r) = self.halfOpenEndpoints(p)
    assert 0 <= l and l <= r and r <= self.len
    var
      sml, smr = ST.calc_e()
    l += self.size; r += self.size
    while l < r:
      if (l and 1) != 0: sml = ST.calc_op(sml, self.d[l]); l.inc
      if (r and 1) != 0: r.dec; smr = ST.calc_op(self.d[r], smr)
      l = l shr 1
      r = r shr 1
    return ST.calc_op(sml, smr)
  proc `[]`*[ST: SegTree](self: ST; p: IndexType): auto = self.get(p)
  proc `[]`*[ST: SegTree](self: ST; p: RangeType): auto = self.prod(p)
  proc `[]=`*[ST: SegTree](self: var ST; p: IndexType; x: ST.S) = self.set(p, x)

  proc all_prod*[ST: SegTree](self: ST): ST.S = self.d[1]

#  proc max_right*[ST:SegTree, f:static[proc(s:ST.S):bool]](self:ST, l:int):auto = self.max_right(l, f)
  proc max_right*[ST: SegTree](self: ST; l: IndexType; f: proc(s: ST.S): bool): int =
    var l = self^^l
    assert l in 0..self.len
    assert f(ST.calc_e())
    if l == self.len: return self.len
    l += self.size
    var sm = ST.calc_e()
    while true:
      while l mod 2 == 0: l = l shr 1
      if not f(ST.calc_op(sm, self.d[l])):
        while l < self.size:
          l = (2 * l)
          if f(ST.calc_op(sm, self.d[l])):
            sm = ST.calc_op(sm, self.d[l])
            l.inc
        return l - self.size
      sm = ST.calc_op(sm, self.d[l])
      l.inc
      if not ((l and -l) != l): break
    return self.len

#  proc min_left*[ST:SegTree, f:static[proc(s:ST.S):bool]](self:ST, r:int):auto = self.min_left(r, f)
  proc min_left*[ST: SegTree](self: ST; r: IndexType; f: proc(s: ST.S): bool): int =
    var r = self^^r
    assert r in 0..self.len
    assert f(ST.calc_e())
    if r == 0: return 0
    r += self.size
    var sm = ST.calc_e()
    while true:
      r.dec
      while r > 1 and (r mod 2 != 0): r = r shr 1
      if not f(ST.calc_op(self.d[r], sm)):
        while r < self.size:
          r = (2 * r + 1)
          if f(ST.calc_op(self.d[r], sm)):
            sm = ST.calc_op(self.d[r], sm)
            r.dec
        return r + 1 - self.size
      sm = ST.calc_op(self.d[r], sm)
      if not ((r and -r) != r): break
    return 0
  #{.pop.}
  discard
#[ import atcoder/extra/structure/set_map ]#
when not declared ATCODER_SET_MAP_HPP:
  const ATCODER_SET_MAP_HPP* = 1
  #type BinaryTreeType = enum
  #  RedBlack,
  #  Splay,
  #  Randomized
  #const SetMapType = BinaryTreeType.RedBlack
# red black
  const USE_RED_BLACK_TREE = true
  const USE_SPLAY_TREE = false
 # splay
 #  const USE_RED_BLACK_TREE = false
 #  const USE_SPLAY_TREE = true
 # RBST
 #  const USE_RED_BLACK_TREE = false
 #  const USE_SPLAY_TREE = false

  {.push discardable inline.}
  import std/strutils
  #[ include atcoder/extra/structure/binary_tree_utils ]#
  when not declared ATCODER_BINARY_TREE_UTILS_HPP:
    const ATCODER_BINARY_TREE_UTILS_HPP* = 1
    #[ include atcoder/extra/structure/binary_tree_node_utils ]#
    when not declared ATCODER_BINARY_TREE_NODE_UTILS_HPP:
      const ATCODER_BINARY_TREE_NODE_UTILS_HPP* = 1
      type BinaryTreeNode* = concept x, type T
        x.l is T
        x.r is T
        x.p is T
    #    T.Countable
      type BinaryTree* = concept x, type T
        T.Node is BinaryTreeNode
        x.root is T.Node
    
      proc greater_func*[K](a,b:K):bool = a < b
    
      proc isLeaf*[Node:BinaryTreeNode](self:Node):bool =
        return self.l == self
    
      proc leftMost*[Node:BinaryTreeNode](self: Node):Node =
        if self.l.isLeaf: return self
        else: return self.l.leftMost
      proc rightMost*[Node:BinaryTreeNode](self: Node): Node =
        if self.r.isLeaf: return self
        else: return self.r.rightMost
      proc parentLeft*[Node:BinaryTreeNode](node: Node): Node =
        var node = node
        while true:
          if node.p == nil: return nil
          elif node.p.l == node: return node.p
          node = node.p
      proc parentRight*[Node:BinaryTreeNode](node: Node): Node =
        var node = node
        while true:
          if node.p == nil: return nil
          elif node.p.r == node: return node.p
          node = node.p
      proc front*[Tree:BinaryTree](self: Tree): Tree.Node = self.root.leftMost
      proc tail*[Tree:BinaryTree](self: Tree): Tree.Node =  self.root.rightMost
      proc begin*[Tree:BinaryTree](self:Tree):Tree.Node = self.root.leftMost
    
      proc succ*[Node:BinaryTreeNode](node: Node): Node =
        if not node.r.isLeaf: return node.r.leftMost
        else: return node.parentLeft
      proc pred*[Node:BinaryTreeNode](node: Node): Node =
        if not node.l.isLeaf: return node.l.rightMost
        else: return node.parentRight
      proc inc*[Node:BinaryTreeNode](node: var Node) =
        var node2 = node.succ
        swap node, node2
      proc dec*[Node:BinaryTreeNode](node: var Node) =
        var node2 = node.pred
        swap node, node2
      proc `+=`*[Node:BinaryTreeNode](node: var Node, n:int) =
        if n < 0: node -= (-n)
        for i in 0..<n: node.inc
      proc `-=`*[Node:BinaryTreeNode](node: var Node, n:int) =
        if n < 0: node += (-n)
        for i in 0..<n: node.dec
    
      proc index*[Node:BinaryTreeNode](t:Node):int =
    #    static:
    #      assert Node.Countable isnot void
        result = t.l.cnt
        var (t, p) = (t, t.p)
        while p != nil:
          if p.r == t: result += p.l.cnt + 1
          t = t.p
          p = p.p
      proc distance*[Node:BinaryTreeNode](t1, t2:Node):int =
    #    static:
    #      assert Node.Countable isnot void
        return t2.index - t1.index
      proc `*`*[Node:BinaryTreeNode](node:Node):auto = node.key
      iterator items*[Node:BinaryTreeNode](s:Slice[Node]):Node =
        var it = s.a
        while true:
          yield it
          if it == s.b: break
          it.inc
      discard
    {.push discardable inline.}
    type SomeSortedTree* = concept x, type T
      T.Tree is BinaryTree
      T.K is typedesc
      T.V is typedesc
      T.Node is typedesc
      T.multi is typedesc
      T.p
      x.End
    type SomeSortedSet* = concept x, type T
      T is SomeSortedTree
      T.V is void
      T.multi is void
    type SomeSortedMap* = concept x, type T
      T is SomeSortedTree
      T.V isnot void
      T.multi is void
    type SomeSortedMultiSet* = concept x, type T
      T is SomeSortedTree
      T.V is void
      T.multi isnot void
    type SomeSortedMultiMap* = concept x, type T
      T is SomeSortedTree
      T.V isnot void
      T.multi isnot void
    type hasSplay* = concept x, type T
      var t:T.Node
      x.tree.splay(t)
    proc begin*[T:SomeSortedTree](self: T):T.Node = self.tree.begin()
  
    proc getKey*[T:SomeSortedTree](self: T, t:T.Node):auto =
      when T.V is void: t.key
      else: t.key[0]
  
    template calc_comp*[T:SomeSortedTree](self:T, x, y:T.K):bool =
      when T.p[0] is typeof(nil):
        x < y
      else:
        let comp = T.p[0]
        comp(x, y)
  
    proc lower_bound*[T:SomeSortedTree](self: var T, t:var T.Node, x:T.K):T.Node =
      if t.isLeaf:
        return t
      if t != self.End and self.calc_comp(self.getKey(t), x):
        return self.lower_bound(t.r, x)
      else:
        var t2 = self.lower_bound(t.l, x)
        if t2.isLeaf: return t
        else: return t2
  
    proc lower_bound*[T:SomeSortedTree](self:var T, x:T.K):T.Node =
      assert self.tree.root != nil
      result = self.lower_bound(self.tree.root, x)
      when T is hasSplay:
        self.tree.splay(result)
        self.tree.root = result
  
    proc upper_bound*[T:SomeSortedTree](self: var T, t:var T.Node, x:T.K):T.Node =
      if t.isLeaf: return t
      if t == self.End or self.calc_comp(x, self.getKey(t)):
        var t2 = self.upper_bound(t.l, x)
        if t2.isLeaf: return t
        else: return t2
      else:
        return self.upper_bound(t.r, x)
  
    proc upper_bound*[T:SomeSortedTree](self: var T, x:T.K):T.Node =
      assert self.tree.root != nil
      result = self.upper_bound(self.tree.root, x)
      when T is hasSplay:
        self.tree.splay(result)
        self.tree.root = result
  
  #  proc find*[T:SomeSortedTree](self: var T, t:var T.Node, x:T.K):T.Node =
  #    echo "find:  ", t.key
  #    if t == self.End or t.isLeaf: return self.End
  #    if self.calc_comp(x, self.getKey(t)): return self.find(t.l, x)
  #    elif self.calc_comp(self.getKey(t), x): return self.find(t.r, x)
  #    else: return t
    proc find*[T:SomeSortedTree](self:var T, x:T.K):T.Node =
      var t = self.lower_bound(x)
      if t != self.End and self.getKey(t) == x: return t
      else: return self.End
  #    result = self.find(self.root, x)
    proc contains*[T:SomeSortedTree](self: var T, x:T.K):bool =
      self.find(x) != self.End
  
    proc insert*[T:SomeSortedMultiSet](self: var T, x:T.K):T.Node =
      self.tree.insert(self.upper_bound(x), x)
    proc insert*[T:SomeSortedMultiMap](self: var T, x:(T.K, T.V)):T.Node =
      self.tree.insert(self.upper_bound(x[0]), x)
  
    proc insert*[T:SomeSortedSet](self: var T, x:T.K):T.Node =
      var t = self.lower_bound(x)
      if t != self.End and t.key == x: return t
      else: return self.tree.insert(t, x)
    proc insert*[T:SomeSortedMap](self: var T, x:(T.K, T.V)):T.Node =
      var it = self.lower_bound(x[0])
      if it != self.End and it.key[0] == x[0]: it.key[1] = x[1]; return it
      else: return self.tree.insert(it, x)
    proc incl*[T:SomeSortedSet | SomeSortedMultiSet](self:var T, x:T.K):T.Node =
      self.insert(x)
    proc incl*[T:SomeSortedMap | SomeSortedMultiMap](self:var T, x:(T.K, T.V)):T.Node =
      self.insert(x)
  
    template getAddr*[T:SomeSortedMap](self:var T, x:T.K):auto =
      var t = self.lower_bound(x)
      if t == self.End or t.key[0] != x:
        var v: T.V
        when v is SomeSortedTree:
          v.init()
        t = self.tree.insert(t, (x, v))
      t.key[1].addr
  
    template `[]`*[T:SomeSortedMap](self: var T, x:T.K):auto =
      var t = self.getAddr(x)
      t[]
    proc `[]=`*[T:SomeSortedMap](self: var T, x:T.K, v:T.V) =
      var t = self.getAddr(x)
      t[] = v
  
    proc erase*[T:SomeSortedSet or SomeSortedMap](self: var T, x:T.K):T.Node =
      mixin erase
      var t = self.lower_bound(x)
      if t == self.End or self.getKey(t) != x: return self.End
      else: return self.tree.erase(t)
    proc erase*[T:SomeSortedMultiSet or SomeSortedMultiMap](self: var T, lb, ub:T.Node):T.Node =
      if lb != ub:
        var
          (L, R) = self.tree.split(lb)
          (RL, RR) = self.tree.split(ub)
        self.tree.root = self.tree.join(L, RR)
      return ub
  
    proc erase*[T:SomeSortedMultiSet or SomeSortedMultiMap](self: var T, x:T.K):T.Node =
      #doAssert T.Tree.Countable isnot void
      mixin erase
      return self.erase(self.lower_bound(x), self.upper_bound(x))
  
    proc erase*[T:SomeSortedTree](self: var T, t:T.Node):T.Node = self.tree.erase(t)
    proc excl*[T:SomeSortedTree](self: var T, x:T.K):T.Node = self.erase(x)
    proc excl*[T:SomeSortedTree](self: var T, t:T.Node):T.Node = self.erase(t)
  
    proc kth_element*[T:SomeSortedTree](self: var T, t:T.Node, k:int):T.Node =
  #    static:
  #      assert T.Tree.Countable isnot void
      let p = t.l.cnt
      if k < p: return self.kth_element(t.l, k)
      elif k > p: return self.kth_element(t.r, k - p - 1)
      else: return t
    
    proc kth_element*[T:SomeSortedTree](self: var T, k:int):T.Node =
      return self.kth_element(self.tree.root, k)
    proc `{}`*[T:SomeSortedTree](self: var T, k:int):T.Node =
      return self.kth_element(k)
  
    proc index*[T:SomeSortedTree](self:T, t:T.Node):int =
  #    static:
  #      assert T.Tree.Countable isnot void
      return index(t)
    proc distance*[T:SomeSortedTree](self:T, t1, t2:T.Node):int =
  #    static:
  #      assert T.Tree.Countable isnot void
      return index(t2) - index(t1)
  
    iterator items*[T:SomeSortedSet or SomeSortedMultiSet](self:T):T.K =
      var it = self.begin
      while it != self.End:
        yield it.key
        it.inc
    iterator pairs*[T:SomeSortedMap or SomeSortedMultiMap](self:T):(T.K, T.V) =
      var it = self.begin
      while it != self.End:
        yield it.key
        it.inc
    proc `end`*[Tree:SomeSortedTree](self:Tree):Tree.Node = self.End
    {.pop.}
    discard
  type MULTI_TRUE = int32
  type MULTI_FALSE = void
  type SortedTree*[Tree; Node; multi; K; V; p: static[tuple]] = object
    tree*: Tree
    End*: Node

  when USE_RED_BLACK_TREE:
    #[ include atcoder/extra/structure/red_black_tree ]#
    when not declared ATCODER_RED_BLACK_TREE_HPP:
      const ATCODER_RED_BLACK_TREE_HPP* = 1
      import std/sugar
    #  {.experimental: "codeReordering".}
      {.push inline, discardable.}
      type
        Color* = enum red, black
        RedBlackTreeNode*[K] = ref object
          p*, l*, r*: RedBlackTreeNode[K]
          key*: K
          color*: Color
          id*, cnt*: int32
          level*: int8
        RedBlackTreeType*[K, Node] = object of RootObj
          root*, leaf*: Node
          next_id*: int32
        RedBlackTree*[K] = RedBlackTreeType[K, RedBlackTreeNode[K]]
      proc getleaf*[K](self: RedBlackTree[K]):RedBlackTreeNode[K] =
        var leaf_node {.global.} :RedBlackTreeNode[K] = nil
        if leaf_node == nil:
          leaf_node = self.Node(color: Color.black, id: -1)
          (leaf_node.l, leaf_node.r) = (leaf_node, leaf_node)
          leaf_node.level = 0
          leaf_node.cnt = 0
        return leaf_node
    
      proc newNode*[T:RedBlackTree](self: var T, parent: T.Node): T.Node =
        result = T.Node(p:parent, l:self.leaf, r: self.leaf, color: Color.red, id: self.next_id)
        result.cnt = 1
    
      proc newNode*[T:RedBlackTree](self: var T, parent: T.Node, key: T.K): T.Node =
        result = self.newNode(parent)
        result.key = key
        self.next_id += 1
      proc init*[T:RedBlackTree](self:var T, root: var T.Node = nil) =
        self.leaf = self.getLeaf()
        if root != nil:
          self.root = root
          (self.root.l, self.root.r) = (self.leaf, self.leaf)
          root.id = -2
          self.root.p = nil
          self.root.color = Color.black
          self.update(root)
        self.next_id = 0
    
      #[ include atcoder/extra/structure/binary_tree_node_utils ]#
    
      # checker, write
      proc write*[T:RedBlackTree](rbt: T, self: T.Node, h = 0) =
        for i in 0..<h: stderr.write " | "
        if self.id == -1:
          stderr.write "*\n"
        else:
          stderr.write "id: ",self.id, " key: ", self.key, " color: ", self.color
          stderr.write " cnt: ", self.cnt, " ", " level: ", self.level
      #    if self.key == T.K.inf: stderr.write "inf"
          if self.p != nil: stderr.write " parent: ", self.p.id
          else: stderr.write " parent: nil"
          stderr.write "\n"
          if h >= 20:
            stderr.write "too deep!!!\n"
            assert false
            return
          rbt.write(self.l, h + 1)
          rbt.write(self.r, h + 1)
      
      proc write*[T:RedBlackTree](self: T) =
        stderr.write "======= RB-TREE =============\n"
        doAssert self.root != T.Node(nil)
        self.write(self.root, 0)
        stderr.write "======= END ==========\n"
      import sets
      proc checkTree*[T:RedBlackTree](self: T, node: T.Node = nil) =
        var node = node
        if node == nil:
          node = self.root
        #doAssert self.root.color == Color.black
        var black_ct_s = initHashSet[int]()
        proc checkTreeSub(node:T.Node, black_ct:int) =
          var black_ct = black_ct
          if node.color == Color.black: black_ct.inc
          if node.id == -1:
            black_ct_s.incl(black_ct)
            return
          if node.color == Color.red:
            doAssert node.l.color == Color.black and node.r.color == Color.black
          let d = if node.id >= 0: 1 else: 0
          doAssert node.cnt == node.l.cnt + node.r.cnt + d
          if node.level != node.l.level + (if node.l.color == Color.black: 1 else: 0) or node.level != node.r.level + (if node.r.color == Color.black: 1 else: 0):
            echo "found!!"
            echo "node: ", node.id
            self.write(node)
          doAssert node.level == node.l.level + (if node.l.color == Color.black: 1 else: 0)
          doAssert node.level == node.r.level + (if node.r.color == Color.black: 1 else: 0)
          checkTreeSub(node.l, black_ct)
          checkTreeSub(node.r, black_ct)
        checkTreeSub(node, 0)
        doAssert black_ct_s.len == 1
    
    
    
    
      template update*[T:RedBlackTree](self:T, node: T.Node) =
        if node == self.leaf or node == nil: return
        node.cnt = node.l.cnt + node.r.cnt
        if node.id >= 0: node.cnt.inc
        node.level = node.l.level + (if node.l.color == Color.black: 1 else: 0)
    
      proc rotateLeft*[T:RedBlackTree](self: var T, parent: T.Node):T.Node {.discardable.} =
        if parent == nil: return
        var right = parent.r
        parent.r = right.l
        if right.l != self.leaf: right.l.p = parent
        right.p = parent.p
        if parent == self.root:
          self.root = right
        if parent.p == nil:
          discard
        elif parent.p.l == parent: parent.p.l = right
        else: parent.p.r = right
        right.l = parent
        parent.p = right
        self.update(parent)
        self.update(right)
        return right
    
      proc rotateRight*[T:RedBlackTree](self: var T, parent: T.Node):T.Node {.discardable.} =
        if parent == nil: return
        var left = parent.l
        parent.l = left.r
        if left.r != self.leaf: left.r.p = parent
        left.p = parent.p
        if parent == self.root:
          self.root = left
        if parent.p == nil:
          discard
        elif parent.p.r == parent: parent.p.r = left
        else: parent.p.l = left
        left.r = parent
        parent.p = left
        self.update(parent)
        self.update(left)
        return left
    
      proc insert*[T:RedBlackTree](self: var T, node:T.Node, next:T.Node): T.Node {.discardable.} =
        proc fixInsert(self: var T, node: T.Node) =
          var curr = node
          #while curr != self.root and curr.p.color == Color.red:
          while curr.p != nil and curr.p.color == Color.red:
            if curr.p.p != nil and curr.p == curr.p.p.l:
              var uncle = curr.p.p.r
              if uncle.color == Color.red:
                curr.p.color = Color.black
                uncle.color = Color.black
                curr.p.p.color = Color.red
                self.update(curr.p)
                self.update(curr.p.p)
                curr = curr.p.p
              else:
                if curr == curr.p.r:
                  curr = curr.p
                  self.rotateLeft(curr)
                curr.p.color = Color.black
                if curr.p.p != nil:
                  curr.p.p.color = Color.red
                  self.rotateRight(curr.p.p)
            elif curr.p.p != nil:
              var uncle = curr.p.p.l
              if uncle.color == Color.red:
                curr.p.color = Color.black
                uncle.color = Color.black
                curr.p.p.color = Color.red
                self.update(curr.p)
                self.update(curr.p.p)
                curr = curr.p.p
              else:
                if curr == curr.p.l:
                  curr = curr.p
                  self.rotateRight(curr)
                curr.p.color = Color.black
                if curr.p.p != nil:
                  curr.p.p.color = Color.red
                  self.rotateLeft(curr.p.p)
          while curr != nil:
            self.update(curr)
            if curr.p == nil: curr.color = Color.black
            curr = curr.p
    
        if next.l == self.leaf:
          # insert at next.l
          next.l = node
          node.p = next
        else:
          var curr = next.l.rightMost
          # insert at curr.r
          curr.r = node
          node.p = curr
        self.update(node)
        self.fixInsert(node)
        return node
    
      proc insert*[T:RedBlackTree](self: var T, next:T.Node, x:T.K): T.Node {.discardable.} =
        var node = self.newNode(T.Node(nil), x)
        return self.insert(node, next)
    
    
      #proc getNodeStr(self:RedBlackTreeNode):string =
      #  if self == nil: "nil"
      #  else: $self.id
    
      proc update_parents[T:RedBlackTree](self:var T, node:T.Node):T.Node {.discardable.} =
        var curr = node
        while curr != nil:
          self.update(curr)
          if curr.p == nil: return curr
          curr = curr.p
    
      proc erase*[T:RedBlackTree](self: var T, node: T.Node):T.Node =
        proc fixErase(self: var T, node: T.Node, parent: T.Node) =
          var
            child = node
            parent = parent
          while child != self.root and child.color == Color.black:
            if parent == nil: break # add!!!!!!!!
            if child == parent.l:
              var sib = parent.r
              if sib.color == Color.red:
                sib.color = Color.black
                parent.color = Color.red
                self.rotateLeft(parent)
                sib = parent.r
              else:
                self.update(parent)
    
              if sib.l.color == Color.black and sib.r.color == Color.black:
                sib.color = Color.red
                self.update(parent)
                child = parent
                parent = child.p
                self.update(parent)
              else:
                if sib.r.color == Color.black:
                  sib.l.color = Color.black
                  sib.color = Color.red
                  self.rotateRight(sib)
                  sib = parent.r
                sib.color = parent.color
                parent.color = Color.black
                sib.r.color = Color.black
                self.rotateLeft(parent)
                self.update_parents(sib)
                child = self.root
                parent = child.p
            else:
              var sib = parent.l
              if sib.color == Color.red:
                sib.color = Color.black
                parent.color = Color.red
                self.rotateRight(parent)
                sib = parent.l
              else:
                self.update(parent)
    
              if sib.r.color == Color.black and sib.l.color == Color.black:
                sib.color = Color.red
                self.update(parent)
                child = parent
                parent = child.p
                self.update(parent)
              else:
                if sib.l.color == Color.black:
                  sib.r.color = Color.black
                  sib.color = Color.red
                  self.rotateLeft(sib)
                  sib = parent.l
                sib.color = parent.color
                parent.color = Color.black
                sib.l.color = Color.black
                self.rotateRight(parent)
                self.update_parents(sib)
                child = self.root
                parent = child.p
    
          if child != self.leaf:
            child.color = Color.black
          var curr = parent
          self.update_parents(curr)
    
        var node = node
        var succ = node.succ
        if node.l != self.leaf and node.r != self.leaf:
          swap(node.color, succ.color)
          swap(node.cnt, succ.cnt)
          # swap node and succ
          if node.r == succ:
            let tmp = succ.l
            succ.l = node.l
            if node.l != self.leaf: node.l.p = succ
            if node.r != self.leaf: node.r.p = succ
            node.l = tmp
            node.r = succ.r
            succ.r = node
            succ.p = node.p
            node.p = succ
            if succ.p != nil:
              if succ.p.l == node: succ.p.l = succ
              if succ.p.r == node: succ.p.r = succ
          else:
            swap(node.p, succ.p)
            swap(node.l, succ.l)
            swap(node.r, succ.r)
            if node.p != nil:
              if node.p.l == succ: node.p.l = node
              if node.p.r == succ: node.p.r = node
            if node.l != self.leaf: node.l.p = node
            if node.r != self.leaf: node.r.p = node
            if succ.p != nil:
              if succ.p.l == node: succ.p.l = succ
              if succ.p.r == node: succ.p.r = succ
            if succ.l != self.leaf: succ.l.p = succ
            if succ.r != self.leaf: succ.r.p = succ
          if self.root == node:
            self.root = succ
    
    
        let child = if node.l != self.leaf: node.l else: node.r
        if child != self.leaf:
          child.p = node.p
          if node.p == nil: self.root = child
          elif node == node.p.l: node.p.l = child
          else: node.p.r = child
    
          if node.color == Color.black:
            self.fixErase(child, node.p)
          else:
            self.update_parents(node.p)
        else:
          if node.p == nil:
            self.root = self.leaf
          elif node == node.p.l:
            node.p.l = self.leaf
          else:
            assert node == node.p.r
            node.p.r = self.leaf
    
          if node.color == Color.black:
            self.fixErase(self.leaf, node.p)
          else:
            self.update_parents(node.p)
        return succ
    
    # split, join
    
      proc expose*[T:RedBlackTree](self: var T, N:T.Node):(T.Node, T.Node, T.Node) =
        if not N.l.isLeaf:
          N.l.p = nil
          N.l.color = Color.black
        if not N.r.isLeaf:
          N.r.p = nil
          N.r.color = Color.black
        N.color = Color.black
        (result[0], result[2]) = (N.l, N.r)
        (N.l, N.r) = (self.leaf, self.leaf)
        result[1] = N
      
      proc join*[T:RedBlackTree](self: var T, TL, k, TR:T.Node):T.Node =
        proc joinRightRB[T:RedBlackTree](self:var T, TL, k, TR:T.Node):T.Node =
          doAssert TL.level >= TR.level
          if TL.color == Color.black and TL.level == TR.level:
            k.color = Color.red
            (k.l, k.r) = (TL, TR)
            k.p = nil
            if not k.l.isLeaf: k.l.p = k
            if not k.r.isLeaf: k.r.p = k
            self.update(k)
            return k
          TL.r.p = nil
          TL.r = self.joinRightRB(TL.r, k, TR)
          if not TL.r.isLeaf: TL.r.p = TL
          #if TL.color == Color.black and TL.r.r.color == Color.red:
          result = TL
          if TL.color == Color.black and TL.r.r.color == Color.red and TL.r.color == Color.red:
            TL.r.r.color = Color.black
            result = self.rotateLeft(TL)
          self.update(result)
        proc joinLeftRB[T:RedBlackTree](self:var T, TL, k, TR:T.Node):T.Node =
          doAssert TL.level <= TR.level
          if TR.color == Color.black and TR.level == TL.level:
            k.color = Color.red
            (k.l, k.r) = (TL, TR)
            k.p = nil
            if not k.l.isLeaf: k.l.p = k
            if not k.r.isLeaf: k.r.p = k
            self.update(k)
            return k
          TR.l.p = nil
          TR.l = self.joinLeftRB(TL, k, TR.l)
          if not TR.l.isLeaf: TR.l.p = TR
          result = TR
          # if TR.color == Color.black and TR.l.l.color == Color.red:
          if TR.color == Color.black and TR.l.l.color == Color.red and TR.l.color == Color.red:
            TR.l.l.color = Color.black
            result = self.rotateRight(TR)
          self.update(result)
        if TL.level > TR.level:
          result = self.joinRightRB(TL, k, TR)
          if result.color == Color.red and result.r.color == Color.red:
            result.color = Color.black
        elif TL.level < TR.level:
          result = self.joinLeftRB(TL, k, TR)
          if result.color == Color.red and result.l.color == Color.red:
            result.color = Color.black
        else:
          (k.l, k.r) = (TL, TR)
          if not k.l.isLeaf: k.l.p = k
          if not k.r.isLeaf: k.r.p = k
          if TL.color == Color.black and TR.color == Color.black:
            k.color = Color.red
          else:
            k.color = Color.black
          result = k
          self.update(result)
        result.color = Color.black
        result.p = nil
      
      proc join*[T:RedBlackTree](self: var T, L, R: T.Node):T.Node =
        proc splitLast(self: var T, k:T.Node):(T.Node, T.Node) = 
          var (L, k, R) = self.expose(k)
          if R.isLeaf:
            return (L, k)
          else:
            var (N, k2) = self.splitLast(R)
            return (self.join(L, k, N), k2)
      
        if L.isLeaf:
          R.color = Color.black
          return R
        else:
          var (L2, k) = self.splitLast(L)
          L2.color = Color.black
          return self.join(L2, k, R)
      
      proc split3*(self:var RedBlackTree, N:self.Node):auto =
        # Nを中心に左右に分ける
        if N.isLeaf:
          doAssert false
          #return (self.leaf, false, self.leaf) # !!!
        var path:seq[(self.Node, int)]
        block:
          var N = N
          while N.p != nil:
            var P = N.p
            if P.l == N:
              path.add (P, 0)
            elif P.r == N:
              path.add (P, 1)
            else:
              doAssert false
            N = P
        var (L, N, R) = self.expose(N)
        for (P, d) in path:
          if d == 0:
            P.r.p = nil
            P.r.color = Color.black
            R = self.join(R, P, P.r)
          else:
            P.l.p = nil
            P.l.color = Color.black
            L = self.join(P.l, P, L)
        return (L, R)
      
      proc split*(self:var RedBlackTree, N:self.Node):auto =
        var prev = self.newNode(self.Node(nil))
        self.insert(prev, N)
        return self.split3(prev)
      
      proc insert_by_join*[T:RedBlackTree](self: var T, node, next:T.Node):T.Node = # nextの前にnodeを入れる
        result = node
        var
          parent:T.Node
          d:int # left: 0, right: 1
        if next.l == self.leaf:
          # insert at next.l
          parent = next
          d = 0
        else:
          var curr = next.l.rightMost
          # insert at curr.r
          parent = curr
          d = 1
        var node = self.join(self.leaf, node, self.leaf)
        while parent != nil:
          var
            grand_parent = parent.p
            d2:int
          if grand_parent != nil:
            if grand_parent.l == parent:
              d2 = 0
            else:
              d2 = 1
          #var (L, p, R) = self.expose(parent)
          if d == 0:
            if parent.r != self.leaf:
              parent.r.p = nil
              parent.r.color = Color.black
            parent.l = self.leaf
            parent = self.join(node, parent, parent.r)
          else:
            if parent.l != self.leaf:
              parent.l.p = nil
              parent.l.color = Color.black
            parent.r = self.leaf
            parent = self.join(parent.l, parent, node)
    
          node = parent
          parent = grand_parent
          d = d2
        self.root = node
      proc insert_by_join*[T:RedBlackTree](self: var T, next:T.Node, key:T.K):T.Node = # nextの前にnodeを入れる
        self.insert_by_join(self.newNode(T.Node(nil), key), next)
    
    
      proc len*[T:RedBlackTree](self: T): int =
        return self.root.cnt
      proc empty*[T:RedBlackTree](self: T): bool =
        return self.len == 0
      
      iterator iterOrder*[T:RedBlackTree](self: T): auto =
        var node = self.root
        var stack: seq[T.Node] = @[]
        while stack.len() != 0 or node != self.leaf:
          if node != self.leaf:
            stack.add(node)
            node = node.l
          else:
            node = stack.pop()
            #if node == self.End: break
            yield node.key
            node = node.r
      {.pop.}
      discard
    type
      SortedSetType*[K; Countable; p: static[tuple]] = SortedTree[RedBlackTree[K], RedBlackTreeNode[K], MULTI_FALSE, K, void, p]
      SortedMultiSetType*[K; Countable; p: static[tuple]] = SortedTree[RedBlackTree[K], RedBlackTreeNode[K], MULTI_TRUE, K, void, p]
      SortedMapType*[K; V: not void; Countable; p: static[tuple]] = SortedTree[RedBlackTree[(K, V)], RedBlackTreeNode[(K, V)], MULTI_FALSE, K, V, p]
      SortedMultiMapType*[K; V: not void; Countable; p: static[tuple]] = SortedTree[RedBlackTree[(K, V)], RedBlackTreeNode[(K, V)], MULTI_TRUE, K, V, p]

    type SetOrMap = SortedMultiSetType or SortedSetType or SortedMultiMapType or SortedMapType
    proc init*[Tree: SetOrMap](self: var Tree) =
      when Tree.V is void:
        type T = Tree.K
      else:
        type T = (Tree.K, Tree.V)
      type Node = Tree.Node
      var End = Node(id: -2)
      End.cnt = 0
      End.color = Color.black
      self.End = End
      self.tree.init(End)
    proc empty*[Tree: SetOrMap](self: Tree): bool = self.tree.empty()
    proc len*[Tree: SetOrMap](self: Tree): int = self.tree.len()
  elif USE_SPLAY_TREE:
    # include atcoder/extra/structure/splay_tree
    type
      SortedSetType*[K; Countable; p: static[tuple]] = SortedTree[SplayTree[K], SplayTreeNode[K, void, void, void], MULTI_FALSE, K, void, p]
      SortedMultiSetType*[K; Countable; p: static[tuple]] = SortedTree[SplayTree[K], SplayTreeNode[K, void, void, void], MULTI_TRUE, K, void, p]
      SortedMapType*[K; V: not void; Countable; p: static[tuple]] = SortedTree[SplayTree[(K, V)], SplayTreeNode[(K, V), void, void, void], MULTI_FALSE, K, V, p]
      SortedMultiMapType*[K; V: not void; Countable; p: static[tuple]] = SortedTree[SplayTree[(K, V)], SplayTreeNode[(K, V), void, void, void], MULTI_TRUE, K,
          V, p]

    type SetOrMap = SortedMultiSetType or SortedSetType or SortedMultiMapType or SortedMapType
    proc init*[Tree: SetOrMap](self: var Tree) =
      when Tree.V is void:
        type T = Tree.K
      else:
        type T = (Tree.K, Tree.V)
      var End = Tree.Node(id: -2)
      End.cnt = 1 # be carefull!!!!!!!!!!!!!!!
      self.End = End
      self.tree.init(End)
    proc len*[Tree: SetOrMap](self: Tree): int = self.tree.root.cnt - 1
    proc empty*[Tree: SetOrMap](self: Tree): bool = self.len == 0

  else:
    # include atcoder/extra/structure/randomized_binary_search_tree_with_parent

    type
      SortedSetType*[K; Countable; p: static[tuple]] = SortedTree[RandomizedBinarySearchTree[K], RandomizedBinarySearchTree[K].Node, MULTI_FALSE, K, void, p]
      SortedMultiSetType*[K; Countable; p: static[tuple]] = SortedTree[RandomizedBinarySearchTree[K], RBSTNode[K, void, void], MULTI_TRUE, K, void, p]
      SortedMapType*[K; V; Countable; p: static[tuple]] = SortedTree[RandomizedBinarySearchTree[(K, V)], RBSTNode[(K, V), void, void], MULTI_FALSE, K, V, p]
      SortedMultiMapType*[K; V; Countable; p: static[tuple]] = SortedTree[RandomizedBinarySearchTree[(K, V)], RBSTNode[(K, V), void, void], MULTI_TRUE, K, V, p]

    type SetOrMap = SortedMultiSetType or SortedSetType or SortedMultiMapType or SortedMapType

    proc init*[Tree: SetOrMap](self: var Tree) =
      when Tree.V is void:
        type T = Tree.K
      else:
        type T = (Tree.K, Tree.V)
      var End = Tree.Node(id: -2)
      End.cnt = 1 # be carefull!!!!!!!!!!!!!!!
      self.End = End
      self.tree.init(End)
#      end_node.l = self.leaf; end_node.r = self.leaf;

  #  RBST(sz, [&](T x, T y) { return x; }, T()) {}

    # proc len*[Tree: SetOrMap](self: Tree): int = self.tree.len() - 1
    # proc empty*[Tree: SetOrMap](self: Tree): bool = self.len() == 0
  #      doAssert self.len + 1 == self.tree.check_tree()

  #    proc `$`*(self: SetOrMap):string = self.Tree(self).to_string(self.root)
  {.pop.}
  proc check_tree*(self: SetOrMap) = self.tree.check_tree

  template SortedSet*(K: typedesc; countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): typedesc =
    SortedSetType[K, when countable: int else: void, (comp, )]
  template SortedMultiSet*(K: typedesc; countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): typedesc =
    SortedMultiSetType[K, when countable: int else: void, (comp, )]
  template SortedMap*(K: typedesc; V: typedesc[not void]; countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): typedesc =
    SortedMapType[K, V, when countable: int else: void, (comp, )]
  template SortedMultiMap*(K: typedesc; V: typedesc[not void]; countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): typedesc =
    SortedMultiMapType[K, V, when countable: static[bool] = false, (comp, )]

  proc default*[T: SetOrMap](self: typedesc[T]): T =
    result.init()
  template initSortedSet*[K](countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): auto =
    block:
      var r: SortedSetType[K, when countable: int else: void, (comp, )]
      r.init()
      r
  template initSortedSet*[K](a: openArray[K]; countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): auto =
    block:
      var s = initSortedSet[K](countable, comp)
      for t in a: s.insert(t)
      s

  template initSortedMultiSet*[K](countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): auto =
    block:
      var r: SortedMultiSetType[K, when countable: int else: void, (comp, )]
      r.init()
      r
  template initSortedMultiSet*[K](a: openArray[K]; countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): auto =
    block:
      var s = initSortedMultiSet[K](countable, comp)
      for t in a: s.insert(t)
      s

  template initSortedMap*[K; V: not void](countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): auto =
    block:
      var r: SortedMapType[K, V, when countable: int else: void, (comp, )]
      r.init()
      r
  template initSortedMap*[K; V: not void](a: openArray[(K, V)]; countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): auto =
    block:
      var s = initSortedMap[K, V](countable, comp)
      for p in a: s.insert(p)
      s

  template initSortedMultiMap*[K; V: not void](countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): auto =
    block:
      var r: SortedMultiMapType[K, V, when countable: int else: void, (comp, )]
      r.init()
      r
  template initSortedMultiMap*[K; V: not void](a: openArray[(K, V)]; countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil): auto =
    block:
      var s = initSortedMultiMap[K, V](countable, comp)
      for p in a: s.insert(p)
      s

  proc `$`*(self: SetOrMap): string =
    var a = newSeq[string]()
    var node = self.tree.root
    var stack: seq[self.Node] = @[]
    while stack.len() != 0 or not node.isLeaf:
      if not node.isLeaf:
        if node != self.End:
          stack.add(node)
        node = node.l
      else:
        node = stack.pop()
        when self.V is void:
          var k = ""
          k.addQuoted(node.key)
          a &= k
        else:
          var k, v = ""
          k.addQuoted(node.key[0])
          v.addQuoted(node.key[1])
          a &= k & ": " & v
        node = node.r
    return "{" & a.join(", ") & "}"
  discard
import std/times
import std/random
import macros

macro ImportExpand(s: untyped):
    untyped = parseStmt($s[2])
ImportExpand "cplib/tmpl/Ang107.nim" <=== "when not declared CPLIB_TMPL_Ang107:\n    const CPLIB_TMPL_Ang107* = 1\n    {.warning[UnusedImport]: off.}\n    {.hint[XDeclaredButNotUsed]: off.}\n    import algorithm\n    import sequtils\n    import tables\n    import macros\n    import math\n    import sets\n    import strutils\n    import strformat\n    import sugar\n    import heapqueue\n    import streams\n    import deques\n    import bitops\n    import std/lenientops\n    import options\n    #入力系\n    proc scanf(formatstr: cstring){.header: \"<stdio.h>\", varargs.}\n    proc getchar(): char {.importc: \"getchar_unlocked\", header: \"<stdio.h>\", discardable.}\n    proc ii(): int {.inline.} = scanf(\"%lld\\n\", addr result)\n    proc lii(N: int): seq[int] {.inline.} = newSeqWith(N, ii())\n    proc si(): string {.inline.} =\n        result = \"\"\n        var c: char\n        while true:\n            c = getchar()\n            if c == ' ' or c == '\\n':\n                break\n            result &= c\n    #chmin,chmax\n    template `max=`(x, y) = x = max(x, y)\n    template `min=`(x, y) = x = min(x, y)\n    #bit演算\n    proc `%`(x: int, y: int): int = (((x mod y)+y) mod y)\n    proc `//`(x: int, y: int): int = (((x) - (x%y)) div (y))\n    proc `%=`(x: var int, y: int): void = x = x%y\n    proc `//=`(x: var int, y: int): void = x = x//y\n    proc `**`(x: int, y: int): int = x^y\n    proc `**=`(x: var int, y: int): void = x = x^y\n    proc `^`(x: int, y: int): int = x xor y\n    proc `|`(x: int, y: int): int = x or y\n    proc `&`(x: int, y: int): int = x and y\n    proc `>>`(x: int, y: int): int = x shr y\n    proc `<<`(x: int, y: int): int = x shl y\n    proc `~`(x: int): int = not x\n    proc `^=`(x: var int, y: int): void = x = x ^ y\n    proc `&=`(x: var int, y: int): void = x = x & y\n    proc `|=`(x: var int, y: int): void = x = x | y\n    proc `>>=`(x: var int, y: int): void = x = x >> y\n    proc `<<=`(x: var int, y: int): void = x = x << y\n    proc `[]`(x: int, n: int): bool = (x and (1 shl n)) != 0\n    #便利な変換\n    proc `!`(x: char, a = '0'): int = int(x)-int(a)\n    #定数\n    const INF = int(3300300300300300491)\n    #converter\n\n    #range\n    iterator range(start: int, ends: int, step: int): int =\n        var i = start\n        if step < 0:\n            while i > ends:\n                yield i\n                i += step\n        elif step > 0:\n            while i < ends:\n                yield i\n                i += step\n    iterator range(ends: int): int = (for i in 0..<ends: yield i)\n    iterator range(start: int, ends: int): int = (for i in\n            start..<ends: yield i)\n"

let start = cpuTime()
#乱数リセット
randomize()

proc input(): (int, int, int, seq[seq[int]], int) =
    let
        W = ii()
        D = ii()
        N = ii()
    var
        A = newSeqOfCap[newSeq[int](N)](D)
        avr_amari = 0

    # echo D, N
    for i in 0 ..< D:
        A.add(lii(N))
        echo A.len()

    # echo A
    for i in A:
        avr_amari += 1000000 - sum(i)
    avr_amari = int(avr_amari / D / 100000)

    echo avr_amari
    return (W, D, N, A, avr_amari)

proc put(a: seq[int], h: seq[int], hight: seq[int]): (seq[array[4, int]], int, bool) =
    var
        is_over = false
        w = newSeq[int](h.len())
        rslt = newSeqOfCap[array[4, int]](a.len())
        cost = 0
    type Tmp = (int, int, array[4, int])
    var tmp: Tmp
    for i in a.reversed():
        var
            puted = false
            aspect_min = 1000000000.0
        for j in 0..<h.len:
            var width = -(-i // h[j])
            if w[j] + width <= 1000:
                puted = true
                var aspect = max(width, h[j]) / min(width, h[j])
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
                var width = min(1000 - w[j], -(-i // h[j]))
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
    cost -= 1000
    for i in 0..<w.len()-1:
        if w[i] == 0 and w[i+1] == 0:
            cost += 1000

    rslt.reverse()
    return (rslt, cost, is_over)

proc get_ans(N: int, D: int, A: seq[seq[int]], h: seq[int], height: seq[int]): (seq[seq[array[4, int]]], int, seq[int]) =
    var
        ans = newSeqWith(D, newSeqOfCap[array[4, int]](N))
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
            if ta[ans[i][j][0]] < ans[i][j][3]:
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
        var give_idx, take_idx = rand(1..<h.len())
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



        if no_over_got:
            if over_n.len() == 0:
                var bunsan_n = 0
                for i in h_n:
                    bunsan_n += (i-avr)**2
                if bunsan > bunsan_n:
                    bunsan = bunsan_n
                    h = h_n
                    height = height_n
                    cost = cost_n
                    ans = ans_n
                    over = over_n
        else:
            if cost > cost_n:
                h = h_n
                height = height_n
                cost = cost_n
                ans = ans_n
                over = over_n

        cnt += 1
        if cnt % 100 == 0:
            if cpuTime() - tmp_time > time_limit:
                return (ans, cost, over, h, height)



proc get_h(D: int, N: int, A: seq[seq[int]], ): (seq[seq[array[4, int]]], seq[seq[array[4, int]]], seq[int], seq[int], seq[int], seq[int]) =
    var
        cost = 10 ** 18
        h = @[1000]
        (ans_ins, _, over_ins, _, _) = yamanobori(N, D, A, h, 0)
        l = int(sqrt(float32(N)))-1
        r = -(-N//2)+1

    var
        (ans_n, cost_n, over_n, h_n, height_n) = yamanobori(D, N, A, h, 0.3)
        rs_ans: seq[seq[array[4, int]]]
        rs_cost: int
        rs_over: seq[int]
        rs_h: seq[int]
        rs_height: seq[int]

    while r - l > 1:
        var
            h_num = (l+r)//2
            w_num = -(-N / h_num)
            avr = newSeqOfCap[float](h_num)
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

        if len(over_n) > 0:
            r = h_num
        else:
            l = h_num

        if cost > cost_n:
            var
                rs_ans = ans_n
                rs_cost = cost_n
                rs_over = over_n
                rs_h = h_n
                rs_hight = height_n

    for i in rs_over:
        if i notin over_ins:
            rs_ans[i] = ans_ins[i]

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

        for j in range(h.len()):
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
        return

    type
        st_type = SegTreeType[int]((a: int, b: int)=>max(a, b), () => -1)
    var
        sts: seq[st_type]
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
            Idx_l = N-2
            Idx_r = N

        var
            prv_same = newseq[int](0)

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

                if Idx_r > len(ans) or Idx_l < 0:
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

                if Idx_r > len(ans) or Idx_l < 0:
                    break
    return (more_good, rslt)

proc is_OK(same: seq[array[2, int]], other: seq[int], Idx: int, h, height: seq[int]): (bool, seq[array[4, int]]) =
    var
        is_over = false
        w = newSeq[int](h.len())
        rslt = newSeq[array[4, int]](same.len()+other.len())

    for (i, idx) in same:
        var
            aspect_min = 10000000.0
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

    return (true, rslt)

proc greedy1(D, N: int, A: seq[seq[int]], ans: seq[seq[array[4, int]]], h, height, over: seq[int]): (array[2, int], array[2, seq[seq[array[4, int]]]]) =
    var
        more_good = [0, 0]

    for mode in [0, 1]:
        for i in countup(mode, len(ans)-1, 2):
            if i in over or i+1 in over:
                continue

            var
                tmp = newSeqOfCap[int](N)
            for i in 0..<N:
                tmp.add(i)
            var
                p_idx = initSortedSet[int](tmp, true)
                p = initSortedMultiSet[int](A[i], true)
                q_idx = initSortedSet[int](tmp, true)
                q = initSortedMultiSet[int](A[i+1], true)

            echo $(p_idx, p)



proc output(ans: seq[seq[array[4, int]]]) =
    for i in ans:
        for j in i:
            echo $(j)





var
    (W, D, N, A, avr_amari) = input()
echo (W, D, N, A, avr_amari)

var
    (ans, ans_ins, h, height, over, over_ins) = get_h(D, N, A)
    A_tenti = newSeqWith(N, newseq[int](D))

echo ans
# discard output(ans)
