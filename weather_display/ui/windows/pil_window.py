from typing import Tuple

from PIL import Image, ImageDraw, ImageFont  # type: ignore

from .base import Window


class PilWindow(Window):
    """Pil window - Renders an image using the PIL library

    Parameters
    ----------
    width : int
        the width of the window
    height : int
        the height of the window
    """

    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)
        self._image = Image.new(mode="1", size=(width, height), color=1)

    def clear(self):
        self._image = Image.new(mode="1", size=self._image.size, color=1)

    def rectangle(self, left: int, top: int, right: int, bottom: int) -> None:
        draw = ImageDraw.Draw(self._image)
        draw.rectangle([left, top, right, bottom], fill=0)

    def text(self, x: int, y: int, body: str, font_path: str, font_size: int) -> None:
        font = ImageFont.truetype(font_path, font_size)
        draw = ImageDraw.Draw(self._image)
        draw.text((x, y), body, font=font)

    def text_size(self, body: str, font_path: str, font_size: int) -> Tuple[int, int]:
        font = ImageFont.truetype(font_path, font_size)
        draw = ImageDraw.Draw(self._image)
        return draw.textsize(body, font=font)

    def image(self, x: int, y: int, path: str):
        im = Image.open(path)
        self._image.paste(im, box=(x, y))

    def get_pil_image(self) -> Image:
        return self._image
