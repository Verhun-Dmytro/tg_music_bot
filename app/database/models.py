import sqlite3

connect_db = sqlite3.connect("music_users.db")
cursor_db = connect_db.cursor()


# Create table and DB #

cursor_db.execute("PRAGMA foreign_keys = ON")

cursor_db.execute("""
    CREATE TABLE IF NOT EXISTS  users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_id INTEGER NOT NULL,
        url_name_id TEXT,
        time TEXT                      
                  )

""")

cursor_db.execute("""
    CREATE TABLE IF NOT EXISTS  music (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name_music TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)                      
                  )

""")

connect_db.commit()
