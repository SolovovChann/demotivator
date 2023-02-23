from PIL import Image, ImageDraw

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

    def demotivate(self, image: Image.Image, caption: str) -> Image.Image:
        padding = self.padding.expand(image, self.background)
        bordered = self.border.expand(padding, self.foreground)
        margined = self.margin.expand(bordered, self.background)

        text_x = int(margined.width / 2)
        text_y = margined.height - int(self.margin.bottom / 2)
        text_position = text_x, text_y

        overlay = ImageDraw.Draw(margined)
        overlay.multiline_text(
            text_position, caption, self.foreground, self.font, 'mm',
            align='center'
        )

        return margined
