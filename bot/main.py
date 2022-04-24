import os
import json
import logging
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

# Token
load_dotenv()
bot_token = os.getenv('TRENDS_NOW_BOT_TOKEN')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Messages

# Start
def start(update: Update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!!!')

# Trend Now
def trend(update: Update, context):
    with open('db/db.json', 'r') as json_db:
        db = json.load(json_db)

    # Title
    update.message.reply_text(db['title'])

    # Description
    update.message.reply_text(db['description'])

    # Link
    if db['link'] is not None:
        update.message.reply_text(db['link'])

    # Images
    if db['imgs'] is not None:
        for img in db['imgs']:
            update.message.bot.send_photo(update.message.chat.id, open(img, 'rb'))

    # Videos
    if db['videos'] is not None:
        for video in db['videos']:
            update.message.bot.send_video(update.message.chat.id, open(video, 'rb'))

# Error
def error(update: Update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Main
def main():
    """Start the bot."""
    # Get the dispatcher to register handlers
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('trend', trend))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()