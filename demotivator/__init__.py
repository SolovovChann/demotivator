import re
from pathlib import Path
from urllib import request

from PIL import Image, ImageDraw, ImageFont

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


def _load_font(
    font: Path | str | ImageFont.FreeTypeFont,
    size: int,
) -> ImageFont.FreeTypeFont:
    match font:
        case Path():
            return ImageFont.truetype(str(font), size)
        case str():
            return ImageFont.truetype(font, size)
        case ImageFont.FreeTypeFont():
            return font
        case _:
            raise TypeError(f'Font type {type(font)} is not supported')


def _is_valid_url(string: str) -> bool:
    return bool(re.match(r'https?:\/\/.+', string, re.M))


def _open_image_by_url(url: str) -> Image.Image:
    response = request.urlopen(url)
    return Image.open(response)
