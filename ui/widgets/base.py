from typing import Optional, Tuple

from data import DataSource
from ui.windows import Window


class Widget:
    """Widget - A base class for widgets

    Widgets are building blocks for building UIs

    Parameters
    ----------
    position : Tuple[int, int]
        the (x, y) position of the widget
    data_source: Optional[DataSource]
        the data source for connecting to an API
    """

    def __init__(
        self, position: Tuple[int, int], data_source: Optional[DataSource] = None
    ) -> None:
        self.position = position
        self.data_source = data_source

    def draw(self, window: Window) -> None:
        """Draw the widget onto the window

        Parameters
        ----------
        window : Window
            the window to draw to
        """
        raise NotImplementedError

    def extent(self, window: Window) -> Tuple[int, int]:
        """Get the bounding box of the widget

        Parameters
        ----------
        window : Window
            the window being drawn to

        Returns
        -------
        Tuple[int, int]
            the height and width of the bounding box
        """
        raise NotImplementedError

    def width(self, window: Window) -> int:
        """Get the width of the widget

        Parameters
        ----------
        window : Window
            the window being drawn to

        Returns
        -------
        int
            the width
        """
        return self.extent(window)[0]

    def height(self, window) -> int:
        """Get the height of the widget

        Parameters
        ----------
        window : Window
            the window being drawn to

        Returns
        -------
        int
            the height
        """
        return self.extent(window)[1]

    @property
    def x(self) -> int:
        """The x position of the widget

        Returns
        -------
        int
            the x position
        """
        return int(self.position[0])

    @property
    def y(self) -> int:
        """The y position of the widget

        Returns
        -------
        int
            the y position
        """
        return int(self.position[1])

    def set_x(self, x: int) -> None:
        """Set the x position of the widget

        Parameters
        ----------
        x : int
            the new x position
        """

        self.position = (x, self.y)

    def set_y(self, y: int) -> None:
        """Set the y position of the widget

        Parameters
        ----------
        y : int
            the new y position
        """

        self.position = (self.x, y)
