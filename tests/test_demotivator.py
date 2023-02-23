from functools import reduce
from pathlib import Path
from unittest import TestCase

from PIL import Image, ImageFont

from demotivator import Demotivator
from demotivator.indent import ImageIndentation

base_dir = Path(__file__).parent.parent

font_path = base_dir / 'font.ttf'
image_path = base_dir / 'capybara.jpg'


class TestDemotivatorDemotivate(TestCase):
    """Test `Demotivator.demotivate` method"""

    font: ImageFont.FreeTypeFont = ImageFont.truetype(str(font_path), 16)
    image: Image.Image = Image.open(image_path)

    def test_demotivate_size(self) -> None:
        padding = ImageIndentation.css_like(10)
        border = ImageIndentation.css_like(1)
        margin = ImageIndentation.css_like(20)

        demotivator = Demotivator(
            self.font,
            border,
            margin,
            padding,
            '#000',
            '#fff',
        )
        image = demotivator.demotivate(self.image, '')

        width = self.image.width + reduce(
            lambda a, b: a + b.right + b.left, [padding, border, margin], 0
        )
        height = self.image.height + reduce(
            lambda a, b: a + b.top + b.bottom,
            [padding, border, margin],
            0
        )

        self.assertEqual(image.width, width)
        self.assertEqual(image.height, height)

    def test_demotivate_mode(self) -> None:
        padding = ImageIndentation.css_like(10)
        border = ImageIndentation.css_like(1)
        margin = ImageIndentation.css_like(20)

        demotivator = Demotivator(
            self.font,
            border,
            margin,
            padding,
            '#000',
            '#fff',
        )
        image = demotivator.demotivate(self.image, '')

        self.assertEqual(image.mode, self.image.mode)
