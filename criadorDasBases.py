import sqlite3


def conectar():
    conn_login = sqlite3.connect('login.db')

    cursor_login = conn_login.cursor()

    cursor_login.execute('''CREATE TABLE IF NOT EXISTS login (
                    id INTEGER PRIMARY KEY,
                    usuario TEXT NOT NULL,
                    senha TEXT NOT NULL
                )''')


    conn = sqlite3.connect('pendencias.db')


    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pendencias (
                       id INTEGER PRIMARY KEY,
                       documento TEXT NOT NULL,
                       observacao TEXT NOT NULL,
                       status TEXT NOT NULL
                  )''')