from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from app.models import UserRole

@main.app_context_processor
def inject_permissions():
    return dict(UserRole=UserRole)