from models import cursor_db, connect_db


cursor_db.execute("SELECT * FROM users  ")




if __name__ == "__main__":
    print(cursor_db.fetchall())
    cursor_db.execute("DELETE FROM users")
    connect_db.commit()