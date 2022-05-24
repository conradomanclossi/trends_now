import os
import json
from image import resize
from message import Message
from dotenv import load_dotenv

# Token
load_dotenv()
token = os.getenv("trends_now_bot_token")

# Requires
message = Message(token=token)

# Commands


def start(update):
    msg = "Hello World!!!"

    message.send_message(update=update, message=msg)


def trend(update):
    with open("db/db.json", "r") as json_db:
        db = json.load(json_db)

        # Title
        message.send_message(update=update, message=db["title"])

        # Description
        message.send_message(update=update, message=db["description"])

        # Link
        if db["link"]:
            message.send_message(update=update, message=db["link"])

        # Images
        if db["imgs"]:
            for img in db["imgs"]:
                message.send_photo(update=update, photo=img)

        # Videos
        if db["videos"]:
            for video in db["videos"]:
                message.send_video(update=update, video=video)


def start_photo(update):

    file_id = update["message"]["photo"][-1]["file_id"]
    file = message.get_file(file_id=file_id)

    # Save photo
    json_string = json.dumps({"file": file})
    file_json = "{}.json".format(update["message"]["from"]["id"])
    json_file = open(file_json, "w")
    json_file.write(json_string)
    json_file.close()

    # Keyboard
    keyboard = {"keyboard": [["Storie", "Feed Landscape"], [
        "Feed Portrait", "Feed Square"]]}

    message.send_message(update=update, keyboard=keyboard)

def photo_format(update):

    user_id = update["message"]["from"]["id"]
    file_json = "{}.json".format(user_id)

    json_file = open(file_json, "r")
    data = json.load(json_file)
    data["format"] = update["message"]["text"]
    json_file = open(file_json, "w")

    json_file.write(json.dumps(data))

    # Keyboards
    keyboard = {}
    if update["message"]["text"] == "Storie" or update["message"]["text"] == "Feed Portrait":
        keyboard = {"keyboard": [["Left"], ["Center"], ["Right"]]}
    else:
        keyboard = {"keyboard": [["Top"], ["Center"], ["Botton"]]}

    message.send_message(update=update, keyboard=keyboard)

def send_photo(update):

    user_id = update["message"]["from"]["id"]
    file_json = "{}.json".format(user_id)

    data = json.load(open(file_json, "r"))

    photo = resize(image=data["file"], canva=data["format"], orientation=update["message"]["text"])

    # Send photo
    message.send_photo(update=update, photo=photo)

    # Delete json file
    os.remove(file_json)