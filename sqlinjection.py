import sqlite3

def get_user(username):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Unsafe query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchone()
