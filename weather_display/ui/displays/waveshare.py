from PIL import Image  # type: ignore

from ..windows import Window
from .base import Display


class WaveshareEpdDisplay(Display):
    """Waveshare EPD display - Renders an image onto a waveshare epd e-ink display.

    Uses the epd library provided by waveshare to render an image to the display.
    """

    def __init__(self) -> None:
        from .waveshare_epd.epd2in7b import EPD

        super().__init__()

        self.epd = EPD()

    def init(self) -> None:
        self.epd.init()
        self.epd.Clear()

    def draw(self, window: Window) -> None:
        self.epd.Clear()

        black_image = window.get_pil_image()
        red_image = Image.new(mode="1", size=black_image.size, color=1)

        self.epd.display(self.epd.getbuffer(black_image), self.epd.getbuffer(red_image))
