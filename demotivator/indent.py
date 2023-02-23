from dataclasses import dataclass

from PIL import Image

from demotivator.typing import Color


@dataclass
class ImageIndentation:
    left: int
    top: int
    right: int
    bottom: int

    @classmethod
    def css_like(cls, *indent: int) -> 'ImageIndentation':
        """
        Create indentation with 1-4 values:

        1. Indentations will be set simultaneously from each edge.

        2. The first value sets the indentations from the
        top and bottom edges, the second - from the left and right.

        3. The first value sets the margin from the top edge,
        the second value from both the left and right edges, and the
        third value from the bottom edge.

        4. Alternately sets the indentations from the
        top, right, bottom, and left edges.
        """
        match indent:
            case (int(), ) as padding:
                padding = padding[0]
                return cls(padding, padding, padding, padding)
            case vertical, horizontal:
                return cls(horizontal, vertical, horizontal, vertical)
            case top, horizontal, bottom:
                return cls(horizontal, top, horizontal, bottom)
            case left, top, right, bottom:
                return cls(left, top, right, bottom)
            case [*padding] if len(padding) > 4:
                message = 'Indentation with %i elements is not supported'
                raise TypeError(message % len(padding))
            case _:
                message = 'Undefined indentation type: %s'
                raise TypeError(message % type(indent))

    def expand(self, image: Image.Image, color: Color = '#000') -> Image.Image:
        width = image.width + self.left + self.right
        height = image.height + self.top + self.bottom

        extended = Image.new(image.mode, (width, height), color)
        extended.paste(image, (self.left, self.top))

        return extended
