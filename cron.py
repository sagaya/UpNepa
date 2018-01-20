from models.user import User
offset = None
import telepot
from telepot.loop import MessageLoop
import pprint
import time

from apscheduler.schedulers.background import BackgroundScheduler
import telepot
import json
from models.user import User
from os import environ

offset = None
bot = telepot.Bot('{}'.format(environ.get("TOKEN")))


def new_stuff():
    global offset
    print(offset)
    content = json.dumps(bot.getUpdates(offset=offset))
    jsonObjects = json.loads(content)
    updates = [int(x["update_id"]) for x in jsonObjects]
    offset = max(updates, default=0) + 1
    print(jsonObjects)
    for jsonObject in jsonObjects:
        if offset != jsonObject["update_id"]:
            if jsonObject:
                print(jsonObject)
                username = jsonObject["message"]["from"]["username"]
                user = User.objects(username=username).first()
                if user:
                    user.chatId = jsonObject["message"]["from"]["id"]
                    user.save()
                    if jsonObject["message"]["text"] == "/start":
                        bot.sendMessage(
                            jsonObject["message"]["from"]["id"], "Hi {}, Welcome to UpNepa. UpNepa is a bot that helps you keep track of PHCN power supply.".format(user.username))
                        offset = jsonObject["update_id"] + 1
                        bot.sendMessage(
                            jsonObject["message"]["from"]["id"], "Congratulations {}! You can now receive notifications for power satus via telegram.".format(user.username))
                        break
                    bot.sendMessage(
                        jsonObject["message"]["from"]["id"], "{} is an Invalid Command".format(jsonObject["message"]["text"]))
                else:
                     bot.sendMessage(
                         jsonObject["message"]["from"]["id"], "Your username is not recognized please set a valid username!")


sched = BackgroundScheduler()

sched.add_job(new_stuff, 'interval', seconds=5)

sched.start()
