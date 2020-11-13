from PIL import Image, ImageDraw, ImageFont

from .base import Window


class PilWindow(Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self._image = Image.new(mode="1", size=(width, height), color=1)

    def clear(self):
        self._image = Image.new(mode="1", size=self._image.size, color=1)

    def rectangle(self, left, top, right, bottom):
        draw = ImageDraw.Draw(self._image)
        draw.rectangle([left, top, right, bottom], fill=0)

    def text(self, x, y, body, font_path, font_size):
        font = ImageFont.truetype(font_path, font_size)
        draw = ImageDraw.Draw(self._image)
        draw.text((x, y), body, font=font)

    def text_size(self, body, font_path, font_size):
        font = ImageFont.truetype(font_path, font_size)
        draw = ImageDraw.Draw(self._image)
        return draw.textsize(body, font=font)

    def image(self, x, y, path):
        im = Image.open(path)
        self._image.paste(im, box=(x, y))

    def get_pil_image(self):
        return self._image
