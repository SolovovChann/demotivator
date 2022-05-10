from typing_extensions import TypeAlias
from io import BytesIO
from PIL import Image


Color: TypeAlias = int | str | tuple[int, int, int] | tuple[int, int, int, int]
ImageSource: TypeAlias = Image.Image | str | bytes | BytesIO
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
