from database import create_table
from data import tambah_buku, hapus_buku
from peminjaman import pinjam_buku

def menu():
    while True:
        print("\n=== SISTEM PERPUSTAKAAN ===")
        print("1. Pendataan Buku")
        print("2. Peminjaman Buku")
        print("3. Keluar")