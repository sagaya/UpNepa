from models.user import User
offset = None
import telepot
from telepot.loop import MessageLoop
import time

from apscheduler.schedulers.background import BackgroundScheduler
import telepot
import json
from models.user import User
from os import environ

bot = telepot.Bot('{}'.format(environ.get("TOKEN")))

def fh():
    print("howdy")
    bot.setWebhook()
    MessageLoop(bot, handle).run_as_thread()
    print('Listening ...')


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

        # bot.sendMessage(chat_id, msg['text'])


# def new_stuff():
#     global initial
#     off = int(get_offset())
#     print(initial)
#     offset = 0
#     if initial is False:
#         offset = off
#     else:
#         offset = off + 1

#     print("Offset is {}".format(offset))
#     content = json.dumps(bot.getUpdates(offset=offset))
#     jsonObjects = json.loads(content)
#     print(jsonObjects)
#     initial = True
#     print(initial)
#     # import pdb; pdb.set_trace()
#     for jsonObject in jsonObjects:
#         if offset != jsonObject["update_id"] or offset is not None:
#             if jsonObject:
#                 print(jsonObject)
#                 username = jsonObject["message"]["from"]["username"]
#                 user = User.objects(username=username).first()
#                 if user:
#                     user.chatId = jsonObject["message"]["from"]["id"]
#                     user.save()
#                     if jsonObject["message"]["text"] == "/start":
#                         bot.sendMessage(
#                             jsonObject["message"]["from"]["id"], "Hi {}, Welcome to UpNepa. UpNepa is a bot that helps you keep track of PHCN power supply.".format(user.username))
#                         offset = jsonObject["update_id"] + 1
#                         bot.sendMessage(
#                             jsonObject["message"]["from"]["id"], "Congratulations {}! You can now receive notifications for power satus via telegram.".format(user.username))
#                         break
#                     bot.sendMessage(
#                         jsonObject["message"]["from"]["id"], "{} is an Invalid Command".format(jsonObject["message"]["text"]))
#                 else:
#                      bot.sendMessage(
#                          jsonObject["message"]["from"]["id"], "Your username is not recognized please set a valid username!")



sched = BackgroundScheduler()

sched.add_job(fh, 'interval', seconds=5)

sched.start()
