from PIL import Image

from .base import Display


class DebugDisplay(Display):
    def draw(self):
        image = Image.open(self.image_path)
        image.show()
