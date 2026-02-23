from database import create_table
from data import tambah_buku, hapus_buku, lihat_buku
from Peminjaman import pinjam_buku, kembalikan_buku


def menu():
    while True:
        print("\n=== SISTEM PERPUSTAKAAN ===")
        print("1. Pendataan Buku")
        print("2. Peminjaman Buku")
        print("3. Keluar")

        pilih = input("Pilih menu: ")

        # ================= MENU PENDATAAN =================
        if pilih == "1":
            while True:
                print("\n=== MENU PENDATAAN BUKU ===")
                print("1. Tambah data buku")
                print("2. Hapus data buku")
                print("3. Lihat daftar buku")
                print("4. Kembali ke menu utama")

                sub = input("Pilih menu pendataan: ")

                if sub == "1":
                    tambah_buku()
                elif sub == "2":
                    hapus_buku()
                elif sub == "3":
                    lihat_buku()
                elif sub == "4":
                    print("↩️ Kembali ke menu utama...")
                    break
                else:
                    print("❌ Pilihan tidak valid")

        # ================= MENU PEMINJAMAN =================
        elif pilih == "2":
            print("\n=== Peminjaman Buku ===")
            print("1. Peminjaman")
            print("2. Pengembalian")
            print("3. Kembali ke menu utama")
            sub_pinjam = input("Pilih menu: ")

            if sub_pinjam == "1":
                pinjam_buku()
            elif sub_pinjam == "2":
                kembalikan_buku() # Ini fungsi baru yang akan kita buat
            else:
                print("↩️ Kembali ke menu utama...")
                break

        # ================= KELUAR PROGRAM =================
        elif pilih == "3":
            print("👋 Program selesai.")
            break

        else:
            print("❌ Pilihan tidak valid")


# PROGRAM UTAMA
if __name__ == "__main__":
    create_table()
    menu()
