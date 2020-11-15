from ui.windows import Window

from .base import Display


class DebugDisplay(Display):
    """Debug display - Render an image using PIL's built in show function.

    Useful for debugging, but it's easier to work with `MatplotlibDisplay`.
    """

    def draw(self, window: Window) -> None:
        window.get_pil_image().show()
