import os
import random
import string

from loguru import logger
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", None)
    if not SECRET_KEY:
        SECRET_KEY = "".join(random.choice(string.ascii_lowercase) for i in range(32))
    TG_API_KEY = os.getenv("TG_API_KEY", ":")
    TG_USER_ID = os.getenv("TG_USER_ID", None)

    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    API_PAGINATION = 10
    PROPAGATE_EXCEPTIONS = True  # needed due to Flask-Restful not passing them up
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "db_data", "data-dev.sqlite"
    )


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProdMySqlConfig(Config):
    # Security
    # REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600
    CSRF_COOKIE_SAMESITE = "Strict"
    SESSION_PROTECTION = "strong"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Strict"

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
    )


class ProdPgConfig(Config):
    # Security
    # REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600
    CSRF_COOKIE_SAMESITE = "Strict"
    SESSION_PROTECTION = "strong"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Strict"

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST")
    # DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    SQLALCHEMY_DATABASE_URI = "postgresql+pg8000://{}:{}@{}/{}".format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
    )


config = {
    "development": DevConfig,
    "testing": TestConfig,
    # "production": ProdPgConfig,
    "production": ProdMySqlConfig,
    "default": DevConfig,
}
