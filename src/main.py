import Database
import Data
import Peminjaman

def menu_utama():
    print("\n========== SISTEM PERPUSTAKAAN ==========")
    print("1. Pendataan Buku")
    print("2. Peminjaman Buku")
    print("3. Keluar")


def menu_data():
    print("\n------ MENU DATA BUKU ------")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Hapus Buku")
    print("4. Kembali")


def menu_peminjaman():
    print("\n------ MENU PEMINJAMAN ------")
    print("1. Pinjam Buku")
    print("2. Kembalikan Buku")
    print("3. Kembali")

def main():
    # Setup database
    Database.setup_database()

    while True:
        menu_utama()
        pilih = input("Pilih menu: ")

        # ===== MENU DATA BUKU =====
        if pilih == "1":
            while True:
                menu_data()
                sub = input("Pilih menu data: ")

                if sub == "1":
                    Data-Buku.tambah_buku()

                elif sub == "2":
                    Data-Buku.lihat_buku()

                elif sub == "3":
                    Data-Buku.hapus_buku()

                elif sub == "4":
                    break

                else:
                    print("❌ Pilihan tidak valid.")

        # ===== MENU PEMINJAMAN =====
        elif pilih == "2":
            while True:
                menu_peminjaman()
                sub = input("Pilih menu peminjaman: ")

                if sub == "1":
                    Peminjaman.pinjam_buku()

                elif sub == "2":
                    Peminjaman.kembalikan_buku()

                elif sub == "3":
                    break

                else:
                    print("❌ Pilihan tidak valid.")

        # ===== KELUAR =====
        elif pilih == "3":
            print("Terima kasih telah menggunakan sistem.")
            break

        else:
            print("❌ Menu tidak tersedia.")


if __name__ == "__main__":
    main()