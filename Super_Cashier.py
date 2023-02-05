
""" Modul ini merupakan modul untuk menjalankan program Super Cashier"""

#import library yang akan digunakan
from tabulate import tabulate

#membuat kelas Transaction
class Transaction:
    
    def __init__(self):
        
        """ 
        fungsi untuk menginisialisasi sebuah atribut data pada class Transaction.
        
        Parameter:
            self.data_transaksi (dict) : variabel untuk menampung data transaksi customer yang masuk
        """
        
        self.data_transaksi = dict()
        
    def add_item(self, nama, jumlah, harga):
        
        """
        Fungsi untuk memasukkan item yang ingin dibeli.
        
        Parameter
            self.nama (str) = nama item
            self.jumlah (int) = jumlah item
            self.harga (int) = harga per item
        
        Output:
            self.data_transaksi (dict) = data transaksi customer yang ditambkan
        """
        
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga
        
        add_data_transaksi = {self.nama: [self.jumlah, self.harga, self.jumlah*self.harga]}
        self.data_transaksi.update(add_data_transaksi)
        print(f"Barang yang ditambahkan adalah {self.jumlah} {self.nama} dengan harga peritemnya Rp{self.harga:,}")
        
    def print_item(self):
        
        """
        Fungsi untuk mencetak item-item yang masuk.
        """
        
        header = ["Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
        print(tabulate([[k,] + v for k,v in self.data_transaksi.items()], 
                       header, tablefmt = "github"))
        
    def update_item_name(self, nama, nama_baru):
        
        """
        Fungsi untuk mengupdate nama item
        """
        
        self.nama_baru = nama_baru
        self.data_transaksi[self.nama_baru] = self.data_transaksi.pop(nama)
        return Transaction.print_item(self)
    
    def update_item_qyt(self, nama, jumlah_baru):
        
        """
        Fungsi untuk mengupdate jumlah item 
        """
        
        self.jumlah_baru = jumlah_baru
        
        self.data_transaksi[self.nama][0] = self.jumlah_baru
        self.data_transaksi[self.nama][2] = self.data_transaksi[self.nama][1]*self.jumlah_baru
        
        return Transaction.print_item(self)
    
    def update_item_price(self, nama, harga_baru):
        
        """
        Fungsi untuk mengupdate harga per item 
        """
        
        self.nama = nama
        self.harga_baru = harga_baru
        
        self.data_transaksi[self.nama][1] = self.harga_baru
        self.data_transaksi[self.nama][2] = self.data_transaksi[self.nama][0]*self.harga_baru
       
        return Transaction.print_item(self)
    
    def delete_item(self, nama):
        
        """
        Fungsi untuk menghapus salah satu item 
        """
        
        self.nama = nama
        del self.data_transaksi[self.nama]
        return Transaction.print_item(self)
    
    def reset_transaction(self):
        
        """
        Fungsi untuk mereset atau menghapus semua data transaksi yang ada
        """
        
        self.data_transaksi.clear()
        print("Semua data transaksi telah berhasil dihapus\n")
        return Transaction.print_item(self)
    
    def check_order(self):
        
        """
        Fungsi untuk mengecek apakah data transaksi yang diinput sudah benar atau belum.
        
        Pengecekan dilakukan dengan mengecek apakah nama yang diinput bukan string kosong " "
        dan jumlah serta harga per item harus dalam tipe data integer. 
        """
        
        item_benar = 0
        banyak_item = 0
        for key in self.data_transaksi:
            if key != " " and type(self.data_transaksi[key][0]) == int and type(self.data_transaksi[key][1]) == int:
                item_benar += 1
            banyak_item += 1
        if item_benar == banyak_item:
            print("Pesanan sudah benar\n")
            print(Transaction.print_item(self))
        else:
            print("Terdapat Kesalahan Input")
    
        
    def total_price(self):
        
        """
        Fungsi untuk menghitung total belanja yang harus dibayar. 
        Dengan memberikan diskon dengan ketentuan:
            a. Jika total belanja customer di atas Rp200.000 maka akan mendapatkan diskon 5%
            b. Jika total belanja customer di atas Rp300.000 maka akan mendapatkan diskon 8%
            c. Jika total belanja customer di atas Rp500.000 maka akan mendapatkan diskon 10% 
        """
        
        total_belanja = 0
        for key in self.data_transaksi:
            total_belanja = total_belanja + self.data_transaksi[key][2]
        print(f"Karena total belanjaan senilai Rp. {total_belanja:,},")
        
        #diskon
        if total_belanja > 200_000 and total_belanja <= 300_000:
            total_belanja = total_belanja - 0.05*total_belanja
            print("maka mendapat diskon 5%")
        elif total_belanja > 300_000 and total_belanja <= 500_000:
            total_belanja = total_belanja - 0.08*total_belanja
            print("maka mendapat diskon 8%")
        elif total_belanja > 500_000:
            total_belanja = total_belanja - 0.1*total_belanja
            print(" maka mendapat diskon 10%")
        else:
            total_belanja
            print("maka tidak mendapat diskon")
        
        print(f"Sehingga total belanja yang harus dibayar menjadi Rp{total_belanja:,}")

