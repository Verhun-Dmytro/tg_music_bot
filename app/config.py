import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_BOT = os.getenv("TOKEN_BOT")
DB_PATH = os.getenv("DB_PATH")