import os
import random
import string

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY  = os.getenv('SECRET_KEY', None)
    if not SECRET_KEY:
        SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))     

    DEBUG = (os.getenv('DEBUG', 'False') == 'True')
    # ADMIN = os.getenv('ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(Config):
    # DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    DB_USER     = os.getenv('DATABASE_USER', None)
    DB_PASSWORD = os.getenv('DATABASE_PASS', None)
    DB_HOST     = os.getenv('DATABASE_HOST', None)
    DB_PORT     = os.getenv('DATABASE_PORT', None)
    DB_NAME     = os.getenv('DATABASE_NAME', None)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.\
        format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
    print(SQLALCHEMY_DATABASE_URI)



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
