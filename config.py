from os import environ
import datetime


class Base:
    DEBUG = environ.get('DEBUG')
    JWT_SECRET_KEY = 'OPTISS'
    SECRET_KEY = 'OPTISS'
    DB = environ.get('DB')
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 465
    # MAIL_USERNAME = "shaggy.hafeez@gmail.com"
    # MAIL_PASSWORD = "Opeyemi123"
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(1440000)
    
