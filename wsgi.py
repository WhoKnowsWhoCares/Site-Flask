import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, UserRole
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
logger.add("./logs/log_{time:YYYY-MM-DD}.log", level='INFO',
           rotation="00:01", retention="90 days",
           backtrace=True, diagnose=True)

app_config = os.getenv('FLASK_ENV') or 'default'
logger.info(f"Starting wsgi with ENV {app_config}")
app = create_app(app_config)
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, UserRole=UserRole) 

if __name__ == '__main__':
    app.run()