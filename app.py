from flask import Flask, render_template
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
app = Flask(__name__)
api = Api(app=app)

connect('upnepa', host=Base.DB)
app.config.from_object(Base)
jwt = JWTManager(app)



api.add_resource(CreateUser, "/register")
api.add_resource(UpdateUser, "/send")
api.add_resource(Index, "/")


#BOT STUFF STARTS HERE!



TOKEN = "518239357:AAGE-1BR1cGhgVLJwLhF8uIsl8EC7QYjUvg"


URL = "https://api.telegram.org/bot{}/".format(TOKEN)


if __name__ == '__main__':
    app.run()
