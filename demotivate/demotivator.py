from .utils import Color, Indent, format_padding
from PIL import Image, ImageDraw, ImageFont


class Demotivator:
    """
    # Demotivator
    Make a demotivator meme from any image
    """

    class Frame:
        """
        # Frame
        External and internal frame of the demotivator
        """

        background: Color = '#000'
        foreground: Color = '#fff'
        width: int = 3

        def __init__(self, padding: Indent, margin: Indent) -> None:
            self.padding = format_padding(padding)
            self.margin = format_padding(margin)
