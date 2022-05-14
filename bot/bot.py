import requests

class Bot:
    def __init__(self, token):
        self.token = token

    def url(self, metod):

        url = "https://api.telegram.org/{}/{}"
        bot_token = "bot{}".format(self.token)

        if metod == "getMe":
            return url.format(bot_token, metod)
        elif metod == "getUpdates":
            return url.format(bot_token, metod)
        elif metod == "sendMessage":
            return url.format(bot_token, metod)

    def get_me(self):

        headers = {
                "Accept": "application/json",
                "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)"
        }

        response = requests.post(self.url(metod="getMe"), headers=headers)

        return response
