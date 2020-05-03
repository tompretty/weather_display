from wand.drawing import Drawing
from wand.image import Image

from .base import Window


class WandWindow(Window):
    def __init__(self, width, height):
        self._image = Image(width=width, height=height, background="white")
        self._image.type = "bilevel"

    def rectangle(self, left, top, right, bottom):
        with Drawing() as draw:
            draw.rectangle(left=left, top=top, right=right, bottom=bottom)
            draw(self._image)

    def text(self, x, y, body, font_size):
        _, height = self.text_size(body, font_size)
        with Drawing() as draw:
            draw.font_size = font_size
            draw.text(x, y + int(height), body)
            draw(self._image)

    def text_size(self, body, font_size):
        with Drawing() as draw:
            draw.font_size = font_size
            metrics = draw.get_font_metrics(self._image, body)
            print(metrics)
        return metrics.text_width, metrics.ascender

    def image(self, x, y, path):
        with Drawing() as draw:
            with Image(filename=path) as im:
                draw.composite(
                    left=x,
                    top=y,
                    image=im,
                    width=im.width,
                    height=im.height,
                    operator="atop",
                )
                draw(self._image)

    def save(self, path):
        self._image.save(filename=path)
