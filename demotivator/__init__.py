import re
from pathlib import Path
from urllib import request

from PIL import Image, ImageDraw, ImageFont

from demotivator.indent import ImageIndentation
from demotivator.typing import Color, Font, Ink

__version__ = '0.2.0'


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


def demotivate(
    image: Path | str | Image.Image,
    font: Path | str | ImageFont.FreeTypeFont,
    caption: str,
    background: Color = '#000',
    foreground: Ink = '#fff',
) -> Image.Image:
    """Make a demotivator with a default frame!"""
    image = _load_image(image)
    unit = min(image.size) // 100
    pil_font = _load_font(font, int(unit * 8))

    border = ImageIndentation.css_like(int(unit * 0.5))
    padding = ImageIndentation.css_like(int(unit * 2))
    margin = ImageIndentation.css_like(
        int(unit * 8),
        int(unit * 8),
        int(unit * 25),
    )

    demotivator = Demotivator(
        pil_font,
        border,
        margin,
        padding,
        background,
        foreground,
    )

    return demotivator.demotivate(image, caption)


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


def _load_image(image: Path | str | Image.Image) -> Image.Image:
    match image:
        case Path():
            return Image.open(str(image))
        case str():
            if _is_valid_url(image):
                return _open_image_by_url(image)

            return Image.open(image)
        case Image.Image():
            return image
        case _:
            raise TypeError(f'Image type {type(image)} is not supported')


def _is_valid_url(string: str) -> bool:
    return bool(re.match(r'https?:\/\/.+', string, re.M))


def _open_image_by_url(url: str) -> Image.Image:
    response = request.urlopen(url)
    return Image.open(response)
