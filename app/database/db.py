import sqlite3
from datetime import date
from .models import DB_PATH

# search user in db and add user
def search_user_and_add(user_id, user_name=None):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("PRAGMA foreign_keys = ON")

            conn.execute("""
                INSERT OR IGNORE INTO users (name_id, url_name_id)
                VALUES (?, ?)
            """, (user_id, "@" + user_name if user_name else None))

            row = conn.execute(
                "SELECT id FROM users WHERE name_id = ?",
                (user_id,)
            )

            row = row.fetchone()

            if row is not None:
                return row[0]
            else:
                return None            

    except sqlite3.Error as e:
        print("DB error:", e)
        return None


# music add playlist user
def add_music_list(user_id, music):

    user_tl_id = search_user_and_add(user_id)

    if user_tl_id is not None:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                conn.execute("PRAGMA foreign_keys = ON")

                conn.execute(
                    "INSERT INTO music (user_id, name_music) VALUES (?, ?)",
                    (user_tl_id, music),
                )

        except sqlite3.Error as e:
            print("DB error:", e)
