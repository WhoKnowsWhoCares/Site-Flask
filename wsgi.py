import os
import logging
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, UserRole
from flask_socketio import SocketIO
from dotenv import load_dotenv
from loguru import logger
from app.models import create_user

load_dotenv()

logging_lvl = os.getenv("LOG_LEVEL", "INFO")
log = logging.getLogger("werkzeug")
log.setLevel(logging_lvl)
logger.add(
    "./logs/log_{time:YYYY-MM-DD}.log",
    level=logging_lvl,
    rotation="00:01",
    retention="30 days",
    backtrace=True,
    diagnose=True,
)

app_config = os.getenv("FLASK_ENV") or "default"
app = create_app(app_config)
migrate = Migrate(app, db)
socketio = SocketIO(app)


@app.cli.command("create_user")
def create_user_command():
    create_user()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, UserRole=UserRole)


if __name__ == "__main__":
    socketio.run(app, use_reloader=True, log_output=True)
