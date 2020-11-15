from abc import ABC


class Logger(ABC):
    """Logger - A base class for loggers.

    Loggers are responsible for logging success/error messages.
    """

    def log_success(self, message: str) -> None:
        """Log a success message.

        Parameters
        ----------
        message : str
            The message to log
        """
        pass

    def log_error(self, message: str) -> None:
        """Log an error message.

        Parameters
        ----------
        message : str
            The message to log
        """
        pass
