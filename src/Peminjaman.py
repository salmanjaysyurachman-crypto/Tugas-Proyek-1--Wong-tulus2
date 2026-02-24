from database import connect_db
from datetime import date

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

    try:
    	pilih = int(input("Pilih ID buku: "))
    except ValueError:
    	print("❌ Masukkan angka yang valid!")
    	return

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
    # Mengambil tanggal hari ini dengan format YYYY-MM-DD
    tanggal = date.today().strftime("%d/%m/%Y")
    print(f"Tanggal pinjam: {tanggal}")

    # simpan peminjaman
    cur.execute("INSERT INTO peminjaman (nama, judul_buku, tanggal_pinjam) VALUES (?, ?, ?)",
            (nama, judul, tanggal))
    # update status buku
    cur.execute("UPDATE buku SET status = 'dipinjam' WHERE id = ?", (pilih,))

    conn.commit()
    conn.close()
    print("✅ Buku berhasil dipinjam\n")

def kembalikan_buku():
    conn = connect_db()
    cur = conn.cursor()

    # 1. Cari data peminjaman
    print("\n=== Pengembalian Buku ===")
    cur.execute("SELECT id, nama, judul_buku, tanggal_pinjam FROM peminjaman")
    data = cur.fetchall()

    for d in data:
        print(f"ID: {d[0]} | Peminjam: {d[1]} | Buku: {d[2]} | Tgl Pinjam: {d[3]}")

    try:
        pilih_id = int(input("Masukkan ID peminjaman untuk dikembalikan: "))
    except ValueError:
        print("❌ Masukkan angka ID!")
        conn.close()
        return

    # 2. Input tanggal kembali manual
    tgl_kembali_input = input("Masukkan tanggal pengembalian (DD/MM/YYYY): ")

    # 3. Logika Denda (Sederhana)
    # Catatan: Untuk hitung denda otomatis, perlu konversi string ke objek date.
    # Untuk sekarang, kita buat konfirmasi denda manual dulu.
    status_denda = input("Apakah terlambat? (y/n): ").lower()
    if status_denda == 'y':
        print("💰 Denda yang harus dibayar: Rp 5.000")

    # 4. Hapus dari daftar pinjam & update status buku kembali ke 'tersedia'
    # Ambil judul buku dulu sebelum datanya dihapus dari tabel peminjaman
    cur.execute("SELECT judul_buku FROM peminjaman WHERE id = ?", (pilih_id,))
    res = cur.fetchone()

    if res:
        judul = res[0]
        cur.execute("DELETE FROM peminjaman WHERE id = ?", (pilih_id,))
        cur.execute("UPDATE buku SET status = 'tersedia' WHERE judul = ?", (judul,))
        conn.commit()
        print(f"✅ Buku '{judul}' telah dikembalikan.")
    else:
        print("❌ ID tidak ditemukan.")

    conn.close()
