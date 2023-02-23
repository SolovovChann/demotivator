from dataclasses import dataclass


@dataclass
class ImageIndentation:
    left: int
    top: int
    right: int
    bottom: int
