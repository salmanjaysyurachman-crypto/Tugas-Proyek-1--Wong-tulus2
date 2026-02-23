# database.py
import sqlite3

def connect_db():
    conn = sqlite3.connect("perpustakaan.db")
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()

    # Tabel buku
    cur.execute("""
    CREATE TABLE IF NOT EXISTS buku (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        judul TEXT,
        pengarang TEXT,
        isbn TEXT,
        status TEXT
    )
    """)

    # Tabel peminjaman
    cur.execute("""
    CREATE TABLE IF NOT EXISTS peminjaman (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        judul_buku TEXT,
        tanggal TEXT
    )
    """)

    conn.commit()
    conn.close()
