import logging

from .base import Logger


def get_logger(name):
    logger = logging.getLogger(name)
    if logger.level == 0:
        logger.setLevel(logging.INFO)
    # Add timestamps to log messages.
    if not logger.handlers:
        file_handler = logging.FileHandler("run.log")
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            fmt="[%(levelname)s %(asctime)s] %(name)s: %(message)s",
            datefmt="%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.propagate = True
    return logger


class ConsoleLogger(Logger):
    """Console logger - Logs messages to the console.

    Internally, this uses pythons logging module for logging.
    """

    def __init__(self):
        super().__init__()
        self.logger = get_logger("weather_display")

    def log_success(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)
