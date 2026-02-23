from database import connect_db


# ================= TAMBAH BUKU =================
def tambah_buku():
    conn = connect_db()
    cur = conn.cursor()

    print("\n=== Tambah Data Buku ===")
    judul = input("Judul buku : ")
    pengarang = input("Pengarang : ")
    isbn = input("ISBN : ")

    cur.execute(
        "INSERT INTO buku (judul, pengarang, isbn, status) VALUES (?, ?, ?, ?)",
        (judul, pengarang, isbn, "tersedia")
    )

    conn.commit()
    conn.close()
    print("✅ Data buku berhasil dimasukkan\n")


# ================= HAPUS BUKU =================
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
        print("❌ Input harus angka!")
        conn.close()
        return

    cur.execute("DELETE FROM buku WHERE id = ?", (pilih,))
    conn.commit()
    conn.close()
    print("🗑️ Data berhasil dihapus\n")


# ================= LIHAT DAFTAR BUKU =================
def lihat_buku():
    conn = connect_db()
    cur = conn.cursor()

    print("\n=== DAFTAR BUKU PERPUSTAKAAN ===")
    cur.execute("SELECT id, judul, pengarang, isbn, status FROM buku")
    data = cur.fetchall()

    if not data:
        print("📭 Belum ada data buku.")
    else:
        print("\nID | Judul | Pengarang | ISBN | Status")
        print("-" * 60)
        for d in data:
            print(f"{d[0]} | {d[1]} | {d[2]} | {d[3]} | {d[4]}")

    conn.close()