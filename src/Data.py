import Database

def TambahBuku():
    judul = input("Judul buku: ")
    stok = int(input("Stok: "))

    conn = Database.Connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Buku (judul, stok) VALUES (?, ?)",
        (judul, stok)
    )

    conn.commit()
    conn.close()

    print("✅ Buku berhasil ditambahkan")


def LihatBuku():
    conn = Database.Connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Buku")
    data = cursor.fetchall()

    if not data:
        print("Belum ada buku.")
    else:
        print("\nDaftar Buku:")
        for buku in data:
            print(f"{buku[0]}. {buku[1]} | Stok: {buku[2]}")

    conn.close()


def HapusBuku():
    LihatBuku()
    id_buku = input("Masukkan ID buku yang ingin dihapus: ")

    conn = Database.Connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Buku WHERE id = ?", (id_buku,))
    conn.commit()
    conn.close()

    print("✅ Buku berhasil dihapus")
