import requests
from bot import Bot
from PIL import Image
from io import BytesIO

class Message(Bot):
    def __init__(self, token):
        super().__init__(token)

    def send_message(self, update, message=False, message_id=False, keyboard=False):

        payload = {
                "disable_web_page_preview": False,
                "disable_notification": False,
                "chat_id": update["message"]["chat"]["id"]
        }

        if message:
            payload["text"] = message

        if message_id:
            payload["reply_to_message_id"] = update["message"]["message_id"]
            
        if keyboard:
            payload["reply_markup"] = keyboard

        headers = {
                "Accept": "application/json",
                "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
                "Content-Type": "application/json"
        }

        return requests.post(self.url("sendMessage"), json=payload, headers=headers)

    def send_photo(self, update, photo, message_id=False, caption=False):

        payload = {
                "disable_notification": False,
                "chat_id": update["message"]["chat"]["id"]
        }

        if caption:
            payload["caption"] = caption

        if message_id:
            payload["reply_to_message_id"] = update["message"]["chat"]["id"]

        img_bytes = BytesIO()
        photo.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        return requests.post(self.url("sendPhoto"), data=payload, files={"photo": img_bytes})

    def send_video(self, video, update, message_id=False, caption=False):

        payload = {
                "disable_notification": False,
                "chat_id": update["message"]["chat"]["id"]
        }

        if caption:
            payload["caption"] = caption

        if message_id:
            payload["reply_to_message_id"] = update["message"]["message_id"]

        return requests.post(self.url("sendMessage"), data=payload, files={"video": open(video, "rb")})
