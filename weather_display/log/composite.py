from typing import Iterable

from .base import Logger


class CompositeLogger(Logger):
    """Composite logger - A wrapper around mutliple loggers.

    This allows you to use multiple loggers where a single logger is expected.
    When logging a message, it iterates through all of the wrapped loggers and
    calls their corresponding log method.

    Parameters
    ----------
    loggers : Iterable[Logger]
        The wrapped loggers
    """

    def __init__(self, loggers: Iterable[Logger]) -> None:
        self.loggers = loggers

    def log_success(self, message: str) -> None:
        for logger in self.loggers:
            logger.log_success(message)

    def log_error(self, message: str) -> None:
        for logger in self.loggers:
            logger.log_error(message)
