from .utils import Color, Indent, Source, format_padding
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


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
            inner = Image.new('RGB', tuple(map(int, expand)), self.background)
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
            outer = Image.new('RGB', tuple(map(int, expand)), self.background)
            outer.paste(image, self.margin[:2])

            return outer

    def __init__(self, image: Source, font: Source) -> None:
        match image:
            case Image.Image():
                self.image = image

            case str() | bytes() | BytesIO():
                self.image = Image.open(image)

            case object:
                message = 'Unable to load Image of type "%s"'
                raise TypeError(message % type(object))

        self.font = ImageFont.truetype(font, min(self.image.size) // 16)

    def __call__(self, frame: Frame, caption: str) -> Image.Image:
        """
        # Demotivator()
        Draw inner and outer borders and text
        """
        framed = frame(self.image)
        text_position = (
            framed.width / 2,
            framed.height - frame.margin[3] / 2)

        draw = ImageDraw.Draw(framed, 'RGB')
        draw.text(
            text_position, caption, frame.foreground,
            self.font, 'mm', align='center')

        return framed
