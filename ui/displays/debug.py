from .base import Display


class DebugDisplay(Display):
    def draw(self, window):
        window.get_pil_image.show()
