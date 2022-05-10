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

        def draw_inner_frame(self, source: Image.Image) -> Image.Image:
            """
            ## Frame.draw_inner_frame()
            Draw a frame from image to frame
            """
            expand = (
                source.width + sum(self.padding[::2]),
                source.height + sum(self.padding[1::2]))
            inner = Image.new('RGB', expand, self.background)
            inner.paste(source, self.padding[:2])

            draw = ImageDraw.Draw(inner, 'RGB')
            draw.rectangle(
                (0, 0) + expand,
                outline=self.foreground,
                width=self.width)

            return inner
