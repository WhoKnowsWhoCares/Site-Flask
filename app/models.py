import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, AnonymousUserMixin
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


class UserRole(Enum):
    USER = 1
    ADMIN = 2


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.USER, nullable=False)
    password_hash = db.Column(db.String(256))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, role):
        return self.role is not None and self.role == role

    def is_administrator(self):
        return self.can(UserRole.ADMIN)

    def __repr__(self):
        return "<User %r>" % self.username


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_user():
    email = os.getenv("DB_USER_MAIL")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")

    user = User.query.filter_by(username=username).first()
    if not user:
        role = UserRole.ADMIN
        db.session.add(
            User(email=email, username=username, password=password, role=role)
        )
        db.session.commit()
