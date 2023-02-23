from pathlib import Path
from unittest import TestCase

from PIL import Image, ImageChops, ImageFont

from demotivator import _load_font, _load_image, _is_valid_url

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


class TestIsValidUrl(TestCase):
    """Test private `_is_valid_url` function"""

    def test_valid_url(self) -> None:
        self.assertTrue(
            _is_valid_url('https://youtu.be/dQw4w9WgXcQ')
        )
        self.assertTrue(
            _is_valid_url('https://pbs.twimg.com/media/Di3y9e_X0AE-8nk.jpg')
        )
        self.assertTrue(
            _is_valid_url(
                'https://media.tenor.com/images/'
                'ff5faf4a21655f2fe7f93f120ec6b803/tenor.gif'
            )
        )

    def test_invalid_url(self) -> None:
        self.assertFalse(_is_valid_url(''))
        self.assertFalse(_is_valid_url('dull string'))
        self.assertFalse(_is_valid_url('( ͡° ͜ʖ ͡°)'))
