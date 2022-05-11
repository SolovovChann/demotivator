from .demotivator import Demotivator
from io import BytesIO
from os.path import realpath

import click
import re
import requests


@click.command()
@click.argument('caption')
@click.argument('source')
@click.argument('output')
@click.option('-f', '--font', default='font.ttf', show_default='font.ttf')
def create_demotivator(caption, source, output, font) -> None:
    """Make demotivator from source image"""
    regex = re.match(r'https?:\/\/.+', source, re.M)

    if isinstance(source, str) and regex:
        request = requests.get(source)
        source = BytesIO(request.content)

    demo = Demotivator(source, font)

    padding = min(demo.image.size) // 50
    margin = padding * 4, padding * 4, padding * 12
    frame = demo.Frame(padding, margin)

    frame.width = padding // 4
    demo(frame, caption).save(output)

    message = 'Demotivator successfuly saved at %s'
    click.echo(message % realpath(output))


if __name__ == '__main__':
    create_demotivator()
