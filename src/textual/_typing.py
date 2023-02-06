import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:  # pragma: no cover
    from typing_extensions import TypeAlias

if sys.version_info >= (3, 8):
    from typing import Final, Literal, Protocol, TypedDict, runtime_checkable
else:
    from typing_extensions import Final, Literal, Protocol, TypedDict, runtime_checkable

__all__ = [
    "Final",
    "Literal",
    "Protocol",
    "runtime_checkable",
    "TypeAlias",
    "TypedDict",
]
