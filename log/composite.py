from .base import Logger


class CompositeLogger(Logger):
    def __init__(self, loggers):
        self.loggers = loggers

    def log_success(self, message):
        for logger in self.loggers:
            logger.log_success(message)

    def log_error(self, message):
        for logger in self.loggers:
            logger.log_error(message)
