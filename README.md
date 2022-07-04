# SolovovChann's PyDemotivator

Everyone loves memes. So why don't you create your own?

## Installation

```bash
pip install -U pip wheel setuptools -r requirements.txt
```

## Ussage

### Console script

You can also use a link to an image on the Internet as a source.

By default, the image is saved in the same directory as the executable file.
To change this, use `--output` option.

The default font is `font.ttf`, located in the same directory as the executable file.
You can replace the font file by specifying the `--font` option.

For usage you need python3.10 in your `$PATH` environment variable.

```bash
./demotivate.py [OPTIONS] CAPTION SOURCE
```

### Module

```python
from demotivate import Demotivator


img = 'input.png'
font = 'font.ttf'
demo = Demotivator(img, font).demotivate('Hello world!')

demo.save('output.png')
```
