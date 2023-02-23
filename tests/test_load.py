from pathlib import Path
from unittest import TestCase

from PIL import Image, ImageChops

from demotivator import _load_image

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
