import sqlite3

DB_NAME = "perpustakaan.db"


def connect():
    return sqlite3.connect(DB_NAME)


