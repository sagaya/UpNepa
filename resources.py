from flask_restful import *
from flask_restful import reqparse
from model.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
import telepot
import json
import datetime

bot = telepot.Bot('518239357:AAGE-1BR1cGhgVLJwLhF8uIsl8EC7QYjUvg')

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
                if data["state"] is True:
                    time = datetime.datetime.now().strftime("%A, %d %b %Y %l:%M %p")
                    bot.sendMessage(
                        user.chatId, "Them don bring light!. The time wey them bring am na {}".format(time))
                    return {"status": True}
                else:
                    bot.sendMessage(user.chatId, "Them don bring light!. The time wey them bring am na {}".format(time))
                    return {"status": True}
            else:
                return {"status": False, "message": "Invalid User"}

        else:
            return {"status": False,"message": "Invalid User"}
        
