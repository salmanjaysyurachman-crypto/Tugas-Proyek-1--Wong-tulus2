import sqlite3

DB_NAME = "perpustakaan.db"


def connect():
    return sqlite3.connect(DB_NAME)


def setup_database():
    conn = connect()
    cursor = conn.cursor()

    # tabel buku
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS buku (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        judul TEXT,
        stok INTEGER
    )
    """)

    # tabel peminjaman
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS peminjaman (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        judul TEXT
    )
    """)

    conn.commit()
    conn.close()