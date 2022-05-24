import json
import requests

class Updates:

    def get(self, url, offset=None):

        payload = {
                "offset": offset,
                "limit": None,
                "timeout": 100
        }

        headers = {
                "Accept": "application/json",
                "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
                "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        return json.loads(response.content.decode("utf8"))

    def get_last_update_id(self, updates):

        self.updates_ids = []

        for update in updates["result"]:
            self.updates_ids.append(int(update["update_id"]))

        return max(self.updates_ids)
