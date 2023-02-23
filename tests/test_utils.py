from pathlib import Path
from unittest import TestCase

from PIL import Image, ImageChops, ImageFont

from demotivator import _load_font, _load_image

base_dir = Path(__file__).parent.parent


def _images_are_similar(first: Image.Image, second: Image.Image) -> bool:
    difference = ImageChops.difference(first, second)
    return difference.getbbox() is None


class TestLoadImage(TestCase):
    """Test private `_load_image` function"""

    path: Path = Path(base_dir) / 'capybara.jpg'
    string: str = str(path)
    image: Image.Image = Image.open(path).convert('RGB')

    def test_str(self) -> None:
        image = _load_image(self.string).convert('RGB')
        self.assertIsInstance(image, Image.Image)
        self.assertTrue(_images_are_similar(image, self.image))

    def test_path(self) -> None:
        image = _load_image(self.path).convert('RGB')
        self.assertIsInstance(image, Image.Image)
        self.assertTrue(_images_are_similar(image, self.image))

    def test_image(self) -> None:
        image = _load_image(self.image).convert('RGB')
        self.assertIsInstance(image, Image.Image)
        self.assertTrue(_images_are_similar(image, self.image))

    def test_type_error(self) -> None:
        self.assertRaises(TypeError, _load_image, None)
        self.assertRaises(TypeError, _load_image, {})
        self.assertRaises(TypeError, _load_image, [])
        self.assertRaises(TypeError, _load_image, tuple())


class TestLoadFont(TestCase):
    """Test private `_load_font` function"""

    size: int = 16
    path: Path = Path(base_dir) / 'font.ttf'
    string: str = str(path)
    font: ImageFont.FreeTypeFont = ImageFont.truetype(string, size)

    def test_str(self) -> None:
        font = _load_font(self.string, self.size)
        self.assertIsInstance(font, ImageFont.FreeTypeFont)

    def test_path(self) -> None:
        font = _load_font(self.path, self.size)
        self.assertIsInstance(font, ImageFont.FreeTypeFont)

    def test_image(self) -> None:
        font = _load_font(self.font, self.size)
        self.assertIsInstance(font, ImageFont.FreeTypeFont)

    def test_type_error(self) -> None:
        self.assertRaises(TypeError, _load_font, None)
        self.assertRaises(TypeError, _load_font, {})
        self.assertRaises(TypeError, _load_font, [])
        self.assertRaises(TypeError, _load_font, tuple())
