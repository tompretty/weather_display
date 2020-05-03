from PIL import Image

from .base import Display


class WaveshareEpdDisplay(Display):
    def __init__(self, image_path):
        from .waveshare_epd.epd2in7b import EPD

        super().__init__(image_path)

        self.epd = EPD()

    def init(self):
        self.epd.init()
        self.epd.Clear()

    def draw(self):
        self.epd.Clear()

        black_image = Image.open(self.image_path)
        red_image = Image.new(mode="1", size=black_image.size, color=1)

        self.epd.display(self.epd.getbuffer(black_image), self.epd.getbuffer(red_image))
