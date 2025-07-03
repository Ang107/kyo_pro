# int_masked_py39.py  ――  Python 3.9 互換版
import random
import builtins
import collections
import collections.abc as _abc
from typing import Optional, Any, Iterable, Mapping


# 内部⇔外部変換の共通基盤 ------------------------------------------------------
class _IntXorMixin:
    def __init__(self, *, mask: int) -> None:
        self._mask = mask  # インスタンスごとに固定

    def _enc(self, x: int) -> int:
        if not isinstance(x, int):
            raise TypeError("このクラスは int しか扱えません")
        return x ^ self._mask

    def _dec(self, x: int) -> int:
        return x ^ self._mask

    @property
    def mask(self) -> int:
        return self._mask


# Sentinel（内部用）
_MISSING = object()


# IntDict --------------------------------------------------------------------
class IntDict(_IntXorMixin, dict):
    def __init__(self, *args: Any, mask: int, **kwargs: Any) -> None:
        _IntXorMixin.__init__(self, mask=mask)
        dict.__init__(self)
        if args or kwargs:
            self.update(*args, **kwargs)

    # 基本演算
    def __setitem__(self, k: int, v: Any) -> None:
        super().__setitem__(self._enc(k), v)

    def __getitem__(self, k: int) -> Any:
        return super().__getitem__(self._enc(k))

    def __delitem__(self, k: int) -> None:
        super().__delitem__(self._enc(k))

    def __contains__(self, k: object) -> bool:
        return isinstance(k, int) and super().__contains__(self._enc(k))

    # メソッド
    def get(self, k: int, default: Any = None) -> Any:
        return super().get(self._enc(k), default)

    def setdefault(self, k: int, default: Any = None) -> Any:
        return super().setdefault(self._enc(k), default)

    def pop(self, k: int, default: Any = _MISSING) -> Any:
        enc = self._enc(k)
        if default is _MISSING:
            return super().pop(enc)
        return super().pop(enc, default)

    def update(self, *args: Any, **kwargs: Any) -> None:
        if args:
            other = args[0]
            if isinstance(other, Mapping):
                for k, v in other.items():
                    self[k] = v
            else:
                for k, v in other:
                    self[k] = v
        for k, v in kwargs.items():
            self[k] = v

    # 反復
    def keys(self):
        for enc in super().keys():
            yield self._dec(enc)

    def items(self):
        for enc, v in super().items():
            yield self._dec(enc), v

    def values(self):
        return super().values()

    def __iter__(self):
        return self.keys()

    # 表示
    def __repr__(self) -> str:
        body = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"{self.__class__.__name__}({{{body}}}, mask={self._mask})"


# IntSet ---------------------------------------------------------------------
class IntSet(_IntXorMixin, set):
    def __init__(self, iterable: Optional[Iterable[int]] = None, *, mask: int) -> None:
        _IntXorMixin.__init__(self, mask=mask)
        if iterable is not None:
            super().__init__(self._enc(x) for x in iterable)
        else:
            super().__init__()

    def add(self, x: int) -> None:
        super().add(self._enc(x))

    def discard(self, x: int) -> None:
        super().discard(self._enc(x))

    def remove(self, x: int) -> None:
        super().remove(self._enc(x))

    def __contains__(self, x: object) -> bool:
        return isinstance(x, int) and super().__contains__(self._enc(x))

    def __iter__(self):
        for enc in super().__iter__():
            yield self._dec(enc)

    def __repr__(self) -> str:
        elems = ", ".join(repr(x) for x in self)
        return f"{self.__class__.__name__}({{{elems}}}, mask={self._mask})"


# IntDefaultDict -------------------------------------------------------------
class IntDefaultDict(_IntXorMixin, collections.defaultdict):
    def __init__(
        self,
        default_factory: Optional[Any] = None,
        *args: Any,
        mask: int,
        **kwargs: Any,
    ) -> None:
        _IntXorMixin.__init__(self, mask=mask)
        collections.defaultdict.__init__(self, default_factory)
        if args or kwargs:
            self.update(*args, **kwargs)

    # 基本演算
    def __setitem__(self, k: int, v: Any) -> None:
        super().__setitem__(self._enc(k), v)

    def __getitem__(self, k: int) -> Any:
        return super().__getitem__(self._enc(k))

    def __delitem__(self, k: int) -> None:
        super().__delitem__(self._enc(k))

    def __contains__(self, k: object) -> bool:
        return isinstance(k, int) and super().__contains__(self._enc(k))

    # defaultdict 固有
    def __missing__(self, k: int):
        if self.default_factory is None:
            raise KeyError(k)
        self[k] = self.default_factory()
        return self[k]

    # 反復
    def keys(self):
        for enc in super().keys():
            yield self._dec(enc)

    def items(self):
        for enc, v in super().items():
            yield self._dec(enc), v

    def __iter__(self):
        return self.keys()

    def __repr__(self) -> str:
        body = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"{self.__class__.__name__}({{{body}}}, mask={self._mask})"


# ビルトイン置換／復元 --------------------------------------------------------
_originals = {}


def enable_int_masking(bit_width: int = 64, *, mask: Optional[int] = None) -> None:
    """dict / set / collections.defaultdict を int 対応版に差し替える"""
    global _originals
    if _originals:  # 既にパッチ済み
        return

    m = random.getrandbits(bit_width) if mask is None else mask

    _originals = {
        "dict": builtins.dict,
        "set": builtins.set,
        "defaultdict": collections.defaultdict,
    }

    builtins.dict = lambda *a, **kw: IntDict(*a, mask=m, **kw)  # type: ignore
    builtins.set = lambda *a, **kw: IntSet(*a, mask=m, **kw)  # type: ignore
    collections.defaultdict = lambda *a, **kw: IntDefaultDict(*a, mask=m, **kw)  # type: ignore


def disable_int_masking() -> None:
    """enable_int_masking での置換を元に戻す"""
    global _originals
    if not _originals:
        return
    builtins.dict = _originals["dict"]
    builtins.set = _originals["set"]
    collections.defaultdict = _originals["defaultdict"]
    _originals.clear()


from collections import defaultdict

mask = random.randrange(1 << 63)


def h(x):
    return x ^ mask


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dd = defaultdict(int)
    for i in a:
        dd[h(i)] += 1
    tmp = sorted(dd.items(), key=lambda x: h(x[0]))
    ok = False
    prev = -1
    cnt = 0
    best_l, best_r = -1, -1
    diff = -1
    l, r = -1, -1

    for i, j in tmp:
        i = h(i)
        if ok:
            if prev + 1 == i and j >= k:
                r = i
                prev = i
            else:
                ok = False
        if not ok:
            if j >= k:
                ok = True
                prev = i
                l = i
                r = i
        if diff < r - l and l != -1:
            best_l = l
            best_r = r
            diff = r - l
        # print(l, r)
    if best_l != -1:
        print(best_l, best_r)
    else:
        print(-1)
