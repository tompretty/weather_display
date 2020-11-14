from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log_success(self, message):
        raise NotImplementedError

    @abstractmethod
    def log_error(self, message):
        raise NotImplementedError
