import os
import sys
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, UserRole
from flask_socketio import SocketIO
from dotenv import load_dotenv
from loguru import logger
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
logger.add("./logs/log_{time:YYYY-MM-DD}.log", level='INFO',
           rotation="00:01", retention="30 days",
           backtrace=True, diagnose=True)
load_dotenv()

logging_lvl = os.getenv('LOG_LEVEL', 'INFO') 
log = logging.getLogger('werkzeug')
log.setLevel(logging_lvl)
logger.add("./logs/log_{time:YYYY-MM-DD}.log", level=logging_lvl,
           rotation="00:01", retention="30 days",
           backtrace=True, diagnose=True)

# logging_lvl = os.getenv('LOG_LEVEL', 'INFO') 
log = logging.getLogger('werkzeug')
log.setLevel('INFO')
logger.add("./logs/log_{time:YYYY-MM-DD}.log", level='INFO',
           rotation="00:01", retention="30 days",
           backtrace=True, diagnose=True)

app_config = os.getenv('FLASK_ENV') or 'default'
app = create_app(app_config)
migrate = Migrate(app, db)
socketio = SocketIO(app)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, UserRole=UserRole) 

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000)
    socketio.run(app)