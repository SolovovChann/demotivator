import argparse


def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    writable_file = argparse.FileType('w')

    parser.add_argument(
        'source',
        action='store',
        type=str,
    )
    parser.add_argument(
        'caption',
        action='store',
        type=str
    )
    parser.add_argument(
        'dest',
        action='store',
        type=writable_file,
        default='demotivator.jpg'
    )
    parser.add_argument(
        '--font', '-f',
        action='store',
        default='font.ttf',
        type=str,
    )
    parser.add_argument('--motivate', action='store_true')

    return parser
