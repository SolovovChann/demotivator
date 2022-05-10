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

        def __call__(self, image: Image.Image) -> Image.Image:
            """
            ## Frame()
            Draw inner and outer frames
            """
            inner = self.draw_inner_frame(image)
            outer = self.draw_outer_frame(inner)

            return outer

        def draw_inner_frame(self, image: Image.Image) -> Image.Image:
            """
            ## Frame.draw_inner_frame()
            Draw a frame from image to frame
            """
            expand = (
                image.width + sum(self.padding[::2]),
                image.height + sum(self.padding[1::2]))
            inner = Image.new('RGB', expand, self.background)
            inner.paste(image, self.padding[:2])

            draw = ImageDraw.Draw(inner, 'RGB')
            draw.rectangle(
                (0, 0) + expand,
                outline=self.foreground,
                width=self.width)

            return inner

        def draw_outer_frame(self, image: Image.Image) -> Image.Image:
            """
            ## Frame.draw_outer_frame()
            Draw a frame from the inner frame to the end of the image
            """
            expand = (
                image.width + sum(self.margin[::2]),
                image.height + sum(self.margin[1::2]))
            outer = Image.new('RGB', expand, self.background)
            outer.paste(image, self.margin[:2])

            return outer
