from database import connect_db

def tambah_buku():
    conn = connect_db()
    cur = conn.cursor()

    print("\n=== Tambah Data Buku ===")
    judul = input("Judul buku : ")
    pengarang = input("Pengarang : ")
    isbn = input("ISBN : ")

    cur.execute("INSERT INTO buku (judul, pengarang, isbn, status) VALUES (?, ?, ?, ?)",
                (judul, pengarang, isbn, "tersedia"))

    conn.commit()
    conn.close()
    print("✅ Data buku berhasil dimasukkan\n")


def hapus_buku():
    conn = connect_db()
    cur = conn.cursor()

    print("\n=== Hapus Data Buku ===")
    cur.execute("SELECT id, judul FROM buku")
    data = cur.fetchall()

    if not data:
        print("❌ Tidak ada data buku")
        return

    for d in data:
        print(f"{d[0]}. {d[1]}")

    pilih = int(input("Pilih ID buku yang ingin dihapus: "))
    try:
        pilih = int(input("Pilih ID buku yang ingin dihapus: "))
    except ValueError:
        print("❌ Input salah! Harap masukkan angka ID saja.")
        conn.close()
        return