import argparse

from demotivator import demotivate


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


def create_demotivator() -> None:
    parser = create_argument_parser()
    args = parser.parse_args()

    bg = '#fff' if args.motivate else '#000'
    fg = '#000' if args.motivate else '#fff'

    demotivator = demotivate(
        args.source, args.font, args.caption,
        foreground=fg,
        background=bg
    )

    demotivator.save(args.dest)


if __name__ == '__main__':
    create_demotivator()
