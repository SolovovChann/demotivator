from demotivator.indent import ImageIndentation
from demotivator.typing import Color, Font, Ink


class Demotivator:
    font: Font

    border: ImageIndentation
    margin: ImageIndentation
    padding: ImageIndentation

    background: Color
    foreground: Ink

    def __init__(
        self,
        font: Font,
        border: ImageIndentation,
        margin: ImageIndentation,
        padding: ImageIndentation,
        background: Color,
        foreground: Ink,
    ) -> None:
        self.font = font
        self.border = border
        self.margin = margin
        self.padding = padding
        self.background = background
        self.foreground = foreground
