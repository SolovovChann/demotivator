from unittest import TestCase

from PIL import Image, ImageChops


def _images_are_similar(first: Image.Image, second: Image.Image) -> bool:
    difference = ImageChops.difference(first, second)
    return difference.getbbox() is None


class TestLoadImage(TestCase):
    """Test private `_load_image` function"""


class TestLoadFont(TestCase):
    """Test private `_load_font` function"""
