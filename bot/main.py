import os
from bot import bot
from commands import *
from dotenv import load_dotenv

# Token
load_dotenv()
token = os.getenv("trends_now_bot_token")

# Main
def main():
    # Requires
    bot = Bot(token=token)

    # Commands
    bot.add_command("/start", start)
    bot.add_command("/trend", trend)
    bot.add_command("Storie", photo_format)
    bot.add_command("Feed Landscape", photo_format)
    bot.add_command("Feed Portrait", photo_format)
    bot.add_command("Feed Square", photo_format)
    bot.add_command("Top", send_photo)
    bot.add_command("Center", send_photo)
    bot.add_command("Botton", send_photo)
    bot.add_command("Right", send_photo)
    bot.add_command("Left", send_photo)

    # Filters
    bot.add_filter("photo", start_photo)

    # Start
    bot.start()

if __name__ == '__main__':
    main()