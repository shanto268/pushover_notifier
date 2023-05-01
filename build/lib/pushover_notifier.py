import http.client
import os
import sys
import urllib

import requests
from dotenv import load_dotenv

load_dotenv("/Users/shanto/Programming/bin/.env")

class PushoverNotifier:
    APP_TOKEN = os.environ.get("POVER_GENERAL_NOTIFYER_APP_TOKEN")
    USER_KEY = os.environ.get("POVER_USER_KEY")

    def send_message_with_title(self, message, title):
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request(
            "POST",
            "/1/messages.json",
            urllib.parse.urlencode(
                {
                    "token": self.APP_TOKEN,
                    "user": self.USER_KEY,
                    "html": 1,
                    "title": title,
                    "message": message,
                }
            ),
            {"Content-type": "application/x-www-form-urlencoded"},
        )
        conn.getresponse()

    def send_message(self, message):
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request(
            "POST",
            "/1/messages.json",
            urllib.parse.urlencode(
                {
                    "token": self.APP_TOKEN,
                    "user": self.USER_KEY,
                    "html": 1,
                    "message": message,
                }
            ),
            {"Content-type": "application/x-www-form-urlencoded"},
        )
        conn.getresponse()

    def send_message_with_image(self, message, image):
        r = requests.post(
            "https://api.pushover.net/1/messages.json",
            data={
                "token": self.APP_TOKEN,
                "user": self.USER_KEY,
                "html": 1,
                "message": message,
            },
            files={
                "attachment": (
                    "image.jpg",
                    open(image, "rb"),
                    "image/jpeg",
                )
            },
        )

    def send_message_with_image_and_title(self, message, image, title):
        r = requests.post(
            "https://api.pushover.net/1/messages.json",
            data={
                "token": self.APP_TOKEN,
                "user": self.USER_KEY,
                "html": 1,
                "title": title,
                "message": message,
            },
            files={
                "attachment": (
                    "image.jpg",
                    open(image, "rb"),
                    "image/jpeg",
                )
            },
        )

if __name__ == "__main__":
    notifier = PushoverNotifier()
    message = str(sys.argv[1])
    title = str(sys.argv[2])
    notifier.send_message_with_title(message, title)

