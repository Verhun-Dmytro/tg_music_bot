import sqlite3
import os
from config import DB_PATH

#DB_PATH = "music_users.db"
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)


# Create table and DB #
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS  users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_id INTEGER UNIQUE NOT NULL,
            url_name_id TEXT,
            time TEXT                      
                   );
        CREATE TABLE IF NOT EXISTS  music (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name_music TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)                      
                    );
    """)
        print("DB READY!")