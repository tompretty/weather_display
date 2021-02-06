from typing import Tuple

from ..windows import Window
from .base import Widget


class BlankWidget(Widget):
    """Blank Widget - It's blank!

    Parameters
    ----------
    position : Tuple[int, int]
        the (x, y) position of the widget
    """

    def __init__(self, size: Tuple[int, int]) -> None:
        super().__init__((0, 0), None)
        self.size = size

    def draw(self, window: Window) -> None:
        pass

    def extent(self, window: Window) -> Tuple[int, int]:
        return self.size
