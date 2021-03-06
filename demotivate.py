#!/usr/bin/env python3.10
import re
from io import IOBase
from pathlib import Path
from typing import Iterable, NamedTuple, TypeAlias
from urllib import request

import click
from PIL import Image, ImageDraw, ImageFont


Color: TypeAlias = float | tuple[float, ...]
Indent: TypeAlias = int | Iterable[int]
Size: TypeAlias = tuple[int, int]
Source: TypeAlias = str | bytes | IOBase | Path
Font = ImageFont.ImageFont | ImageFont.FreeTypeFont | ImageFont.TransposedFont

__version__ = '0.1.0'


class Indentation(NamedTuple):
    left: int
    top: int
    right: int
    bottom: int


def get_indentation(indent: Indent) -> Indentation:
    """Convert css-like padding to 4 int tuple"""
    match indent:
        case int(padding) | [padding]:
            return Indentation(padding, padding, padding, padding)

        case [vertical, horizontal]:
            return Indentation(horizontal, vertical, horizontal, vertical)

        case [top, horizontal, bottom]:
            return Indentation(horizontal, top, horizontal, bottom)

        case [*padding] if len(padding) == 4:
            return Indentation(*padding)

        case [*padding] if len(padding) > 4:
            message = 'Padding with %i elements is not supported'
            raise ValueError(message % len(padding))

        case object:
            message = 'Padding type "%s" is not supported'
            raise ValueError(message % type(object))


def expand_image(
    image: Image.Image,
    indent: Indentation,
    color: Color = '#000'
) -> Image.Image:
    """Expand new image with indentation"""
    width = image.width + indent.left + indent.right
    height = image.height + indent.top + indent.bottom
    extended = Image.new('RGB', (width, height), color)
    extended.paste(image, (indent.left, indent.top))

    return extended


@click.command(context_settings={'show_default': True})
@click.argument('caption')
@click.argument('source')
@click.option('-f', '--font', default='font.ttf')
@click.option('-o', '--output', default='demotivator.jpg', type=click.File('wb'))
@click.version_option(__version__)
def create_demotivator(caption, source, output: click.File, font) -> None:
    """Make demotivator from source image"""
    regex = re.compile(r'https?:\/\/.+', re.M)

    if isinstance(source, str) and regex.match(source):
        source = Image.open(request.urlopen(source))

    try:
        demo = Demotivator(source, font)
        demo.demotivate(caption).save(output)
        click.echo('File "%s" successfuly saved' % output.name)
    except Exception as exc:
        click.echo('Something went wrong: "%s"' % exc)
        exit(1)


class Demotivator:
    """Make a demotivator meme from any image"""

    class Frame:
        """Demotivator frames builder"""

        background: Color = '#000'
        foreground: Color = '#fff'
        width: int = 3

        def __init__(self, padding: Indentation, margin: Indentation) -> None:
            self.padding = padding
            self.margin = margin

        def draw(self, image: Image.Image) -> Image.Image:
            """Draw inner and outer frames"""
            inner = expand_image(image, self.padding)
            ImageDraw.Draw(inner, 'RGB').rectangle(
                xy=(0, 0, inner.width, inner.height),
                outline=self.foreground,
                width=self.width)
            outer = expand_image(inner, self.margin)

            return outer

    def __init__(self, image: Image.Image | Source, font: Font | Source) -> None:
        self.image = image if isinstance(image, Image.Image) \
            else Image.open(image)

        self.font = font if isinstance(image, Font) \
            else ImageFont.truetype(font, min(self.image.size) // 16)

    def demotivate(self, caption: str, frame: Frame = None) -> Image.Image:
        """Draw inner and outer borders and text"""
        if frame is None:
            indent = min(self.image.size) // 50
            padding = get_indentation(min(self.image.size) // 50)
            margin = get_indentation([indent * 4, indent * 4, indent * 12])
            frame = self.Frame(padding, margin)

        framed = frame.draw(self.image)
        position = framed.width / 2, framed.height - frame.margin.bottom / 2
        ImageDraw.Draw(framed, 'RGB').text(
            xy=position,
            text=caption,
            fill=frame.foreground,
            font=self.font,
            anchor='mm',
            align='center')

        return framed


if __name__ == '__main__':
    create_demotivator()
