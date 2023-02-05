# Background Project

Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain. Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan Programmer untuk membuatkan fitur - fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar.

# Feature Requirements

1.	Membuat ID transaksi
Membuat ID transaksi dilakukan dengan membuat object dari kelas transaksi yang sudah didefinisikan.
2.	Memasukkan data transaksi yang berisi nama, jumlah, dan harga peritem
3.	Mengupdate data transaksi dengan:
a.	Update nama, jika terjadi kesalahan saat input nama item.
b.	Update jumlah jika terjadi kesalahan saat input jumlah item.
c.	Update harga jika terdai kesalahan saat input harga per item.
4.	Membatalkan data transaksi dengan pilihan:
a.	Menghapus salah satu item
b.	Menghapus semuanya data transaksi
5.	Melakukan pengecekan terhadap data transaksi.
6.	Menghitung total belanja dengan ketentuan diskon sebagai berikut:
    - Jika totalbelanja di atas Rp200.000 maka akan mendapatkan diskon 5%.
    - Jika totalbelanja di atas Rp300.000 maka akan mendapatkan diskon 8%.
    - Jika totalbelanja di atas Rp500.000 maka akan mendapatkan diskon 10%.

# Flowchart

![image.png](attachment:image.png)



# Code (penjelasan tentang fungsinya)

- `class Transaction:` Kelas digunakan untuk menampung method-method yang berisi feature requirements yang dibutuhkan.

- `def __init__(self):`   fungsi untuk menginisialisasi sebuah atribut data pada class Transaction. Pada fungsi ini terdapat satu parameter `self.data_transaksi (dict)` yang merupakan variabel untuk menampung data transaksi customer yang masuk.

- ` def add_item(self, nama, jumlah, harga):`  Fungsi untuk memasukkan item yang ingin dibeli. Dengan input nama, jumlah, dan harga peritem.

- `print_item(self):` Fungsi untuk mencetak item-item yang masuk dengan memberikan input berupa tabulate.

- `update_item_name(self, nama, nama_baru):`  Fungsi untuk mengupdate nama item.

- `update_item_qyt(self, nama, jumlah_baru):`  Fungsi untuk mengupdate jumlah item. 

- `def update_item_price(self, nama, harga_baru):`  Fungsi untuk mengupdate harga per item .

- `def delete_item(self, nama):` Fungsi untuk menghapus salah satu item .

- `def reset_transaction(self):` Fungsi untuk mereset atau menghapus semua data transaksi yang ada.

- ` def check_order(self):`Fungsi untuk mengecek apakah data transaksi yang diinput sudah benar atau belum. Pengecekan dilakukan dengan mengecek apakah nama yang diinput bukan string kosong " " dan jumlah serta harga per item harus dalam tipe data integer. 

- `total_price(self):`  Fungsi untuk menghitung total belanja yang harus dibayar. 
    Dengan memberikan diskon dengan ketentuan:
        a. Jika total belanja customer di atas Rp200.000 maka akan mendapatkan diskon 5%
        b. Jika total belanja customer di atas Rp300.000 maka akan mendapatkan diskon 8%
        c. Jika total belanja customer di atas Rp500.000 maka akan mendapatkan diskon 10% 







# Test Code

#### Test 1:
Customer ingin menambahkan dua item dengan method `add_item()` kemudian mencetak list data yang sudah masuk dengan `print_item()`

![image-2.png](attachment:image-2.png)

![image-3.png](attachment:image-3.png)

#### Test 2:
Customer salah membeli barang, sehingga ingin menghapus item "Pasta Gigi" dengan method `delete_item()`

![image-4.png](attachment:image-4.png)

#### Test 3:
Ternyata customer salah memasukkan semua item yang ingin dibelanjakan, sehingga customer ingin menghapus semua data transaksi yang masuk dengan method `reset_transaction()`

![image-5.png](attachment:image-5.png)

#### Test 4:
Customer menginput kembali item-item yang ingin dibeli, kemudian akan menghitung semua total belanja yang harus dibayar dengan method `total_price()`

![image-6.png](attachment:image-6.png)

![image-7.png](attachment:image-7.png)

# Conclution

Modul Transaction sudah berhasil menjalankan feature requirements yang diharapkan Andi sehingga bisa digunakan untuk sistem self-service pada Supermarketnya

# Improvement Suggestions

Agar program lebih mudah digunakan, bisa ditambahkan fungsi input pada setiap methodnya.
