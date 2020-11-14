from abc import ABC


class Logger(ABC):
    def log_success(self, message):
        pass

    def log_error(self, message):
        pass
