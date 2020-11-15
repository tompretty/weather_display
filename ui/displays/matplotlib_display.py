import matplotlib.pyplot as plt  # type: ignore
from ui.windows import Window

from .base import Display


class MatplotlibDisplay(Display):
    """Matplotlib display - Renders an image using matplotlib.

    Displays the window using a matplotlib figure. Useful for debugging.
    """

    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def draw(self, window: Window) -> None:
        self.ax.imshow(window.get_pil_image())
        plt.ion()
        plt.show()
        plt.pause(0.001)
