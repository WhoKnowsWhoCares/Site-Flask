import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config

from app.models import db, login_manager, create_user


bootstrap = Bootstrap()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    moment.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    with app.app_context():
        db.create_all()
        create_user()

    return app
