import sqlite3
from datetime import datetime

conn = sqlite3.connect('data.db')

sql = conn.cursor()



sql.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, telegram_id INTEGER, phone_number TEXT, reg_date DATETIME);')


sql.execute('CREATE TABLE IF NOT EXISTS use_words (id INTEGER PRIMARY KEY AUTOINCREMENT, translator TEXT, telegram_id INTEGER, text TEXT);')


def register_user(telegram_id, first_name, phone_number):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()

    sql.execute("INSERT INTO users (telegram_id, firstname, phone_number, reg_date) VALUES (?,?,?,?);", (telegram_id,first_name,phone_number, datetime.now()))

    connection.commit()
    connection.close()

def chek_user(telegram_id):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()

    user = sql.execute("SELECT telegram_id FROM users WHERE telegram_id=?; ", (telegram_id,)).fetchone()

    if user:
        return True
    else:
        return False
    

def add_user_words(telegram_id, text, translated_text):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()

    sql.execute("INSERT INTO user_words (telegram_id, text, translated_text, added_date) VALUES (?,?,?)" ,(telegram_id, text,translated_text, datetime.now()))

    connection.commit()
    connection.close()