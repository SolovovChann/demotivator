from typing import Protocol, TypeAlias


class Font(Protocol):
    def getmask(
        self,
        text: str | bytes,
        mode: str = ...,
        direction=...,
        features=...
    ): ...


RGB: TypeAlias = tuple[int, int, int] | tuple[int, int, int, int]

Ink: TypeAlias = str | int | RGB

Color: TypeAlias = float | Ink | tuple[float] | tuple[int]
