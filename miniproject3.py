import math

class Device:
    def __init__(self, nama, warna, brand, harga, stok):
        self.nama = nama
        self.warna = warna
        self.brand = brand
        self.harga = harga
        self.stok = stok
    
    def display_info(self):
        print(f"Nama device: {self.nama}")
        print(f"Brand device: {self.brand}")
        print(f"Warna device: {self.warna}")
        print(f"Harga device: {self.harga}")
        print(f"Stok device: {self.stok}")

class DeviceNode:
    def __init__(self, device):
        self.device = device
        self.next = None

class Tokovape:
    def __init__(self, nama, alamat, jam_buka_dantutup):
        self.nama = nama
        self.alamat = alamat
        self.jam_buka_dantutup = jam_buka_dantutup
        self.head = None

    def tambahkan_di_awal(self, device):
        new_node = DeviceNode(device)
        new_node.next = self.head
        self.head = new_node
        print(f"Device {device.nama} telah ditambahkan di awal di TokoVape.")

    def tambahkan_di_akhir(self, device):
        new_node = DeviceNode(device)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Device {device.nama} telah ditambahkan di akhir di TokoVape.")

    def tambahkan_di_antara(self, device, nama_sebelumnya):
        new_node = DeviceNode(device)
        if not self.head:
            print("List kosong. Tambahkan node di awal atau akhir.")
            return
        current = self.head
        while current:
            if current.device.nama == nama_sebelumnya:
                new_node.next = current.next
                current.next = new_node
                print(f"Device {device.nama} telah ditambahkan di antara node dengan nama {nama_sebelumnya}.")
                return
            current = current.next
        print(f"Tidak ditemukan node dengan nama {nama_sebelumnya}.")

    def hapus_di_awal(self):
        if not self.head:
            print("List kosong.")
            return
        self.head = self.head.next
        print("Device di awal telah dihapus dari TokoVape.")

    def hapus_di_akhir(self):
        if not self.head:
            print("List kosong.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        print("Device di akhir telah dihapus dari TokoVape.")

    def hapus_di_antara(self, nama_sebelumnya):
        if not self.head or not self.head.next:
            print("List tidak memiliki cukup node untuk dihapus di antara.")
            return
        prev = None
        current = self.head
        while current.next:
            if current.device.nama == nama_sebelumnya:
                if prev:
                    prev.next = current.next
                    print(f"Device setelah node dengan nama {nama_sebelumnya} telah dihapus dari TokoVape.")
                    return
                else:
                    print("Node pertama tidak bisa dihapus di antara.")
                    return
            prev = current
            current = current.next
        print(f"Tidak ditemukan node dengan nama {nama_sebelumnya}.")

    def lihat_devices(self):
        print("Daftar Devices di TokoVape:")
        current = self.head
        while current:
            current.device.display_info()
            current = current.next

    def jump_search(self, key, value):
        if not self.head:
            print("List kosong.")
            return -1
        step = int(math.sqrt(len(self)))
        prev = None
        current = self.head
        while current and current.device.__dict__[key] < value:
            prev = current
            for _ in range(step):
                if current.next:
                    current = current.next
                else:
                    break
        while prev and prev.device.__dict__[key] < value:
            prev = prev.next
        if prev and prev.device.__dict__[key] == value:
            return prev.device
        print(f"Device dengan {key} {value} tidak ditemukan.")
        return -1

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

if __name__ == "__main__":
    toko_vape = Tokovape("TokoVape Barokah", "Jl. Raya No. 123", "08:00 - 22:00")
    
    while True:
        print("\nPilih operasi:")
        print("1. Tambah Device di Awal")
        print("2. Tambah Device di Akhir")
        print("3. Tambah Device di Antara")
        print("4. Hapus Device di Awal")
        print("5. Hapus Device di Akhir")
        print("6. Hapus Device di Antara")
        print("7. Lihat Devices")
        print("8. Cari Device")
        print("9. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4/5/6/7/8/9): ")

        if choice == "1":
            nama = input("Masukkan nama device: ")
            warna = input("Masukkan warna device: ")
            brand = input("Masukkan brand device: ")
            harga = float(input("Masukkan harga device: "))
            stok = int(input("Masukkan stok device: "))
            new_device = Device(nama, warna, brand, harga, stok)
            toko_vape.tambahkan_di_awal(new_device)

        elif choice == "2":
            nama = input("Masukkan nama device: ")
            warna = input("Masukkan warna device: ")
            brand = input("Masukkan brand device: ")
            harga = float(input("Masukkan harga device: "))
            stok = int(input("Masukkan stok device: "))
            new_device = Device(nama, warna, brand, harga, stok)
            toko_vape.tambahkan_di_akhir(new_device)

        elif choice == "3":
            nama = input("Masukkan nama device: ")
            warna = input("Masukkan warna device: ")
            brand = input("Masukkan brand device: ")
            harga = float(input("Masukkan harga device: "))
            stok = int(input("Masukkan stok device: "))
            nama_sebelumnya = input("Masukkan nama device sebelumnya: ")
            new_device = Device(nama, warna, brand, harga, stok)
            toko_vape.tambahkan_di_antara(new_device, nama_sebelumnya)

        elif choice == "4":
            toko_vape.hapus_di_awal()

        elif choice == "5":
            toko_vape.hapus_di_akhir()

        elif choice == "6":
            nama_sebelumnya = input("Masukkan nama device sebelumnya: ")
            toko_vape.hapus_di_antara(nama_sebelumnya)

        elif choice == "7":
            toko_vape.lihat_devices()

        elif choice == "8":
            key = input("Masukkan kunci pencarian (nama/harga/stok): ")
            value = input("Masukkan nilai pencarian: ")
            result = toko_vape.jump_search(key, value)
            if result != -1:
                print("Device ditemukan:")
                result.display_info()

        elif choice == "9":
            print("Terima kasih! Sampai jumpa.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")