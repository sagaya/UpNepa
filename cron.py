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


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])


bot.setWebhook()
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(2)




# def get_offset():
#     global initial
#     content = json.dumps(bot.getUpdates())
#     jsonObjects = json.loads(content)
#     print(jsonObjects)
#     updates = [int(x["update_id"]) for x in jsonObjects]
#     offset = max(updates, default=0) 
#     if offset != 0:
#         initial = False
#     return offset


# initial = False


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



# sched = BackgroundScheduler()

# sched.add_job(new_stuff, 'interval', seconds=5)

# sched.start()
