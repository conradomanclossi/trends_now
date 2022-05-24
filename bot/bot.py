import gc
import json
import requests
from chat import Chat
from updates import Updates

class Bot(Chat):
    def __init__(self, token):
        self.token = token
        self._url = "https://api.telegram.org/{}/{}"
        self.bot_token = "bot{}".format(self.token)
        self.updates = Updates()
        super().__init__()

    def url(self, metod):

        if metod == "file":
            return self._url.format(metod, self.bot_token)
        else:
            return self._url.format(self.bot_token, metod)

    def get_me(self):

        headers = {
                "Accept": "application/json",
                "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)"
        }

        return requests.post(self.url(metod="getMe"), headers=headers)

    def get_file(self, file_id):

        payload = {"file_id": file_id}

        headers = {
                "Accept": "application/json",
                "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
                "Content-Type": "application/json"
        }

        response = requests.post(self.url("getFile"), json=payload, headers=headers)

        path = json.loads(response.content.decode("utf8"))["result"]["file_path"]

        return self.url("file") + "/{}".format(path)

    def start(self):
        try:
            self.get_me().raise_for_status()
            print("Bot Started")

            try:
                print("Bot Listening")
                last_update_id = None

                while True:
                    updates = self.updates.get(self.url("getUpdates"), last_update_id)

                    if updates is not None:
                        if len(updates["result"]) > 0:
                            last_update_id = self.updates.get_last_update_id(updates) + 1
                            self.handler(updates)

                    # Clean Memory
                    gc.collect()
            except KeyboardInterrupt:
                print("Bot Stoped")

        except requests.exception.HTTPError as error:
            print(error)
