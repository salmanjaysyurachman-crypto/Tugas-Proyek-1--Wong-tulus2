from database import create_table
from data import tambah_buku, hapus_buku
from Peminjaman import pinjam_buku

def menu():
    while True:
        print("\n=== SISTEM PERPUSTAKAAN ===")
        print("1. Pendataan Buku")
        print("2. Peminjaman Buku")
        print("3. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            print("\n1. Tambah data buku")
            print("2. Hapus data buku")
            sub = input("Pilih: ")

            if sub == "1":
                tambah_buku()
            elif sub == "2":
                hapus_buku()

        elif pilih == "2":
            pinjam_buku()

        elif pilih == "3":
            print("Program selesai.")
            break

        else:
            print("❌ Pilihan tidak valid")


if __name__ == "__main__":
    create_table()
    menu()