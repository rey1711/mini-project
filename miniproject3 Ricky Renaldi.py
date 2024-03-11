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

    def merge_sort(self, arr, key=lambda x: x, ascending=True):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_half = self.merge_sort(left_half, key, ascending)
        right_half = self.merge_sort(right_half, key, ascending)
        return self.merge(left_half, right_half, key, ascending)

    def merge(self, left, right, key, ascending):
        result = []
        left_index, right_index = 0, 0
        while left_index < len(left) and right_index < len(right):
            if ascending:
                if key(left[left_index]) < key(right[right_index]):
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1
            else:
                if key(left[left_index]) > key(right[right_index]):
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

    def sort_devices(self, key1, key2, ascending=True):
        if key1 not in ["harga", "stok"] or key2 not in ["harga", "stok"]:
            print("Kunci pengurutan tidak valid.")
            return
        sorted_devices = self.merge_sort(self.devices, key=lambda x: (getattr(x, key1), getattr(x, key2)), ascending=ascending)
        print(f"Daftar Devices di TokoVape (Diurutkan berdasarkan {key1} dan {key2}):")
        for device in sorted_devices:
            device.display_info()

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
        print("8. Sorting Devices")
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
            key1 = input("Masukkan kunci pengurutan pertama (harga/stok): ")
            key2 = input("Masukkan kunci pengurutan kedua (harga/stok): ")
            ascending = input("Urutkan secara ascending? (y/n): ").lower() == "y"
            toko_vape.sort_devices(key1, key2, ascending)

        elif choice == "9":
            print("Terima kasih! Sampai jumpa.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
