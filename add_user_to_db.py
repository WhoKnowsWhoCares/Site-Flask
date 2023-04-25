import pg8000
import os
import bcrypt
from dotenv import load_dotenv

load_dotenv()

DB_USER     = os.getenv('DATABASE_USER', 'postgres')
DB_PASSWORD = os.getenv('DATABASE_PASS', '')
DB_HOST     = os.getenv('DATABASE_HOST', 'localhost')
DB_PORT     = os.getenv('DATABASE_PORT', '5432')
DB_NAME     = os.getenv('DATABASE_NAME', 'site_db')

conn = pg8000.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

password = "my_password".encode("utf-8") 
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

cur = conn.cursor()
cmd = f"INSERT INTO users (username, email, role, password) VALUES ('test', 'test@mail.com', '1', {hashed_password});"
cur.execute(cmd)
conn.commit()

cur.close()
conn.close()
