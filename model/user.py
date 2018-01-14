from mongoengine import *
from flask_jwt_extended import create_access_token
from flask_bcrypt import generate_password_hash
import json

class User(Document):
    username = StringField(required=True)
    password = StringField()
    chatId = IntField()

    @classmethod
    def create_new_user(cls, **kwargs):
        new_user = cls(**kwargs)
        try:
            new_user.save()
        except Exception as e:
            return {"status": False}
        else:
            json_object = json.loads(new_user.to_json())
            return {"status": True, "user": json_object, 'token': 'Bearer {}'.format(create_access_token(identity=json_object))}
