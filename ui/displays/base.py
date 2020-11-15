from abc import ABC, abstractmethod

from ui.windows import Window


class Display(ABC):
    """Display - A base class for displays.

    A display is responsible for actually showing an image that has been created
    by a `window` object.
    """

    @abstractmethod
    def draw(self, window: Window) -> None:
        """Display the window.

        Parameters
        ----------
        window : Window
            The Window object that has rendered an image for displaying
        """
        raise NotImplementedError

    def init(self) -> None:
        """Initialize the display.

        Perform any logic a display might need when initialising.
        """
        pass
