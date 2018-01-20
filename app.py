from flask import Flask, render_template, request, json,redirect,url_for
from flask_restful import *
from mongoengine import *
from flask_cors import CORS
import json
from os import environ
import requests
from config import Base
from flask_jwt_extended import JWTManager
from resources import *
from cron import *
from flask_mail import Mail, Message

app = Flask(__name__)
api = Api(app=app)
app.config.from_object(Base)


connect('upnepa', host=Base.DB)
jwt = JWTManager(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = environ.get("EMAIL")
app.config['MAIL_PASSWORD'] = environ.get("PASS")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True

mail = Mail(app)

api.add_resource(CreateUser, "/register")
api.add_resource(UpdateUser, "/send")


@app.route('/index')
@app.route("/", methods=['GET', 'POST'])
def index():
    form = EmailForm()

    if form.validate_on_submit():
        msg = Message('Hello', sender='id@email.com',
                      recipients=[form.email.data])
        msg.body = "New Email {}".format(form.email.data)
        mail.send(msg)
        return redirect(url_for('index', form=form))
    return render_template("index.html", form=form)


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
bot.setWebhook()
bot.message_loop(handle)


if __name__ == '__main__':
    # bot.setWebhook()
    app.run()
