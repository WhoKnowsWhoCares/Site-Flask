import os
import random
import string

from loguru import logger
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class Config:
    SECRET_KEY  = os.getenv('SECRET_KEY', None)
    if not SECRET_KEY:
        SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))     
    TG_API_KEY = os.getenv('TG_API_KEY', None)
    TG_USER_ID = os.getenv('TG_USER_ID', None)

    DEBUG = (os.getenv('DEBUG', 'False') == 'True')
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TESTING = True


class ProductionConfig(Config):

    # Security
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    DB_USER     = os.getenv('DATABASE_USER', '')
    DB_PASSWORD = os.getenv('DATABASE_PASS', '')
    DB_HOST     = os.getenv('DATABASE_HOST', 'localhost')
    DB_PORT     = os.getenv('DATABASE_PORT', '5432')
    DB_NAME     = os.getenv('DATABASE_NAME', 'site_db')
    SQLALCHEMY_DATABASE_URI = 'postgresql+pg8000://{}:{}@{}:{}/{}'.\
        format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
