import enum
import sys
from sre_constants import error as error
from typing import Any, AnyStr, Callable, Generic, Iterator, Mapping, Tuple, TypeVar, Union, overload
from typing_extensions import Literal as _Literal

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")

# ----- re variables and constants -----
if sys.version_info >= (3, 7):
    class Match(Generic[AnyStr]):
        pos: int
        endpos: int
        lastindex: int | None
        lastgroup: AnyStr | None
        string: AnyStr

        # The regular expression object whose match() or search() method produced
        # this match instance.
        re: Pattern[AnyStr]
        def expand(self, template: AnyStr) -> AnyStr: ...
        # group() returns "AnyStr" or "AnyStr | None", depending on the pattern.
        @overload
        def group(self, __group: _Literal[0] = ...) -> AnyStr: ...
        @overload
        def group(self, __group: str | int) -> AnyStr | Any: ...
        @overload
        def group(self, __group1: str | int, __group2: str | int, *groups: str | int) -> Tuple[AnyStr | Any, ...]: ...
        # Each item of groups()'s return tuple is either "AnyStr" or
        # "AnyStr | None", depending on the pattern.
        @overload
        def groups(self) -> Tuple[AnyStr | Any, ...]: ...
        @overload
        def groups(self, default: _T) -> Tuple[AnyStr | _T, ...]: ...
        # Each value in groupdict()'s return dict is either "AnyStr" or
        # "AnyStr | None", depending on the pattern.
        @overload
        def groupdict(self) -> dict[str, AnyStr | Any]: ...
        @overload
        def groupdict(self, default: _T) -> dict[str, AnyStr | _T]: ...
        def start(self, __group: int | str = ...) -> int: ...
        def end(self, __group: int | str = ...) -> int: ...
        def span(self, __group: int | str = ...) -> tuple[int, int]: ...
        @property
        def regs(self) -> Tuple[tuple[int, int], ...]: ...  # undocumented
        # __getitem__() returns "AnyStr" or "AnyStr | None", depending on the pattern.
        @overload
        def __getitem__(self, __key: _Literal[0]) -> AnyStr: ...
        @overload
        def __getitem__(self, __key: int | str) -> AnyStr | Any: ...
        if sys.version_info >= (3, 9):
            def __class_getitem__(cls, item: Any) -> GenericAlias: ...
    class Pattern(Generic[AnyStr]):
        flags: int
        groupindex: Mapping[str, int]
        groups: int
        pattern: AnyStr
        def search(self, string: AnyStr, pos: int = ..., endpos: int = ...) -> Match[AnyStr] | None: ...
        def match(self, string: AnyStr, pos: int = ..., endpos: int = ...) -> Match[AnyStr] | None: ...
        def fullmatch(self, string: AnyStr, pos: int = ..., endpos: int = ...) -> Match[AnyStr] | None: ...
        def split(self, string: AnyStr, maxsplit: int = ...) -> list[AnyStr]: ...
        def findall(self, string: AnyStr, pos: int = ..., endpos: int = ...) -> list[Any]: ...
        def finditer(self, string: AnyStr, pos: int = ..., endpos: int = ...) -> Iterator[Match[AnyStr]]: ...
        @overload
        def sub(self, repl: AnyStr, string: AnyStr, count: int = ...) -> AnyStr: ...
        @overload
        def sub(self, repl: Callable[[Match[AnyStr]], AnyStr], string: AnyStr, count: int = ...) -> AnyStr: ...
        @overload
        def subn(self, repl: AnyStr, string: AnyStr, count: int = ...) -> tuple[AnyStr, int]: ...
        @overload
        def subn(self, repl: Callable[[Match[AnyStr]], AnyStr], string: AnyStr, count: int = ...) -> tuple[AnyStr, int]: ...
        if sys.version_info >= (3, 9):
            def __class_getitem__(cls, item: Any) -> GenericAlias: ...

else:
    from typing import Match, Pattern

class RegexFlag(enum.IntFlag):
    A: int
    ASCII: int
    DEBUG: int
    I: int
    IGNORECASE: int
    L: int
    LOCALE: int
    M: int
    MULTILINE: int
    S: int
    DOTALL: int
    X: int
    VERBOSE: int
    U: int
    UNICODE: int
    T: int
    TEMPLATE: int

A = RegexFlag.A
ASCII = RegexFlag.ASCII
DEBUG = RegexFlag.DEBUG
I = RegexFlag.I
IGNORECASE = RegexFlag.IGNORECASE
L = RegexFlag.L
LOCALE = RegexFlag.LOCALE
M = RegexFlag.M
MULTILINE = RegexFlag.MULTILINE
S = RegexFlag.S
DOTALL = RegexFlag.DOTALL
X = RegexFlag.X
VERBOSE = RegexFlag.VERBOSE
U = RegexFlag.U
UNICODE = RegexFlag.UNICODE
T = RegexFlag.T
TEMPLATE = RegexFlag.TEMPLATE
_FlagsType = Union[int, RegexFlag]

if sys.version_info < (3, 7):
    # undocumented
    _pattern_type: type

@overload
def compile(pattern: AnyStr, flags: _FlagsType = ...) -> Pattern[AnyStr]: ...
@overload
def compile(pattern: Pattern[AnyStr], flags: _FlagsType = ...) -> Pattern[AnyStr]: ...
@overload
def search(pattern: AnyStr, string: AnyStr, flags: _FlagsType = ...) -> Match[AnyStr] | None: ...
@overload
def search(pattern: Pattern[AnyStr], string: AnyStr, flags: _FlagsType = ...) -> Match[AnyStr] | None: ...
@overload
def match(pattern: AnyStr, string: AnyStr, flags: _FlagsType = ...) -> Match[AnyStr] | None: ...
@overload
def match(pattern: Pattern[AnyStr], string: AnyStr, flags: _FlagsType = ...) -> Match[AnyStr] | None: ...

# New in Python 3.4
@overload
def fullmatch(pattern: AnyStr, string: AnyStr, flags: _FlagsType = ...) -> Match[AnyStr] | None: ...
@overload
def fullmatch(pattern: Pattern[AnyStr], string: AnyStr, flags: _FlagsType = ...) -> Match[AnyStr] | None: ...
@overload
def split(pattern: AnyStr, string: AnyStr, maxsplit: int = ..., flags: _FlagsType = ...) -> list[AnyStr | Any]: ...
@overload
def split(pattern: Pattern[AnyStr], string: AnyStr, maxsplit: int = ..., flags: _FlagsType = ...) -> list[AnyStr | Any]: ...
@overload
def findall(pattern: AnyStr, string: AnyStr, flags: _FlagsType = ...) -> list[Any]: ...
@overload
def findall(pattern: Pattern[AnyStr], string: AnyStr, flags: _FlagsType = ...) -> list[Any]: ...

# Return an iterator yielding match objects over all non-overlapping matches
# for the RE pattern in string. The string is scanned left-to-right, and
# matches are returned in the order found. Empty matches are included in the
# result unless they touch the beginning of another match.
@overload
def finditer(pattern: AnyStr, string: AnyStr, flags: _FlagsType = ...) -> Iterator[Match[AnyStr]]: ...
@overload
def finditer(pattern: Pattern[AnyStr], string: AnyStr, flags: _FlagsType = ...) -> Iterator[Match[AnyStr]]: ...
@overload
def sub(pattern: AnyStr, repl: AnyStr, string: AnyStr, count: int = ..., flags: _FlagsType = ...) -> AnyStr: ...
@overload
def sub(
    pattern: AnyStr, repl: Callable[[Match[AnyStr]], AnyStr], string: AnyStr, count: int = ..., flags: _FlagsType = ...
) -> AnyStr: ...
@overload
def sub(pattern: Pattern[AnyStr], repl: AnyStr, string: AnyStr, count: int = ..., flags: _FlagsType = ...) -> AnyStr: ...
@overload
def sub(
    pattern: Pattern[AnyStr], repl: Callable[[Match[AnyStr]], AnyStr], string: AnyStr, count: int = ..., flags: _FlagsType = ...
) -> AnyStr: ...
@overload
def subn(pattern: AnyStr, repl: AnyStr, string: AnyStr, count: int = ..., flags: _FlagsType = ...) -> tuple[AnyStr, int]: ...
@overload
def subn(
    pattern: AnyStr, repl: Callable[[Match[AnyStr]], AnyStr], string: AnyStr, count: int = ..., flags: _FlagsType = ...
) -> tuple[AnyStr, int]: ...
@overload
def subn(
    pattern: Pattern[AnyStr], repl: AnyStr, string: AnyStr, count: int = ..., flags: _FlagsType = ...
) -> tuple[AnyStr, int]: ...
@overload
def subn(
    pattern: Pattern[AnyStr], repl: Callable[[Match[AnyStr]], AnyStr], string: AnyStr, count: int = ..., flags: _FlagsType = ...
) -> tuple[AnyStr, int]: ...
def escape(pattern: AnyStr) -> AnyStr: ...
def purge() -> None: ...
def template(pattern: AnyStr | Pattern[AnyStr], flags: _FlagsType = ...) -> Pattern[AnyStr]: ...
