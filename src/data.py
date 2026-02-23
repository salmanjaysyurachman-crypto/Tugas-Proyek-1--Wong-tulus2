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

    try:
        pilih = int(input("Pilih ID buku yang ingin dihapus: "))
    except ValueError:
        print("❌ Input salah! Harap masukkan angka ID saja.")
        conn.close()
        return

    cur.execute("DELETE FROM buku WHERE id = ?", (pilih,))
    conn.commit()
    conn.close()
    print("🗑️ Data berhasil dihapus\n")

def menu_pendataan():
    while True:
        print("\n=== MENU PENDATAAN BUKU ===")
        print("1. Tambah data buku")
        print("2. Hapus data buku")
        print("3. Keluar dari pendataan")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_buku()
        elif pilih == "2":
            hapus_buku()
        elif pilih == "3":
            print("Kembali ke menu utama...")
            break
        else:
            print("Pilihan tidak valid")