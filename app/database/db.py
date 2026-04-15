from database.models import connect_db, cursor_db
import sqlite3
from datetime import date


# search user in db and add user
def search_user_and_add(user_id, user_name=None):

    cursor_db.execute("SELECT id FROM users WHERE name_id = ?", (user_id,))
    row = cursor_db.fetchone()

    try:
        if row is None:
            cursor_db.execute(
                "INSERT INTO users (name_id, url_name_id, time) VALUES(?,?,?)",
                (user_id,"@" + user_name if  user_name is not None else user_name, date.today()),
            )
            connect_db.commit()
            return cursor_db.lastrowid
        else:
            return row[0]
    except sqlite3.Error as e:
        print("DB error: ", e)
        return None


# music add playlist user
def add_music_list(user_id, music):

    user_tl_id = search_user_and_add(user_id)

    if user_tl_id is not None:
        try:
            cursor_db.execute(
                "INSERT INTO music (user_id,  name_music) VALUES(?,?)",
                (user_tl_id, music),
            )
            connect_db.commit()

        except sqlite3.Error as e:
            print("DB error: ", e)
