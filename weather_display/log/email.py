import os
import smtplib
import ssl

from dotenv import load_dotenv

from .base import Logger

load_dotenv()


class EmailLogger(Logger):
    """Email logger - Sends an email when logging an error message.

    Sends an email from a gmail account whose details are configured through
    environment variables. The recipient address is also configured this way.

    Env vars
    ----------
    EMAILER_ADDRESS : str
        The sender's address (must be a gmail account)
    EMAILER_PASSWORD: str
        The sender's password
    EMAILEE_ADDRESS: str
        The recipient's address
    """

    EMAILEE_ADDRESS = os.getenv("EMAILEE_ADDRESS", default="")
    EMAILER_ADDRESS = os.getenv("EMAILER_ADDRESS", default="")
    EMAILER_PASSWORD = os.getenv("EMAILER_PASSWORD", default="")

    def log_error(self, message: str) -> None:
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
            server.login(EmailLogger.EMAILER_ADDRESS, EmailLogger.EMAILER_PASSWORD)

            server.sendmail(
                EmailLogger.EMAILER_ADDRESS,
                EmailLogger.EMAILEE_ADDRESS,
                self.error_message(message),
            )

    def error_message(self, message: str) -> str:
        return f"""\
Subject: WEATHER DISPLAY ERROR


[ERROR] weather_display: {message}
"""
