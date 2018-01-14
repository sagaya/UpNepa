
from os import environ


class Base:
    DEBUG = environ.get('DEBUG')
    JWT_SECRET_KEY = 'OPTISS'
    SECRET_KEY = 'OPTISS'
    
