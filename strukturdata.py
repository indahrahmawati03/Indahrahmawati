from collections import deque

barang_masuk = deque()
transaksi = []

# Gunakan linked list untuk stok_barang
class Node:
    def __init__(self, barang):
        self.barang = barang
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, barang):
        new_node = Node(barang)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_by_id(self, id_barang):
        current = self.head
        while current:
            if current.barang["id"] == id_barang:
                return current.barang
            current = current.next
        return None

    def remove_by_id(self, id_barang):
        current = self.head
        prev = None
        while current:
            if current.barang["id"] == id_barang:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return current.barang
            prev = current
            current = current.next
        return None

    def display(self):
        current = self.head
        if not current:
            print("Stok kosong.")
        while current:
            b = current.barang
            print(f"{b['id']} - {b['nama']} ({b['kategori']}) {b['kondisi']}")
            current = current.next

stok_barang = LinkedList()

# Fungsi
def tambah_barang():
    jumlah = int(input("Masukkan jumlah barang yang akan ditambahkan: "))
    for i in range(jumlah):
        print(f"\nBarang ke-{i+1}")
        id_barang = input("ID Barang: ")
        nama = input("Nama Barang: ")
        kategori = input("Kategori (Atasan/Bawahan): ")
        kondisi = input("Berapa kondisi barang %: ")
        try:
            harga_asli = float(input("Harga asli barang: "))
        except ValueError:
            print("Input harga tidak valid. Barang dilewati.")
            continue
        
        barang = {
            "id": id_barang,
            "nama": nama,
            "kategori": kategori,
            "kondisi": kondisi,
            "harga_asli": harga_asli
        }
        barang_masuk.append(barang)
    print("Barang berhasil ditambahkan ke antrian.")

def proses_barang_masuk():
    print("\nMemproses Barang Masuk...")
    while barang_masuk:
        barang = barang_masuk.popleft()
        kondisi = int(barang["kondisi"].replace("%", ""))
        if kondisi >= 70:
            stok_barang.append(barang)
            print(f"✔ Barang {barang['id']} diterima dan dimasukkan ke stok.")
        else:
            print(f"✖ Barang {barang['id']} ditolak (kondisi < 70%).")

def lihat_stok():
    print("\nStok Barang Saat Ini:")
    stok_barang.display()

def tambah_transaksi():
    print("\nTransaksi Penjualan")
    id_transaksi = input("ID Transaksi: ")
    id_barang = input("ID Barang yang dijual: ")
    tanggal = input("Tanggal (YYYY-MM-DD): ")

    barang = stok_barang.find_by_id(id_barang)
    if barang:
        harga_jual = barang["harga_asli"] * 0.8
        transaksi.append({
            "id_transaksi": id_transaksi,
            "barang_id": id_barang,
            "jenis": "jual",
            "tanggal": tanggal,
            "harga": harga_jual
        })
        stok_barang.remove_by_id(id_barang)
        print(f"✔ Barang {id_barang} berhasil dijual, seharga Rp {harga_jual:,.2f}.")
    else:
        print(f"✖ Barang {id_barang} tidak ditemukan di stok.")

def lihat_transaksi():
    print("\nRiwayat Transaksi:")
    if not transaksi:
        print("Belum ada transaksi.")
    else:
        for t in transaksi:
            print(f"{t['id_transaksi']} | Barang: {t['barang_id']} | Tanggal: {t['tanggal']} | Harga: {t['harga']}")

def menu():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tambah Barang ke Antrian")
        print("2. Proses Barang Masuk ke Stok")
        print("3. Lihat Stok")
        print("4. Transaksi Penjualan")
        print("5. Lihat Riwayat Transaksi")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            proses_barang_masuk()
        elif pilihan == "3":
            lihat_stok()
        elif pilihan == "4":
            tambah_transaksi()
        elif pilihan == "5":
            lihat_transaksi()
        elif pilihan == "0":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

menu()
