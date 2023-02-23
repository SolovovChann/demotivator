import random
from unittest import TestCase

from PIL import Image

from demotivator.indent import ImageIndentation


def _random_list(count: int, pool: range) -> list[int]:
    """Generate N random elements from the range"""
    return [
        random.choice(pool)
        for _ in range(count)
    ]


class TestIndentationIndent(TestCase):
    """Test `Indentation.indent()` method"""

    image = Image.new('RGB', (255, 127), 'magenta')

    def test_indent_size(self) -> None:
        indent = ImageIndentation.css_like(10)
        indented = indent.expand(self.image, '#fff')
        width = self.image.width + 10 + 10
        height = self.image.height + 10 + 10

        self.assertEqual(indented.width, width)
        self.assertEqual(indented.height, height)

    def test_indent_mode(self) -> None:
        indent = ImageIndentation.css_like(10)
        indented = indent.expand(self.image, '#fff')

        self.assertEqual(indented.mode, self.image.mode)


class TestIndentionCssLike(TestCase):
    """Test `Indentation.css_like()` class method"""

    def test_single_value(self) -> None:
        a = random.randint(0, 100)
        indent = ImageIndentation.css_like(a)

        self.assertEqual(indent.left, a)
        self.assertEqual(indent.top, a)
        self.assertEqual(indent.right, a)
        self.assertEqual(indent.bottom, a)
