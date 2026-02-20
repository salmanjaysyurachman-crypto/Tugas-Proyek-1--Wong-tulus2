from database import connect_db

def pinjam_buku():
    conn = connect_db()
    cur = conn.cursor()

    print("\n=== Peminjaman Buku ===")

    cur.execute("SELECT id, judul, status FROM buku")
    buku = cur.fetchall()

    if not buku:
        print("❌ Tidak ada buku")
        return

    for b in buku:
        print(f"{b[0]}. {b[1]} - {b[2]}")

    pilih = int(input("Pilih ID buku: "))

    # cek status buku
    cur.execute("SELECT judul, status FROM buku WHERE id = ?", (pilih,))
    data = cur.fetchone()

    if data is None:
        print("❌ Buku tidak ditemukan")
        return

    judul, status = data

    if status == "dipinjam":
        print("❌ Buku sudah dipinjam")
        return

    nama = input("Nama peminjam: ")
    tanggal = input("Tanggal pinjam: ")

    # simpan peminjaman
    cur.execute("INSERT INTO peminjaman (nama, judul_buku, tanggal) VALUES (?, ?, ?)",
                (nama, judul, tanggal))

    # update status buku
    cur.execute("UPDATE buku SET status = 'dipinjam' WHERE id = ?", (pilih,))

    conn.commit()
    conn.close()
    print("✅ Buku berhasil dipinjam\n")
