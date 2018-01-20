from models.user import User
from os import environ
offset = None
import telepot
from telepot.loop import MessageLoop
import pprint
import time


def handle(jsonObject):
    username = jsonObject["from"]["username"]
    user = User.objects(username=username).first()
    if user:
        user.chatId = jsonObject["from"]["id"]
        user.save()
        if jsonObject["text"] == "/start":
            bot.sendMessage(
                jsonObject["from"]["id"], "Hi {}, Welcome to UpNepa. UpNepa is a bot that helps you keep track of PHCN power supply.".format(user.username))
            bot.sendMessage(
                jsonObject["from"]["id"], "Congratulations {}! You can now receive notifications for power satus via telegram.".format(user.username))
        else:
            bot.sendMessage(
                jsonObject["from"]["id"], "Invalid Command")
    else:
        bot.sendMessage(
            jsonObject["from"]["id"], "Your username is not recognized please set a valid username!")


bot = telepot.Bot('{}'.format(environ.get("TOKEN")))
bot.message_loop(handle)
# bot.setWebhook()