from PIL import Image

from .base import Display


class WaveshareEpdDisplay(Display):
    def __init__(self):
        from .waveshare_epd.epd2in7b import EPD

        super().__init__()

        self.epd = EPD()

    def init(self):
        self.epd.init()
        self.epd.Clear()

    def draw(self, window):
        self.epd.Clear()

        black_image = window.get_pil_image()
        red_image = Image.new(mode="1", size=black_image.size, color=1)

        self.epd.display(self.epd.getbuffer(black_image), self.epd.getbuffer(red_image))
