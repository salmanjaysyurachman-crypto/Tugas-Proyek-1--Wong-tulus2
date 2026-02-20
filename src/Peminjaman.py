# Peminjaman.py
import Database
import Data

def pinjam_buku():
    Data.LihatBuku()

    try:
        id_buku = int(input("Pilih ID buku: "))
    except:
        print("Masukkan angka!")
        return

    conn = Database.connect()
    cursor = conn.cursor()

    # ambil buku
    cursor.execute("SELECT * FROM buku WHERE id = ?", (id_buku,))
    buku = cursor.fetchone()

    if buku is None:
        print("Buku tidak ditemukan")
        conn.close()
        return

    if buku[2] <= 0:
        print("Stok habis")
        conn.close()
        return

    nama = input("Nama peminjam: ")

    # simpan peminjaman
    cursor.execute("INSERT INTO peminjaman (nama, judul) VALUES (?, ?)", (nama, buku[1]))

    # kurangi stok
    cursor.execute("UPDATE buku SET stok = stok - 1 WHERE id = ?", (id_buku,))

    conn.commit()
    conn.close()
    print("✅ Buku berhasil dipinjam")


def kembalikan_buku():
    nama = input("Nama peminjam: ")

    conn = Database.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM peminjaman WHERE nama = ?", (nama,))
    data = cursor.fetchone()

    if data is None:
        print("Data tidak ditemukan")
        conn.close()
        return

    judul = data[2]

    # tambah stok
    cursor.execute("UPDATE buku SET stok = stok + 1 WHERE judul = ?", (judul,))
    cursor.execute("DELETE FROM peminjaman WHERE id = ?", (data[0],))

    conn.commit()
    conn.close()
    print("✅ Buku dikembalikan")