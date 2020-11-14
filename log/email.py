import os
import smtplib
import ssl

from dotenv import load_dotenv

from .base import Logger

load_dotenv()


class EmailLogger(Logger):
    EMAILEE_ADDRESS = os.getenv("EMAILEE_ADDRESS")
    EMAILER_ADDRESS = os.getenv("EMAILER_ADDRESS")
    EMAILER_PASSWORD = os.getenv("EMAILER_PASSWORD")

    def log_error(self, message):
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
            server.login(EmailLogger.EMAILER_ADDRESS, EmailLogger.EMAILER_PASSWORD)

            server.sendmail(
                EmailLogger.EMAILER_ADDRESS,
                EmailLogger.EMAILEE_ADDRESS,
                self.error_message(message),
            )

    def error_message(self, message):
        return f"""\
Subject: WEATHER DISPLAY ERROR


[ERROR] weather_display: {message}
"""
