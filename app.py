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

from cron import *

if __name__ == '__main__':
    # bot.setWebhook()
    app.run()
