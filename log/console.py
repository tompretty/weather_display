import logging

from .base import Logger


def get_logger(name):
    logger = logging.getLogger(name)
    if logger.level == 0:
        logger.setLevel(logging.INFO)
    # Add timestamps to log messages.
    if not logger.handlers:
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter(
            fmt="[%(levelname)s %(asctime)s] %(name)s: %(message)s",
            datefmt="%m-%d %H:%M:%S",
        )
        console.setFormatter(formatter)
        logger.addHandler(console)
        logger.propagate = True
    return logger


class ConsoleLogger(Logger):
    def __init__(self):
        super().__init__()
        self.logger = get_logger("weather_display")

    def log_success(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)
