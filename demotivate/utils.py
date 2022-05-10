from typing_extensions import TypeAlias
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont


Color: TypeAlias = int | str | tuple[int, int, int] | tuple[int, int, int, int]
Source: TypeAlias = Image.Image | str | bytes | BytesIO
Indent: TypeAlias = tuple[int, int, int, int]
Number: TypeAlias = int | float
Position: TypeAlias = tuple[int, int]


def format_padding(padding: int | Indent) -> Indent:
    match padding:
        case int(padding) | [padding]:
            return [padding] * 4

        case [vertical, horizontal]:
            return [horizontal, vertical, horizontal, vertical]

        case [top, horizontal, bottom]:
            return [horizontal, top, horizontal, bottom]

        case [*padding] if len(padding) == 4:
            return padding

        case [*padding] if len(padding) > 4:
            message = 'Padding with %i elements is not supported' % len(
                padding)
            raise ValueError(message)

        case object:
            message = 'Padding type "%s" is not supported' % type(object)
            raise ValueError(message)


class Placeholder:
    """
    # Placeholder
    Create test image
    """

    def __init__(
        self,
        font: str,
        background: str = '#5576d1',
        foreground: str = '#fff'
    ):
        self.font = font
        self.background = background
        self.foreground = foreground

    def __call__(self, width: int, height: int) -> Image.Image:
        """
        ## Placeholder
        Create image with set width and height
        """
        size = width, height
        text = '%ix%i' % size
        xy = tuple(i // 2 for i in size)

        image = Image.new('RGB', size, self.background)
        font = ImageFont.truetype(self.font, min(size) // 6)
        overlay = ImageDraw.Draw(image, 'RGB')

        overlay.text(xy, text, self.foreground, font, 'mm', align='center')

        return image
