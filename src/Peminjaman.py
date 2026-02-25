from database import connect_db
from datetime import date, datetime


# ================= PINJAM BUKU =================
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

    tanggal_pinjam = date.today()
    print(f"Tanggal pinjam: {tanggal_pinjam.strftime('%d/%m/%Y')}")

    # INPUT TANGGAL KEMBALI
    tgl_kembali_input = input("Masukkan tanggal kembali (DD/MM/YYYY): ")

    try:
        tanggal_kembali = datetime.strptime(tgl_kembali_input, "%d/%m/%Y").date()
    except ValueError:
        print("❌ Format tanggal salah!")
        return

    cur.execute(
        "INSERT INTO peminjaman (nama, judul_buku, tanggal_pinjam, tanggal_pengembalian) VALUES (?, ?, ?, ?)",
        (nama, judul, tanggal_pinjam.strftime("%d/%m/%Y"), tgl_kembali_input)
    )

    cur.execute("UPDATE buku SET status = 'dipinjam' WHERE id = ?", (pilih,))

    conn.commit()
    conn.close()

    print("✅ Buku berhasil dipinjam\n")


# ================= KEMBALIKAN BUKU =================
def kembalikan_buku():
    conn = connect_db()
    cur = conn.cursor()

    print("\n=== Pengembalian Buku ===")

    cur.execute("SELECT id, nama, judul_buku, tanggal_pengembalian FROM peminjaman")
    data = cur.fetchall()

    if not data:
        print("❌ Tidak ada data peminjaman")
        return

    for d in data:
        print(f"ID: {d[0]} | {d[1]} | {d[2]} | Harus kembali: {d[3]}")

    try:
        pilih_id = int(input("Masukkan ID peminjaman: "))
    except ValueError:
        print("❌ Masukkan angka ID!")
        return

    cur.execute("SELECT judul_buku, tanggal_pengembalian FROM peminjaman WHERE id = ?", (pilih_id,))
    res = cur.fetchone()

    if not res:
        print("❌ ID tidak ditemukan.")
        return

    judul, tanggal_kembali_str = res
    tanggal_kembali = datetime.strptime(tanggal_kembali_str, "%d/%m/%Y").date()
    hari_ini = date.today()

    # CEK TERLAMBAT
    if hari_ini > tanggal_kembali:
        selisih = (hari_ini - tanggal_kembali).days
        denda = selisih * 5000
        print(f"⚠ Terlambat {selisih} hari")
        print(f"💰 Denda: Rp {denda}")
    else:
        print("✅ Tidak ada denda")

    cur.execute("DELETE FROM peminjaman WHERE id = ?", (pilih_id,))
    cur.execute("UPDATE buku SET status = 'tersedia' WHERE judul = ?", (judul,))

    conn.commit()
    conn.close()

    print(f"📚 Buku '{judul}' telah dikembalikan.")
