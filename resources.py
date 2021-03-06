from flask_restful import *
from flask_restful import reqparse
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
import telepot
import json
from flask import render_template
import datetime
from os import environ
from flask_wtf import FlaskForm
from wtforms import StringField

bot = telepot.Bot('{}'.format(environ.get("TOKEN")))


class Index(Resource):

    def get(self):

        return {"status":True}

class CreateUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True,
                        help="This field is required")

    def post(self):
        data = self.parser.parse_args()
        new_user = User.create_new_user(**data)
        if new_user["status"] is True:
            return new_user
        return new_user


class UpdateUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("state", type=bool, required=True,
                        help="This field is required")

    @jwt_required
    def post(self):
        data = self.parser.parse_args()
        current_user = get_jwt_identity()
        req_id = ObjectId(current_user['_id']['$oid'])
        user = User.objects(id=req_id).first()
        if user is not None:
            
            if user.chatId is not None:
                date_obj = datetime.datetime.now()
                time = date_obj.strftime("%A, %d %b %Y %l:%M %p")
                if data["state"] is True:
                    bot.sendMessage(
                        user.chatId, "Them don bring light!. The time wey them bring am na {}".format(time))
                    return {"status": True}
                else:
                    bot.sendMessage(user.chatId, "Them don carry light o!. The time wey them carry am na {}".format(time))
                    return {"status": True}
            else:
                return {"status": False, "message": "Invalid User"}

        else:
            return {"status": False,"message": "Invalid User"}
        

class EmailForm(FlaskForm):
    email = StringField("email")
