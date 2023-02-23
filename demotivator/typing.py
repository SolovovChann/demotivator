from typing import Protocol


class Font(Protocol):
    def getmask(
        self,
        text: str | bytes,
        mode: str = ...,
        direction=...,
        features=...
    ): ...
