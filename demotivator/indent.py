from dataclasses import dataclass

from PIL import Image

from demotivator.typing import Color


@dataclass
class ImageIndentation:
    left: int
    top: int
    right: int
    bottom: int

    def expand(self, image: Image.Image, color: Color = '#000') -> Image.Image:
        width = image.width + self.left + self.right
        height = image.height + self.top + self.bottom

        extended = Image.new(image.mode, (width, height), color)
        extended.paste(image, (self.left, self.top))

        return extended
