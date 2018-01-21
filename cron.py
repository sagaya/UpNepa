from models.user import User
offset = None
import telepot
from telepot.loop import MessageLoop
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import json
from os import environ
from mongoengine import *
from config import Base


connect('upnepa', host=Base.DB)


def handle(jsonObject):
    content_type, chat_type, chat_id = telepot.glance(jsonObject)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        username = jsonObject["from"]["username"]
        user = User.objects(username=username).first()
        if user:
            user.chatId = jsonObject["from"]["id"]
            user.save()
            if jsonObject["text"] == "/start":
                bot.sendMessage(jsonObject["from"]["id"], "Hi {}, Welcome to UpNepa. UpNepa is a bot that helps you keep track of PHCN power supply.".format(user.username))
                bot.sendMessage(jsonObject["from"]["id"], "Congratulations {}! You can now receive notifications for power satus via telegram.".format(user.username))
            else:
                bot.sendMessage(jsonObject["from"]["id"], "{} is an Invalid Command".format(jsonObject["text"]))
        else:
            bot.sendMessage(jsonObject["from"]["id"], "Your username is not recognized please set a valid username!")

bot = telepot.Bot('{}'.format(environ.get("TOKEN")))
def fetch():
    print("Howdy")
    MessageLoop(bot, handle).run_forever()
    print('Listening ...')

sched = BlockingScheduler()

sched.add_job(fetch, 'interval', seconds=1)

sched.start()
