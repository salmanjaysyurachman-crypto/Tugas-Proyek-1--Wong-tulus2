import database as db

def tambah_buku():
    judul = input("Judul buku: ")
    stok = int(input("Stok: "))

buku = {
        "judul": judul,
        "stok": stok
    }

db.buku_db.append(buku)
print("✅ Buku ditambahkan")

def lihat_buku():
    if not db.buku_db:
     print("Belum ada buku")
     return

    for i, b in enumerate(db.buku_db):
        print(f"{i+1}. {b['judul']} | stok: {b['stok']}")

def hapus_buku():
    lihat_buku()
    i = int(input("Pilih buku yang dihapus: ")) - 1

    if 0 <= i < len(db.buku_db):
        db.buku_db.pop(i)
        print("✅ Buku dihapus")
    else:
        print("❌ Tidak valid")