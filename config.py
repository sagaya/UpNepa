from os import environ
import datetime


class Base:
    DEBUG = environ.get('DEBUG')
    JWT_SECRET_KEY = 'OPTISS'
    SECRET_KEY = 'OPTISS'
    DB = environ.get('DB')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(1440000)
    
