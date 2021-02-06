from abc import ABC, abstractmethod
from typing import Tuple

from PIL import Image  # type: ignore


class Window(ABC):
    """Window - A base class for windows.

    A window is responsible for rendering an image, which is then displayed by
    a `Display`. A window provides a number of methods for adding graphical elements
    to the image e.g text and images.

    Parameters
    ----------
    width : int
        The width of the image
    height: int
        The height of the image
    """

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def clear(self) -> None:
        """Clear the current image.
        """
        pass

    @abstractmethod
    def rectangle(self, left: int, top: int, right: int, bottom: int) -> None:
        """Draw a rectangle onto the screen.

        Parameters
        ----------
        left : int
            x co-ord of the left edge
        top : int
            y co-ord of the top edge
        right : int
            x co-ord of the right edge
        bottom : int
            y co-ord of teh bottom edge
        """
        raise NotImplementedError

    @abstractmethod
    def text(self, x: int, y: int, body: str, font_path: str, font_size: int):
        """Draw some text to the screen

        Parameters
        ----------
        x : int
            x co-ord of start of text
        y : int
            y co-ord of start of text
        body : str
            the text to draw
        font_path : str
            path to the font file
        font_size : int
            font size to draw
        """
        raise NotImplementedError

    @abstractmethod
    def text_size(self, body: str, font_path: str, font_size: int) -> Tuple[int, int]:
        """Get size of the texts bounding box.

        Parameters
        ----------
        body : str
            the text
        font_path : str
            path to font file
        font_size : int
            font size

        Returns
        ------
        Tuple[int, int]
            width and height of the bounding box
        """
        raise NotImplementedError

    @abstractmethod
    def image(self, x: int, y: int, path: str) -> None:
        """Draw an image to the screen.

        Parameters
        ----------
        x : int
            x co-ord of start of image
        y : int
            y co-ord of start of image
        path : str
            path to image file
        """
        raise NotImplementedError

    @abstractmethod
    def get_pil_image(self) -> Image:
        """Get the rendered image as a PIL image.

        Returns
        -------
        Image
            the rendered image
        """
        raise NotImplementedError
