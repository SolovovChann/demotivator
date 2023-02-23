from unittest import TestCase

from PIL import Image

from demotivator.indent import ImageIndentation


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
