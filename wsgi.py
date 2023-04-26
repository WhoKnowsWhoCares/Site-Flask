import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, UserRole
from dotenv import load_dotenv

load_dotenv()

app_config = os.getenv('FLASK_ENV') or 'default'
app = create_app(app_config)
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, UserRole=UserRole) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)